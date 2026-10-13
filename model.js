// Auto-generated Decision Tree Classifier (WISDM 10s Window Model)
// Features: xmean, ymean, zmean, xdev, ydev, zdev
function classifyActivity(xmean, ymean, zmean, xdev, ydev, zdev) {
  if (ydev <= 6.166861) {
    if (ydev <= 1.259961) {
      if (ymean <= 5.437325) {
        if (zmean <= 1.426925) {
          if (ydev <= 0.301966) {
            return {
              activity: "Sitting",
              confidence: 1.0000,
              probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
            };
          } else {
            return {
              activity: "Standing",
              confidence: 1.0000,
              probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 1.0, "Upstairs": 0.0, "Walking": 0.0}
            };
          }
        } else {
          return {
            activity: "Sitting",
            confidence: 1.0000,
            probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
          };
        }
      } else {
        if (xmean <= 2.841450) {
          if (zdev <= 1.485056) {
            if (ydev <= 0.670616) {
              return {
                activity: "Standing",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 1.0, "Upstairs": 0.0, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Standing",
                confidence: 0.6667,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.3333, "Standing": 0.6667, "Upstairs": 0.0, "Walking": 0.0}
              };
            }
          } else {
            return {
              activity: "Sitting",
              confidence: 1.0000,
              probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
            };
          }
        } else {
          if (zmean <= 0.739328) {
            if (zmean <= -3.616050) {
              return {
                activity: "Sitting",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Standing",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 1.0, "Upstairs": 0.0, "Walking": 0.0}
              };
            }
          } else {
            return {
              activity: "Sitting",
              confidence: 1.0000,
              probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
            };
          }
        }
      }
    } else {
      if (zdev <= 2.747300) {
        if (xmean <= 0.720400) {
          if (xdev <= 1.456036) {
            if (xmean <= -2.098475) {
              return {
                activity: "Sitting",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 1.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Upstairs",
                confidence: 0.9556,
                probabilities: {"Downstairs": 0.0222, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.9556, "Walking": 0.0222}
              };
            }
          } else {
            if (zdev <= 2.158468) {
              return {
                activity: "Downstairs",
                confidence: 0.7303,
                probabilities: {"Downstairs": 0.7303, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.191, "Walking": 0.0787}
              };
            } else {
              return {
                activity: "Upstairs",
                confidence: 0.5600,
                probabilities: {"Downstairs": 0.34, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.56, "Walking": 0.1}
              };
            }
          }
        } else {
          if (ydev <= 3.827803) {
            if (ymean <= 8.866625) {
              return {
                activity: "Upstairs",
                confidence: 0.6094,
                probabilities: {"Downstairs": 0.2031, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.6094, "Walking": 0.1875}
              };
            } else {
              return {
                activity: "Walking",
                confidence: 0.6624,
                probabilities: {"Downstairs": 0.0955, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.242, "Walking": 0.6624}
              };
            }
          } else {
            if (ymean <= 9.573500) {
              return {
                activity: "Downstairs",
                confidence: 0.6977,
                probabilities: {"Downstairs": 0.6977, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.1395, "Walking": 0.1628}
              };
            } else {
              return {
                activity: "Upstairs",
                confidence: 0.7273,
                probabilities: {"Downstairs": 0.1818, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.7273, "Walking": 0.0909}
              };
            }
          }
        }
      } else {
        if (ymean <= 3.390725) {
          if (xdev <= 5.366645) {
            if (zmean <= -0.222925) {
              return {
                activity: "Upstairs",
                confidence: 0.5455,
                probabilities: {"Downstairs": 0.2727, "Jogging": 0.1364, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.5455, "Walking": 0.0455}
              };
            } else {
              return {
                activity: "Walking",
                confidence: 0.9200,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.08, "Walking": 0.92}
              };
            }
          } else {
            if (zmean <= -2.862950) {
              return {
                activity: "Upstairs",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 1.0, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Jogging",
                confidence: 0.8958,
                probabilities: {"Downstairs": 0.0312, "Jogging": 0.8958, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0729, "Walking": 0.0}
              };
            }
          }
        } else {
          if (zmean <= 2.383118) {
            if (zmean <= -1.833675) {
              return {
                activity: "Downstairs",
                confidence: 0.4474,
                probabilities: {"Downstairs": 0.4474, "Jogging": 0.0789, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.3684, "Walking": 0.1053}
              };
            } else {
              return {
                activity: "Walking",
                confidence: 0.8374,
                probabilities: {"Downstairs": 0.0781, "Jogging": 0.0129, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0716, "Walking": 0.8374}
              };
            }
          } else {
            if (xdev <= 2.043053) {
              return {
                activity: "Upstairs",
                confidence: 0.9200,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.08, "Standing": 0.0, "Upstairs": 0.92, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Downstairs",
                confidence: 0.7925,
                probabilities: {"Downstairs": 0.7925, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.1698, "Walking": 0.0377}
              };
            }
          }
        }
      }
    }
  } else {
    if (zmean <= -4.229250) {
      return {
        activity: "Walking",
        confidence: 1.0000,
        probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 1.0}
      };
    } else {
      if (zmean <= 2.386225) {
        if (ydev <= 6.866797) {
          if (zdev <= 5.255377) {
            if (ymean <= 7.217350) {
              return {
                activity: "Upstairs",
                confidence: 0.6500,
                probabilities: {"Downstairs": 0.15, "Jogging": 0.2, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.65, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Jogging",
                confidence: 0.6667,
                probabilities: {"Downstairs": 0.1333, "Jogging": 0.6667, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.1, "Walking": 0.1}
              };
            }
          } else {
            if (ymean <= 6.521425) {
              return {
                activity: "Jogging",
                confidence: 1.0000,
                probabilities: {"Downstairs": 0.0, "Jogging": 1.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Jogging",
                confidence: 0.6000,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.6, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.4, "Walking": 0.0}
              };
            }
          }
        } else {
          if (zdev <= 2.330840) {
            return {
              activity: "Downstairs",
              confidence: 1.0000,
              probabilities: {"Downstairs": 1.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
            };
          } else {
            if (ydev <= 7.696101) {
              return {
                activity: "Jogging",
                confidence: 0.9250,
                probabilities: {"Downstairs": 0.005, "Jogging": 0.925, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.07, "Walking": 0.0}
              };
            } else {
              return {
                activity: "Jogging",
                confidence: 0.9990,
                probabilities: {"Downstairs": 0.0, "Jogging": 0.999, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.001, "Walking": 0.0}
              };
            }
          }
        }
      } else {
        if (ydev <= 8.093534) {
          return {
            activity: "Upstairs",
            confidence: 1.0000,
            probabilities: {"Downstairs": 0.0, "Jogging": 0.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 1.0, "Walking": 0.0}
          };
        } else {
          return {
            activity: "Jogging",
            confidence: 1.0000,
            probabilities: {"Downstairs": 0.0, "Jogging": 1.0, "Sitting": 0.0, "Standing": 0.0, "Upstairs": 0.0, "Walking": 0.0}
          };
        }
      }
    }
  }
}

// Export for Node.js if available, otherwise attach to window
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { classifyActivity };
} else if (typeof window !== 'undefined') {
  window.classifyActivity = classifyActivity;
}
