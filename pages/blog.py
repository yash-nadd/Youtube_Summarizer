import streamlit as st

def show():
    st.write("# How to Use YouTube Summarizer and PDF Tool")
    st.markdown(
        """
        ## YouTube Summarizer

        1. Enter the YouTube URL in the input field on the home page.
        2. Click on the 'Submit' button.
        3. Wait for a few moments while the summarization is being processed.
        4. The video and its summary will be displayed below the input field.

        ## PDF Tool

        1. After generating the video summary, navigate to the 'Tools' section.
        2. Click on the 'Convert Summary to PDF' button to create a PDF file of the summary.
        3. Once the PDF is created, you will see a 'Download PDF' button.
        4. Click the 'Download PDF' button to download the summary as a PDF file to your device.
        """
    )
