import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os


class Alternatives:
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
            <div style="background-color: #000066; text-align: center; padding: 10px; border-radius: 5px; margin-bottom: 30px;">
              <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Medicano</h1>
              <h2 style="color: white; font-size: 20px; margin-top: 5px;">A Medical Assistant</h2>
            </div>
        """, unsafe_allow_html=True)

        name = st.text_input("Enter name of the medicine you're using or considering")
        symptoms = st.text_input("What condition or symptoms are you treating with this medicine?")
        ingredients = st.text_input("Do you know the active ingredient in the medicine?")
        price = st.text_input("Are you looking for more affordable alternatives?")

        # Constructing the prompt
        prompt = (f"You are provided with the following information about a medicine:\n\n"
                  f"Medicine Name: {name}\n"
                  f"Condition/Symptoms Treated: {symptoms}\n"
                  f"Active Ingredient: {ingredients}\n"
                  f"Price Consideration: {price}\n\n"
                  "Based on this information, your task is to find and suggest alternative medicines that can be used to "
                  "treat the same condition or symptoms. Provide a detailed comparison of the alternatives, including their "
                  "active ingredients, effectiveness, safety profile, availability, and cost in various regions. Make sure to "
                  "highlight the pros and cons of each alternative. Additionally, provide any relevant research or resources "
                  "to support your suggestions.")

        if st.button("Find Alternatives"):
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

            st.title(f"Alternatives Of {name}")
            st.markdown(response_content)
