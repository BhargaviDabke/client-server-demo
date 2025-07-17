import requests

url = "http://localhost:8000/sqrt/4"

# Make api call to url and print results
response = requests.get(url)
if response.status_code == 200:
    print(f"Response from server: {response.json()}")
else:
    print(f"Failed to get response, status code: {response.status_code}")
    
# Make a POST request to create a greeting
greeting_url = "http://localhost:8000/greetings"
name = "Alice"
greeting_response = requests.post(greeting_url, json={"name": name})
if greeting_response.status_code == 200:
    print(f"Greeting response: {greeting_response.json()}")
else:
    print(f"Failed to create greeting, status code: {greeting_response.status_code}")   
