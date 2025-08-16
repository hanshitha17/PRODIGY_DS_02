# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- SETTINGS ----------
INPUT_FILE = "train.csv"      # Make sure train.csv is in the same folder as this script
OUTPUT_DIR = "eda_outputs"    # where cleaned data & plots are saved
# ------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load dataset
    print(f"Loading {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)

    # Show basic info
    print("\n--- DATA INFO ---")
    print(df.info())
    print("\n--- MISSING VALUES ---")
    print(df.isna().sum())

    # Handle missing values (numeric → median, categorical → mode)
    for col in df.select_dtypes(include="number"):
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(exclude="number"):
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna("Unknown")

    # Remove duplicates
    df = df.drop_duplicates()

    # Save cleaned dataset
    cleaned_file = os.path.join(OUTPUT_DIR, "cleaned_train.csv")
    df.to_csv(cleaned_file, index=False)
    print(f"\nCleaned data saved to {cleaned_file}")

    # Summary statistics
    summary = df.describe(include="all").transpose()
    summary.to_csv(os.path.join(OUTPUT_DIR, "summary.csv"))
    print(f"Summary saved to {OUTPUT_DIR}/summary.csv")

    # Basic plots
    # 1. Correlation heatmap
    if not df.select_dtypes(include="number").empty:
        plt.figure(figsize=(8,6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
        plt.close()

    # 2. Histogram of numeric columns
    for col in df.select_dtypes(include="number").columns[:5]:  # limit to 5
        plt.figure()
        df[col].hist(bins=30)
        plt.title(f"Histogram of {col}")
        plt.savefig(os.path.join(OUTPUT_DIR, f"hist_{col}.png"))
        plt.close()

    # 3. Bar plot for categorical columns
    for col in df.select_dtypes(exclude="number").columns[:3]:  # limit to 3
        plt.figure(figsize=(8,4))
        df[col].value_counts().head(10).plot(kind="bar")
        plt.title(f"Top categories of {col}")
        plt.savefig(os.path.join(OUTPUT_DIR, f"bar_{col}.png"))
        plt.close()

    print("\nEDA complete! Check the 'eda_outputs' folder for results.")

if __name__ == "__main__":
    main()
