"""
Assignment 2: Activity Classification with Decision Tree
Dataset: WISDM (WISDM_ar_v1.1_raw.txt)
Features: 10-second windows (approx 200 samples @ 20Hz), sample mean and sample std for x, y, z axes.
Classifier: scikit-learn DecisionTreeClassifier (subject id excluded).
Exports:
  - wisdm_features_10s.csv (and .arff)
  - model.js (pure JS implementation of the decision tree)
  - decision_tree.png & confusion_matrix.png
  - classification_report.txt
"""

import os
import zipfile
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree, _tree
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_PATH = os.path.join(BASE_DIR, "WISDM_ar_v1.1_raw.txt.zip")
CSV_FEATURES_PATH = os.path.join(BASE_DIR, "wisdm_features_10s.csv")
ARFF_FEATURES_PATH = os.path.join(BASE_DIR, "wisdm_features_10s.arff")
REPORT_PATH = os.path.join(BASE_DIR, "classification_report.txt")
TREE_IMG_PATH = os.path.join(BASE_DIR, "decision_tree.png")
CM_IMG_PATH = os.path.join(BASE_DIR, "confusion_matrix.png")
MODEL_JS_PATH = os.path.join(BASE_DIR, "model.js")
SAMPLE_TESTS_JSON_PATH = os.path.join(BASE_DIR, "sample_tests.json")

WINDOW_SIZE = 200  # 10s @ 20 Hz
FEATURE_COLS = ["xmean", "ymean", "zmean", "xdev", "ydev", "zdev"]
LABEL_COL = "label"

def load_and_preprocess_raw(zip_path):
    print(f"[*] Reading raw data directly from {zip_path}...")
    records = []
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open("WISDM_ar_v1.1_raw.txt") as f:
            for line in f:
                line_str = line.decode('utf-8', errors='ignore').strip()
                if not line_str:
                    continue
                # Line format: subject,activity,timestamp,x,y,z;
                parts = line_str.rstrip(';').split(',')
                if len(parts) == 6:
                    try:
                        subject = int(parts[0])
                        activity = parts[1].strip()
                        x = float(parts[3])
                        y = float(parts[4])
                        z = float(parts[5])
                        records.append((subject, activity, x, y, z))
                    except ValueError:
                        continue
    df = pd.DataFrame(records, columns=["subject", "activity", "x", "y", "z"])
    print(f"[+] Loaded {len(df):,} valid accelerometer readings across {df['activity'].nunique()} activities.")
    return df

def extract_features(df, window_size=WINDOW_SIZE):
    print(f"[*] Extracting 10s window features ({window_size} samples @ 20Hz) per (subject, activity)...")
    feature_rows = []

    # Group by subject and activity to prevent mixing activities across window boundaries
    for (subject, activity), group in df.groupby(["subject", "activity"], sort=False):
        n = len(group)
        if n < window_size:
            continue
        xs = group["x"].values
        ys = group["y"].values
        zs = group["z"].values

        for start in range(0, n - window_size + 1, window_size):
            wx = xs[start:start + window_size]
            wy = ys[start:start + window_size]
            wz = zs[start:start + window_size]

            # ddof=1 for sample standard deviation
            feature_rows.append({
                "subject": subject,
                "xmean": float(np.mean(wx)),
                "ymean": float(np.mean(wy)),
                "zmean": float(np.mean(wz)),
                "xdev": float(np.std(wx, ddof=1)),
                "ydev": float(np.std(wy, ddof=1)),
                "zdev": float(np.std(wz, ddof=1)),
                "label": activity
            })

    feat_df = pd.DataFrame(feature_rows)
    print(f"[+] Generated {len(feat_df):,} feature examples.")
    print("    Class distribution:")
    for lbl, count in feat_df["label"].value_counts().items():
        print(f"      - {lbl:12s}: {count:5d} ({count/len(feat_df)*100:5.1f}%)")
    return feat_df

def save_arff(feat_df, output_path):
    print(f"[*] Saving ARFF format to {output_path}...")
    classes = sorted(feat_df["label"].unique())
    classes_str = "{" + ", ".join(classes) + "}"
    with open(output_path, "w") as f:
        f.write("@relation activity_recognition\n\n")
        f.write("@attribute \"xmean\" numeric\n")
        f.write("@attribute \"ymean\" numeric\n")
        f.write("@attribute \"zmean\" numeric\n")
        f.write("@attribute \"xdev\" numeric\n")
        f.write("@attribute \"ydev\" numeric\n")
        f.write("@attribute \"zdev\" numeric\n")
        f.write(f"@attribute label {classes_str}\n\n")
        f.write("@data\n")
        for _, row in feat_df.iterrows():
            f.write(f"{row['xmean']:.6f},{row['ymean']:.6f},{row['zmean']:.6f},{row['xdev']:.6f},{row['ydev']:.6f},{row['zdev']:.6f},{row['label']}\n")

