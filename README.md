# 📱 Assignment 2: Activity Classification with Decision Tree

Implementation for **Assignment 2** (`02_ActivityClassification.pdf`, slide 62) for the Wearable Computing course.

---

## 1. Overview & Methodology

### Requirements Addressed
1. **Feature Extraction**: Segment the WISDM accelerometer dataset (`WISDM_ar_v1.1_raw.txt`) into **~10-second windows** ($N = 200$ samples @ $20\text{ Hz}$). For each window, compute the sample mean ($\bar{x}, \bar{y}, \bar{z}$) and sample standard deviation ($s_x, s_y, s_z$) across all three axes.

> 🌐 **Live Mobile App & Interactive Demo**: [https://cantfirmed.github.io/wearable-02/](https://cantfirmed.github.io/wearable-02/)

2. **Subject ID Removal**: Exclude the subject identifier column before training to prevent the classifier from memorizing individual identities.
3. **Model Training & Evaluation**: Train a Decision Tree classifier (using `scikit-learn` CART / J48 equivalent) and perform comprehensive evaluation (10-fold Stratified Cross-Validation, holdout test split, confusion matrix, precision/recall/F1 metrics).
4. **Mobile Implementation**: Implement the trained decision tree in a mobile application (responsive PWA with HTML5 `devicemotion`, interactive simulator, and visual tree inspector).

---

## 2. Classifier Performance Evaluation

### Dataset Statistics
- **Raw accelerometer readings**: 1,086,465 valid rows.
- **10-second window examples**: 5,348 examples.
- **Class distribution**:
  - `Walking`: 2,073 (38.8%)
  - `Jogging`: 1,667 (31.2%)
  - `Upstairs`: 603 (11.3%)
  - `Downstairs`: 486 (9.1%)
  - `Sitting`: 288 (5.4%)
  - `Standing`: 231 (4.3%)

### Metrics
- **10-Fold Stratified Cross-Validation Accuracy**: **$85.45\% \pm 0.97\%$**
- **Holdout Test Set (20%) Accuracy**: **$86.26\%$**

#### Detailed Classification Report (Holdout Test Set)

| Activity | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Jogging** | 0.96 | 0.99 | 0.98 | 333 |
| **Sitting** | 0.97 | 1.00 | 0.98 | 58 |
| **Standing** | 1.00 | 0.96 | 0.98 | 46 |
| **Walking** | 0.83 | 0.97 | 0.90 | 415 |
| **Upstairs** | 0.64 | 0.53 | 0.58 | 121 |
| **Downstairs** | 0.60 | 0.27 | 0.37 | 97 |
| **Overall Accuracy** | | | **0.86** | 1,070 |
| **Macro Average** | 0.84 | 0.79 | 0.80 | 1,070 |
| **Weighted Average** | 0.85 | 0.86 | 0.85 | 1,070 |

> [!NOTE]
> `Jogging`, `Sitting`, and `Standing` have near-perfect F1 scores ($\approx 0.98$). The main source of confusion is between `Walking`, `Upstairs`, and `Downstairs`, which is well-documented in human activity recognition literature when relying solely on tri-axial accelerometer statistics without barometric pressure or gyroscopes.

Visual artifacts generated:
- Confusion Matrix: [`ue02/confusion_matrix.png`](./confusion_matrix.png)
- Decision Tree Visualization: [`ue02/decision_tree.png`](./decision_tree.png)

---

## 3. How to Run the Training Pipeline

The automated script extracts features directly from the zip archive, saves both `.csv` and `.arff` files, evaluates the classifier, and transpiles the model into pure JavaScript.

```bash
# 1. Activate environment
source ue02/.venv/bin/activate

# 2. Run training & evaluation pipeline
python ue02/train_classifier.py
```

Generated outputs:
- `wisdm_features_10s.csv`: Extracted 10s window features.
- `wisdm_features_10s.arff`: ARFF formatted file for optional WEKA comparison.
- `model.js`: Transpiled decision tree function `classifyActivity(...)` for mobile execution.
- `classification_report.txt`: Full textual evaluation metrics and tree rules.

---

## 4. How to Run the Mobile App

The mobile application is located at [`ue02/index.html`](./index.html).

### Launching locally:
```bash
python3 -m http.server 8000 --directory ue02
```
Open `http://localhost:8000` (or `http://<your-lan-ip>:8000` on your smartphone).

### Features:
1. **Live Motion Sensor**: Connects to the phone's accelerometer via `devicemotion`, buffers 10 seconds of motion, calculates rolling mean & standard deviation, and updates the predicted activity in real time.
2. **Interactive Simulator**: Features test vectors with ground truth from the WISDM test set and 6 interactive sliders to test arbitrary sensor conditions.
3. **Model & Tree Inspector**: Inspect the tree rules, confusion matrix, and full tree diagram directly within the app.
