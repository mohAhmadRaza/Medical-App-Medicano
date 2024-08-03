import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os


class Blogs:
    def __init__(self):
        # loading environment variables from .env file
        load_dotenv()
        self.AI71_API_KEY = os.getenv("AI71_API_KEY")
        self.client = AI71(self.AI71_API_KEY)

    def app(self):

        # Streamlit UI components
        st.markdown("""
            <div style="background-color: #000066; text-align: center; padding: 10px; border-radius: 5px; margin-bottom: 30px;">
              <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Medicano</h1>
              <h2 style="color: white; font-size: 20px; margin-top: 5px;">A Medical Assistant</h2>
            </div>
        """, unsafe_allow_html=True)

        topic = st.text_input("Enter topic for blog & articles")

        # Constructing the prompt
        prompt = (f"You are provided with the topic to provide 5 blogs and 5 references about it:\n\n"
                  f"topic Name: {topic}\n"
                  "Based on this information, your task is to find and display 5 blogs medicines that can be used to "
                  "read the same topic. Give the links in table formate add five columns with respective names")

        if st.button("Find Blogs"):
            response = self.client.chat.completions.create(
                model="tiiuae/falcon-180b-chat",
                messages=[
                    {"role": "system", "content": "You are a mblog and articles assistant."},
                    {"role": "user", "content": prompt},
                ],
                stream=True,
            )

            # Collect the streamed response content
            response_content = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    response_content += chunk.choices[0].delta.content

            st.title(f"Blogs Related to {topic}")
            st.markdown(response_content)
