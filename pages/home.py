import streamlit as st
import subprocess
import os

# Set page config as the first command

def show():
    st.markdown(
        """
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 0;
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #000;
                padding: 10px;
                width: 100%;
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

            .main-header {
                text-align: center;
                margin-top: 50px;
            }

            .main {
                background-color: #1e1e1e;
                color: white;
                padding-top: 60px;
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
                color: white;
                background-color: #1a1a1a;
            }

            .input-box::placeholder {
                color: grey;
            }


            .centered-title {
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 24px;
                margin-top: 20px;
            }

            .audience-boxes {
                display: flex;
                justify-content: space-evenly;
                margin-top: 50px;
            }

            .audience-box {
                background-color: #e6ccff;
                padding: 20px;
                text-align: center;
                border-radius: 20px;
                width: 200px;
                color: black;
            }

            .faq-section {
                background-color: #1a1a1a;
                padding: 30px;
                border-radius: 20px;
                margin-top: 50px;
                color: white;
            }

            .footer {
                background-color: #e6ccff;
                padding: 20px;
                text-align: center;
                margin-top: 50px;
                color: black;
            }

            body, h1, h2, h3, h4, p, div, span {
                color: white;
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-header" style="text-align: center;">
            <h1 style="margin-bottom: 0; line-height: 1.2;">
                <span style="color: #ffffff;">Watch less</span>, 
                <span style="color: #9D4FDB;"><i>understand more.</i></span>
            </h1>
            <h4 style="margin-top: 0; color: #FFFFFF;">Summarize YouTube videos in seconds!</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    if "video_url" not in st.session_state:
        st.session_state.video_url = ""

    if "summary" not in st.session_state:
        st.session_state.summary = ""

    col1, col2 = st.columns([3, 1])

    with col1:
        video_url = st.text_input("Enter YouTube URL", value=st.session_state.video_url)

    with col2:
        summary_length = st.number_input("Length", min_value=10, max_value=200, value=100, step=10)

    # Centering the button here
    
    submit_button = st.button("Submit", key="submit_button", help="Generate Summary")
   

    if submit_button and video_url:
        with open('pages/texts/video_id.txt', 'w') as file:
            file.write(video_url)

        st.write("Generating summary... Please wait.")

        try:
            subprocess.run(["python3", "summarizer.py", str(summary_length)], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Error occurred while generating summary: {e}")
            st.stop()

        if os.path.exists('pages/texts/summary.txt'):
            with open('pages/texts/summary.txt', 'r') as file:
                summary = file.read()

            video_id = video_url.split('=')[-1]

            st.session_state.video_url = video_url
            st.session_state.summary = summary
            st.session_state.video_id = video_id

        else:
            st.write("Summary not available yet.")

    if st.session_state.summary:
        st.subheader("Summary of the video:")
        st.markdown(
            f"""
            <div style="border: 2px solid #e6e6e6; padding: 20px; border-radius: 10px; display: flex; justify-content: space-between;">
                <div style="flex: 1; padding-right: 20px;">
                    <iframe width="100%" height="315" src="https://www.youtube.com/embed/{st.session_state.video_id}" frameborder="0" allowfullscreen></iframe>
                </div>
                <div style="flex: 2;">
                    <h4>Summary</h4>
                    <p>{st.session_state.summary}</p>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <h3 style="font-weight: bold; color:#9D4FDB;">Who Can Benefit from the Summarizer?</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="audience-boxes">
            <div class="audience-box">
                <img src="https://imonkey-blog.imgix.net/blog/wp-content/uploads/2017/03/14175146/shutterstock_348710576-750x500.jpg?auto=fortmat&fit=clip&expires=1758585600&width=830&height=553" alt="Students" style="width: 100%; height: auto; border-radius: 10px;">
                <div style="margin-top: 10px;  color: black;">Students</div>
            </div>
            <div class="audience-box">
                <img src="https://www.uab.edu/news/images/community_researchers.jpg" alt="Researchers" style="width: 100%; height: auto; border-radius: 10px;">
                <div style="margin-top: 10px; color: black;">Researchers</div>
            </div>
            <div class="audience-box">
                <img src="https://cryodragon.ca/wp-content/uploads/2016/07/Professional-Website-Design-Business-Meeting.jpg" alt="Professionals" style="width: 100%; height: auto; border-radius: 10px;">
                <div style="margin-top: 10px; color: black;">Professionals</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="faq-section">
            <h3>FREQUENTLY ASKED QUESTIONS</h3>
            <p>Q: Can I summarize any video?<br>A: Yes, as long as it's public.</p>
            <p>Q: How long does it take?<br>A: Just a few seconds depending on the video length.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            <p>
                <a href="mailto:example@example.com" style="color: black;">Email</a> |
                <a href="https://www.linkedin.com" style="color: black;">LinkedIn</a> |
                <a href="https://twitter.com" style="color: black;">Twitter</a> |
                <a href="https://www.instagram.com" style="color: black;">Instagram</a>
            </p>
            <p style=" color: black;">© 2024 YouTube Summarizer. All rights reserved.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Call the show function to run the app
show()