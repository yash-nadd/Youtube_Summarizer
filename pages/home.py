import streamlit as st
import subprocess
import os



def show():
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
        .submit-button {
            background-color: #ad8aff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
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
    <div class="main-header">
        <h1>Watch less, <span style="color: #ad8aff;">understand more.</span></h1>
        <h4>summarize YouTube videos in seconds!</h4>
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/YouTube_icon_%282013-2017%29.png/800px-YouTube_icon_%282013-2017%29.png" width="50" style="margin-right: 10px;">
            <h1>YouTube Summarizer</h1>
        </div>
        """, unsafe_allow_html=True
    )

    # Use session state for the video URL
    if "video_url" not in st.session_state:
        st.session_state.video_url = ""

    if "summary" not in st.session_state:
        st.session_state.summary = ""
    
    # Create two columns
    col1, col2 = st.columns([3, 1])  # Adjust proportions as needed

    with col1:
        video_url = st.text_input("Enter YouTube URL", value=st.session_state.video_url)

    with col2:
        summary_length = st.number_input("Length", min_value=10, max_value=200, value=100, step=10)

    submit_button = st.button("Submit")

    if submit_button and video_url:
        with open('texts/video_id.txt', 'w') as file:
            file.write(video_url)

        st.write("Generating summary... Please wait.")

        try:
            subprocess.run(["python3", "summarizer.py", str(summary_length)], check=True)
        except subprocess.CalledProcessError as e:
            st.error(f"Error occurred while generating summary: {e}")
            st.stop()

        if os.path.exists('texts/summary.txt'):
            with open('texts/summary.txt', 'r') as file:
                summary = file.read()

            video_id = video_url.split('=')[-1]

            # Store in session state
            st.session_state.video_url = video_url
            st.session_state.summary = summary
            st.session_state.video_id = video_id

        else:
            st.write("Summary not available yet.")

    # Display the summary if available
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
    <div class="audience-boxes">
        <div class="audience-box"><br>Students</div>
        <div class="audience-box"><br>Researchers</div>
        <div class="audience-box"><br>Professionals</div>
    </div>
    """,
    unsafe_allow_html=True
    

    
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

 