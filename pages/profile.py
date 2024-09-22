import streamlit as st

def show():
    st.write("# Profile")
    st.markdown(f"**Username**: {st.session_state.username}")
    st.markdown(f"**Logged in**: {'Yes' if st.session_state.logged_in else 'No'}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Login"
