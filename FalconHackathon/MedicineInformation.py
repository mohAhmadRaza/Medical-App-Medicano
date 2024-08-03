import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os

class Information:
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

        with st.form("medicine_form"):
            medicine = st.text_input("Enter The Medicine Name")
            submit_medicine = st.form_submit_button("Find Description")

            if submit_medicine:
                prompt = (
                    f"You are provided with a medicine named '{medicine}'. Please perform the following tasks in a detailed and professional manner, ensuring that all headings are bold: \n"
                    f"1. **Medicine Name and Detailed Description**: Provide a comprehensive description of the medicine, including its uses, chemical composition, and purpose.\n"
                    f"2. **When to Use '{medicine}'**: Explain the conditions or scenarios in which this medicine should be used.\n"
                    f"3. **Disadvantages**: List any potential side effects or disadvantages of using '{medicine}'.\n"
                    f"4. **When Not to Use**: Specify situations or conditions in which this medicine should not be used.\n"
                    f"5. **Price Comparison in Different Countries**: Create a table that includes the following columns:\n"
                    f"   - **Country Name**: The name of the country.\n"
                    f"   - **Medicine Name in Local Market**: The name of the medicine as it is known in that country.\n"
                    f"   - **Price**: The price of the medicine in that country.\n"
                    f"   - **Chemical Composition and Purpose**: The chemical composition of the medicine and its intended purpose.\n"
                    f"6. **Pros and Cons**: Summarize the main advantages and disadvantages of using '{medicine}'.\n"
                    f"Ensure that the information is well-organized, clear, and professional, and include relevant hyperlinks where appropriate, such as links to medical journals, articles, or other authoritative sources."
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

                st.title(f"{medicine} Description")
                st.markdown(response_content)