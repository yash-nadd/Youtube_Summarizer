import streamlit as st

def show():
    # Common CSS for consistent styling
    st.markdown(
        """
        <style>
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
                margin-top: 20px;
                border-radius: 10px;
                background-color: #1e1e1e; /* Darker background for content */
            }
            .footer {
                text-align: center;
                margin-top: 50px;
            }
        </style>
        """, unsafe_allow_html=True
    )
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
 

    st.write("# Profile")
    
    st.markdown(
        """
        <div class="content">
             <p style="color: white;"><strong>Username</strong>: {username}</p>
        <p style="color: white;"><strong>Logged in</strong>: {status}</p>
        </div>
        """.format(username=st.session_state.username, status='Yes' if st.session_state.logged_in else 'No'),
        unsafe_allow_html=True
    )

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Login"
        st.success("You have been logged out.")

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

