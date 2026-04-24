# ACC102 Track4 Interactive Data Analysis Tool: Apple Inc. Financial & Market Performance
import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# -------------------------- Page Configuration --------------------------
st.set_page_config(
    page_title="AAPL Financial Analysis | ACC102 Track4",
    page_icon="📊",
    layout="wide"
)

# -------------------------- Load Local Data (No WRDS Needed) --------------------------
@st.cache_data
def load_data():
    # Load all saved CSV data
    financial_metrics = pd.read_csv("aapl_financial_metrics.csv", index_col="fiscal_year")
    stock_data = pd.read_csv("aapl_stock_price_data.csv", index_col="date", parse_dates=True)
    income_stmt = pd.read_csv("aapl_income_statement.csv", index_col="fiscal_year")
    balance_sheet = pd.read_csv("aapl_balance_sheet.csv", index_col="fiscal_year")
    return financial_metrics, stock_data, income_stmt, balance_sheet

# Load data
financial_metrics, stock_data, income_stmt, balance_sheet = load_data()

# -------------------------- Page Header --------------------------
st.title("📊 Apple Inc. (AAPL) Financial & Market Performance Analysis")
st.subheader("ACC102 Track4 Interactive Data Analysis Tool")
st.markdown("---")

# -------------------------- Sidebar Interactive Controls --------------------------
st.sidebar.header("⚙️ Analysis Controls")
# Year range selector
year_range = st.sidebar.slider(
    "Select Fiscal Year Range",
    min_value=int(financial_metrics.index.min()),
    max_value=int(financial_metrics.index.max()),
    value=(int(financial_metrics.index.min()), int(financial_metrics.index.max()))
)
# Metric selector for charts
selected_profit_metrics = st.sidebar.multiselect(
    "Select Profitability Metrics to Display",
    options=financial_metrics.columns[:4].tolist(),
    default=financial_metrics.columns[:4].tolist()
)
selected_solvency_metrics = st.sidebar.multiselect(
    "Select Solvency Metrics to Display",
    options=financial_metrics.columns[4:].tolist(),
    default=financial_metrics.columns[4:].tolist()
)

# Filter data by selected year range
filtered_metrics = financial_metrics.loc[year_range[0]:year_range[1]]

# -------------------------- 1. Core Financial Statements Section --------------------------
st.header("📑 Core Financial Statements")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Income Statement (USD Millions)")
    st.dataframe(income_stmt.loc[year_range[0]:year_range[1]], use_container_width=True)

with col2:
    st.subheader("Balance Sheet (USD Millions)")
    st.dataframe(balance_sheet.loc[year_range[0]:year_range[1]], use_container_width=True)

st.markdown("---")

# -------------------------- 2. Core Financial Metrics Section --------------------------
st.header("📈 Core Financial Metrics")
st.subheader("Calculated per ACC102 Course Requirements")
st.dataframe(filtered_metrics, use_container_width=True)

# Interactive Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Profitability Metrics Trend")
    profit_fig = px.line(
        filtered_metrics,
        x=filtered_metrics.index,
        y=selected_profit_metrics,
        labels={"value": "Percentage (%)", "index": "Fiscal Year", "variable": "Metric"},
        height=400
    )
    st.plotly_chart(profit_fig, use_container_width=True)

with col2:
    st.subheader("Solvency Metrics Trend")
    solvency_fig = px.bar(
        filtered_metrics,
        x=filtered_metrics.index,
        y=selected_solvency_metrics,
        barmode="group",
        labels={"value": "Metric Value", "index": "Fiscal Year", "variable": "Metric"},
        height=400
    )
    st.plotly_chart(solvency_fig, use_container_width=True)

st.markdown("---")

# -------------------------- 3. Stock Market Performance Section --------------------------
st.header("📈 Stock Market Performance (2020-2024)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Close Price Trend")
    price_fig = px.line(
        stock_data,
        x=stock_data.index,
        y="close",
        labels={"close": "Stock Price (USD)", "index": "Date"},
        height=400
    )
    st.plotly_chart(price_fig, use_container_width=True)

with col2:
    st.subheader("5-Year Cumulative Return")
    return_fig = px.line(
        stock_data,
        x=stock_data.index,
        y="Cumulative Return",
        labels={"Cumulative Return": "Cumulative Return", "index": "Date"},
        height=400
    )
    return_fig.update_layout(yaxis_tickformat=".0%")
    st.plotly_chart(return_fig, use_container_width=True)

st.markdown("---")

# -------------------------- 4. Analysis & Conclusion Section --------------------------
st.header("🔍 Key Analysis & Conclusion")
st.markdown("""
1.  **Profitability Performance**: Apple Inc. maintained stable and strong profitability from 2022 to 2025. The company's gross profit margin stayed at around 45%-49%, net profit margin remained above 23%, and ROE consistently exceeded 150%, reflecting excellent cost control ability and outstanding shareholder value creation capacity.
2.  **Solvency & Financial Health**: Apple's current ratio stayed at a healthy level above 0.8, and debt-to-asset ratio was controlled within 80%, indicating the company has sufficient short-term liquidity to cover current liabilities, and a stable long-term capital structure with controllable financial risk.
3.  **Market Performance**: From 2020 to 2024, Apple's stock price showed an overall upward trend, with a positive cumulative return over the 5-year period, which is consistent with its stable profitability performance, reflecting the capital market's long-term recognition of the company's operational strength and business stability.
""")

st.header("⚠️ Analysis Limitations")
st.markdown("""
1.  This analysis only uses annual financial data, which cannot reflect seasonal fluctuations of Apple's business.
2.  The analysis only focuses on Apple's own performance, without in-depth peer comparison and industry benchmarking.
3.  The analysis does not consider the impact of macroeconomic factors (exchange rate fluctuations, supply chain changes, interest rate changes) on the company's performance.
4.  The stock return analysis only covers the 2020-2024 period, affected by the specific market environment of the period.
""")

st.markdown("---")
st.caption("Data Source: WRDS Compustat & CRSP Databases | For ACC102 Academic Assignment Only")
st.caption("Disclaimer: This tool does not constitute any investment advice or financial recommendation.")