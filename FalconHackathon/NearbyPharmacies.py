import streamlit as st
import requests
from dotenv import load_dotenv
import os

class Pharmacies:
    def __init__(self, api_key):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    def find_nearby_pharmacies(self, location, radius):
        params = {
            'key': self.api_key,
            'location': location,
            'radius': radius,
            'type': 'pharmacy',
            'language': 'en',
            'region': 'us'
        }
        
        response = requests.get(self.endpoint_url, params=params)
        results = response.json()

        if results.get('status') == 'OK':
            return results.get('results', [])
        else:
            st.error(f"Error: {results.get('status')}")
            return []

    def app(self):
        st.title("Nearby Pharmacy Finder")

        # User inputs
        location = st.text_input("Enter location (latitude,longitude):", "52.369358,4.889258")
        radius = st.slider("Select radius (meters):", 100, 5000, 500)

        if st.button("Find Pharmacies"):
            if location:
                with st.spinner("Searching for pharmacies..."):
                    pharmacies = self.find_nearby_pharmacies(location, radius)

                    if pharmacies:
                        st.write(f"Found {len(pharmacies)} pharmacies:")
                        for place in pharmacies:
                            st.write(f"**Name:** {place['name']}")
                            st.write(f"**Address:** {place.get('vicinity', 'No address available')}")
                            st.write(f"**Location:** Latitude: {place['geometry']['location']['lat']}, Longitude: {place['geometry']['location']['lng']}")
                            st.write("---")
                    else:
                        st.write("No pharmacies found.")
            else:
                st.warning("Please enter a valid location.")

