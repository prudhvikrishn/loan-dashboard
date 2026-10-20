# Loan Data Dashboard

An interactive Streamlit dashboard for exploring a dataset of 367 loan applicants.

## What it shows

- **Area filter** in the sidebar (Urban, Semiurban, Rural); every chart updates to match.
- **Summary statistics** for all numeric columns.
- **Loan amount distribution** as a histogram with a density curve.
- **Loan amount by education** as a box plot (graduate vs not graduate).
- **Correlation heatmap** across the numeric and encoded columns.
- **Raw data** table, shown on request.

## Data preparation

`loan_test.csv` has 11 columns: gender, marital status, dependents, education, self-employment, applicant and co-applicant income, loan amount, loan term, credit history and property area.

Before charting, the app:
- fills missing applicant income and loan amount with the median, missing co-applicant income with 0, and missing credit history with 1;
- converts "3+" dependents to 3;
- encodes yes/no and category columns as numbers so they appear in the correlation heatmap;
- adds a `Total_Income` column (applicant + co-applicant income).

## Run it

```
pip install -r requirements.txt
streamlit run loan_dashboard.py
```

## Tech stack

Python, pandas, Streamlit, seaborn, Matplotlib.
