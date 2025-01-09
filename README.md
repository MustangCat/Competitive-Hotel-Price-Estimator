# Competitive-Hotel-Price-Estimator

This Streamlit app, Competitive Hotel Price Estimator, is designed to help local hotels compare their pricing strategies with competitors and gain insights into demand patterns. The app allows users to upload hotel pricing data and provides interactive analysis, visualizations, and key metrics to improve hotel pricing decisions.

## Objective

The objective of this app is to assist local hotels in understanding their competitive positioning in the market by comparing:
- Room prices with competitor prices.
- Occupancy rates over time and during local events.
- The effectiveness of promotions and lead time patterns.

## Features

1. **Data Upload:** Users can upload a CSV file containing hotel pricing data or use an in-built example file.
2. **Filter by Room Type:** The app includes a multi-select filter to analyze specific room types.
3. **Interactive Data Visualizations:**
  - Average price by room type.
  - Occupancy rate over time.
  - Revenue over time.
  - Occupancy rate by day of the week.
  - Lead time distribution.
  - Promotion effectiveness.
  - Price vs. competitor price correlation.
  - Event impact on occupancy rates.
4. **Price Elasticity of Demand Calculator:** This tool helps hotels understand how sensitive demand is to changes in price.


## How to Use
1. **Upload Data:** Upload a CSV file with the following columns:
   
    `Date`: Date of the booking.
  
    `Room_Type`: Type of room (e.g., Suite, Deluxe, Standard).
  
    `Price`: Price per room.
  
    `Competitor_Price`: Competitor's price for a similar room type.
  
    `Occupancy_Rate`: Occupancy rate as a percentage.
  
    `Quantity_Sold`: Number of rooms sold.
  
    `Lead_Time`: Number of days between booking and stay.
    
    `Promotion`: Type of promotion offered.
  
    `Event_Nearby`: Whether there was an event nearby.
  
3. **Explore Visualizations:** Use the filter and explore various insights provided by the app.
4. **Calculate Price Elasticity:** Input initial and new price and quantity values to calculate price elasticity of demand.


## Example Analysis
  **Key Performance Indicators** see KPI cards that include total revenue, quanlity sold, and occupancy rate.
  ![image](https://github.com/user-attachments/assets/bba157f7-f9e3-43a9-95b8-61fee3b01084)

  
  **Average Price by Room Type:** Quickly identify which room types have higher or lower average prices.
  ![image](https://github.com/user-attachments/assets/5c34cd9f-4e7e-49a7-9ff0-295e6c0f4166)

  
  **Revenue Analysis:** Visualize revenue trends over time to identify peak year weeks.
  ![image](https://github.com/user-attachments/assets/3b9f9a4a-2c50-42d0-8042-1ba1ac606fb3)


  **Occupancy Rate Analysis** Visualize occupancy rate by day of the week to optimize high-demand bookings
  ![image](https://github.com/user-attachments/assets/b8ec5e8f-6cc1-435e-b098-e086a883c177)
  ![image](https://github.com/user-attachments/assets/ea171fca-8369-4326-b64d-aa0431a9e60a)


  
  **Lead Time Distribution:** Understand booking patterns to optimize pricing for last-minute bookings.
  ![image](https://github.com/user-attachments/assets/7dffb804-e79d-4a76-af89-dac406554500)

  
  **Competitor Price Correlation:** See a correlation between own hotel and competitor prices.
  ![image](https://github.com/user-attachments/assets/d00ec9ee-045f-47ea-b32f-2481ee5330c6)

  
  **Event Impact on Occupancy:** See how local events influence hotel demand.
  ![image](https://github.com/user-attachments/assets/eabcb69d-b8c4-45d4-857b-00dc72515ee9)


## Requirements
- Python 3.7 or higher
- Streamlit
- Pandas
- Matplotlib
- Numpy


## Installation
1. Clone the repository:
`git clone https://github.com/your-username/competitive-hotel-price-estimator.git`
2. Navigate to the project directory:
`cd competitive-hotel-price-estimator`
3. Install the required dependencies:
`pip install -r requirements.txt`
4. Run the Streamlit app:
`streamlit run app.py`


## Future Improvements
  - Add machine learning models to predict future occupancy rates.
  - Include benchmarking against industry standards.
  - Add export functionality for analyzed reports.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or new features.
