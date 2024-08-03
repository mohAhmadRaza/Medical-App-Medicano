import streamlit as st

class Homes:
    @staticmethod
    def app():
        # Streamlit UI components
        st.markdown("""
        <div style="background-color: #000066; text-align: center; padding: 10px;border-radius : 5px">
          <h1 style="color: white; font-size: 70px; margin-bottom: -40px;">Medicano</h1>
          <h2 style="color: white; font-size: 20px; margin-top: 5px;">A Medical Assistant</h2>
        </div>
        """, unsafe_allow_html=True)
        # Title of the application
        st.title("Welcome")
        
        # Add an image or logo if you have one
        # st.image("path_to_your_logo.png", width=200)
        
        # Description of the app
        st.header("About Medicano")
        st.write("""
        Medicano is a comprehensive mobile application designed to provide detailed information about medications. Our goal is to help users make informed decisions about their health by offering insights into medication uses, pricing, alternatives, and availability.
        """)
        
        # Features of the app
        st.header("Key Features")
        st.write("""
        - **Detailed Medicine Information:** Get comprehensive details about medications, including their uses, ingredients, and potential side effects.
        - **Alternative Options:** Find alternative medicines based on user input about symptoms and preferences.
        - **Local Availability:** Check the availability of medicines in local pharmacies.
        - **Health Articles and News:** Stay updated with the latest health news and articles.
        - **Personalized Recommendations:** Receive suggestions tailored to your health needs and preferences.
        - **Voice Search Integration:** Easily search for medicines using voice commands.
        - **Symptom Checker:** Input symptoms to find possible medicines or treatments.
        """)
        
        # Team members
        st.header("Meet Our Team")
        st.write("""
        - **Ahmad Raza:** CEO & Lead Developer
        - **Flap** Co-founder & UI/UX Designer
        - **Mobarak** Co-founder & Backend Developer
        - **Arslan** Co-founder & idea Specialist
        - **Kolmax** Co-founder & Presenter
        """)
        
        # Contact Information
        st.header("Contact Us")
        st.write("""
        For any inquiries or feedback, please reach out to us at [sktfscm21557034@gmail.com](mailto:sktfscm21557034@gmail.com).
        """)
        
        # Additional sections if needed
        # st.header("Additional Section Title")
        # st.write("Content for additional section.")
        
        # Footer
        st.write("© 2024 Medicano. All rights reserved.")
