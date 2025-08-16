# PRODIGY_DS_02

---

# 📊 EDA Project – `train.csv`

This project performs **data cleaning** and **exploratory data analysis (EDA)** on the provided dataset (`train.csv`).
The script automatically cleans missing values, removes duplicates, generates summary statistics, and creates basic plots to explore relationships between variables.

---

## 🚀 Features

* Loads the dataset (`train.csv`)
* Cleans data:

  * Fills missing values (median for numbers, mode for categorical)
  * Removes duplicates
* Saves a cleaned dataset (`eda_outputs/cleaned_train.csv`)
* Generates:

  * Summary statistics (`eda_outputs/summary.csv`)
  * Correlation heatmap
  * Histograms (numeric columns)
  * Bar plots (categorical columns)

---

## 📂 Project Structure

```
PRODIGY_DS_02/
├── train.csv          # input dataset
├── eda.py             # main script
├── README.md          # project documentation
├── requirements.txt   # dependencies (pandas, matplotlib, seaborn)
└── eda_outputs/       # generated outputs
    ├── cleaned_train.csv
    ├── summary.csv
    ├── correlation_heatmap.png
    ├── hist_<col>.png
    ├── bar_<col>.png
```

---
