import streamlit as st
import requests


API_URL = "http://fastapi:8000"

st.title ("Online Shoppers Intention")

if "token" not in st.session_state:
    st.session_state.token = None


tab = st.radio ("Select Action", ["Login", "Sign Up"])

if tab == "Sign Up":
    st.subheader ("Create a new Account")
    new_username = st.text_input ("New Username", key = "signup_user")
    new_password = st.text_input ("New Password", type="password", key="signup_pass")

    if st.button ("Create Account"):
        response = requests.post (f"{API_URL}/users/", json = {"username": new_username, "password": new_password})
        if response.status_code == 200:
            st.success ("Account Created!")
        else:
            st.error (f"Error: {response.json().get ('detail', 'Unknown error')}")

elif tab == "Login":
    st.subheader ("Login")
    username = st.text_input ("Username", key="login_user")
    password =  st.text_input ("Password", type="password", key="login_pass")
    if st.button ("Login"):
        response = requests.post (f"{API_URL}/token", data={"username": username, "password": password})
        if response.status_code == 200:
            st.session_state.token = response.json () ["access_token"]
            st.success ("Login successful!")



if st.session_state.token:
    st.subheader ("Make a Prediction")
    col1, col2 = st.columns(2)
    with col1:
        PageValues = st.number_input ("PageValues", min_value=0.0, step=0.01, format="%.4f")
        Administrative = st.number_input ("Administrative", min_value=0.0, step=1.0)
        Administrative_Duration = st.number_input ("Administrative_Duration", min_value=0.0, step=1.0)
        Informational = st.number_input ("Informational", min_value=0.0, step=1.0)
        Informational_Duration = st.number_input ("Informational_Duration", min_value=0.0, step=1.0)
    with col2:  
        ProductRelated_Duration = st.number_input (" ProductRelated_Duration", min_value=0.0, step=1.0)
        BounceRates = st.number_input ("BounceRates", min_value=0.0, step=0.01, format="%.4f")
        SpecialDay = st.number_input ("SpecialDay", min_value=0.0, max_value=1.0, step=0.01)
        Month = st.selectbox ("Month", ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Agu', 'Sep', 'Oct', 'Nov', 'Dec'])
        VisitorType = st.selectbox ("VisitorType", ["Returning_Visitor", "New_Visitor", "Other"])

    if st.button ("Predict"):
        input_data = {
            "PageValues": PageValues,
            "Administrative": Administrative,
            "Administrative_Duration": Administrative_Duration,
            "Informational": Informational,
            "Informational_Duration": Informational_Duration,
            "ProductRelated_Duration": ProductRelated_Duration,
            "BounceRates":BounceRates,
            "SpecialDay": SpecialDay,
            "Month": Month,
            "VisitorType": VisitorType
        }

        headers = {"Authorization": f"Bearer {st.session_state.token}"}
        response = requests.post (f"{API_URL}/predict/", json=input_data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
            st.info(f"Probability: {result['probability']:.4f}")
        else:
            st.error(f"Prediction failed: {response.text}")


if st.session_state.token:
    if st.button("Logout"):
        st.session_state.token = None
        st.experimental_rerun()