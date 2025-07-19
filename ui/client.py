import streamlit as st
import requests

st.title("Square Root Calculator")

number = st.number_input("Enter a number:", min_value=0.0, value=4.0, step=1.0)

if st.button("Calculate Square Root"):
    url = f"http://fastapi-server:8000/sqrt/{number}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Square root of {number} is {result['sqrt']}")
        else:
            st.error(f"Failed to get response, status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")

# # Make api call to url and print results
# response = requests.get(url)
# if response.status_code == 200:
#     print(f"Response from server: {response.json()}")
# else:
#     print(f"Failed to get response, status code: {response.status_code}")
    
# # Make a POST request to create a greeting
# greeting_url = "http://localhost:8000/greetings"
# name = "Alice"
# greeting_response = requests.post(greeting_url, json={"name": name})
# if greeting_response.status_code == 200:
#     print(f"Greeting response: {greeting_response.json()}")
# else:
#     print(f"Failed to create greeting, status code: {greeting_response.status_code}")   
