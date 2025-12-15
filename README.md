# 📊 Amazon Sales Analytics Dashboard

### **Overview**
In the world of E-commerce, raw data is abundant, but actionable insights are rare. I built this project to bridge that gap. 

This is an end-to-end data analytics application that transforms over **19,000+ raw transaction records** into a live, interactive dashboard. Instead of relying on static Excel reports, this tool allows stakeholders to filter sales performance by category, track revenue trends in real-time, and view predictive sales forecasts.

The goal was simple: move beyond "what happened" and start answering "what is the trend?" using Python-based data engineering.

**[🔴 View Live Dashboard Here]([https://share.streamlit.io](https://amazon-sales-dashboard-gtdviz4cd8r73hbjwbjv3z.streamlit.app/))** 
---

### **✨ Key Features**
* **Interactive Sales Forecasting:** Implemented a **30-Day Moving Average** algorithm to smooth out daily volatility and visualize long-term business trends.
* **Dynamic Filtering:** Users can slice and dice the data by **Product Category**, instantly updating all KPIs and charts without reloading the page.
* **Automated Data Cleaning:** The system automatically handles missing values (cancelled orders) and standardizes date formats, ensuring 100% reporting accuracy.
* **Business KPIs:** Real-time tracking of Total Revenue, Order Volume, and Average Order Value (AOV).
* **Market Insights:** Visual breakdown of top-selling categories (e.g., Kurtas, Western Dresses) and size distribution analysis.

---

### **⚙️ How It Works (Technical Deep Dive)**
The application follows a standard Data Science pipeline: **ETL (Extract, Transform, Load) → Analysis → Visualization.**

#### **1. Data Extraction & Cleaning (Pandas)**
The raw dataset (`Amazon_Sales.xlsx`) contained significant noise, including unformatted dates and incomplete transactions. 
* **Date Parsing:** I used `pd.to_datetime()` with error coercion to convert text-based dates into valid Timestamp objects, enabling time-series analysis.
* **Handling Nulls:** Transactions with missing `Amount` or `Status` were filtered out to prevent skewed revenue calculations.

#### **2. The Analytics Engine**
Once the data is clean, the Python script performs aggregations:
* **Trend Analysis:** The system groups sales by day and calculates a rolling average. This helps identify if the business is growing despite daily fluctuations.
* **Category Segmentation:** Transactions are grouped by Product Family to identify high-performing inventory.

#### **3. The Frontend (Streamlit & Plotly)**
* **Streamlit** handles the user interface, creating a reactive web experience where Python scripts run in the background.
* **Plotly Express** is used for rendering charts. Unlike static images, these charts allow users to hover over data points to see exact revenue figures and zoom into specific time periods (e.g., the sales peak in May 2022).

---

### **🛠️ Tech Stack**
* **Language:** Python 3.11
* **Dashboard Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Plotly Express
* **Version Control:** Git & GitHub

---

### **🚀 How to Run Locally**
If you want to run this dashboard on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/amazon-sales-dashboard.git](https://github.com/your-username/amazon-sales-dashboard.git)

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py

📈 Project Insights
Through this analysis, I uncovered several key business findings:

Seasonal Peaks: Sales volume reached its highest point in May 2022, suggesting a strong correlation with mid-year sales events.

Category Dominance: Kurtas and Western Dresses account for the majority of revenue, indicating a strong customer preference for ethnic and fusion wear.

Order Size: The majority of orders consist of single items, but there is a significant cluster of multi-item orders (~2,500) suitable for future Market Basket Analysis.

📬 Contact
Built by Satyaban Jena Aspiring Data Engineer | B.Tech CSE Final Year
