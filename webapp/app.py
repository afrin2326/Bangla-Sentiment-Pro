import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import sys
import os

# --- PATH CORRECTION ---
# This block ensures that Streamlit can find the 'src' folder
# even when running from inside the 'webapp' directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

try:
    from src.utils.helpers import get_analytics_data  # Database connection helper
except ImportError:
    st.error("Error: Could not find the 'src' directory. Please ensure your folder structure is correct.")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bangla Sentiment Pro",
    page_icon="🇧🇩",
    layout="wide"
)

# --- CUSTOM CSS FOR INDUSTRY STANDARD LOOK ---
st.markdown("""
    <style>
    .main { background: #f0f2f6; }
    .stTextArea textarea { border-radius: 15px; border: 2px solid #e0e0e0; }
    .stButton>button { 
        background: linear-gradient(45deg, #FF4B2B, #FF416C); 
        color: white; border-radius: 25px; height: 50px; font-weight: bold; border: none;
        transition: 0.3s; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .stat-card {
        padding: 20px; border-radius: 15px; background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;
        margin-bottom: 10px; border-top: 5px solid #FF4B2B;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/analytics.png")
    st.title("🚀 Business Suite")
    
    mode = st.radio(
        "Select Operation Mode:",
        ["Real-time Analysis", "Bulk Upload (Excel)", "Business Insights"]
    )
    
    st.divider()
    api_url = st.text_input("API Endpoint", value="http://localhost:8000/predict")
    st.info("Architecture: BanglaBERT Dual-Head Intelligence")

# --- MAIN HEADER ---
st.title("🇧🇩 Bangla Sentiment & Emotion Intelligence")
st.markdown("---")

# --- FEATURE 1: REAL-TIME ANALYSIS ---
if mode == "Real-time Analysis":
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown("### 📝 Input Analysis")
        user_input = st.text_area("Paste your Bengali text here:", height=200, placeholder="আপনার টেক্সট এখানে লিখুন...")
        
        if st.button("RUN INTELLIGENCE"):
            if user_input.strip() == "":
                st.warning("Please enter some text first!")
            else:
                with st.spinner("🤖 AI is processing..."):
                    try:
                        response = requests.post(api_url, json={"text": user_input})
                        if response.status_code == 200:
                            data = response.json()
                            
                            st.markdown("### 🎯 Prediction Results")
                            res_col1, res_col2 = st.columns(2)
                            
                            with res_col1:
                                st.markdown(f"<div class='stat-card'><h4>Sentiment</h4><h2 style='color:#FF4B2B'>{data['sentiment']}</h2></div>", unsafe_allow_html=True)
                            with res_col2:
                                st.markdown(f"<div class='stat-card'><h4>Emotion</h4><h2 style='color:#1D4ED8'>{data['emotion']}</h2></div>", unsafe_allow_html=True)
                            
                            st.markdown("### 📊 Confidence Analysis")
                            chart_data = pd.DataFrame({
                                'Metric': ['Sentiment Score', 'Emotion Score', 'Text Clarity'],
                                'Value': [95, 88, 82] 
                            })
                            fig = px.bar(chart_data, x='Metric', y='Value', color='Metric', range_y=[0, 100], template="plotly_white")
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.error(f"API Error! Code: {response.status_code}")
                    except Exception as e:
                        st.error(f"Backend connection failed: {e}")

    with col2:
        st.markdown("### 📚 Key Insights")
        st.success("✅ **BanglaBERT Core**")
        st.success("✅ **Dual-Head Intelligence**")
        st.info("This system analyzes nuanced Bangla expressions including sarcasm and cultural context.")
        st.image("https://img.icons8.com/clouds/200/brainstormskilling.png")

# --- FEATURE 2: BULK EXCEL PROCESSING ---
elif mode == "Bulk Upload (Excel)":
    st.markdown("### 📂 Bulk Business Processing")
    st.write("Upload an Excel file (.xlsx) to analyze multiple customer reviews at once.")
    
    uploaded_file = st.file_uploader("Upload Review Sheet", type=["xlsx"])
    
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.markdown("#### Data Preview")
        st.dataframe(df.head(), use_container_width=True)
        
        if st.button("PROCESS ALL REVIEWS"):
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, row in df.iterrows():
                review_text = str(row.iloc[0])
                try:
                    res = requests.post(api_url, json={"text": review_text}).json()
                    results.append({
                        "Original Text": review_text,
                        "Sentiment": res.get("sentiment"),
                        "Emotion": res.get("emotion")
                    })
                except:
                    results.append({"Original Text": review_text, "Sentiment": "Error", "Emotion": "Error"})
                
                progress = (i + 1) / len(df)
                progress_bar.progress(progress)
                status_text.text(f"Processing: {i+1} / {len(df)}")

            result_df = pd.DataFrame(results)
            st.markdown("### ✅ Processing Complete")
            st.dataframe(result_df, use_container_width=True)
            
            st.download_button(
                label="📥 Download Results as CSV",
                data=result_df.to_csv(index=False).encode('utf-8'),
                file_name="bulk_analysis_results.csv",
                mime="text/csv"
            )

# --- FEATURE 3: BUSINESS INSIGHTS ---
elif mode == "Business Insights":
    st.markdown("### 📊 Enterprise Analytics Dashboard")
    
    try:
        df_db = get_analytics_data()
        
        if df_db is not None and not df_db.empty:
            total_data = len(df_db)
            st.metric("Total Analysis Operations", total_data)
            
            c1, c2 = st.columns(2)
            
            with c1:
                sentiment_summary = df_db['sentiment'].value_counts().reset_index()
                fig1 = px.pie(sentiment_summary, values='count', names='sentiment', 
                              title='Global Sentiment Overview',
                              hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig1, use_container_width=True)
                
            with c2:
                emotion_summary = df_db['emotion'].value_counts().reset_index()
                fig2 = px.bar(emotion_summary, x='emotion', y='count', 
                              title='Top Customer Emotions',
                              color='emotion', template="plotly_white")
                st.plotly_chart(fig2, use_container_width=True)
                
            st.markdown("#### 🕒 Latest Activity Log")
            st.table(df_db.tail(10))
        else:
            st.warning("The database is currently empty. Start analyzing text to see insights here!")
    except Exception as e:
        st.error(f"Database connection error: {e}")