import os
import pandas as pd
import streamlit as st

# Set page title and apply some CSS for better styling
st.set_page_config(page_title="Automated Threat Hunting", layout="wide")

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem;} /* Adjusts top padding */
    .stButton>button {margin-top: 10px;} /* Adds space above buttons */
    .uploadedFile {display: flex; justify-content: center;} /* Centers uploaded file */
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with an icon
st.markdown("## 🔷 Automated Threat Hunting Dashboard - Created by Ravi Kumar Mishra")

# Use columns for better alignment
col1, col2 = st.columns([3, 2])  # Adjust column width ratios

with col1:
    st.subheader("📂 Upload a CSV file containing log data")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"], key="file_uploader")

with col2:
    if uploaded_file:
        st.success("✅ File uploaded successfully!")

# Check if a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif os.path.exists("data/logs.csv"):
    df = pd.read_csv("data/logs.csv")
else:
    st.warning("⚠️ Please upload a CSV file to proceed.")
    st.stop()

# Display raw data in a well-aligned way
st.subheader("📄 Raw Data Preview")
st.dataframe(df, use_container_width=True)

# Highlight severity
def highlight_severity(val):
    colors = {"Low": "green", "Medium": "yellow", "High": "orange", "Critical": "red"}
    return f"background-color: {colors.get(val, 'white')}; color: black"

st.subheader("🎨 Styled Data with Severity Highlighting")
styled_df = df.style.applymap(highlight_severity, subset=["severity"])
st.dataframe(styled_df, use_container_width=True)

# 📌 Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        🔥 Developed with ❤️ by <b>Ravi Kumar Mishra</b>
    </p>
""", unsafe_allow_html=True)