import streamlit as st
import os
from dotenv import load_dotenv
from ai71 import AI71


class Pharmacies:
    def __init__(self):
        # loading environment variables from .env file
        load_dotenv()
        self.AI71_API_KEY = os.getenv("AI71_API_KEY")
        self.client = AI71(self.AI71_API_KEY)

    def app(self):

        # Streamlit UI components
        st.markdown("""
            <div style="background-color: #000066; text-align: center; padding: 10px;border-radius : 5px;margin-bottom: 10px;">
              <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Medicano</h1>
              <h2 style="color: white; font-size: 20px; margin-top: 5px;">A Medical Assistant</h2>
            </div>
            """, unsafe_allow_html=True)

        country = st.text_input("Enter The Country Name")
        state = st.text_input("Enter the State Name")
        city = st.text_input("Enter The City Name")
        town = st.text_input("Enter the Town/Village Name")
        others = st.text_input("Further Location")

        if st.button("Find Pharmacies"):
            prompt = f"""
            You are a highly capable AI designed to provide comprehensive and accurate information. The user has provided the following location details to find pharmacies:
        
            - Country: {country}
            - State: {state}
            - City: {city}
            - Town/Village: {town}
            - Additional Location Information: {others}
        
            Please identify and list all available pharmacies in this location. For each pharmacy, include the following details if available:
            1. Pharmacy Name
            2. Address
            3. Contact Information
            4. Operating Hours
            5. Services Offered
        
            If the exact location is not available, provide the nearest pharmacies or general information about pharmacies in the specified area. Make sure to include any relevant details that could assist the user in locating a pharmacy. Use google map or any other to find pharmacies
            """

            response = self.client.chat.completions.create(
                model="tiiuae/falcon-180b-chat",
                messages=[
                    {"role": "system", "content": "You are a google map."},
                    {"role": "user", "content": prompt},
                ],
                stream=True,
            )

            # Collect the streamed response content
            response_content = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    response_content += chunk.choices[0].delta.content

            st.title(f"Pharmacies Located")
            st.markdown(response_content)