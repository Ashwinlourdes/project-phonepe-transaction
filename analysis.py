import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import requests 


# Streamlit Part

st.set_page_config(layout= "wide")
st.markdown("<h1 style='text-align:center; margin:0;'>PHONEPE TRANSACTION INSIGHT</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Full-page watermark layer */
    .watermark-layer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;            /* allow clicks through the watermark */
      z-index: 0;                       /* sit behind page content (which we'll raise) */
      display: block;
      background-image: url("https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png");
      background-repeat: no-repeat;
      background-position: right 20px top 10px; /* position: right-top; tweak offsets */
      background-size: var(--logo-width, 220px) auto; /* width in px; keep aspect ratio */
      opacity: var(--logo-opacity, 0.2);  /* transparency (0.0 - 1.0) */
      filter: none;                        /* optional: blur(1px) or grayscale(1) */
    }

    /* Ensure your actual content appears above watermark */
    .stApp > .main, .css-1outpf7, .block-container {
      position: relative;
      z-index: 1;
    }

    </style>
    <div class="watermark-layer"></div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='page-title'></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:left; padding-top:5px; padding-bottom:10px;">
            <img src="https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    select = option_menu("MENU", ["HOME","BUSINESS CASES"])

    st.markdown(
        """
        <style>
        .sidebar-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: inherit;
            text-align: center;
            font-size: 18px;
            color: grey;
            padding-bottom: 10px;
        }
        </style>
        <div class="sidebar-footer">
            PROJECT BY — <b>DHANUSHKUMAR S</b>
        </div>
        """,
        unsafe_allow_html=True
    )
    
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
    st.markdown("### Core Deliverables")
    st.markdown("""
    - Provides a macro-level perspective of India’s payment ecosystem.
    - Helps predict future adoption trajectories for both payments and insurance.
    - Supports policy and regulatory discussions around digital finance penetration.
    - Acts as a knowledge base for practitioners, researchers, and policymakers.
                Welcome to **PhonePe Transaction Insight** – a data-driven dashboard designed to uncover meaningful insights from PhonePe's digital transaction ecosystem.

    This project leverages PhonePe Pulse data to provide a comprehensive view of transaction behaviors, user engagement, and market opportunities across India. It aims to support strategic business decisions through interactive visualizations and data analysis.
 ---
Welcome to **PhonePe Transaction Insight** – a data-driven dashboard designed to uncover meaningful insights from PhonePe's digital transaction ecosystem.

    This project leverages PhonePe Pulse data to provide a comprehensive view of transaction behaviors, user engagement, and market opportunities across India. It aims to support strategic business decisions through interactive visualizations and data analysis.""")


    st.markdown(""" ###  Project Objective

    To analyze and visualize PhonePe’s transaction data across various dimensions—state, time period, category, and user demographics—to derive actionable insights that can drive business growth, product improvements, and policy decisions.

    ---

    ###  Business Use Cases

    #### 1. **Decoding Transaction Dynamics on PhonePe**
    PhonePe observed significant variations in transaction behavior across states, quarters, and payment categories. This use case helps uncover patterns of growth, stagnation, or decline, enabling leadership to craft region-specific and category-specific strategies.
                
                .Total Transaction Amount Trend by State
                .Total Transaction Amount by State
                .Quarterly Transaction by State
                .Total Transaction trend by Transaction type
                .Year-over-Year Growth by State

    #### 2. **Device Dominance and User Engagement Analysis**
    By analyzing registered users and app open data segmented by device brand and region, this use case highlights how user engagement varies across devices—informing UI optimization, device-specific campaigns, and tech enhancements.

                .Top Device Brands by Total Users
                .Brand Engagement % Across States
                .Correlation of Registered Users and App Opens by Brand
                .AppOpens_per_User Across States
                .Top Underutilized Device Brands (Low Engagement Ratio)

    #### 3. **Insurance Penetration and Growth Potential**
    With increasing traction in its insurance offerings, PhonePe needs to identify states with high potential but low current adoption. This use case supports strategic marketing and partnership decisions in the insurance domain.

                .Quarterly Insurance Transaction Trend - Top 5 States
                .Average Premium Paid per Policy by State
                .Quarterly Insurance Transaction Trends - Bottom 10 States
                .Top 10 Fastest Growing States in Insurance Transactions
                .Bottom 10 States by Insurance Transaction Growth

    #### 4. **Transaction Analysis for Market Expansion**
    In a competitive market, identifying emerging regions with high transaction growth is key. This use case explores transaction volumes at the state level to pinpoint areas ripe for market penetration and expansion
    
                .Transaction Count and Amount by State, Year, Quarter
                .Top 10 States by Total Transaction Amount
                .Top 10 States by Transaction Amount YoY Growth in 2024
                .Potential States for Market Expansion (Low Amount, High Growth)
                .Average Transaction value for State

    #### 5--**User Engagement and Growth Strategy**
    State-wise Summary: Total Registered Users & App Opens, User Growth Over Time for Top 5 States,Engagement Ratio by State (App Opens / Registered Users),District-Level Analysis: Example for Maharashtra**
               
                 .Total Registered Users by State
                .Quarterly Registered Users Trend - Top 10 States
                .Top 10 States by Average User Engagement Ratio
                .Districts in Maharashtra by Registered Users
                .Registered and Active Users by State
                .Top Districts by Registered Users
""")
elif select == "BUSINESS CASES" :
    
    col1,col2,col3 = st.columns(3)
    with col2:
        st.markdown("<h5 style='text-align: center;'>Select Case Study</h5>", unsafe_allow_html=True)
        cases = st.selectbox("", ["Decoding Transaction Dynamics on PhonePe",
                                  "Device Dominance and User Engagement Analysis",
                                  "Insurance Penetration and Growth Potential",
                                    "Transaction Analysis for Market Expansion", 
                                   "User Engagement and Growth Strategy" ])
    if cases == "Decoding Transaction Dynamics on PhonePe":
            st.header("Analysis 1: Decoding Transaction Dynamics on PhonePe")
            top_states = pd.read_csv('D:\phonepe project\my_data.csv')
            st.subheader('Total Transaction Amount Trend by State')
            fig, ax = plt.subplots(figsize=(12, 9))
            sns.lineplot(data=top_states, x="Year", y="Total_Amount", hue="State", marker="o", palette='Set1', ax=ax)
            ax.set_title("Total Transaction Amount Trend by State")
            ax.set_xlabel("Year")
            ax.set_ylabel("Total Amount")
            ax.legend(title="State", bbox_to_anchor=(1.05, 1), loc='upper left')
            st.pyplot(fig)

            tate_totals = top_states.groupby('State')['Total_Amount'].sum().reset_index()

