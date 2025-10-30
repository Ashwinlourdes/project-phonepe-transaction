import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector
import plotly.express as px
import requests


 
# ===================== Database Connection =====================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="phonepedb1"
    )
@st.cache_data(ttl=600)
def load_table(table):
    db = get_connection()
    df = pd.read_sql(f"SELECT * FROM {table}", db)
    db.close()
    if 'Years' in df.columns:
        df['Years'] = df['Years'].astype(int)
    if 'Quarter' in df.columns:
        df['Quarter'] = df['Quarter'].astype(int)
    return df

# ===================== LOAD DATA =====================
@st.cache_data
def load_all_data():
    trans_df = load_table('agg_transaction_data')
    user_df = load_table('map_user_data')
    device_df = load_table('agg_user_data')
    insurance_df = load_table('agg_insurance_data')
    map_trans_df = load_table('map_transaction_data')
    
    for df in [trans_df, user_df, device_df, insurance_df, map_trans_df]:
        df['States'] = df['States'].str.replace('-', ' ').str.title()
    
    return trans_df, user_df, device_df, insurance_df, map_trans_df


trans_df, user_df, device_df, insurance_df, map_trans_df = load_all_data()
st.markdown("<h1 style='text-align:center; margin:0;'>PHONEPE TRANSACTION INSIGHT</h1>", unsafe_allow_html=True)


with st.sidebar:
    select = option_menu("MENU", ["HOME","BUSINESS CASES"])
if select == "HOME":
    st.markdown("""
    Welcome! This interactive dashboard presents a comprehensive analysis of PhonePe’s transaction, user, and insurance datasets. It is built to help stakeholders understand the evolution of India’s digital payment ecosystem, assess adoption patterns, and identify strategic opportunities in a rapidly expanding financial technology landscape.""")
    st.markdown("### Project Context ")
    st.markdown("""
    India’s digital payment ecosystem has transformed dramatically over the past decade, primarily driven by the Unified Payments Interface (UPI). Among the key players, PhonePe has emerged as a market leader, facilitating billions of transactions every month. Understanding these trends is critical for:  
    \n**Domain:** Finance / Digital Payments.
    \n**Product teams:** to design services tailored to user behavior.
    \n**Marketing teams:** to identify high-growth regions and adoption barriers.
    \n**Operations teams:** to mitigate risks and optimize resource allocation.
    \nThis dashboard consolidates analytical frameworks from digital finance, consumer behavior, and economic geography with empirical data from PhonePe, enabling data-backed decision-making.""")
    
    st.markdown(""" ###  Project Objective

    To analyze and visualize PhonePe’s transaction data across various dimensions—state, time period, category, and user demographics—to derive actionable insights that can drive business growth, product improvements, and policy decisions.

    ---

    ###  Business Use Cases

    #### 1. **Decoding Transaction Dynamics on PhonePe**
    PhonePe observed significant variations in transaction behavior across states, quarters, and payment categories. This use case helps uncover patterns of growth, stagnation, or decline, enabling leadership to craft region-specific and category-specific strategies.
                
                    1. Total Transaction Volumes Variation Across States Over the Years
                    2. States with Highest Quarter-over-Quarter Growth Rate in Transactions
                    3. Average Transaction Value Trend Per State Across Quarters
                    4. Payment Categories Comparison in Volume and Value Over Time
                    5. Top 10 States Contributing Most to Total Transaction Value

    #### 2. **Device Dominance and User Engagement Analysis**
    By analyzing registered users and app open data segmented by device brand and region, this use case highlights how user engagement varies across devices—informing UI optimization, device-specific campaigns, and tech enhancements.

                    1. the distribution of registered users by device brand?
                    2. app open counts compare across major device brands?
                    3. How has device brand usage changed over time (quarterly trend)?
                    4. Which regions show dominance for specific device brands?
                    5. Which device brands are underperforming despite high user registrations?

    #### 3. **3.Insurance Penetration & Growth Potential Analysis**
    With increasing traction in its insurance offerings, PhonePe needs to identify states with high potential but low current adoption. This use case supports strategic marketing and partnership decisions in the insurance domain.
                
                1. Which states contribute the most to total insurance transactions?
                2. How has insurance transaction volume changed quarter-over-quarter?
                3. What is the average policy value per state?
                4. Which states demonstrate the fastest growth in insurance adoption?
                5. Which top 10 states have untapped potential (low adoption vs user base)



    #### 4. **Transaction Analysis for Market Expansion**
    In a competitive market, identifying emerging regions with high transaction growth is key. This use case explores transaction volumes at the state level to pinpoint areas ripe for market penetration and expansion
    
                1. Which states record the highest transaction volumes and values?
                2. How do quarterly trends differ between top-performing and emerging states?
                3. What is the average transaction growth rate across regions?
                4. What are the top 10 fastest-growing districts in transaction value?
                5. Which payment categories dominate in high-performing states?
                6. Which states experienced a slowdown or decline in recent quarters?

    #### 5  **User Engagement and Growth Strategy**
    State-wise Summary: Total Registered Users & App Opens, User Growth Over Time for Top 5 States,Engagement Ratio by State (App Opens / Registered Users),District-Level Analysis: Example for Maharashtra**
               
                1. Which states and districts have the highest registered user counts?
                2. What is the quarterly growth rate of active users across states?
                3. What is the ratio of app opens per user by state?
                4. Which states or districts show under-engagement (low app opens vs users)?
                5. Which state-category combinations drive higher engagement?
                6. What are the top 10 high-engagement districts supporting growth strategy?
""")

