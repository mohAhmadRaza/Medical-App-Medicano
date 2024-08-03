import streamlit as st

def app():

    # Custom CSS for styling FAQs
    custom_css = """
    <style>
    .initial-message {
        color: black;
        padding: 5px;  /* Padding around the content */
        font-size: 17px;  /* Larger font size */
        line-height: 1.5;  /* Slightly increased line height for readability */
        text-align: center;
        margin-bottom: 10px;
        margin-top: 10px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Streamlit UI components
    st.markdown("""
    <div style="background-color: #000066; text-align: center; padding: 10px;border-radius : 5px">
      <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Medicano</h1>
      <h2 style="color: white; font-size: 20px; margin-top: 5px;">A Medical Assistant</h2>
    </div>
    """, unsafe_allow_html=True)