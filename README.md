# ACC102-Track4-AAPL-Financial-Analysis
ACC102 Track4 Interactive Data Analysis Tool for Apple Inc. Financial &amp; Market Performance
# ACC102 Track4 Interactive Data Analysis Tool: Apple Inc. Financial & Market Performance
**Student ID: 2470786
**Module: ACC102 Accounting in a Digital Age**
**University: Xi'an Jiaotong-Liverpool University**

## 🎯 Project Overview
This is an interactive data analysis tool for Track4 of the ACC102 mini assignment. The project analyzes the financial performance and stock market performance of Apple Inc. (AAPL) from 2022 to 2025, using data from the WRDS Compustat and CRSP academic databases.

The tool is built with Streamlit, allowing users to interactively filter fiscal year ranges, select financial metrics, and view dynamic visualizations of the company's performance.

## 📊 Data Source
- **Financial Statement Data**: WRDS Compustat North America Funda Database (2022-2025 fiscal year consolidated financial statements)
- **Stock Trading Data**: WRDS CRSP Daily Stock File (dsf) (2020-2024 daily trading data)
- Data Access Date: 23 April 2026

## 📁 Repository Structure
├── ACC102_Track4_Assignment.ipynb # Core Python analysis Jupyter Notebook├── app.py # Streamlit interactive tool main file├── aapl_financial_metrics.csv # Calculated core financial metrics├── aapl_income_statement.csv # Income statement data├── aapl_balance_sheet.csv # Balance sheet data├── aapl_stock_price_data.csv # Stock price & return data├── requirements.txt # Required Python packages└── README.md # Project documentation
plaintext

## 🚀 How to Run the Tool Locally
1.  Clone this repository to your local machine
git clone [[https://github.com/YawenDing24/ACC102-Track4-AAPL-Financial-Analysis.git]
plaintext
2.  Navigate to the project folder
cd ACC102-Track4-AAPL-Financial-Analysis
plaintext
3.  Install required packages
pip install -r requirements.txt
plaintext
4.  Run the Streamlit app
streamlit run app.py
plaintext
5.  The tool will automatically open in your default browser at `http://localhost:8501`

## 📌 Core Analysis Content
1.  Core financial statements (Income Statement & Balance Sheet)
2.  Profitability metrics calculation: Gross Profit Margin, Net Profit Margin, ROE, ROA
3.  Solvency metrics calculation: Current Ratio, Debt to Asset Ratio
4.  Interactive trend visualizations for financial metrics
5.  Stock price trend and cumulative return analysis
6.  In-depth analysis of findings and limitations

## ⚠️ Disclaimer
This project is completed exclusively for the ACC102 course assignment, for academic purposes only. It does not constitute any investment advice, financial recommendation, or valuation opinion for Apple Inc.
