import streamlit as st
import pandas as pd
import requests
import os

# API Base URL
API_BASE_URL = "http://localhost:5050"

# File path for the FDA-approved drug repurposing database
data_path = r"C:\Users\Sona\Desktop\PDD -SONA\PDD -SONA\pharmrevise-app\backend\data.csv"

# Custom CSS for a vibrant UI
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f5;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background: linear-gradient(to right, #36D1DC, #5B86E5);
            color: white;
        }
        .stTitle, .stHeader, .stSubheader {
            text-align: center;
            color: #ffffff;
        }
        .stTextInput input {
            background-color: #e6e6e6;
            border-radius: 10px;
            padding: 8px;
            font-size: 18px;
        }
        .stButton button {
            background-color: #ff8c00 !important;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
        }
        .stButton button:hover {
            background-color: #ff6600 !important;
        }
        .stDataframe table {
            background-color: white;
            border-radius: 10px;
        }
        .stSuccess {
            color: #008000 !important;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    apply_custom_css()
    st.title("PharmReVise: FDA-Approved Drug Repurposing Database")
    
    tabs = st.tabs(["Home", "Database", "Tools", "About", "Feedback"])

    with tabs[0]:
        home_page()
    with tabs[1]:
        display_database()
    with tabs[2]:
        tools_menu()
    with tabs[3]:
        about_page()
    with tabs[4]:
        feedback_page()

# Home Page
def home_page():
    st.subheader("Unlocking Drug Repurposing Potential")
    search_term = st.text_input("Search for a drug, target, or indication:")
    if search_term:
        df = pd.read_csv(data_path)
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        st.dataframe(filtered_df)

# Display Database
def display_database():
    st.subheader("Full Drug Repurposing Database")
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.dataframe(df)
    else:
        st.error("Database file not found!")

# Tools Menu
def tools_menu():
    st.subheader("Explore Drug Discovery Tools")
    tool = st.selectbox("Select a tool:", [
        "Drug-Target Docking", "Binding Affinity Prediction", "AI-Powered Target Identification", 
        "Molecular Similarity Search", "Pathway & Mechanism of Action Analysis", "ADMET Prediction", 
        "Clinical Trial Data Lookup", "Case Studies & Research Papers Search", "Drug-Drug Interaction Risk", 
        "Toxicity & Side Effect Prediction", "FDA Approval Status Checker", "Marketed By & Brand Name Lookup", 
        "Patent & Regulatory Data Search", "AI-Powered Repurposing Score"
    ])
    
    input_fields = {}
    
    if tool in ["Drug-Target Docking", "Binding Affinity Prediction"]:
        input_fields["Drug Name"] = st.text_input("Enter Drug Name:")
        input_fields["Target Protein"] = st.text_input("Enter Target Protein:")
    elif tool == "AI-Powered Target Identification":
        input_fields["Disease Name"] = st.text_input("Enter Disease Name:")
    elif tool == "Molecular Similarity Search":
        input_fields["Drug Name"] = st.text_input("Enter Drug Name:")
    elif tool == "Pathway & Mechanism of Action Analysis":
        input_fields["Drug Name"] = st.text_input("Enter Drug Name:")
    elif tool == "Drug-Drug Interaction Risk":
        input_fields["Drug Name"] = st.text_input("Enter Drug Name:")
        input_fields["Combination Drug"] = st.text_input("Enter Combination Drug:")
    else:
        input_fields["Drug Name"] = st.text_input("Enter Drug Name:")
    
    if st.button("Run Analysis"):
        response = requests.post(f"{API_BASE_URL}/api/{tool.lower().replace(' ', '-').replace('&', 'and')}", json=input_fields)
        if response.status_code == 200:
            result = response.json()
            st.write("### Results")
            st.table(pd.DataFrame([result]))
        else:
            st.error("Failed to fetch results. Please try again.")

# About Page
def about_page():
    st.subheader("About PharmReVise")
    st.write(
        """
        **PharmReVise** is a powerful platform designed for drug repurposing research using FDA-approved medications. 
        Our goal is to accelerate drug discovery by utilizing existing pharmaceuticals for new therapeutic applications.
        
        ### Key Features:
        - Access a curated database of FDA-approved drugs.
        - Perform drug-target docking and binding affinity predictions.
        - AI-powered tools for target identification and molecular similarity searches.
        - Pathway analysis and ADMET predictions.
        - Explore clinical trial data and drug-drug interaction risks.
        
        **Who can use this?**
        - Researchers and scientists in drug discovery.
        - Clinicians exploring alternative treatment options.
        - Students and educators in pharmaceutical sciences.
        - Biotech and pharmaceutical companies.
        
        Join us in revolutionizing drug repurposing for better healthcare outcomes!
        """
    )

# Feedback Page
def feedback_page():
    st.subheader("Share Your Feedback")
    feedback = st.text_area("Let us know your thoughts!")
    if st.button("Submit Feedback"):
        st.markdown("<p class='stSuccess'>Thank you for your feedback!</p>", unsafe_allow_html=True)
    st.write("© PharmReVise | Sona")

if __name__ == "__main__":
    main()
