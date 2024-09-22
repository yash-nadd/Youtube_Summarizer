import streamlit as st
import subprocess
import os

def show():
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

