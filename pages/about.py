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
                z-index: 100;
            }
            .navbar a {
                color: white;
                margin: 0 15px;
                text-decoration: none;
            }
            .navbar a:hover {
                color: #ad8aff;
            }
            .main-header h1 {
                text-align: center;
                margin-top: 60px;
                color: #ad8aff;
            }
            .content {
                padding: 20px;
                margin-top: 100px; /* Adjust for fixed navbar */
                border-radius: 10px;
                background-color: #1e1e1e;
                color: white; /* Darker background for content */
            }
            .faq-section {
                background-color: #1a1a1a;
                padding: 30px;
                border-radius: 20px;
                margin-top: 50px;
                color: white; /* Set the text color to white */
            }
            .footer {
                background-color: #e6ccff;
                padding: 20px;
                text-align: center;
                margin-top: 50px;
                color: black; /* Adjust for contrast against light background */
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.write("# About YouTube Summarizer")
    
    st.markdown(
        """
        <div class="content">
            The YouTube Summarizer is a tool designed to automatically extract and summarize the transcript of a YouTube video,
            providing a brief overview of the video's content.
            <br><br>
            Built using Python and Streamlit, this tool integrates various APIs and machine learning, deep learning, and natural language processing models to generate concise video summaries.
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
                <p style="color: #000000;">© 2024 YouTube Summarizer. All rights reserved.</p>
            </p>
        </div>
        """, unsafe_allow_html=True
    )
