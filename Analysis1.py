import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector
import pandas as pd
import plotly.express as px
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt



# Dataframe Creation

# sql connection

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="phonepedb"  
    )
    
cursor = mydb.cursor()

cursor.execute("SELECT * FROM agg_insurance_data")


table1= cursor.fetchall()

A_insurance= pd.DataFrame(table1, columns=("States", "Years", "Quarter", "Transaction_type",
                                               "Insurance_count", "Insurance_amount"))

#aggre_transaction_df
cursor.execute("SELECT * FROM agg_transaction_data")
table2= cursor.fetchall()

A_transaction= pd.DataFrame(table2, columns=("States", "Years", "Quarter", "Transaction_type",
                                               "Transaction_count", "Transaction_amount"))


#aggre_user_df
cursor.execute("SELECT * FROM agg_user_data")
table3= cursor.fetchall()

A_user= pd.DataFrame(table3, columns=("States", "Years", "Quarter", "Brands",
                                               "Transaction_count", "Percentage"))

#map_insurance
cursor.execute("SELECT * FROM map_insurance_data")
table4= cursor.fetchall()
M_insurance= pd.DataFrame(table4, columns=("States", "Years", "Quarter", "District","Transaction_type",
                                               "Transaction_count", "Transaction_amount"))

#map_transction
cursor.execute("SELECT * FROM map_transaction_data")
table5= cursor.fetchall()
M_transaction= pd.DataFrame(table5, columns=("States", "Years", "Quarter", "District","Transaction_type",
                                               "Transaction_count", "Transaction_amount"))

#map_user
cursor.execute("SELECT * FROM map_user_data")
table6= cursor.fetchall()
M_user= pd.DataFrame(table6, columns=("States", "Years", "Quarter", "District",
                                               "RegisteredUsers", "AppOpens"))

#top_insurance
cursor.execute("SELECT * FROM top_insurance_Pincode_data")
table7= cursor.fetchall()
T_insurance= pd.DataFrame(table7, columns=("States", "Years", "Quarter", "Pincodes","Transaction_type",
                                               "Transaction_count", "Transaction_amount"))

#top_transaction
cursor.execute("SELECT * FROM top_transaction_Pincode_data")
table8= cursor.fetchall()
T_transaction= pd.DataFrame(table8, columns=("States", "Years", "Quarter", "Pincodes","Transaction_type",
                                               "Transaction_count", "Transaction_amount"))

#top_user
cursor.execute("SELECT * FROM top_user_Pincode_data")
table9= cursor.fetchall()
T_user= pd.DataFrame(table9, columns=("States", "Years", "Quarter", "Pincodes",
                                               "RegisteredUsers"))

## Functions