# Create interactive bar chart with Plotly
            fig = px.bar(top_states, 
                        x='State', 
                        y='Total_Amount',
                        title='Total Transaction Amount by State',
                        labels={'Total_Amount': 'Total Amount', 'State': 'State'},
                        color='Total_Amount',
                        color_continuous_scale='Viridis')

            # Show chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)
            


            Quarterly_by_state=pd.read_csv('D:\phonepe project\my_data1.csv')
            Quarterly_by_state.columns = Quarterly_by_state.columns.str.strip()
            Quarterly_by_state['time'] = Quarterly_by_state['Year'].astype(str) + '-Q' + Quarterly_by_state['Quater'].astype(str)
            pivot_df = Quarterly_by_state.pivot(index='State', columns='time', values='Total_Amount').fillna(0)
            st.subheader('Quarterly Transaction by State')
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(pivot_df, cmap='YlGnBu', ax=ax)
            ax.set_xlabel('Time (Year-Quarter)')
            ax.set_ylabel('State')
            st.pyplot(fig)


            Payment_category=pd.read_csv('D:\phonepe project\my_data2')
            st.subheader('Total Transaction trend by Transaction type')
            fig, ax = plt.subplots(figsize=(12, 9))
            sns.lineplot(data=Payment_category, x="Year", y="Total_Amount", hue="Transaction_type", marker="o", palette='Set1', ax=ax)
            ax.set_xlabel("Year")
            ax.set_ylabel("Total Amount")
            ax.legend(title="State", bbox_to_anchor=(1.05, 1), loc='upper left')
            st.pyplot(fig)


            Growth_rate_overstate=pd.read_csv('D:\phonepe project\my_data3')
            pivot_df = Growth_rate_overstate.pivot(index="State", columns="Year", values="YoY_Growth_Percentage")
            st.subheader('Year-over-Year Growth by State')
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(pivot_df,annot=True, cmap='YlGnBu', ax=ax)
            ax.set_xlabel('Year')
            ax.set_ylabel('State')
            st.pyplot(fig)

    elif cases == "Device Dominance and User Engagement Analysis":
            
            st.header("Analysis 2: Device Dominance and User Engagement Analysis")

            Merged=pd.read_csv('D:\phonepe project\my_data4')
            top_brands = Merged.groupby('brand')['count'].sum().sort_values(ascending=False)
            st.subheader('Top Device Brands by Total Users')
            fig, ax = plt.subplots(figsize=(10, 6))
            top_brands.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_xlabel('Device Brand')
            ax.set_ylabel('Total Users')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)


            st.subheader(" Brand Engagement % Across States")
            engagement = Merged.groupby(['state', 'brand'])['Brand_Engagement (%)'].mean().reset_index()
            heatmap_data = engagement.pivot(index='state', columns='brand', values='Brand_Engagement (%)')
            fig, ax = plt.subplots(figsize=(16, 10))
            sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='YlGnBu', cbar_kws={'label': 'Engagement %'}, ax=ax)
            ax.set_xlabel('Brand')
            ax.set_ylabel('State')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)


            st.subheader("Correlation of Registered Users and App Opens by Brand")
            # Aggregated data by brand
            brand_data = Merged.groupby('brand')[['registeredusers', 'appopens']].sum().reset_index()
            # Calculate Pearson correlation coefficient and display with explanation
            correlation = brand_data['registeredusers'].corr(brand_data['appopens'])
            st.markdown(f"**Pearson correlation coefficient:** {correlation:.2f}  \n"
                        "This indicates the strength and direction of linear relationship between registered users and app opens.")
            # Improved scatter plot with titles, axis labels, and hover data
            fig = px.scatter(
                brand_data,
                x='registeredusers',
                y='appopens',
                text='brand',
                title='Registered Users vs App Opens by Brand',
                labels={'registeredusers': 'Registered Users', 'appopens': 'App Opens'},
                hover_name='brand',
                template='plotly_white'
            )
            fig.update_traces(
                textposition='top center',
                marker=dict(size=12, color='royalblue', opacity=0.7, line=dict(width=1, color='DarkSlateGrey'))
            )
            fig.update_layout(
                xaxis=dict(title='Registered Users', zeroline=True, zerolinewidth=2, zerolinecolor='LightPink'),
                yaxis=dict(title='App Opens', zeroline=True, zerolinewidth=2, zerolinecolor='LightPink'),
                margin=dict(l=40, r=40, t=60, b=40)
            )
            st.plotly_chart(fig, use_container_width=True)
            engagement = Merged.groupby(['state', 'brand'])['appopens'].mean().reset_index()
            heatmap_data = engagement.pivot(index='state', columns='brand', values='appopens')
            st.subheader(' AppOpens_per_User Across States')
            fig, ax = plt.subplots(figsize=(16, 10))
            sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='YlGnBu', cbar_kws={'label': 'appopens'}, ax=ax)
            ax.set_xlabel('Brand')
            ax.set_ylabel('State')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

            brand_data['engagement_ratio'] = brand_data['appopens'] / brand_data['registeredusers']
            underutilized = brand_data.sort_values(by='engagement_ratio').head(5)
            st.subheader("Top Underutilized Device Brands (Low Engagement Ratio)")
            fig, ax = plt.subplots()
            sns.barplot(data=underutilized, x='brand', y='engagement_ratio', ax=ax, palette='Reds_r')
            ax.set_ylabel("App Opens per Registered User")
            plt.xticks(rotation=45)
            st.pyplot(fig)
    elif cases == "Insurance Penetration and Growth Potential":
            st.header("Analysis 3: Insurance Penetration and Growth Potential")
            Agg_Insurance=pd.read_csv('D:\phonepe project\my_data6')
            state_summary = Agg_Insurance.groupby('state')[['transaction_count', 'transaction_amount']].sum().sort_values(by='transaction_count', ascending=False)
            st.subheader("Quarterly Insurance Transaction Trend - Top 5 States ")
            top_states = state_summary.head(5).index.tolist()
            fig, ax = plt.subplots(figsize=(10, 6))
            for state in top_states:
                df = Agg_Insurance[Agg_Insurance['state'] == state]
                df_grouped = df.groupby(['year', 'quater'])['transaction_count'].sum().reset_index()
                df_grouped['Time'] = df_grouped['year'].astype(str) + ' Q' + df_grouped['quater'].astype(str)
                ax.plot(df_grouped['Time'], df_grouped['transaction_count'], label=state, marker='o')
            ax.set_xlabel("Quarter")
            ax.set_ylabel("Transaction Count")
            plt.xticks(rotation=45)
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
            #Average policy ticket size & premium paid per transaction by state
            state_avg = Agg_Insurance.groupby('state').agg({
                'transaction_amount': 'sum',
                'transaction_count': 'sum'
            })
            state_avg['avg_premium_per_policy'] = state_avg['transaction_amount'] / state_avg['transaction_count']

            st.subheader("Average Premium Paid per Policy by State")
            st.dataframe(state_avg[['avg_premium_per_policy']].sort_values(by='avg_premium_per_policy', ascending=False))



            bottom_states = state_summary.tail(10).index.tolist()
            st.subheader("Quarterly Insurance Transaction Trends - Bottom 10 States")
            fig, ax = plt.subplots(figsize=(10, 6))
            for state in bottom_states:
                df = Agg_Insurance[Agg_Insurance['state'] == state]
                df_grouped = df.groupby(['year', 'quater'])['transaction_count'].sum().reset_index()
                df_grouped['Time'] = df_grouped['year'].astype(str) + ' Q' + df_grouped['quater'].astype(str)
                ax.plot(df_grouped['Time'], df_grouped['transaction_count'], label=state, marker='o')
            ax.set_xlabel("Quarter")
            ax.set_ylabel("Transaction Count")
            ax.legend()
            ax.grid(True)
            plt.xticks(rotation=45)
            st.pyplot(fig)


            growth_data = []
            for state in Agg_Insurance['state'].unique():
                df = Agg_Insurance[Agg_Insurance['state'] == state]
                df_grouped = df.groupby(['year', 'quater'])['transaction_count'].sum().reset_index()
                df_grouped = df_grouped.sort_values(by=['year', 'quater'])

                if len(df_grouped) >= 2:
                    start = df_grouped.iloc[0]['transaction_count']
                    end = df_grouped.iloc[-1]['transaction_count']
                    growth = ((end - start) / start * 100) if start > 0 else None
                    growth_data.append((state, start, end, growth))

            growth_df = pd.DataFrame(growth_data, columns=['state', 'Start_Count', 'End_Count', 'Growth_Percent'])
            growth_df = growth_df.dropna().sort_values(by='Growth_Percent', ascending=False)
            top10_growth = growth_df.head(10)
            st.subheader("Top 10 Fastest Growing States in Insurance Transactions")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(x='Growth_Percent', y='state', data=top10_growth, palette='Greens_r', ax=ax)
            ax.set_xlabel("Growth Percentage (%)")
            ax.set_ylabel("State")
            plt.tight_layout()
            st.pyplot(fig)

            bottom10_growth = growth_df.tail(10)
            st.subheader("Bottom 10 States by Insurance Transaction Growth")
            fig2, ax2 = plt.subplots(figsize=(7, 5))
            sns.barplot(x='Growth_Percent', y='state', data=bottom10_growth, palette='Reds', ax=ax2)
            ax2.set_xlabel("Growth Percentage (%)")
            ax2.set_ylabel("State")
            plt.tight_layout()
            st.pyplot(fig2)
        
    elif cases == "Transaction Analysis for Market Expansion":
            st.header("Analysis 4: Transaction Analysis for Market Expansion")

            Map_Trans=pd.read_csv('D:\phonepe project\my_data7')
            state_time_summary = Map_Trans.groupby(['state', 'year', 'quater']).agg({
                    'count': 'sum',
                    'Transacion_amount': 'sum'
                }).reset_index()

            st.subheader("Transaction Count and Amount by State, Year, Quarter")
            st.dataframe(state_time_summary.head(20))
                                

                    
            state_summary = Map_Trans.groupby('state').agg({
                'count': 'sum',
                'Transacion_amount': 'sum'
            }).reset_index()
            state_summary = state_summary.sort_values(by='Transacion_amount', ascending=False)
            st.subheader("Top 10 States by Total Transaction Amount")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(data=state_summary.head(10), x='Transacion_amount', y='state', palette='viridis', ax=ax)
            ax.set_xlabel('Transaction Amount (₹)')
            ax.set_ylabel('State')
            st.pyplot(fig)

            annual_summary = Map_Trans.groupby(['state', 'year']).agg({
                'count': 'sum',
                'Transacion_amount': 'sum'
            }).reset_index()

            annual_summary = annual_summary.sort_values(by=['state', 'year'])

            annual_summary['Transaction_amount_YoY_growth'] = annual_summary.groupby('state')['Transacion_amount'].pct_change() * 100

            # Latest year growth
            latest_year = annual_summary['year'].max()
            growth_latest_year = annual_summary[annual_summary['year'] == latest_year]
            growth_latest_year = growth_latest_year.sort_values(by='Transaction_amount_YoY_growth', ascending=False)
            latest_year = annual_summary['year'].max()
            growth_latest_year = annual_summary[annual_summary['year'] == latest_year]
            growth_latest_year = growth_latest_year.sort_values(by='Transaction_amount_YoY_growth', ascending=False)
            st.subheader('Top 10 States by Transaction Amount YoY Growth in 2024')
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(
                data=growth_latest_year.head(10),
                x='Transaction_amount_YoY_growth',
                y='state',
                palette='coolwarm',
                ax=ax
            )
            ax.set_xlabel('YoY Growth (%)')
            ax.set_ylabel('State')
            st.pyplot(fig)

            median_amount = growth_latest_year['Transacion_amount'].median()
            potential_states = growth_latest_year[
                (growth_latest_year['Transacion_amount'] < median_amount) &
                (growth_latest_year['Transaction_amount_YoY_growth'] > 10)
            ]
            st.subheader('Potential States for Market Expansion (Low Amount, High Growth)')
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(data=potential_states, x='Transaction_amount_YoY_growth', y='state', palette='magma', ax=ax)
            ax.set_xlabel('YoY Growth (%)')
            ax.set_ylabel('State')

            st.pyplot(fig)
            state_summary = Map_Trans.groupby('state').agg({
                'Transacion_amount': 'sum',
                'count': 'sum'
            }).reset_index()

            state_summary['avg_transaction_value'] = state_summary['Transacion_amount'] / state_summary['count']
            st.subheader(" Average Transaction value for State")

            # Show result
            st.dataframe(state_summary[['state', 'avg_transaction_value']].sort_values(by='avg_transaction_value', ascending=False))
    
    
    elif cases == "User Engagement and Growth Strategy":

            st.header("Analysis 5: User Engagement and Growth Strategy")
            Map_User=pd.read_csv('D:\phonepe project\mydata8')
            st.subheader('Total Registered Users by State')
            state_summary = Map_User.groupby('state')[['registeredUsers', 'appOpens']].sum().sort_values(by='registeredUsers', ascending=False)
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.barplot(x=state_summary.index, y=state_summary['registeredUsers'], ax=ax)
            ax.set_xlabel('State')
            ax.set_ylabel('Registered Users')
            plt.xticks(rotation=90)
            st.pyplot(fig)

            

            top_states = state_summary.head(10).index
            st.subheader('Quarterly Registered Users Trend - Top 10 States')
            fig, ax = plt.subplots(figsize=(10, 6))
            for state in top_states:
                df = Map_User[Map_User['state'] == state].groupby(['year', 'quater'])[['registeredUsers']].sum().reset_index()
                df['Time'] = df['year'].astype(str) + ' Q' + df['quater'].astype(str)
                ax.plot(df['Time'], df['registeredUsers'], label=state)
            ax.set_xlabel('Time')
            ax.set_ylabel('Registered Users')
            plt.xticks(rotation=45)
            ax.legend()
            st.pyplot(fig)


            Map_User['Engagement_Ratio'] = Map_User['appOpens'] / Map_User['registeredUsers']
            Map_User.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
            Map_User.dropna(subset=['Engagement_Ratio'], inplace=True)
            engagement_ratio = Map_User.groupby('state')['Engagement_Ratio'].mean().sort_values(ascending=False)
            st.subheader('Top 10 States by Average User Engagement Ratio')
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x=engagement_ratio.head(10).index, y=engagement_ratio.head(10).values, ax=ax)
            ax.set_ylabel('Engagement Ratio (App Opens / Registered Users)')
            ax.set_xlabel('State')
            plt.xticks(rotation=90)
            st.pyplot(fig)

            district_data = Map_User[Map_User['state'] == 'maharashtra'].groupby('district_name')[['registeredUsers', 'appOpens']].sum().sort_values(by='registeredUsers', ascending=False)
            st.subheader('Districts in Maharashtra by Registered Users')
            fig, ax = plt.subplots(figsize=(12, 6))
            sns.barplot(x=district_data.index, y=district_data['registeredUsers'], ax=ax)
            ax.set_ylabel('Registered Users')
            ax.set_xlabel('District')
            plt.xticks(rotation=90)
            st.pyplot(fig)

            state_summary = Map_User.groupby('state')[['registeredUsers', 'appOpens']].sum().sort_values(by='registeredUsers', ascending=False)
            st.subheader('Registered and Active Users by State')
            st.dataframe(state_summary)

            district_summary = Map_User.groupby(['state', 'district_name'])[['registeredUsers', 'appOpens']].sum().sort_values(by='registeredUsers', ascending=False)
            st.subheader('Top Districts by Registered Users')
            st.dataframe(district_summary.head(20))
