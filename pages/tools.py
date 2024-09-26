import streamlit as st
import os
import base64
from fpdf import FPDF

def show():
    
    st.write("# Tools Section")
    st.write("This section can contain links or information about tools related to the YouTube Summarizer.")

    if os.path.exists('pages/texts/summary.txt'):
        with open('pages/texts/summary.txt', 'r') as file:
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
    st.markdown(
        """
        <style>
            * {
                box-sizing: border-box; /* Include padding and border in width calculations */
            }

            body {
                margin: 0; /* Remove default body margin */
                padding: 0; /* Remove default body padding */
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #000;
                padding: 10px;
                width: 100%; /* Ensure the navbar is as wide as the viewport */
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 100; /* Keep navbar above other content */
            }

            .navbar a {
                color: white;
                margin: 0 15px;
                text-decoration: none;
            }

            .navbar a:hover {
                color: #ad8aff;
            }

            /* Main header styling */
            .main-header {
                text-align: center;
                margin-top: 50px;
            }

            .main {
                background-color: #1e1e1e;
                color: white;
                padding-top: 60px; /* Add padding to prevent content from being hidden behind the navbar */
            }
            /* Styling for the navigation bar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #000;
            padding: 10px;
        }
        .navbar a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
        }
        .navbar a:hover {
            color: #ad8aff;
        }

        /* Main header styling */
        .main-header h1, .main-header h4 {
            text-align: center;
            margin-top: 50px;
            color: #ad8aff; /* Light color for the header text */
        }

        /* Input section styling */
        .input-section {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .input-box {
            width: 50%;
            padding: 10px;
            border-radius: 25px;
            border: 2px solid #ad8aff;
            color: white;  /* Set the input text color to white */
        }

        /* Audience boxes styling */
        .audience-boxes {
            display: flex;
            justify-content: space-evenly;
            margin-top: 50px;
        }
        .audience-box {
            background-color: #e6ccff;
            padding: 50px;
            text-align: center;
            border-radius: 20px;
            width: 200px;
            color: black; /* Adjust for contrast against light background */
        }

        /* FAQ Section */
        .faq-section {
            background-color: #1a1a1a;
            padding: 30px;
            border-radius: 20px;
            margin-top: 50px;
            color: white; /* Set the text color to white */
        }
        

        /* Footer Contact section */
        .footer {
            background-color: #e6ccff;
            padding: 20px;
            text-align: center;
            margin-top: 50px;
            color: black; /* Adjust for contrast against light background */
        }
        .main {
            background-color: #1e1e1e;  /* Dark black shade */
            color: white;  /* Ensure main content text color is white */
        }

        /* Ensuring that all text elements default to white on the dark background */
        body, h1, h2, h3, h4, p, div, span {
            color: white; /* Set all text to white by default */
        }
        

            /* Additional styles below */
            /* Your other styles here */
        </style>
        """, unsafe_allow_html=True
    )
 
    st.markdown(
    """
    <div class="faq-section">
        <h3>FREQUENTLY ASKED QUESTIONS</h3>
        <p>Q: Can I summarize any video?<br>A: Yes, as long as it's public.</p>
        <p>Q: How long does it take?<br>A: Just a few seconds to get the summary.</p>
        <p>Q: Can I save the summary?<br>A: Yes, download it as a PDF.</p>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <div class="footer">
        <p> 
            <a href="mailto:your-email@example.com" style="color: #000000;">Email</a> | 
            <a href="https://www.linkedin.com/in/your-linkedin-profile" target="_blank" style="color: #000000;">LinkedIn</a> | 
            <a href="https://twitter.com/your-twitter-handle" target="_blank" style="color: #000000;">Twitter</a> | 
            <a href="https://www.instagram.com/your-instagram-handle" target="_blank" style="color: #000000;">Instagram</a>
            <br>
            <br>
            <p style="color : #000000;">© 2024 YouTube Summarizer. All rights reserved.</p>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

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
