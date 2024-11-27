import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Debugging print statements to verify environment variables
firebase_api_key = os.getenv('FIREBASE_API_KEY')
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(f"FIREBASE_API_KEY: {firebase_api_key}")
print(f"GOOGLE_APPLICATION_CREDENTIALS: {credentials_path}")

# Check if the default app is already initialized
if not firebase_admin._apps:
    if credentials_path:
        print(f"Using credentials file: {credentials_path}")
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
    else:
        print("Error: No GOOGLE_APPLICATION_CREDENTIALS found.")

# Firebase Authentication URLs
SIGN_UP_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
SIGN_IN_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
PASSWORD_RESET_URL = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"

def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        }
        if username:
            payload["displayName"] = username 
        payload = json.dumps(payload)
        if firebase_api_key:
            print(f"Making request to {SIGN_UP_URL} with API key {firebase_api_key}")
            r = requests.post(SIGN_UP_URL, params={"key": firebase_api_key}, data=payload)
            return r.json()
        else:
            print("Error: No FIREBASE_API_KEY found.")
            return {"error": "Missing FIREBASE_API_KEY"}
    except Exception as e:
        st.warning(f'Signup failed: {e}')

def sign_in_with_email_and_password(email, password, return_secure_token=True):
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        }
        payload = json.dumps(payload)
        if firebase_api_key:
            print(f"Making request to {SIGN_IN_URL} with API key {firebase_api_key}")
            r = requests.post(SIGN_IN_URL, params={"key": firebase_api_key}, data=payload)
            data = r.json()

            if 'error' in data:
                st.warning(data['error']['message'])
                return None

            user_info = {
                'email': data.get('email'),
                'username': data.get('displayName', 'No Name')
            }
            return user_info
        else:
            print("Error: No FIREBASE_API_KEY found.")
            return None
    except Exception as e:
        st.warning(f'Signin failed: {e}')
        return None

def reset_password(email):
    try:
        payload = {
            "email": email,
            "requestType": "PASSWORD_RESET"
        }
        payload = json.dumps(payload)
        if firebase_api_key:
            print(f"Making request to {PASSWORD_RESET_URL} with API key {firebase_api_key}")
            r = requests.post(PASSWORD_RESET_URL, params={"key": firebase_api_key}, data=payload)
            if r.status_code == 200:
                return True, r.json()
            else:
                return False, r.json()
        else:
            print("Error: No FIREBASE_API_KEY found.")
            return False, {"error": "Missing FIREBASE_API_KEY"}
    except Exception as e:
        return False, {'error': str(e)}

def app():
    st.title(' Welcome ')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'signedin' not in st.session_state:
        st.session_state.signedin = False

    if not st.session_state.signedin:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                if user and 'email' in user:
                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
                else:
                    st.warning('Account creation failed.')
        else:
            if st.button('Login'):
                userinfo = sign_in_with_email_and_password(email=email, password=password)
                if userinfo and 'email' in userinfo and 'username' in userinfo:
                    st.session_state.username = userinfo['username']
                    st.session_state.useremail = userinfo['email']
                    st.session_state.signedin = True
                    st.success(f'Welcome back, {st.session_state.username}!')
                else:
                    st.warning('Login failed or incomplete user information returned.')

            if st.button('Forget Password'):
                email = st.text_input('Email for Password Reset')
                success, message = reset_password(email)
                if success:
                    st.success("Password reset email sent successfully.")
                else:
                    st.warning(f"Password reset failed: {message}")

    if st.session_state.signedin:
        st.text(f'Name: {st.session_state.username}')
        st.text(f'Email id: {st.session_state.useremail}')
        if st.button('Sign out'):
            st.session_state.signedin = False
            st.session_state.username = ''
            st.session_state.useremail = ''
            st.success('You have signed out.')

# Running the app function
if __name__ == "__main__":
    app()
