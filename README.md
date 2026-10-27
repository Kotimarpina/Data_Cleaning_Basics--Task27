Task 27 – Date Cleaning Basics

Project Overview

This project is part of my Data Analytics Internship at Veda Technology.

The goal of this task was to clean inconsistent date formats in a retail sales dataset and identify invalid or missing dates. I used Python with Pandas to process the dates and Excel to review the original data, cleaned output, and issue log.

Date cleaning is an important step in data preprocessing because inconsistent or invalid dates can affect sorting, filtering, time-based analysis, and reporting.

Objectives

- Standardize dates into a consistent format.
- Identify invalid dates and missing values.
- Maintain an issue log for records that need attention.
- Compare the original date values with the cleaned output.
- Practise date handling using Python, Pandas, and Excel.

Tools Used

- Python – Data processing
- Pandas – Reading, parsing, and cleaning dates
- Microsoft Excel – Reviewing the dataset and results

Dataset

A synthetic retail sales dataset was created for this task. It contains 25 sample order records with fields such as:

- Order ID
- Order Date (Raw)
- Customer ID
- Product
- Region
- Sales

The raw date column contains different formats, two intentionally invalid dates, and one missing date.

Cleaning Process

1. Parsing Different Date Formats

Used Pandas to convert date strings into a consistent date type.

pd.to_datetime(value, errors="coerce", dayfirst=True)

The "dayfirst=True" setting interprets ambiguous numeric dates using a day-first convention. The expected date convention should always be confirmed against the source dataset.

2. Identifying Invalid Dates

Used "errors="coerce"" so values that cannot be parsed become "NaT" (Not a Time).

For example, "31/02/2026" is not a valid calendar date and is flagged for review rather than automatically corrected.

3. Identifying Missing Dates

Blank date values are labelled as missing so they can be investigated separately from invalid dates.

4. Creating an Issue Log

Records with invalid or missing dates are added to a separate issue log with a recommended next action. This helps keep track of records that require verification.

Results

The script was run on the 25-row practice dataset.

Date status| Records
Valid dates| 22
Invalid dates| 2
Missing dates| 1
Total records| 25

Invalid and missing dates are flagged for review. They are not assigned guessed replacement dates.

Files in This Repository

File| Description
"Task_27_Date_Cleaning_Basics.py"| Python script for parsing dates and generating an issue log
"retail_sales_dirty_dates.csv"| Original practice dataset with mixed date formats
"retail_sales_cleaned_dates.csv"| Dataset containing the parsed date column and date status
"date_issue_log.csv"| Records with invalid or missing dates and recommended actions
"Veda_Technology_Task_27_Date_Cleaning_Basics.xlsx"| Excel workbook with raw data, cleaned dates, issue log, and summary

How to Run the Project

Step 1: Install Pandas

pip install pandas

Step 2: Download the Files

Keep the Python script and "retail_sales_dirty_dates.csv" in the same folder.

Step 3: Run the Script

python Task_27_Date_Cleaning_Basics.py

The script generates:

- "retail_sales_cleaned_dates.csv"
- "date_issue_log.csv"

You can also provide custom input and output paths:

python Task_27_Date_Cleaning_Basics.py input.csv cleaned.csv

The input CSV must contain the required "Order Date (Raw)" column.

What I Learned

Through this task, I practised handling different date formats with Pandas and learned how to distinguish valid, invalid, and missing dates.

I also learned why it is important to check the source date convention before parsing ambiguous values and to maintain an issue log instead of making unsupported corrections.

Conclusion

This task provided practical experience in date cleaning and basic data-quality checks. The cleaned output and issue log make it easier to identify records that are ready for analysis and records that need further verification.

---

Internship: Veda Technology
Track: Data Analytics
Task: 27 – Date Cleaning Basics
Tools: Python, Pandas, Microsoft Excel