elif select == "BUSINESS CASES" :
    case_study = st.selectbox(
    " Select Analysis Module",
    ["Select Analysis Module",
        "1. Transaction Dynamics",
        "2. Device Dominance",
        "3. Insurance Penetration",
        "4. Market Expansion",
        "5. User Engagement"
    ])
    all_states = sorted(trans_df['States'].unique())
    all_years = sorted(trans_df['Years'].unique())
    all_quarters = sorted(trans_df['Quarter'].unique())

    # select for states
    selected_states = st.selectbox(
        "Select States",
        options=['All']+all_states,
        help="Choose one or more states to analyze"
    )

    # Year filter
    selected_year = st.selectbox(
        "Select Year",
        options=['All'] + all_years,
        help="Filter by specific year or view all years"
    )

    # Quarter filter
    selected_quarter = st.selectbox(
        "Select Quarter",
        options=['All'] + all_quarters,
        help="Filter by specific quarter or view all quarters"
    )

    # Apply filters
    filtered_df = trans_df.copy()
    if selected_states!="All":
        filtered_df = filtered_df[filtered_df['States']==(selected_states)]
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['Years'] == selected_year]
    if selected_quarter != 'All':
        filtered_df = filtered_df[filtered_df['Quarter'] == selected_quarter]

    if case_study == "1. Transaction Dynamics":
            st.title("1. Transaction Dynamics on PhonePe")
            st.header("1️⃣ total transaction volumes vary across states over the years")

            vol_by_state_year = filtered_df.groupby(['States','Years'])['Transaction_count'].sum().reset_index()

            fig1 = px.line(vol_by_state_year, 
                        x='Years', 
                        y='Transaction_count', 
                        color='States',
                        title='Transaction Volume Trends by State',
                        markers=True,
                        labels={'Transaction_count': 'Transaction Count', 'Years': 'Year'})
            fig1.update_layout(hovermode='x unified', height=500)
            st.plotly_chart(fig1, use_container_width=True)

            total_contrib = vol_by_state_year.groupby('States')['Transaction_count'].sum().nlargest(10).reset_index()
            fig1b = px.pie(total_contrib, values='Transaction_count', names='States',
                            title='Top 10 States Contribution', hole=0.4)
            st.plotly_chart(fig1b, use_container_width=True)
            #  QUESTION 2
            st.header("2️⃣ Which states is the highest growth rate in transactions quarter-over-quarter?")

            trans_sorted = filtered_df.sort_values(['States', 'Years', 'Quarter'])
            trans_sorted['QoQ_Growth_%'] = trans_sorted.groupby('States')['Transaction_count'].pct_change() * 100

            avg_growth = trans_sorted.groupby('States')['QoQ_Growth_%'].mean().reset_index()
            avg_growth = avg_growth.sort_values('QoQ_Growth_%', ascending=False)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader(" Top 10 High-Growth States")
                top_growth = avg_growth.head(10)
                fig2a = px.bar(top_growth, 
                            x='States', 
                            y='QoQ_Growth_%',
                            title='Highest QoQ Growth Rate',
                            color='QoQ_Growth_%',
                            color_continuous_scale='Greens')
                fig2a.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig2a, use_container_width=True)

            with col2:
                st.subheader("📉 Bottom 10 Declining States")
                bottom_growth = avg_growth.tail(10).sort_values('QoQ_Growth_%')
                fig2b = px.bar(bottom_growth, 
                            x='States', 
                            y='QoQ_Growth_%',
                            title='Lowest QoQ Growth Rate',
                            color='QoQ_Growth_%',
                            color_continuous_scale='Reds_r')
                fig2b.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig2b, use_container_width=True)

            # ===================== QUESTION 3 =====================
            st.subheader("3️⃣ Total Transaction Volume by State Wise in years?")
            vol_by_state_year = filtered_df.groupby(['States', 'Years'])['Transaction_count'].sum().reset_index()

            latest_year = vol_by_state_year['Years'].max()
            latest_year_data = vol_by_state_year[vol_by_state_year['Years'] == latest_year]

            fig = px.choropleth(
                latest_year_data,
                geojson='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson',
                featureidkey='properties.ST_NM',
                locations='States',
                color='Transaction_count',
                color_continuous_scale='Blues',
                scope='asia',
                title=f'Total Transaction Volume by State in {latest_year}'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)


            #QUESTION 4 
            st.header("4️⃣ How do payment categories compare in volume and value over time?")

            cat_comparison = filtered_df.groupby(['Transaction_type', 'Years', 'Quarter']).agg({
                'Transaction_count': 'sum',
                'Transaction_amount': 'sum'
            }).reset_index()

            col1, col2 = st.columns(2)

            with col1:
                fig4a = px.bar(cat_comparison, 
                            x='Transaction_type', 
                            y='Transaction_count', 
                            color='Years',
                            barmode='group',
                            title='Transaction Volume by Category',
                            labels={'Transaction_count': 'Count'})
                fig4a.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig4a, use_container_width=True)

            with col2:
                fig4b = px.bar(cat_comparison, 
                            x='Transaction_type', 
                            y='Transaction_amount', 
                            color='Years',
                            barmode='group',
                            title='Transaction Value by Category',
                            labels={'Transaction_amount': 'Amount (₹)'})
                fig4b.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig4b, use_container_width=True)

            # Trend line
            st.subheader(" Category Trend Over Quarters")
            fig4c = px.line(cat_comparison, 
                            x='Quarter', 
                            y='Transaction_count', 
                            color='Transaction_type',
                            facet_col='Years',
                            markers=True,
                            title='Transaction Volume Trend by Category')
            st.plotly_chart(fig4c, use_container_width=True)

      
            #QUESTION 5
            st.header("5️⃣ Which top 10 states contribute the most to total transaction value?")

            top_states_value = filtered_df.groupby('States')['Transaction_amount'].sum().reset_index()
            top_states_value = top_states_value.sort_values('Transaction_amount', ascending=False).head(10)

            col1, col2 = st.columns(2)

            with col1:
                fig7a = px.bar(top_states_value, 
                            x='States', 
                            y='Transaction_amount',
                            title='Top 10 States by Transaction Value',
                            color='Transaction_amount',
                            color_continuous_scale='Blues',
                            labels={'Transaction_amount': 'Total Value (₹)'})
                fig7a.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig7a, use_container_width=True)

            with col2:
                fig7b = px.pie(top_states_value, 
                            values='Transaction_amount', 
                            names='States',
                            title='Share of Top 10 States',
                            hole=0.4)
                st.plotly_chart(fig7b, use_container_width=True)

            # Percentage contribution
            total_value = filtered_df['Transaction_amount'].sum()
            top_states_value['Percentage'] = (top_states_value['Transaction_amount'] / total_value) * 100
    elif case_study == "2. Device Dominance":
        filtered_device = device_df.copy()
        if selected_states != 'All':
            filtered_device = filtered_device[filtered_device['States'] == selected_states]
        if selected_year != 'All':
            filtered_device = filtered_device[filtered_device['Years'] == selected_year]
        if selected_quarter != 'All':
            filtered_device = filtered_device[filtered_device['Quarter'] == selected_quarter]
        st.title("2. Device Dominance and User Engagement Analysis")

            # QUESTION 1
        st.header("1️⃣ What is the distribution of registered users by device brand?")

        brand_dist = filtered_device.groupby('Brands')['Transaction_count'].sum().reset_index()
        brand_dist = brand_dist.sort_values('Transaction_count', ascending=False)

        col1, col2 = st.columns(2)

        with col1:
            fig1a = px.bar(brand_dist.head(15), 
                        x='Brands', 
                        y='Transaction_count',
                        title='Top 15 Device Brands by User Count',
                        color='Transaction_count',
                        color_continuous_scale='Blues',
                        labels={'Transaction_count': 'User Count'})
            fig1a.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1a, use_container_width=True)

        with col2:
            fig1b = px.pie(brand_dist.head(10), 
                        values='Transaction_count', 
                        names='Brands',
                        title='Market Share - Top 10 Brands',
                        hole=0.4)
            st.plotly_chart(fig1b, use_container_width=True)

        # QUESTION 2
        st.header("2️⃣ Device Dominance: Total User Count by State")
        device_by_state = device_df.groupby(['States', 'Brands'])['Transaction_count'].sum().reset_index()

        # For choropleth, aggregate total transaction count by state
        state_totals = device_by_state.groupby('States')['Transaction_count'].sum().reset_index()

        fig = px.choropleth(
            state_totals,
            geojson='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson',
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_count',
            color_continuous_scale='Viridis',
            scope='asia',
            title='Device Dominance: Total User Count by State'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

        # QUESTION 3 
        st.header("3️⃣ How has device brand usage changed over time (quarterly trend)?")

        quarterly_trend = device_df.groupby(['Years', 'Quarter', 'Brands'])['Transaction_count'].sum().reset_index()

        # Select top 5 brands for cleaner visualization
        top5_brands = device_df.groupby('Brands')['Transaction_count'].sum().nlargest(5).index.tolist()
        quarterly_trend_top = quarterly_trend[quarterly_trend['Brands'].isin(top5_brands)]

        fig4 = px.line(quarterly_trend_top, 
                    x='Quarter', 
                    y='Transaction_count', 
                    color='Brands',
                    facet_col='Years',
                    markers=True,
                    title='Quarterly Device Usage Trend - Top 5 Brands',
                    labels={'Transactioncount': 'User Count'})
        st.plotly_chart(fig4, use_container_width=True)

        # QUESTION 4 
        st.header("4️⃣ Which regions show dominance for specific device brands?")

        state_brand = filtered_device.groupby(['States', 'Brands'])['Transaction_count'].sum().reset_index()

        # Top brand per state
        top_brand_per_state = state_brand.loc[state_brand.groupby('States')['Transaction_count'].idxmax()]
        top_brand_per_state = top_brand_per_state.sort_values('Transaction_count', ascending=False).head(15)

        fig5 = px.bar(top_brand_per_state, 
                    x='States', 
                    y='Transaction_count',
                    color='Brands',
                    title='Dominant Device Brand by State (Top 15)',
                    labels={'Transactioncount': 'User Count'})
        fig5.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig5, use_container_width=True)

        #QUESTION 5
        st.header("5️⃣ Which device brands are underperforming despite high user registrations?")

        # Calculate performance ratio (market share vs user count)
        brand_performance = filtered_device.groupby('Brands').agg({
            'Transaction_count': 'sum',
            'Percentage': 'mean'
        }).reset_index()

        # Expected vs Actual performance
        total_users = brand_performance['Transaction_count'].sum()
        brand_performance['ExpectedShare'] = (brand_performance['Transaction_count'] / total_users) * 100
        brand_performance['PerformanceGap'] = brand_performance['Percentage'] - brand_performance['ExpectedShare']
        underperforming = brand_performance[brand_performance['PerformanceGap'] < 0].sort_values('PerformanceGap').head(10)

        fig7 = px.bar(underperforming, 
                    x='Brands', 
                    y='PerformanceGap',
                    title='Top 10 Underperforming Device Brands',
                    color='PerformanceGap',
                    color_continuous_scale='Reds_r',
                    labels={'PerformanceGap': 'Performance Gap (%)'})
        fig7.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig7, use_container_width=True)

    elif case_study == "3. Insurance Penetration":
         st.title("3. Insurance Penetration & Growth Potential Analysis")

         filtered_insurance = insurance_df.copy()
         if selected_states != 'All':
            filtered_insurance = filtered_insurance[filtered_insurance['States'] == selected_states]
         if selected_year != 'All':
            filtered_insurance = filtered_insurance[filtered_insurance['Years'] == selected_year]
         if selected_quarter != 'All':
            filtered_insurance = filtered_insurance[filtered_insurance['Quarter'] == selected_quarter]

        #QUESTION 1 
         st.header("1️⃣ Which states contribute the most to total insurance transactions?")

         top_states = filtered_insurance.groupby('States')['Insurance_count'].sum().reset_index()
         top_states = top_states.sort_values('Insurance_count', ascending=False).head(10)

         col1, col2 = st.columns(2)

         with col1:
            fig1a = px.bar(top_states, 
                        x='States', 
                        y='Insurance_count',
                        title='Top 10 States by Insurance Transactions',
                        color='Insurance_count',
                        color_continuous_scale='Blues',
                        labels={'Insurance_count': 'Transaction Count'})
            fig1a.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1a, use_container_width=True)

         with col2:
            fig1b = px.pie(top_states, 
                        values='Insurance_count', 
                        names='States',
                        title='Market Share - Top 10 States',
                        hole=0.4)
            st.plotly_chart(fig1b, use_container_width=True)


        #QUESTION 2
         st.header("2️⃣ How has insurance transaction volume changed quarter-over-quarter?")

         qtr_volume = filtered_insurance.groupby(['Years', 'Quarter'])['Insurance_count'].sum().reset_index()
         qtr_volume = qtr_volume.sort_values(['Years', 'Quarter'])
         qtr_volume['QoQ_Change_%'] = qtr_volume['Insurance_count'].pct_change() * 100

         fig2 = px.line(qtr_volume, 
                    x='Quarter', 
                    y='QoQ_Change_%', 
                    color='Years',
                    markers=True,
                    title='Quarter-over-Quarter Insurance Volume Change (%)',
                    labels={'QoQ_Change_%': 'QoQ Change (%)'})
         st.plotly_chart(fig2, use_container_width=True)

        # ===================== QUESTION 3 =====================
         st.header("3️⃣ What is the average policy value per state?")

         filtered_insurance['AvgPolicyValue'] = filtered_insurance['Insurance_amount'] / filtered_insurance['Insurance_count']
         avg_policy = filtered_insurance.groupby('States')['AvgPolicyValue'].mean().reset_index()
         avg_policy = avg_policy.sort_values('AvgPolicyValue', ascending=False).head(15)

         fig3 = px.bar(avg_policy, 
                    x='States', 
                    y='AvgPolicyValue',
                    title='Top 15 States by Average Policy Value',
                    color='AvgPolicyValue',
                    color_continuous_scale='Greens',
                    labels={'AvgPolicyValue': 'Avg Policy Value (₹)'})
         fig3.update_layout(xaxis_tickangle=-45)
         st.plotly_chart(fig3, use_container_width=True)

        # ===================== QUESTION 4 =====================
         st.header("4️⃣ Which states demonstrate the fastest growth in insurance adoption?")

         growth_data = filtered_insurance.groupby(['States', 'Years'])['Insurance_count'].sum().reset_index()
         growth_data = growth_data.sort_values(['States', 'Years'])
         growth_data['YoY_Growth_%'] = growth_data.groupby('States')['Insurance_count'].pct_change() * 100

         avg_growth = growth_data.groupby('States')['YoY_Growth_%'].mean().reset_index()
         fastest_growth = avg_growth.sort_values('YoY_Growth_%', ascending=False).head(10)

         fig4 = px.bar(fastest_growth, 
                    x='States', 
                    y='YoY_Growth_%',
                    title='Top 10 Fastest Growing States - Insurance Adoption',
                    color='YoY_Growth_%',
                    color_continuous_scale='Reds',
                    labels={'YoY_Growth_%': 'Avg YoY Growth (%)'})
         fig4.update_layout(xaxis_tickangle=-45)
         st.plotly_chart(fig4, use_container_width=True)      
        # QUESTION 5
         st.header("5️⃣ Which top 10 states have untapped potential (low adoption vs user base)?")

         user_base = user_df.groupby('States')['RegisteredUser'].sum().reset_index()
         ins_adoption = filtered_insurance.groupby('States')['Insurance_count'].sum().reset_index()

         merged = pd.merge(user_base, ins_adoption, on='States', how='left')
         merged['InsurancePerUser'] = merged['Insurance_count'] / merged['RegisteredUser']
         untapped = merged.nsmallest(10, 'InsurancePerUser')

         fig7 = px.bar(untapped, 
                    x='States', 
                    y='InsurancePerUser',
                    title='Top 10 States with Untapped Potential (Low Adoption per User)',
                    color='RegisteredUser',
                    color_continuous_scale='Oranges',
                    labels={'InsurancePerUser': 'Insurance per User', 
                            'RegisteredUser': 'User Base'})
         fig7.update_layout(xaxis_tickangle=-45)
         st.plotly_chart(fig7, use_container_width=True)

         

        # ===================== QUESTION 6 =====================
         st.header("6️⃣ What are the regional variations in insurance penetration per 1,000 users?")

         merged['PenetrationPer1000'] = (merged['Insurance_count'] / merged['RegisteredUser']) * 1000
         top_penetration = merged.nlargest(15, 'PenetrationPer1000')

         fig8 = px.bar(top_penetration, 
                    x='States', 
                    y='PenetrationPer1000',
                    title='Top 15 States - Insurance Penetration per 1,000 Users',
                    color='PenetrationPer1000',
                    color_continuous_scale='Purples',
                    labels={'PenetrationPer1000': 'Penetration per 1,000 Users'})
         fig8.update_layout(xaxis_tickangle=-45)
         st.plotly_chart(fig8, use_container_width=True)

    elif case_study == "4. Market Expansion":
        filtered_agg = trans_df.copy()
        filtered_map = map_trans_df.copy()

        if selected_states != 'All':
            filtered_agg = filtered_agg[filtered_agg['States'] == selected_states]
            filtered_map = filtered_map[filtered_map['States'] == selected_states]
        if selected_year != 'All':
            filtered_agg = filtered_agg[filtered_agg['Years'] == selected_year]
            filtered_map = filtered_map[filtered_map['Years'] == selected_year]
        if selected_quarter != 'All':
            filtered_agg = filtered_agg[filtered_agg['Quarter'] == selected_quarter]
            filtered_map = filtered_map[filtered_map['Quarter'] == selected_quarter]

        st.title("4.Transaction Analysis for Market Expansion")

        # ===================== QUESTION 1 =====================
        st.header("1️⃣ Which states record the highest transaction volumes and values?")

        state_metrics = filtered_agg.groupby('States').agg({
            'Transaction_count': 'sum',
            'Transaction_amount': 'sum'
        }).reset_index()
        state_metrics = state_metrics.sort_values('Transaction_count', ascending=False).head(10)

        col1, col2 = st.columns(2)

        with col1:
            fig1a = px.bar(state_metrics, 
                        x='States', 
                        y='Transaction_count',
                        title='Top 10 States by Transaction Volume',
                        color='Transaction_count',
                        color_continuous_scale='Blues',
                        labels={'Transaction_count': 'Transaction Count'})
            fig1a.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1a, use_container_width=True)

        with col2:
            fig1b = px.bar(state_metrics, 
                        x='States', 
                        y='Transaction_amount',
                        title='Top 10 States by Transaction Value',
                        color='Transaction_amount',
                        color_continuous_scale='Greens',
                        labels={'Transaction_amount': 'Transaction Value (₹)'})
            fig1b.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1b, use_container_width=True)

        # ===================== QUESTION 2 =====================
        st.header("2️⃣ How do quarterly trends differ between top-performing and emerging states?")

        # Top 5 states
        top5_states = state_metrics.head(5)['States'].tolist()

        quarterly = filtered_agg.groupby(['States', 'Years', 'Quarter'])['Transaction_count'].sum().reset_index()
        quarterly_top = quarterly[quarterly['States'].isin(top5_states)]

        fig2 = px.line(quarterly_top, 
                    x='Quarter', 
                    y='Transaction_count', 
                    color='States',
                    facet_col='Years',
                    markers=True,
                    title='Quarterly Trends - Top 5 Performing States',
                    labels={'Transaction_count': 'Transaction Count'})
        st.plotly_chart(fig2, use_container_width=True)
        # ===================== QUESTION 3 =====================
        st.header("3️⃣ What is the average transaction growth rate across regions?")

        growth_data = filtered_agg.groupby(['States', 'Years', 'Quarter'])['Transaction_count'].sum().reset_index()
        growth_data = growth_data.sort_values(['States', 'Years', 'Quarter'])
        growth_data['QoQ_Growth_%'] = growth_data.groupby('States')['Transaction_count'].pct_change() * 100

        avg_growth = growth_data.groupby('States')['QoQ_Growth_%'].mean().reset_index()
        avg_growth = avg_growth.sort_values('QoQ_Growth_%', ascending=False).head(10)

        fig3 = px.bar(avg_growth, 
                    x='States', 
                    y='QoQ_Growth_%',
                    title='Top 10 States by Average Growth Rate',
                    color='QoQ_Growth_%',
                    color_continuous_scale='Reds',
                    labels={'QoQ_Growth_%': 'Avg QoQ Growth (%)'})
        fig3.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig3, use_container_width=True)
        # ===================== QUESTION 4 =====================
        st.header("4️⃣ What are the top 10 fastest-growing districts in transaction value?")

        district_growth = filtered_map.groupby(['District', 'Years'])['Transaction_amount'].sum().reset_index()
        district_growth = district_growth.sort_values(['District', 'Years'])
        district_growth['YoY_Growth_%'] = district_growth.groupby('District')['Transaction_amount'].pct_change() * 100

        fastest_districts = district_growth.groupby('District')['YoY_Growth_%'].mean().nlargest(10).reset_index()

        fig6 = px.bar(fastest_districts, 
                    x='District', 
                    y='YoY_Growth_%',
                    title='Top 10 Fastest-Growing Districts',
                    color='YoY_Growth_%',
                    color_continuous_scale='Greens',
                    labels={'YoY_Growth_%': 'Avg YoY Growth (%)'})
        fig6.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig6, use_container_width=True)
        # ===================== QUESTION 5 =====================
        st.header("5️⃣ Which payment categories dominate in high-performing states?")

        category_state = filtered_agg[filtered_agg['States'].isin(top5_states)]
        category_metrics = category_state.groupby(['States', 'Transaction_type'])['Transaction_count'].sum().reset_index()

        fig7 = px.bar(category_metrics, 
                    x='States', 
                    y='Transaction_count', 
                    color='Transaction_type',
                    barmode='stack',
                    title='Payment Category Distribution - Top 5 States',
                    labels={'Transactioncount': 'Transaction Count'})
        fig7.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig7, use_container_width=True)       
        # ===================== QUESTION 6 =====================
        st.header("6️⃣Transaction Volume for Market Expansion by State")

        market_expansion = filtered_agg.groupby('States')['Transaction_count'].sum().reset_index()

        fig = px.choropleth(
            market_expansion,
            geojson='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson',
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_count',
            color_continuous_scale='Oranges',
            scope='asia',
            title='Transaction Volume for Market Expansion by State'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
    elif case_study == "5. User Engagement":
        filtered_user = user_df.copy()
        if selected_states != 'All':
            filtered_user = filtered_user[filtered_user['States'] == selected_states]
        if selected_year != 'All':
            filtered_user = filtered_user[filtered_user['Years'] == selected_year]
        if selected_quarter != 'All':
            filtered_user = filtered_user[filtered_user['Quarter'] == selected_quarter]
        st.title("5. User Engagement and Growth Strategy")
                   # ===================== QUESTION 1 =====================
        st.header("1️⃣ Which states and districts have the highest registered user counts?")

        # States
        state_users = filtered_user.groupby('States')['RegisteredUser'].sum().reset_index()
        state_users = state_users.sort_values('RegisteredUser', ascending=False).head(10)

        # Districts
        district_users = filtered_user.groupby(['States', 'District'])['RegisteredUser'].sum().reset_index()
        district_users = district_users.sort_values('RegisteredUser', ascending=False).head(10)

        col1, col2 = st.columns(2)

        with col1:
            fig1a = px.bar(state_users, 
                        x='States', 
                        y='RegisteredUser',
                        title='Top 10 States by Registered Users',
                        color='RegisteredUser',
                        color_continuous_scale='Blues',
                        labels={'RegisteredUser': 'Registered Users'})
            fig1a.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1a, use_container_width=True)

        with col2:
            fig1b = px.bar(district_users, 
                        x='District', 
                        y='RegisteredUser',
                        color='States',
                        title='Top 10 Districts by Registered Users',
                        labels={'RegisteredUser': 'Registered Users'})
            fig1b.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig1b, use_container_width=True)

        # ===================== QUESTION 2 =====================
        st.header("2️⃣Registered Users by State")

        user_engagement = user_df.groupby('States')['RegisteredUser'].sum().reset_index()

        fig = px.choropleth(
            user_engagement,
            geojson='https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson',
            featureidkey='properties.ST_NM',
            locations='States',
            color='RegisteredUser',
            color_continuous_scale='Purples',
            scope='asia',
            title='Registered Users by State'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
        # ===================== QUESTION 3=====================
        st.header("3️⃣ What is the ratio of app opens per user by state?")
        state_correlation = filtered_user.groupby('States').agg({
            'RegisteredUser': 'sum',
            'AppOpens': 'sum'
        }).reset_index()


        opens_per_user = state_correlation.copy()
        opens_per_user['OpensPerUser'] = opens_per_user['AppOpens'] / opens_per_user['RegisteredUser']
        opens_per_user = opens_per_user.sort_values('OpensPerUser', ascending=False).head(15)

        fig5 = px.bar(opens_per_user, 
                    x='States', 
                    y='OpensPerUser',
                    title='Top 15 States by App Opens per User',
                    color='OpensPerUser',
                    color_continuous_scale='Viridis',
                    labels={'OpensPerUser': 'App Opens per User'})
        fig5.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig5, use_container_width=True)
        # ===================== QUESTION 4 =====================
        st.header("4️⃣ Which states or districts show under-engagement (low app opens vs users)?")

        under_engaged = opens_per_user.nsmallest(10, 'OpensPerUser')

        fig6 = px.bar(under_engaged, 
                    x='States', 
                    y='OpensPerUser',
                    title='Top 10 Under-Engaged States',
                    color='OpensPerUser',
                    color_continuous_scale='Reds_r',
                    labels={'OpensPerUser': 'App Opens per User'})
        fig6.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig6, use_container_width=True)
        # ===================== QUESTION 5 =====================
        st.header(" 5️⃣Which state-category combinations drive higher engagement?")

        # Merge user data with transaction data
        trans_by_state = trans_df.groupby(['States', 'Transaction_type', 'Years', 'Quarter'])['Transaction_count'].sum().reset_index()
        user_by_state = user_df.groupby(['States', 'Years', 'Quarter']).agg({
            'RegisteredUser': 'sum',
            'AppOpens': 'sum'
        }).reset_index()

        merged_engagement = pd.merge(trans_by_state, user_by_state, on=['States', 'Years', 'Quarter'], how='inner')
        merged_engagement['EngagementScore'] = (merged_engagement['Transaction_count'] * merged_engagement['AppOpens']).pow(0.5)

        top_combinations = merged_engagement.groupby(['States', 'Transaction_type'])['EngagementScore'].mean().reset_index()
        top_combinations = top_combinations.nlargest(15, 'EngagementScore')

        fig8 = px.bar(top_combinations, 
                    x='States', 
                    y='EngagementScore', 
                    color='Transaction_type',
                    barmode='stack',
                    title='Top State-Category Engagement Combinations',
                    labels={'EngagementScore': 'Engagement Score'})
        fig8.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig8, use_container_width=True)
        # ===================== QUESTION 6 =====================
        st.header("6️⃣ What are the top 10 high-engagement districts supporting growth strategy?")

        district_engagement = filtered_user.groupby(['States', 'District']).agg({
            'RegisteredUser': 'sum',
            'AppOpens': 'sum'
        }).reset_index()

        district_engagement['OpensPerUser'] = district_engagement['AppOpens'] / district_engagement['RegisteredUser']
        district_engagement['EngagementScore'] = (district_engagement['RegisteredUser'] * district_engagement['OpensPerUser']).pow(0.5)
        top_districts = district_engagement.nlargest(10, 'EngagementScore')

        fig10 = px.bar(top_districts, 
                    x='District', 
                    y='EngagementScore',
                    color='States',
                    title='Top 10 High-Engagement Districts',
                    labels={'EngagementScore': 'Engagement Score'})
        fig10.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig10, use_container_width=True)

