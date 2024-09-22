import streamlit as st
import os
import base64
from fpdf import FPDF

def show():
    st.write("# Tools Section")
    st.write("This section can contain links or information about tools related to the YouTube Summarizer.")

    if os.path.exists('texts/summary.txt'):
        with open('texts/summary.txt', 'r') as file:
            summary = file.read()

        if st.button("Convert Summary to PDF"):
            create_pdf(summary)
            st.success("PDF created successfully!")

            with open("summary.pdf", "rb") as pdf_file:
                pdf_data = pdf_file.read()
                pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name="summary.pdf",
                    mime="application/pdf"
                )

                st.markdown(
                    f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="600px"></iframe>',
                    unsafe_allow_html=True
                )
    else:
        st.write("No summary available for PDF conversion.")

def create_pdf(summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.cell(200, 10, txt="YouTube Video Summary", ln=True, align='C')
    pdf.ln(10)

    # Normalize the summary to handle unsupported characters
    summary = summary.encode('latin-1', 'replace').decode('latin-1')

    # Add the summary to the PDF
    pdf.multi_cell(0, 10, txt=summary)
    
    # Save the PDF
    pdf.output("summary.pdf")