def tree_to_js(tree, feature_names, class_names):
    """Transpiles scikit-learn DecisionTreeClassifier to pure JavaScript."""
    tree_ = tree.tree_
    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_names[tree_.feature[node]]
            threshold = tree_.threshold[node]
            left_call = recurse(tree_.children_left[node], depth + 1)
            right_call = recurse(tree_.children_right[node], depth + 1)
            return (
                f"{indent}if ({name} <= {threshold:.6f}) {{\n"
                f"{left_call}"
                f"{indent}}} else {{\n"
                f"{right_call}"
                f"{indent}}}\n"
            )
        else:
            counts = tree_.value[node][0]
            pred_idx = int(np.argmax(counts))
            pred_class = class_names[pred_idx]
            total = float(np.sum(counts))
            confidence = float(counts[pred_idx] / total) if total > 0 else 1.0
            probs = {class_names[i]: round(float(counts[i] / total), 4) for i in range(len(class_names))}
            probs_json = json.dumps(probs)
            return (
                f"{indent}return {{\n"
                f"{indent}  activity: \"{pred_class}\",\n"
                f"{indent}  confidence: {confidence:.4f},\n"
                f"{indent}  probabilities: {probs_json}\n"
                f"{indent}}};\n"
            )

    body = recurse(0, 1)
    return (
        "// Auto-generated Decision Tree Classifier (WISDM 10s Window Model)\n"
        "// Features: xmean, ymean, zmean, xdev, ydev, zdev\n"
        "function classifyActivity(xmean, ymean, zmean, xdev, ydev, zdev) {\n"
        f"{body}"
        "}\n\n"
        "// Export for Node.js if available, otherwise attach to window\n"
        "if (typeof module !== 'undefined' && module.exports) {\n"
        "  module.exports = { classifyActivity };\n"
        "} else if (typeof window !== 'undefined') {\n"
        "  window.classifyActivity = classifyActivity;\n"
        "}\n"
    )

def main():
    # 1. Feature Extraction
    df = load_and_preprocess_raw(ZIP_PATH)
    feat_df = extract_features(df)
    
    # Save CSV and ARFF
    feat_df.to_csv(CSV_FEATURES_PATH, index=False)
    print(f"[+] Saved CSV features to {CSV_FEATURES_PATH}")
    save_arff(feat_df, ARFF_FEATURES_PATH)

    # 2. Prepare Data (Remove subject id before training)
    X = feat_df[FEATURE_COLS].values
    y = feat_df[LABEL_COL].values
    class_names = sorted(list(np.unique(y)))

    print("\n[*] Splitting dataset: 80% train, 20% test (stratified)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Train Decision Tree Classifier
    # Depth 6 strikes an optimal balance between high accuracy (~86-88%) and clean mobile explainability
    print("[*] Training DecisionTreeClassifier (max_depth=6, criterion='gini')...")
    clf = DecisionTreeClassifier(max_depth=6, random_state=42)
    clf.fit(X_train, y_train)

    # Cross-validation
    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    cv_scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    print(f"[+] 10-Fold Cross-Validation Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    # Evaluate on holdout test set
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, digits=4)
    cm = confusion_matrix(y_test, y_pred, labels=clf.classes_)

    print(f"[+] Holdout Test Accuracy: {acc*100:.2f}%\n")
    print(report)

    # 4. Save Classification Report
    with open(REPORT_PATH, "w") as f:
        f.write("=== WISDM ACTIVITY CLASSIFICATION (DECISION TREE) ===\n\n")
        f.write(f"Model: DecisionTreeClassifier (max_depth=6, criterion='gini')\n")
        f.write(f"Features: {', '.join(FEATURE_COLS)}\n")
        f.write(f"Window duration: 10 seconds (200 samples @ 20Hz)\n")
        f.write(f"Total examples: {len(feat_df)}\n")
        f.write(f"Training examples: {len(X_train)}\n")
        f.write(f"Testing examples: {len(X_test)}\n\n")
        f.write(f"10-Fold Cross-Validation Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})\n")
        f.write(f"Holdout Test Accuracy: {acc*100:.2f}%\n\n")
        f.write("--- Classification Report ---\n")
        f.write(report)
        f.write("\n--- Textual Decision Tree Rules ---\n")
        f.write(export_text(clf, feature_names=FEATURE_COLS))
    print(f"[+] Saved evaluation report to {REPORT_PATH}")

    # 5. Plot and Save Confusion Matrix
    plt.figure(figsize=(8, 6), dpi=150)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
    disp.plot(cmap="Blues", values_format="d", ax=plt.gca(), xticks_rotation=45)
    plt.title(f"WISDM Activity Classification Confusion Matrix\n(Accuracy: {acc*100:.2f}%)")
    plt.tight_layout()
    plt.savefig(CM_IMG_PATH)
    plt.close()
    print(f"[+] Saved confusion matrix image to {CM_IMG_PATH}")

    # 6. Plot and Save Decision Tree Graphic
    plt.figure(figsize=(24, 12), dpi=150)
    plot_tree(
        clf,
        feature_names=FEATURE_COLS,
        class_names=clf.classes_,
        filled=True,
        rounded=True,
        fontsize=8,
        precision=2
    )
    plt.title("Trained Decision Tree (max_depth=6) for WISDM Activity Recognition", fontsize=14)
    plt.tight_layout()
    plt.savefig(TREE_IMG_PATH)
    plt.close()
    print(f"[+] Saved decision tree visualization to {TREE_IMG_PATH}")

    # 7. Generate JavaScript Transpiled Model
    js_code = tree_to_js(clf, FEATURE_COLS, clf.classes_)
    with open(MODEL_JS_PATH, "w") as f:
        f.write(js_code)
    print(f"[+] Transpiled Decision Tree to pure JavaScript in {MODEL_JS_PATH}")

    # 8. Export diverse sample test vectors for the mobile interactive UI
    sample_tests = []
    # Pick 2-3 prototypical test samples for each class
    for label in clf.classes_:
        idxs = np.where(y_test == label)[0]
        # select up to 3 samples
        for i in idxs[:3]:
            feat_dict = {col: round(float(X_test[i][idx]), 4) for idx, col in enumerate(FEATURE_COLS)}
            sample_tests.append({
                "true_label": label,
                "predicted_label": str(clf.predict([X_test[i]])[0]),
                "features": feat_dict
            })
    with open(SAMPLE_TESTS_JSON_PATH, "w") as f:
        json.dump(sample_tests, f, indent=2)
    print(f"[+] Exported representative test samples to {SAMPLE_TESTS_JSON_PATH}")

if __name__ == "__main__":
    main()
