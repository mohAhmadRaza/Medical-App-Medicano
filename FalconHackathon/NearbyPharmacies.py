import streamlit as st
import requests

class Pharmacies:
    def __init__(self):
        self.geocoding_url = "https://nominatim.openstreetmap.org/search"
        self.search_url = "https://nominatim.openstreetmap.org/search"

    def get_coordinates(self, place_name):
        params = {
            'q': place_name,
            'format': 'json',
            'addressdetails': 1,
            'limit': 1  # Get the most relevant result
        }
        headers = {
            'User-Agent': 'PharmacyFinderApp/1.0'
        }

        try:
            response = requests.get(self.geocoding_url, params=params, headers=headers)
            response.raise_for_status()
            results = response.json()

            if results:
                location = results[0]
                return location['lat'], location['lon']
            else:
                st.error("Place not found. Please try another place.")
                return None, None
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
            return None, None

    def find_nearby_pharmacies(self, location, radius):
        lat, lon = location
        search_radius = radius / 1000  # Convert meters to kilometers

        params = {
            'q': 'pharmacy',
            'format': 'json',
            'addressdetails': 1,
            'limit': 5,
            'dedupe': 1,
            'lat': lat,
            'lon': lon,
            'radius': search_radius
        }

        headers = {
            'User-Agent': 'PharmacyFinderApp/1.0'
        }

        try:
            response = requests.get(self.search_url, params=params, headers=headers)
            response.raise_for_status()
            results = response.json()

            return results
        except requests.RequestException as e:
            st.error(f"Request failed: {e}")
            return []

    def app(self):
        st.title("Nearby Pharmacy Finder")

        # User inputs
        place_name = st.text_input("Enter a place name (e.g., Sialkot, Pakistan):", "Sialkot, Pakistan")
        radius = st.slider("Select radius (meters):", 100, 5000, 500)

        if st.button("Find Pharmacies"):
            if place_name:
                with st.spinner("Finding location..."):
                    lat, lon = self.get_coordinates(place_name)

                    if lat and lon:
                        with st.spinner("Searching for pharmacies..."):
                            pharmacies = self.find_nearby_pharmacies((lat, lon), radius)

                            if pharmacies:
                                st.write(f"Found {len(pharmacies)} pharmacies:")
                                for place in pharmacies:
                                    name = place.get('display_name', 'No name available')
                                    address = ", ".join([place.get('address', {}).get(component, '') for component in ['road', 'suburb', 'city', 'state', 'country']]).strip(', ')
                                    st.write(f"**Name:** {name}")
                                    st.write(f"**Address:** {address if address else 'No address available'}")
                                    st.write(f"**Location:** Latitude: {place.get('lat')}, Longitude: {place.get('lon')}")
                                    st.write("---")
                            else:
                                st.write("No pharmacies found.")
            else:
                st.warning("Please enter a valid place name.")
