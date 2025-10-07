# project-phonepe-transaction

#PhonePe Digital Payment Data Analysis & Dashboard
#Project Overview
With increasing reliance on digital payment systems like PhonePe, understanding transaction dynamics, user engagement, and insurance data is crucial for service improvement and user targeting. This project extracts, analyzes, and visualizes PhonePe aggregate datasets across payment categories, insurance, geographical trends, and user activity. The final deliverable is an interactive Streamlit dashboard for real-time exploration and insights.
#Approach
#Data Extraction & ETL
#Clone PhonePe Pulse Dataset.

ETL process using Python (pandas) to load/transform data.

#SQL Database & Tables
Set up MySQL.

Aggregated Tables: Aggregated_user, Aggregated_transaction, Aggregated_insurance

Map Tables: Map_user, Map_map, Map_insurance

Top Tables: Top_user, Top_map, Top_insurance

Store data using well-structured schemas.

#SQL Data Analysis
Write SQL queries for all business cases.
Sample queries included for segmentation, fraud, region, retention, and benchmarking.

Analysis & Visualization
Use Python (pandas, matplotlib, seaborn) to process query results.
Visualize with bar charts, pie charts, and maps.

#Dashboard
Build an interactive dashboard with Streamlit for data exploration.
Results & Skills
ETL and integration proficiency

SQL for complex analytical queries

Interactive Python dashboards with clear visualizations

Data-driven insights for actionable business recommendations

#Project Evaluation
Code Quality: Python and SQL best practices

Query Efficiency: Fast, accurate SQL statements

Visualization: Effective dashboard designs

Insights Validity: Business relevance of findings

Documentation: Clear instructions and reporting

Technical Tags
Python SQL Streamlit Data Visualization ETL Data Analysis

Dataset
PhonePe Pulse GitHub Repository
Visualization Techniques Used

Interactive Dashboard – Built with Streamlit, allowing filtering by year, quarter, and state.- Ranking Analysis – Displays only the top-performing states, districts, and pincodes in descending order based on transaction amount and registered users.
Bar Graphs – All visualizations are shown as bar graphs for clear ranking comparisons.
Benefits of This Analysis

Enhanced Decision-Making – Helps identify high-performing regions for targeted marketing or resource allocation.
Regional Performance Tracking – Tracks the growth and adoption of PhonePe in different parts of India.
Market Insights – Highlights areas with high adoption and transaction activity.
This project offers a focused, data-driven view into PhonePe’s top-performing regions, using only bar graphs for a simple and effective visual comparison.
Project Objective
To analyze and visualize PhonePe’s transaction data across various dimensions—state, time period, category, and user demographics—to derive actionable insights that can drive business growth, product improvements, and policy decisions.

Business Use Cases
1. Decoding Transaction Dynamics on PhonePe
PhonePe observed significant variations in transaction behavior across states, quarters, and payment categories. This use case helps uncover patterns of growth, stagnation, or decline, enabling leadership to craft region-specific and category-specific strategies.

           .Total Transaction Amount Trend by State
           .Total Transaction Amount by State
           .Quarterly Transaction by State
           .Total Transaction trend by Transaction type
           .Year-over-Year Growth by State

2. Device Dominance and User Engagement Analysis
By analyzing registered users and app open data segmented by device brand and region, this use case highlights how user engagement varies across devices—informing UI optimization, device-specific campaigns, and tech enhancements.

           .Top Device Brands by Total Users
           .Brand Engagement % Across States
           .Correlation of Registered Users and App Opens by Brand
           .AppOpens_per_User Across States
           .Top Underutilized Device Brands (Low Engagement Ratio)

3. Insurance Engagement Analysis
With increasing traction in its insurance offerings, PhonePe needs to identify states with high potential but low current adoption. This use case supports strategic marketing and partnership decisions in the insurance domain.

           .Yearly State Insurance Transaction Summary
           .District-Level Annual Insurance Activity
           .Quarterly Insurance Performance Review by State
           .Quarterly District Insurance Transactions 
           .Quarterly Insurance Transaction Trend - Top 5 States

4. Transaction Analysis for Market Expansion
In a competitive market, identifying emerging regions with high transaction growth is key. This use case explores transaction volumes at the state level to pinpoint areas ripe for market penetration and expansion

           .Transaction Count and Amount by State, Year, Quarter
           .Top 10 States by Total Transaction Amount
           .Top 10 States by Transaction Amount YoY Growth in 2024
           .Potential States for Market Expansion (Low Amount, High Growth)
           .Average Transaction value for State

5--User Engagement and Growth Strategy
State-wise Summary: Total Registered Users & App Opens, User Growth Over Time for Top 5 States,Engagement Ratio by State (App Opens / Registered Users)**

            .Total Registered Users by State
           .Quarterly Registered Users Trend - Top 10 States
           .Top 10 States by Average User Engagement Ratio
           .Districts in Maharashtra by Registered Users
           .Registered and Active Users by State
           .Top Districts by Registered Users
