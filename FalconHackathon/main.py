import streamlit as st
from streamlit_option_menu import option_menu

import Blogs
import Home, Alternatives, DiagnoseDisease, MedicineInformation, NearbyPharmacies

st.set_page_config(
    page_title="Medicano",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_apps(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Create a list of app titles for the sidebar
        titles = [app['title'] for app in self.apps]

        with st.sidebar:
            app_title = option_menu(
                menu_title='Medicano',
                options=titles,
                icons=['house-fill', 'heart-pulse', 'capsule', 'info-circle', 'journal-text'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'white'},
                    "icon": {"color": "black", "font-size": "23px"},
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#000066",},
                    "nav-link-selected": {"background-color": "white"}}
            )

        # Find the selected app from the list and run its function
        selected_app = next((app for app in self.apps if app['title'] == app_title), None)
        if selected_app:
            selected_app['function']()


# Initialize the MultiApp instance
Medical = MultiApp()

# Add apps to the MultiApp instance
Medical.add_apps("Home", Home.Home().app())
Medical.add_apps("Diagnose Disease", lambda: DiagnoseDisease.Diagnose().app())
Medical.add_apps("Medicine Alternatives", lambda: Alternatives.Alternatives().app())
Medical.add_apps("Medicine Information", lambda: MedicineInformation.Information().app())
Medical.add_apps("NearbyPharmacies", lambda: NearbyPharmacies.Pharmacies().app())
Medical.add_apps("Blogs", lambda:Blogs.Blogs().app())

# Run the selected app
Medical.run()
