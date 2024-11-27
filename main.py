import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Login Page",
)

# Debugging print statements to verify environment variables
firebase_api_key = os.getenv('FIREBASE_API_KEY')
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(f"FIREBASE_API_KEY: {firebase_api_key}")
print(f"GOOGLE_APPLICATION_CREDENTIALS: {credentials_path}")

# Import app modules
import about, account, home

# Embed Google Analytics script
st.markdown(
    f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{os.getenv('analytics_tag')}');
    </script>
    """,
    unsafe_allow_html=True
)

# MultiApp class for managing multiple pages
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Login',
                options=['Home', 'Account',  'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Run the selected app
        if app == "Home":
            home.app()
        elif app == "Account":
            account.app()
        elif app == 'About':
            about.app()

# Create an instance of the MultiApp class
app = MultiApp()

# Add all your apps here
app.add_app("Home", home.app)
app.add_app("Account", account.app)
app.add_app("About", about.app)

# Run the multi-page app
app.run()
