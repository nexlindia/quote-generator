import pandas as pd
from fpdf import FPDF
import streamlit as st

def load_rates(file_path):
    """Load activity rates from an Excel file."""
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    return df.set_index('Activity Name')['B2B Price (₹)'].to_dict()

def calculate_total(selected_activities, rates, margin=0.10):
    """Calculate total cost including margin."""
    base_cost = sum(rates[activity] for activity in selected_activities)
    total_cost = base_cost * (1 + margin)
    return round(total_cost, 2)

def generate_pdf_quote(selected_activities, rates, total_cost, file_name="quotation.pdf"):
    """Generate a PDF quotation."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Quotation", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for activity in selected_activities:
        pdf.cell(0, 10, f"{activity}: ₹{rates[activity]:,.2f}", ln=True)
    
    pdf.ln(10)
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, f"Total Cost (incl. 10% margin): ₹{total_cost:,.2f}", ln=True)
    
    pdf.output(file_name)
    return file_name

# Streamlit UI
def main():
    st.title("Quote Generator")
    file_path = "list_of_activities.xlsx"
    rates = load_rates(file_path)
    
    selected_activities = st.multiselect("Select Activities", options=list(rates.keys()))
    if st.button("Generate Quote"):
        if selected_activities:
            total = calculate_total(selected_activities, rates)
            file_name = generate_pdf_quote(selected_activities, rates, total)
            with open(file_name, "rb") as file:
                st.download_button(label="Download PDF", data=file, file_name=file_name, mime="application/pdf")
        else:
            st.error("Please select at least one activity.")

if __name__ == "__main__":
    main()
