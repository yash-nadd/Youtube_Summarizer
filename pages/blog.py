import streamlit as st

def show():
    # Common CSS for consistent styling
    st.markdown(
        """
        <style>
            * {
                box-sizing: border-box; /* Include padding and border in width calculations */
            }
            body {
                margin: 0;
                padding: 0;
                background-color: #000; /* Set background color to black */
                color: white; /* Ensure text color is white for contrast */
            }
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #000;
                padding: 10px;
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
            .main-header h1, .main-header h4 {
                text-align: center;
                margin-top: 60px;
                color: #ad8aff; /* Light color for the header text */
            }
            h2 {
                color: #ad8aff;
                margin-top: 30px;
            }
            .content {
                padding: 20px;
                margin-top: 20px;
                border-radius: 10px;
                background-color: #1e1e1e; /* Darker background for content */
            }
            .footer {
                background-color: #e6ccff;
                padding: 20px;
                text-align: center;
                margin-top: 50px;
                color: black; /* Adjust for contrast against light background */
            }
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
                color: white; /* Set the input text color to white */
            }
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
            .faq-section {
                background-color: #1a1a1a;
                padding: 30px;
                border-radius: 20px;
                margin-top: 50px;
                color: white; /* Set the text color to white */
            }
            .main {
                background-color: #1e1e1e; /* Dark black shade */
                color: white; /* Ensure main content text color is white */
            }
            h1 {
                color: #9D4FDB; /* Change the color of h1 headings */
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.write("<h1>How to Use YouTube Summarizer and PDF Tool</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content">
            YouTube Summarizer

            1. Enter the YouTube URL in the input field on the home page.
            2. Click on the 'Submit' button.
            3. Wait for a few moments while the summarization is being processed.
            4. The video and its summary will be displayed below the input field.

            PDF Tool

            1. After generating the video summary, navigate to the 'Tools' section.
            2. Click on the 'Convert Summary to PDF' button to create a PDF file of the summary.
            3. Once the PDF is created, you will see a 'Download PDF' button.
            4. Click the 'Download PDF' button to download the summary as a PDF file to your device.
        </div>
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
        """, unsafe_allow_html=True
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
        """, unsafe_allow_html=True
    )