def transaction_amount_count_Y(df, year):
    tacy = df[df["Years"] == year]
    tacy.reset_index(drop=True, inplace=True)
         
    tacy_group = tacy.groupby("States")[["Transaction_count",
                                               "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)
    title_suffix = "All Years"

    #tacy = df[df["Years"] == year]
    #tacy.reset_index(drop=True, inplace=True)

    #tacy_group = tacy.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    #tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
    
        fig_amount0 = px.bar(tacy_group, x="States", y= "Transaction_amount", 
                            title= f"{year} - TRANSACTION AMOUNT", 
                            color_discrete_sequence= px.colors.sequential.Bluered, 
                            height= 600, width= 500)
        st.plotly_chart(fig_amount0)

    with col2:

        fig_count0 = px.bar(tacy_group, x="States", y= "Transaction_count", 
                           title= f"{year} - TRANSACTION COUNT", 
                           color_discrete_sequence= px.colors.sequential.BuGn_r, 
                           height= 600, width= 500)
        st.plotly_chart(fig_count0)


    col1,col2 = st.columns(2)
    with col1:
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data1 = response.json()

        # Normalize states to match geojson
        tacy_group["States"] = tacy_group["States"].str.strip().str.title().str.replace("-", " ")
        mapping = {
            "Andaman & Nicobar Islands": "Andaman & Nicobar",
            "Nct Of Delhi": "Delhi",
            "Jammu & Kashmir": "Jammu And Kashmir",
            "Dadra & Nagar Havelli & Daman & Diu": "Dadra And Nagar Haveli And Daman And Diu"
        }
        tacy_group["States"] = tacy_group["States"].replace(mapping)

        fig_india_1 = px.choropleth(
            tacy_group, geojson=data1,
            locations="States",
            featureidkey="properties.ST_NM",
            color="Transaction_amount",
            color_continuous_scale="Rainbow",
            range_color=(tacy_group["Transaction_amount"].min(), tacy_group["Transaction_amount"].max()),
            hover_name="States",
            title=f"{year} - TRANSACTION AMOUNT",
            fitbounds="locations",
            height=900,
            width=900
        )
        fig_india_1.update_geos(visible=False)
        fig_india_1.update_layout(coloraxis_colorbar=dict(
                thickness=15,   # smaller thickness of colorbar (default is ~30)
                len=0.6,        # shorter length, relative to map height
                y=0.5,          # center it vertically
                yanchor="middle"
            ))
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth(
            tacy_group, geojson=data1,
            locations="States",
            featureidkey="properties.ST_NM",
            color="Transaction_count",
            color_continuous_scale="Rainbow",
            range_color=(tacy_group["Transaction_count"].min(), tacy_group["Transaction_count"].max()),
            hover_name="States",
            title=f"{year} - TRANSACTION COUNT",
            fitbounds="locations",
            height=900,
            width=900
        )
        fig_india_2.update_geos(visible=False)
        fig_india_2.update_layout(coloraxis_colorbar=dict(
                thickness=15,   # smaller thickness of colorbar (default is ~30)
                len=0.6,        # shorter length, relative to map height
                y=0.5,          # center it vertically
                yanchor="middle"
            ))
        st.plotly_chart(fig_india_2)

        return tacy

def transaction_amount_count_Y_Q(df, quarter):

    tacy = df[df["Quarter"] == quarter]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("States")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)

    with col1:    
        fig_amount = px.bar(tacy_group, x="States", y= "Transaction_amount", title= f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Bluered)
        st.plotly_chart(fig_amount)

    with col2:    
        fig_count = px.bar(tacy_group, x="States", y= "Transaction_count", title= f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.BuGn_r)
        st.plotly_chart(fig_count)

    col1,col2 = st.columns(2)

    with col1:
        # ... GeoJSON loading as before
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data1 = json.loads(response.content)

        states_name = [feature["properties"]["ST_NM"] for feature in data1["features"]]
        states_name.sort()

        # Ensure DataFrame states match GeoJSON
        tacy_group["States"] = (
            tacy_group["States"].str.strip().str.title().str.replace("-", " ")
        )
        mapping = {
            "Andaman & Nicobar Islands": "Andaman & Nicobar",
            "Nct Of Delhi": "Delhi",
            "Jammu & Kashmir": "Jammu And Kashmir",
            "Dadra & Nagar Havelli & Daman & Diu": "Dadra And Nagar Haveli And Daman And Diu"
        }
        tacy_group["States"] = tacy_group["States"].replace(mapping)

        with col1:
            fig_india_1 = px.choropleth(
                tacy_group,
                geojson=data1,
                locations="States",
                featureidkey="properties.ST_NM",
                color="Transaction_amount",
                color_continuous_scale="Rainbow",
                range_color=(
                    tacy_group["Transaction_amount"].min(),
                    tacy_group["Transaction_amount"].max()
                ),
                hover_name="States",
                title=f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION AMOUNT",
                fitbounds="locations",
                height=900,
                width=900
            )
            fig_india_1.update_geos(visible=False)
            fig_india_1.update_layout(coloraxis_colorbar=dict(
                thickness=15,   # smaller thickness of colorbar (default is ~30)
                len=0.6,        # shorter length, relative to map height
                y=0.5,          # center it vertically
                yanchor="middle"
            ))
            st.plotly_chart(fig_india_1)

        with col2:
            fig_india_2 = px.choropleth(
                tacy_group,
                geojson=data1,
                locations="States",
                featureidkey="properties.ST_NM",
                color="Transaction_count",
                color_continuous_scale="Rainbow",
                range_color=(
                    tacy_group["Transaction_count"].min(),
                    tacy_group["Transaction_count"].max()
                ),
                hover_name="States",
                title=f"{tacy['Years'].min()} QUARTER {quarter} - TRANSACTION COUNT",
                fitbounds="locations",
                height=900,
                width=900
            )
            fig_india_2.update_geos(visible=False)
            fig_india_2.update_layout(coloraxis_colorbar=dict(
                thickness=15,   # smaller thickness of colorbar (default is ~30)
                len=0.6,        # shorter length, relative to map height
                y=0.5,          # center it vertically
                yanchor="middle"
            ))

            st.plotly_chart(fig_india_2)


            return tacy

def Agg_tran_type(df, state):


    tacy = df[df["States"] == state]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("Transaction_type")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_pie_1 = px.pie(data_frame= tacy_group, names= "Transaction_type", values= "Transaction_amount",
                                width= 600, title= f"{df['Years'].min()} {state.upper()} - TRANSACTION AMOUNT", hole= 0.5,)
        st.plotly_chart(fig_pie_1)

    with col2:
        fig_pie_2 = px.pie(data_frame= tacy_group, names= "Transaction_type", values= "Transaction_count",
                                width= 600, title= f"{df['Years'].min()} {state.upper()} - TRANSACTION COUNT", hole= 0.5,)
        st.plotly_chart(fig_pie_2)

def Agg_user_plot_1(df, year):
    A_user_Y  = df[df["Years"] == year]
    A_user_Y.reset_index(drop= True, inplace= True)

    A_user_Y_group = pd.DataFrame(A_user_Y.groupby("Brands")["Transaction_count"].sum())
    A_user_Y_group.reset_index(inplace=True)

    fig_bar_1 = px.bar(A_user_Y_group, x= "Brands", y= "Transaction_count",
                    title= f"{year} - BRANDS AND TRANSACTION COUNT", width= 800, color_discrete_sequence= px.colors.sequential.Blues_r,
                    hover_name= "Brands")

    st.plotly_chart(fig_bar_1)

    return A_user_Y

def Agg_user_plot_2(df, quarter):

    A_user_Y_Q  = df[df["Quarter"] == quarter]
    A_user_Y_Q.reset_index(drop= True, inplace= True)

    A_user_Y_Q_group = pd.DataFrame(A_user_Y_Q.groupby("Brands")["Transaction_count"].sum()) 
    A_user_Y_Q_group.reset_index(inplace=True)


    fig_bar_2 = px.bar(A_user_Y_Q_group, x= "Brands", y= "Transaction_count",
                        title= f"{df['Years'].min()} QUARTER {quarter} - BRANDS AND TRANSACTION COUNT", width= 800, 
                        color_discrete_sequence= px.colors.sequential.Blues_r, hover_name= "Brands")

    st.plotly_chart(fig_bar_2)

    return A_user_Y_Q

def Agg_user_plot_3(df, state):
    Agg_user_Y_Q_S = df[df["States"] == state]
    Agg_user_Y_Q_S.reset_index(drop=True, inplace=True)

    fig_line_3 = px.line(Agg_user_Y_Q_S, x= "Brands", y= "Transaction_count", hover_data= "Percentage",
                        title= f"{df['Years'].min()} {state.upper()} QUARTER {df['Quarter'].min()} - BRANDS, TRANSACTION COUNT AND PERCENTAGE ", width=1000, markers=True)

    st.plotly_chart(fig_line_3)

def Map_insu_Districts(df, state):

    tacy = df[df["States"] == state]
    tacy.reset_index(drop=True, inplace=True)

    tacy_group = tacy.groupby("District")[["Transaction_count", "Transaction_amount"]].sum()
    tacy_group.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        fig_bar_1 = px.bar(tacy_group, x= "Transaction_amount", y= "District", orientation = "h", height = 800,
                                title= f"{state.upper()} - DISTRICTS AND TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Agsunset_r)
        st.plotly_chart(fig_bar_1)
    with col2:
        fig_bar_2 = px.bar(tacy_group, x= "Transaction_count", y= "District", orientation = "h", height = 800,
                                title= f"{state.upper()} -  DISTRICTS AND TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.Burgyl_r)
        
        st.plotly_chart(fig_bar_2)

def map_user_plot_1(df,year):

    M_user_Y  = df[df["Years"] == year]
    M_user_Y.reset_index(drop= True, inplace= True)

    M_user_Y_group = M_user_Y.groupby("States")[["RegisteredUsers", "AppOpens"]].sum()
    M_user_Y_group.reset_index(inplace=True)

    fig_line_4 = px.line(M_user_Y_group, x= "States", y= ["RegisteredUsers", "AppOpens"],
                        title= f" {year} - REGISTERED USERS AND APPOPENS ", width=1000, height = 800, markers=True)

    st.plotly_chart(fig_line_4)

    return M_user_Y

def map_user_plot_2(df,quarter):

    M_user_Y_Q  = df[df["Quarter"] == quarter]
    M_user_Y_Q.reset_index(drop= True, inplace= True)

    M_user_Y_Q_group = M_user_Y_Q.groupby("States")[["RegisteredUsers", "AppOpens"]].sum()
    M_user_Y_Q_group.reset_index(inplace=True)

    fig_line_5 = px.line(M_user_Y_Q_group, x= "States", y= ["RegisteredUsers", "AppOpens"],
                        title= f"{df['Years'].min()} QUARTER {quarter} - REGISTERED USERS AND APPOPENS ", width=1000, 
                        height = 800, markers=True, color_discrete_sequence= px.colors.sequential.Rainbow_r)

    st.plotly_chart(fig_line_5)

    return M_user_Y_Q

def map_user_plot_3(df,state):
    M_user_Y_Q_S = df[df["States"] == state]
    M_user_Y_Q_S.reset_index(drop=True, inplace=True)

    # Create columns once and use both inside it
    col1, col2 = st.columns(2)

    with col1:
        Fig_map_user_bar_1 = px.bar(
            M_user_Y_Q_S,
            x="RegisteredUsers",
            y="District",
            orientation="h",
            title=f"{df['Years'].min()} QUARTER {df['Quarter'].min()} {state.upper()} DISTRICTS - REGISTERED USER",
            height=800,
            color_discrete_sequence=px.colors.sequential.haline_r
        )
        st.plotly_chart(Fig_map_user_bar_1)

    with col2:
        Fig_map_user_bar_2 = px.bar(
            M_user_Y_Q_S,
            x="AppOpens",
            y="District",
            orientation="h",
            title=f"{df['Years'].min()} QUARTER {df['Quarter'].min()} {state.upper()} DISTRICTS - APPOPENS",
            height=800,
            color_discrete_sequence=px.colors.sequential.Magenta_r
        )
        st.plotly_chart(Fig_map_user_bar_2)


def top_ins_plot_1(df,state):
    T_ins_Y  = df[df["States"] == state]
    T_ins_Y.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:
        fig_top_ins_bar_1 = px.bar(T_ins_Y, x= "Quarter", y= "Transaction_amount", hover_data= "Pincodes",
                                title= f"{df['Years'].min()} YEAR's TRANSACTION AMOUNT", height= 800, color_discrete_sequence= px.colors.sequential.Purpor_r)

        st.plotly_chart(fig_top_ins_bar_1)

    with col2:
        fig_top_ins_bar_2 = px.bar(T_ins_Y, x= "Quarter", y= "Transaction_count", hover_data= "Pincodes",
                                title= f"{df['Years'].min()} YEAR's TRANSACTION COUNT", height= 800, color_discrete_sequence= px.colors.sequential.Cividis_r)

        st.plotly_chart(fig_top_ins_bar_2)

def top_user_plot_1(df,year):
    T_user_Y  = df[df["Years"] == year]
    T_user_Y.reset_index(drop= True, inplace= True)

    T_user_Y_group = pd.DataFrame(T_user_Y.groupby(["States", "Quarter"])["RegisteredUsers"].sum())
    T_user_Y_group.reset_index(inplace=True)

    fig_top_user_plot_1 = px.bar(T_user_Y_group, x= "States", y= "RegisteredUsers", color= "Quarter",
                            width= 1000, height= 800, color_discrete_sequence = px.colors.sequential.Bluered_r,
                            hover_name= "States", title= f"{year} REGISTERED USERS")

    st.plotly_chart(fig_top_user_plot_1)

    return T_user_Y

def top_user_plot_2(df,state):
    T_user_Y_S = df[df["States"] == state]
    T_user_Y_S.reset_index(drop= True, inplace= True)

    fig_top_user_plot_2 = px.bar(T_user_Y_S, x= "Quarter", y= "RegisteredUsers",
                                title = "REGISTERED USERS, PINCODES, QUARTER",
                                width= 1000, height= 800, color= "RegisteredUsers", hover_data= "Pincodes",
                                color_continuous_scale= px.colors.sequential.Magenta_r)

    st.plotly_chart(fig_top_user_plot_2)


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

    #### 3. **Insurance Engagement Analysis**
    With increasing traction in its insurance offerings, PhonePe needs to identify states with high potential but low current adoption. This use case supports strategic marketing and partnership decisions in the insurance domain.
                
                .Yearly State Insurance Transaction Summary
                .District-Level Annual Insurance Activity
                .Quarterly Insurance Performance Review by State
                .Quarterly District Insurance Transactions 
                .Quarterly Insurance Transaction Trend - Top 5 States



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
                                    "Transaction Analysis for Market Expansion", 
                                    "Insurance Engagement Analysis",
                                    "User Engagement and Growth Strategy" ])
    if cases == "Decoding Transaction Dynamics on PhonePe":
        st.subheader("The Big Picture: Yearly Transaction Insights")
        col1, col2 = st.columns(2)
        with col1:
            years = st.selectbox(
                "Which Year Do You Want to Explore?", 
                A_transaction["Years"].unique(), 
                index=0
            )

        st.markdown("#### Total Transaction Amount & Count Overview")
        Agg_tran_tac_y = transaction_amount_count_Y(A_transaction, years)

        st.subheader("Decoding Statewise Transaction Types — Yearly Lens")
        col1, col2 = st.columns(2)
        with col1:
            states = st.selectbox(
                "Select State for a Closer Look", 
                Agg_tran_tac_y["States"].unique()
            )
        st.markdown(f"#### Transaction Types in {states} ({years})")
        Agg_tran_type(Agg_tran_tac_y, states)

        st.subheader("Quarterly Pulse of the Year")
        col1, col2 = st.columns(2)
        with col1:
            quarters = st.slider(
                "Select Quarter", 
                int(Agg_tran_tac_y["Quarter"].min()),
                int(Agg_tran_tac_y["Quarter"].max()),
                int(Agg_tran_tac_y["Quarter"].min())
            )
        
        st.markdown(f"#### Transactions Overview: Quarter {quarters}, {years}")
        Agg_tran_tac_y_Q = transaction_amount_count_Y_Q(Agg_tran_tac_y, quarters)

        col1, col2 = st.columns(2)
        with col1:
            states = st.selectbox(
                "Select a State to View Quarterly Breakdown", 
                Agg_tran_tac_y_Q["States"].unique()
            )

        st.markdown(f"#### Transaction Types by State: {states}, Quarter {quarters}")
        Agg_tran_type(Agg_tran_tac_y_Q, states)
        Payment_category = A_transaction.rename(columns={'Years': 'Year', 'Transaction_amount': 'Total_Amount'})
        # Plot Total Transaction trend by Transaction type
        st.subheader('Total Transaction trend by Transaction type')
        fig, ax = plt.subplots(figsize=(12, 9))
        sns.lineplot(data=Payment_category, x="Year", y="Total_Amount", hue="Transaction_type", marker="o", palette='Set1', ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Amount")
        ax.legend(title="Transaction Type", bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

        top_states = A_transaction.groupby(['Years', 'States'], as_index=False).agg({'Transaction_amount': 'sum'})
        top_states = top_states.rename(columns={'Years': 'Year', 'States': 'State', 'Transaction_amount': 'Total_Amount'})

        # Plot Total Transaction Amount Trend by State
        st.subheader('Total Transaction Amount Trend by State')
        fig, ax = plt.subplots(figsize=(12, 9))
        sns.lineplot(data=top_states, x="Year", y="Total_Amount", hue="State", marker="o", palette='Set1', ax=ax)
        ax.set_title("Total Transaction Amount Trend by State")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Amount")
        ax.legend(title="State", bbox_to_anchor=(1.05, 1), loc='upper left')
        st.pyplot(fig)

            
    elif cases == "Device Dominance and User Engagement Analysis":
    
        st.subheader("Top Device Brands and Their Transaction Volume")
        col1, col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", A_user["Years"].min(), A_user["Years"].max(), A_user["Years"].min())
        
        st.subheader("YEAR WISE BRANDS AND TRANSACTION COUNT")
        A_user_y = Agg_user_plot_1(A_user, years)
        with col2:
            quarters = st.slider("Select Quarter", A_user_y["Quarter"].min(), A_user_y["Quarter"].max(), A_user_y["Quarter"].min())
        st.subheader("QUARTER WISE BRANDS AND TRANSACTION COUNT")
        A_user_y_Q = Agg_user_plot_2(A_user_y, quarters)
        


        st.subheader("User Engagement Trends Across the Nation")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Year Wise RegisterUers and AppOpens")
            Map_user_Y = map_user_plot_1(M_user, years)
        with col2:
            st.subheader("Quarter Wise RegisterUers and AppOpens")
            Map_user_Y_Q = map_user_plot_2(Map_user_Y, quarters)

        st.subheader("Statewise Device Popularity and User Activity")
        col1, col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State for In-Depth Device Analysis", A_user_y_Q["States"].unique())
        st.markdown(f"#### Device Brand Popularity and Transaction Count in {states} ({years}, Q{quarters})")
        Agg_user_plot_3(A_user_y_Q, states)
        st.markdown(f"#### User Engagement Bar Charts for {states} ({years}, Q{quarters})")
        map_user_plot_3(Map_user_Y_Q, states)
        Merged=pd.read_csv('D:\phonepe project\my_data4')
        brand_data = Merged.groupby('brand')[['registeredusers', 'appopens']].sum().reset_index()
        brand_data['engagement_ratio'] = brand_data['appopens'] / brand_data['registeredusers']
        underutilized = brand_data.sort_values(by='engagement_ratio').head(5)
        st.subheader("Top Underutilized Device Brands (Low Engagement Ratio)")
        fig, ax = plt.subplots()
        sns.barplot(data=underutilized, x='brand', y='engagement_ratio', ax=ax, palette='Reds_r')
        ax.set_ylabel("App Opens per Registered User")
        plt.xticks(rotation=45)
        st.pyplot(fig)
            
        brand_data = A_user.groupby('Brands').agg({
        'Transaction_count': 'sum',
                'Percentage': 'mean'  # or any other metric approximating app opens if available
            }).reset_index()
        top_brands = brand_data.sort_values('Transaction_count', ascending=False)
        st.subheader('Top Device Brands by Total Users')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_brands, x='Brands', y='Transaction_count', ax=ax, color='skyblue')
        ax.set_xlabel('Device Brand')
        ax.set_ylabel('Total Users')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)



    elif cases == "Transaction Analysis for Market Expansion":
    
        st.subheader("Yearly State-Level Transaction Trends")
        col1, col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_transaction["Years"].min(), M_transaction["Years"].max(), M_transaction["Years"].min())
        Map_tran_tac_y = transaction_amount_count_Y(M_transaction, years)

        st.subheader("Top States by Transaction Performance")
        col1, col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State for In-Depth Analysis", Map_tran_tac_y["States"].unique())
        st.markdown(f"#### District-Level Transaction Overview for {states} ({years})")
        Map_insu_Districts(Map_tran_tac_y, states)
        
        df = M_transaction.rename(columns={
            'States': 'state', 
            'Years': 'year', 
            'Transaction_count': 'count', 
            'Transaction_amount': 'Transaction_amount'  # Adjust spelling if needed
        })
            
        if 'Transacion_amount' in df.columns:
            df = df.rename(columns={'Transacion_amount': 'Transaction_amount'})
        state_summary = df.groupby('state').agg({
            'Transaction_amount': 'sum',
            'count': 'sum'
        }).reset_index()
        state_summary['avg_transaction_value'] = state_summary['Transaction_amount'] / state_summary['count']
        st.subheader("Average Transaction Value by State")
        st.dataframe(state_summary[['state', 'avg_transaction_value']].sort_values(by='avg_transaction_value', ascending=False))
        state_summary_sorted = state_summary.sort_values(by='Transaction_amount', ascending=False)
        st.subheader("Top 10 States by Total Transaction Amount")
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.barplot(data=state_summary_sorted.head(10), x='Transaction_amount', y='state', palette='viridis', ax=ax)
        ax.set_xlabel('Transaction Amount (₹)')
        ax.set_ylabel('State')
        st.pyplot(fig)

        # Annual summary for YoY growth calculation
        annual_summary = df.groupby(['state', 'year']).agg({
            'count': 'sum',
            'Transaction_amount': 'sum'
        }).reset_index()

        annual_summary = annual_summary.sort_values(by=['state', 'year'])
        annual_summary['Transaction_amount_YoY_growth'] = annual_summary.groupby('state')['Transaction_amount'].pct_change() * 100

        # Latest year YoY growth bar plot
        latest_year = annual_summary['year'].max()
        growth_latest_year = annual_summary[annual_summary['year'] == latest_year].sort_values(by='Transaction_amount_YoY_growth', ascending=False)
        st.subheader(f'Top 10 States by Transaction Amount YoY Growth in {latest_year}')
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
        st.subheader("Quarterly State Performance Breakdown")
        col1, col2 = st.columns(2)
        with col1:
            quarters = st.slider("Select Quarter", Map_tran_tac_y["Quarter"].min(), Map_tran_tac_y["Quarter"].max(), Map_tran_tac_y["Quarter"].min())
        Map_tran_tac_y_Q = transaction_amount_count_Y_Q(Map_tran_tac_y, quarters)
        st.markdown(f"#### District-Level Quarterly Transaction Analysis for {states} (Q{quarters}, {years})")
        Map_insu_Districts(Map_tran_tac_y_Q, states)
                


        
        
    elif cases == "Insurance Engagement Analysis":
    
        st.subheader("Yearly State Insurance Transaction Summary")
        col1, col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_insurance["Years"].min(), M_insurance["Years"].max(), M_insurance["Years"].min())
        Map_insu_tac_y = transaction_amount_count_Y(M_insurance, years)

        st.subheader("District-Level Annual Insurance Activity")
        col1, col2 = st.columns(2)
        with col1:
            states = st.selectbox("Select State for Insurance Breakdown", Map_insu_tac_y["States"].unique())
        st.markdown(f"#### Annual Insurance Transactions by District in {states} ({years})")
        Map_insu_Districts(Map_insu_tac_y, states)

        st.subheader("Quarterly Insurance Performance Review by State")
        col1, col2 = st.columns(2)
        with col1:
            quarters = st.slider("Select Quarter", Map_insu_tac_y["Quarter"].min(), Map_insu_tac_y["Quarter"].max(), Map_insu_tac_y["Quarter"].min())
        Map_insu_tac_y_Q = transaction_amount_count_Y_Q(Map_insu_tac_y, quarters)

        st.markdown(f"#### Quarterly District Insurance Transactions in {states} (Q{quarters}, {years})")
        Map_insu_Districts(Map_insu_tac_y_Q, states)
        state_summary = A_insurance.groupby('States')[['Insurance_count', 'Insurance_amount']].sum().sort_values(by='Insurance_count', ascending=False)

        st.subheader("Quarterly Insurance Transaction Trend - Top 5 States")

        # Get top 5 states by transaction count
        top_states = state_summary.head(5).index.tolist()
        fig, ax = plt.subplots(figsize=(10, 6))
        for state in top_states:
            df = A_insurance[A_insurance['States'] == state]
            # Group by year and quarter for transaction counts
            df_grouped = df.groupby(['Years', 'Quarter'])['Insurance_count'].sum().reset_index()
            # Create a column for time labels
            df_grouped['Time'] = df_grouped['Years'].astype(str) + ' Q' + df_grouped['Quarter'].astype(str)
            ax.plot(df_grouped['Time'], df_grouped['Insurance_count'], label=state, marker='o')
        ax.set_xlabel("Quarter")
        ax.set_ylabel("Transaction Count")
        plt.xticks(rotation=45)
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)


    elif cases == "User Engagement and Growth Strategy":
    
        st.subheader("Annual User Engagement Overview")
        col1, col2 = st.columns(2)
        with col1:
            years = st.slider("Select Year", M_user["Years"].min(), M_user["Years"].max(), M_user["Years"].min())
            Map_user_Y = map_user_plot_1(M_user, years)
        with col2:
            quarters = st.slider("Select Quarter", Map_user_Y["Quarter"].min(), Map_user_Y["Quarter"].max(), Map_user_Y["Quarter"].min())
            Map_user_Y_Q = map_user_plot_2(Map_user_Y, quarters)

        st.subheader("State-Level User Engagement Breakdown")
        states = st.selectbox("Select State", Map_user_Y_Q["States"].unique())
        st.markdown(f"#### Detailed User Engagement Metrics for {states} ({years}, Q{quarters})")
        map_user_plot_3(Map_user_Y_Q, states)
        state_summary = M_user.groupby('States')[['RegisteredUsers', 'AppOpens']].sum().sort_values(by='RegisteredUsers', ascending=False)
        st.subheader('Registered and Active Users by State')
        st.dataframe(state_summary)

        # Group by state and district, aggregate and sort by registered users descending
        district_summary = M_user.groupby(['States', 'District'])[['RegisteredUsers', 'AppOpens']].sum().sort_values(by='RegisteredUsers', ascending=False)
        st.subheader('Top Districts by Registered Users')
        st.dataframe(district_summary.head(20))
        top_states = state_summary.head(10).index
        st.subheader('Quarterly Registered Users Trend - Top 10 States')
        fig, ax = plt.subplots(figsize=(10, 6))

        for state in top_states:
            df = M_user[M_user['States'] == state].groupby(['Years', 'Quarter'])[['RegisteredUsers']].sum().reset_index()
            df['Time'] = df['Years'].astype(str) + ' Q' + df['Quarter'].astype(str)
            ax.plot(df['Time'], df['RegisteredUsers'], label=state)

        ax.set_xlabel('Time')
        ax.set_ylabel('Registered Users')
        plt.xticks(rotation=45)
        ax.legend()
        st.pyplot(fig)

        # Calculate Engagement Ratio and handle infinities or NaNs
        M_user['Engagement_Ratio'] = M_user['AppOpens'] / M_user['RegisteredUsers']
        M_user.replace([float('inf'), -float('inf')], pd.NA, inplace=True)
        M_user.dropna(subset=['Engagement_Ratio'], inplace=True)

        engagement_ratio = M_user.groupby('States')['Engagement_Ratio'].mean().sort_values(ascending=False)

        st.subheader('Top 10 States by Average User Engagement Ratio')
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=engagement_ratio.head(10).index, y=engagement_ratio.head(10).values, ax=ax)
        ax.set_ylabel('Engagement Ratio (App Opens / Registered Users)')
        ax.set_xlabel('State')
        plt.xticks(rotation=90)
        st.pyplot(fig)




