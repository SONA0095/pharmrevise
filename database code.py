import streamlit as st
import pandas as pd
import os

# Correct file path
file_path = r"C:\Users\Sona\Desktop\PDD -SONA\databases\data.csv"

# Check if file exists
if not os.path.exists(file_path):
    st.error("❌ Data file not found! Please check the file path.")
else:
    # Load dataset
    df = pd.read_csv(file_path)

    # Page Configuration
    st.set_page_config(page_title="PharmReVise", layout="wide")

    # Custom Styling
    st.markdown("""
        <style>
            .title { text-align: center; font-size: 60px; font-weight: bold; color: black; } 
            .subtitle { text-align: center; font-size: 30px; font-weight: bold; color: blue; } 
            .filters { font-size: 18px; font-weight: bold; }
            .data-sources { 
                text-align: center; 
                background-color: rgba(0, 0, 0, 0.05); 
                padding: 10px; 
                border-radius: 10px; 
                font-size: 16px; 
                font-weight: bold; 
                color: black;
            }
            .footer { text-align: center; font-size: 18px; font-weight: bold; color: blue; }
        </style>
    """, unsafe_allow_html=True)

    # Logo + Title
    st.markdown('<p class="title">PharmReVise</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Drug Repurposing Database - FDA Approved Drugs</p>', unsafe_allow_html=True)

    # Search Query Input
    search_query = st.text_input("🔍 Enter Possible Repurposed Use:", "", key="search",
                                help="Example: Cancer, Liver Disease, Alzheimer’s")

    # Filters
    st.markdown('<p class="filters">📊 Apply Filters:</p>', unsafe_allow_html=True)

    # AI Predicted Repurposing Potential Filter
    repurposing_potential = st.selectbox("AI Predicted Repurposing Potential", ["All", "Low", "Moderate", "High"], index=0)

    # Filtered Search Logic
    if st.button("Search 🔎"):
        results = df.copy()

        # Apply search query filter
        if search_query:
            results = results[results["Possible Repurposed Use"].str.contains(search_query, case=False, na=False)]

        # Apply AI Predicted Repurposing Potential filter
        if repurposing_potential != "All":
            results = results[results["AI Predicted Repurposing Potential"] == repurposing_potential]

        # Display results
        if not results.empty:
            st.write("### ✅ Matching FDA-Approved Drugs for Repurposing:")
            st.dataframe(results)  # Display filtered table
        else:
            st.warning("⚠️ No matching results found. Try another search term or adjust filters.")

    # Sources for Data Collection
    st.markdown('<p class="data-sources">Sources for Data Collection:</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="data-sources">
    DrugBank, PubChem, ChEMBL, ClinicalTrials.gov, FDA Orange Book, RxNorm,  
    SIDER (Side Effect Resource), FAERS (FDA Adverse Event Reporting System), Open Targets,  
    KEGG Pathways, PKDB (Pharmacokinetics Database), DailyMed, Pharmaceutical Company Websites
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown('<p class="footer">Created by SONA S</p>', unsafe_allow_html=True)
