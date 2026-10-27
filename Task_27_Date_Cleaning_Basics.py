"""Task 27 – Date Cleaning Basics | Veda Technology
Cleans mixed-format dates, flags invalid/missing dates, and creates an issue log.
Requires pandas: pip install pandas
Run: python Task_27_Date_Cleaning_Basics.py
Optional: python Task_27_Date_Cleaning_Basics.py input.csv cleaned.csv
"""
import sys
from pathlib import Path
import pandas as pd

RAW_DATE_COLUMN = "Order Date (Raw)"

def parse_date(value):
    """Parse using day-first convention; invalid or blank values become NaT."""
    if pd.isna(value) or not str(value).strip():
        return pd.NaT
    return pd.to_datetime(str(value).strip(), errors="coerce", dayfirst=True)

def clean_dates(df):
    df = df.copy()
    if RAW_DATE_COLUMN not in df.columns:
        raise ValueError(f"Required column not found: {RAW_DATE_COLUMN}")
    df["Order Date (Clean)"] = df[RAW_DATE_COLUMN].map(parse_date)
    raw_text = df[RAW_DATE_COLUMN].fillna("").astype(str).str.strip()
    df["Date Status"] = "Valid"
    df.loc[raw_text.eq(""), "Date Status"] = "Missing"
    df.loc[raw_text.ne("") & df["Order Date (Clean)"].isna(), "Date Status"] = "Invalid"
    return df

def main():
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("retail_sales_dirty_dates.csv")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("retail_sales_cleaned_dates.csv")
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    result = clean_dates(pd.read_csv(input_path))
    result.to_csv(output_path, index=False, date_format="%Y-%m-%d")
    issues = result[result["Date Status"] != "Valid"][["Order ID", RAW_DATE_COLUMN, "Date Status"]].copy()
    issues["Recommended Action"] = issues["Date Status"].map({
        "Invalid": "Check the original source record before correcting.",
        "Missing": "Recover the missing date from the original source."
    })
    issue_path = output_path.with_name("date_issue_log.csv")
    issues.to_csv(issue_path, index=False)
    print(f"Rows processed: {len(result)}")
    print(f"Valid dates: {(result['Date Status'] == 'Valid').sum()}")
    print(f"Invalid dates: {(result['Date Status'] == 'Invalid').sum()}")
    print(f"Missing dates: {(result['Date Status'] == 'Missing').sum()}")
    print(f"Cleaned data: {output_path.resolve()}")
    print(f"Issue log: {issue_path.resolve()}")

if __name__ == "__main__":
    main()
