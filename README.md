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

           1. Total Transaction Volumes Variation Across States Over the Years
           2. States with Highest Quarter-over-Quarter Growth Rate in Transactions
           3.Total Transaction Volume by State Wise?
           4. Payment Categories Comparison in Volume and Value Over Time
           5. Top 10 States Contributing Most to Total Transaction Value

2. Device Dominance and User Engagement Analysis
By analyzing registered users and app open data segmented by device brand and region, this use case highlights how user engagement varies across devices—informing UI optimization, device-specific campaigns, and tech enhancements.

           1 the distribution of registered users by device brand?
           2  Total User Count by State
           3 How has device brand usage changed over time (quarterly trend)?
           4️ Which regions show dominance for specific device brands?
           5️ Which device brands are underperforming despite high user registrations?

3.Insurance Penetration & Growth Potential Analysis
With increasing traction in its insurance offerings, PhonePe needs to identify states with high potential but low current adoption. This use case supports strategic marketing and partnership decisions in the insurance domain.


           1️ Which states contribute the most to total insurance transactions?
           2️ How has insurance transaction volume changed quarter-over-quarter?
           3️ What is the average policy value per state?
           4️ Which states demonstrate the fastest growth in insurance adoption?
           5️ What are the emerging states showing rapid growth in insurance adoption?

4. Transaction Analysis for Market Expansion
In a competitive market, identifying emerging regions with high transaction growth is key. This use case explores transaction volumes at the state level to pinpoint areas ripe for market penetration and expansion

           1️ Which states record the highest transaction volumes and values?
           2️ How do quarterly trends differ between top-performing and emerging states?
           3️ What is the average transaction growth rate across regions?
           4️ What are the top 10 fastest-growing districts in transaction value?
           5️ Which payment categories dominate in high-performing states?
           6️ Transaction Volume for Market Expansion by State


5--User Engagement and Growth Strategy
State-wise Summary: Total Registered Users & App Opens, User Growth Over Time for Top 5 States,Engagement Ratio by State (App Opens / Registered Users)**

           1️ Which states and districts have the highest registered user counts?
           2️ Registered Users by State
           3️ What is the ratio of app opens per user by state?
           4️ Which states or districts show under-engagement (low app opens vs users)?
           5️ Which state-category combinations drive higher engagement?
           6️ What are the top 10 high-engagement districts supporting growth strategy?
