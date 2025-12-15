import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. SETUP THE PAGE ---
st.set_page_config(page_title="Amazon Sales Analytics", layout="wide")
st.title("📊 E-Commerce Sales Analytics Dashboard")
st.markdown("### Interactive Insights from Amazon Sales Data")

# --- 2. LOAD DATA (Cached for speed) ---
@st.cache_data
def load_data():
    # REPLACE with your exact file name
    df = pd.read_excel('Amazon_Sales.xlsx')
    
    # Cleaning
    df.drop(columns=['index', 'Unnamed: 22'], inplace=True, errors='ignore')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Amount', 'Date'], inplace=True)
    
    # Feature Engineering
    df['Month'] = df['Date'].dt.month_name()
    df['Year'] = df['Date'].dt.year
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

# --- 3. SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()[:3] # Default selects first 3
)

# Filter the dataframe based on selection
filtered_df = df[df['Category'].isin(selected_category)]

# --- 4. KEY METRICS (KPIs) ---
total_revenue = filtered_df['Amount'].sum()
total_orders = len(filtered_df)
avg_order_value = filtered_df['Amount'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders}")
col3.metric("Avg Order Value", f"₹{avg_order_value:.0f}")

st.markdown("---")

# --- 5. CHARTS & INSIGHTS ---

# Row 1: Sales Trend + Forecast
st.subheader("📈 Sales Trend & 30-Day Forecast")

# Calculate the Moving Average (Trend)
daily_sales = filtered_df.groupby('Date')['Amount'].sum().reset_index()
daily_sales['Trend'] = daily_sales['Amount'].rolling(window=30).mean()

# Create the chart with two lines: Actual Sales and Trend
fig_trend = px.line(daily_sales, x='Date', y=['Amount', 'Trend'], 
                    labels={'value': 'Revenue (INR)', 'variable': 'Metric'},
                    color_discrete_map={'Amount': 'lightblue', 'Trend': 'red'})

st.plotly_chart(fig_trend, use_container_width=True)

# Row 2: Category & Size Analysis
col4, col5 = st.columns(2)

with col4:
    st.subheader("🏆 Top Selling Categories")
    category_sales = filtered_df.groupby('Category')['Amount'].sum().reset_index().sort_values('Amount', ascending=False)
    fig_cat = px.bar(category_sales, x='Category', y='Amount', color='Amount', template="plotly_white")
    st.plotly_chart(fig_cat, use_container_width=True)

with col5:
    st.subheader("📦 Sales by Size")
    size_sales = filtered_df.groupby('Size')['Qty'].sum().reset_index()
    fig_size = px.pie(size_sales, names='Size', values='Qty', hole=0.4)
    st.plotly_chart(fig_size, use_container_width=True)

# Row 3: Data View
with st.expander("View Raw Data"):
    st.dataframe(filtered_df.head(100))