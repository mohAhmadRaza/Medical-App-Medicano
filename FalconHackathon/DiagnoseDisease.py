import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os


class Diagnose:
    def __init__(self):
        # loading environment variables from .env file
        load_dotenv()
        self.AI71_API_KEY = os.getenv("AI71_API_KEY")
        self.client = AI71(self.AI71_API_KEY)

    def app(self):

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

        with st.form("diagnose_form"):
            options = [
                "Cholangitis",
                "Cholecystitis",
                "Cholelithiasis",
            ]
            symptoms = st.multiselect("Select Your Symptoms", options)
            submit_diagnose = st.form_submit_button("Diagnose")

            if submit_diagnose:
                prompt = (
                    f"Based on the symptoms listed: {symptoms}, please perform a detailed diagnostic analysis. "
                    f"Your task is to provide a comprehensive overview of the potential disease, including the following sections:\n"
                    f"- **Disease Name**: Clearly state the name of the disease.\n"
                    f"- **History**: Describe the historical context and background of the disease.\n"
                    f"- **Introduction**: Provide an introduction to the disease, including its significance and impact.\n"
                    f"- **Causes**: Outline the primary causes and contributing factors of the disease.\n"
                    f"- **Symptoms**: List and explain the symptoms associated with the disease.\n"
                    f"- **Side Effects**: Detail any potential side effects related to the disease or its treatments.\n"
                    f"- **Measures to Cure**: Recommend treatment options and measures to cure or manage the disease.\n"
                    f"Please ensure that each section is well-organized with clear headings. Additionally, include relevant hyperlinks where applicable:\n"
                    f"- **Blog Links**: For additional readings and blog posts.\n"
                    f"- **Article Links**: For scholarly articles and research papers.\n"
                    f"Ensure the output is professionally structured and provides valuable information for users seeking medical advice."
                )

                response = self.client.chat.completions.create(
                    model="tiiuae/falcon-180b-chat",
                    messages=[
                        {"role": "system", "content": "You are a medical assistant."},
                        {"role": "user", "content": prompt},
                    ],
                    stream=True,
                )

                # Collect the streamed response content
                response_content = ""
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        response_content += chunk.choices[0].delta.content

                st.title("Disease Diagnosis")
                st.markdown(response_content)