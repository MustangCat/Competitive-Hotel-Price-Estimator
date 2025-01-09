import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.title("Competitive Hotel Price Estimator")
st.markdown("""
Upload your hotel pricing data to compare and analyze price competitiveness with other hotels in the area.
""")

# File uploader for hotel pricing data
uploaded_file = st.file_uploader("Upload CSV", type=".csv")

# Checkbox to use example file
use_example_file = st.checkbox(
    "Use example file", True, help="Use in-built example file to demo the app"
)

# Default example file values
hotel_data_example = "local_hotel_ota_sample.csv"

if use_example_file:
    uploaded_file = hotel_data_example

# Processing the uploaded or example file
if uploaded_file:
    try:
        # Read the uploaded file
        df = pd.read_csv(uploaded_file)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date

        st.markdown("### Data preview")
        st.dataframe(df.head())

        # Date range slider
        st.markdown("### Filter by Date Range")
        min_date = pd.to_datetime(df['Date']).min().date()
        max_date = pd.to_datetime(df['Date']).max().date()
        start_date, end_date = st.slider(
            "Select Date Range",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date),
            format="YYYY-MM-DD"
        )
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

        # Segment filter by Room_Type
        st.markdown("### Filter by Room Type")
        room_types = df["Room_Type"].unique()
        selected_room_types = st.multiselect("Select Room Types", options=room_types, default=room_types, key='room_type_filter')

        # Filter the dataframe based on selected room types
        filtered_df = df[df["Room_Type"].isin(selected_room_types)]

        # KPI Cards
        st.markdown("### Key Performance Indicators")
        col1, col2, col3 = st.columns(3)
        total_revenue = filtered_df['Price'].sum()
        total_quantity = filtered_df['Quantity_Sold'].sum()
        avg_occupancy = filtered_df['Occupancy_Rate'].str.rstrip('%').astype(float).mean()

        prev_start_date = start_date - (end_date - start_date)
        prev_end_date = start_date
        prev_df = filtered_df[(filtered_df['Date'] >= prev_start_date) & (filtered_df['Date'] < prev_end_date)]
        prev_revenue = prev_df['Price'].sum() if not prev_df.empty else 0
        prev_quantity = prev_df['Quantity_Sold'].sum() if not prev_df.empty else 0
        prev_avg_occupancy = prev_df['Occupancy_Rate'].str.rstrip('%').astype(float).mean() if not prev_df.empty else 0

        col1.metric("Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("Quantity Sold", f"{total_quantity}")
        col3.metric("Avg Occupancy Rate", f"{avg_occupancy:.2f}%")

        # Analysis 1: Average price by room type
        avg_price_by_room = filtered_df.groupby("Room_Type")["Price"].mean().sort_values()
        st.markdown("### Average Price by Room Type")
        st.bar_chart(avg_price_by_room)

        # Analysis 2: Comparison of average prices (hotel vs competitors)
        avg_price = filtered_df["Price"].mean()
        avg_competitor_price = filtered_df["Competitor_Price"].mean()

        st.markdown("### Price Comparison")
        st.write(f"**Average Hotel Price:** ${avg_price:.2f}")
        st.write(f"**Average Competitor Price:** ${avg_competitor_price:.2f}")
        
        # Analysis 3: Occupancy rate visualization
        filtered_df["Occupancy_Rate"] = filtered_df["Occupancy_Rate"].str.rstrip('%').astype(float)
        fig, ax = plt.subplots(figsize=(12, 6))
        filtered_df.plot(x="Date", y="Occupancy_Rate", kind="line", ax=ax, color='blue', alpha=0.7)
        ax.set_title("Occupancy Rate Over Time", fontsize=14)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Occupancy Rate (%)", fontsize=12)
        ax.grid(True)
        st.pyplot(fig)

        # Insight
        st.markdown("### Insight: Occupancy Rate")
        avg_occupancy = filtered_df["Occupancy_Rate"].mean()
        st.write(f"The average occupancy rate over the selected period is **{avg_occupancy:.2f}%**.")
        st.write("There are noticeable fluctuations in occupancy rate, which could be influenced by seasonal trends or local events.")

        # Additional Analysis 1: Revenue Analysis
        filtered_df['Revenue'] = filtered_df['Price'] * filtered_df['Quantity_Sold']
        st.markdown("### Revenue Over Time")
        fig, ax = plt.subplots(figsize=(12, 6))
        filtered_df.plot(x="Date", y="Revenue", kind="line", ax=ax, color='green', alpha=0.7)
        ax.set_title("Revenue Over Time", fontsize=14)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Revenue ($)", fontsize=12)
        ax.grid(True)
        st.pyplot(fig)
        st.write(f"The total revenue over the selected period is **${filtered_df['Revenue'].sum():.2f}**.")

        # Additional Analysis 2: Occupancy Rate by Day of the Week
        st.markdown("### Occupancy Rate by Day of the Week")
        avg_occupancy_by_day = filtered_df.groupby("Day_of_Week")["Occupancy_Rate"].mean().reindex([
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ])
        fig, ax = plt.subplots(figsize=(10, 6))
        avg_occupancy_by_day.plot(kind='line', marker='o', ax=ax, color='orange', alpha=0.8)
        ax.set_title("Average Occupancy Rate by Day of the Week", fontsize=14)
        ax.set_xlabel("Day of the Week", fontsize=12)
        ax.set_ylabel("Occupancy Rate (%)", fontsize=12)
        ax.grid(True)
        st.pyplot(fig)

        # Additional Analysis 3: Lead Time Analysis
        st.markdown("### Lead Time Analysis")
        fig, ax = plt.subplots(figsize=(12, 6))
        filtered_df['Lead_Time'].plot(kind='hist', bins=20, ax=ax, color='purple', alpha=0.7)
        ax.set_title("Distribution of Lead Time", fontsize=14)
        ax.set_xlabel("Lead Time (Days)", fontsize=12)
        ax.set_ylabel("Frequency", fontsize=12)
        ax.grid(True)
        st.pyplot(fig)
        st.write(f"The average lead time for bookings is **{filtered_df['Lead_Time'].mean():.2f} days**.")

        # Additional Analysis 4: Promotion Effectiveness
        st.markdown("### Promotion Effectiveness")
        avg_revenue_by_promotion = filtered_df.groupby("Promotion")["Revenue"].mean().sort_values()
        st.bar_chart(avg_revenue_by_promotion)
        st.write("This analysis shows the average revenue generated by different types of promotions.")

        # Additional Analysis 5: Price vs. Competitor Price Correlation
        st.markdown("### Price vs. Competitor Price Correlation")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(filtered_df["Price"], filtered_df["Competitor_Price"], alpha=0.7)
        ax.set_title("Price vs. Competitor Price Correlation", fontsize=14)
        ax.set_xlabel("Hotel Price ($)")
        ax.set_ylabel("Competitor Price ($)")
        ax.grid(True)
        st.pyplot(fig)

        # Additional Analysis 6: Event Impact on Occupancy
        st.markdown("### Event Impact on Occupancy")
        avg_occupancy_with_event = filtered_df[filtered_df["Event_Nearby"] != "None"]["Occupancy_Rate"].mean()
        avg_occupancy_without_event = filtered_df[filtered_df["Event_Nearby"] == "None"]["Occupancy_Rate"].mean()
        st.write(f"**Average Occupancy with Nearby Events:** {avg_occupancy_with_event:.2f}%")
        st.write(f"**Average Occupancy without Nearby Events:** {avg_occupancy_without_event:.2f}%")
        st.write("This analysis shows how nearby events influence occupancy rates.")

        # Step for Price Elasticity Calculator
        st.markdown("### Price Elasticity of Demand Calculator")
        st.markdown("""
        This tool calculates the price elasticity of demand based on changes in price and quantity sold.
        Enter two data points (initial and new price, initial and new quantity sold) to compute the elasticity.
        """)

        col1, col2 = st.columns(2)
        with col1:
            initial_price = st.number_input("Initial Price", min_value=0.0, format="%.2f")
            new_price = st.number_input("New Price", min_value=0.0, format="%.2f")
        with col2:
            initial_quantity = st.number_input("Initial Quantity Sold", min_value=0)
            new_quantity = st.number_input("New Quantity Sold", min_value=0)

        if initial_price > 0 and new_price > 0 and initial_quantity > 0 and new_quantity > 0:
            # Calculate percentage changes
            price_change = (new_price - initial_price) / initial_price
            quantity_change = (new_quantity - initial_quantity) / initial_quantity

            # Calculate price elasticity of demand
            elasticity = quantity_change / price_change

            st.markdown("### Price Elasticity Result")
            st.write(f"**Price Elasticity of Demand:** {elasticity:.2f}")

            # Interpretation of elasticity
            if abs(elasticity) > 1:
                st.write("The demand is **elastic**: consumers are sensitive to price changes.")
            elif abs(elasticity) < 1:
                st.write("The demand is **inelastic**: consumers are less sensitive to price changes.")
            else:
                st.write("The demand is **unit elastic**: proportional change in quantity to price.")

            # Visualization of demand curve
            fig,ax = plt.subplots()
            prices = np.linspace(initial_price, new_price, 100)
            quantities = initial_quantity * (1 + elasticity * ((prices - initial_price) / initial_price))
            ax.plot(prices, quantities, label="Demand Curve")
            ax.scatter([initial_price, new_price], [initial_quantity, new_quantity], color="red", zorder=5)
            ax.set_xlabel("Price")
            ax.set_ylabel("Quantity Sold")
            ax.set_title("Demand Curve Visualization")
            ax.legend()
            st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error reading file: {e}")
