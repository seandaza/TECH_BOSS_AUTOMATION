import requests

#Creates a new auth token to use for access to the PUT and DELETE /booking

url = 'https://restful-booker.herokuapp.com/auth'  #Setting the route

payload = {
    "username" : "admin",
    "password" : "password123"
}

#Setting the request header
headers = {'Content-Type': 'application/json'}

#using POST method to create a new auth token and saving it in response
response = requests.post(url,data=payload)

#Printing the status code of the response
print(response.status_code)

#saving the token to a variable
token = response.json()['token']

#showing the token
print(token)

#Saving the token to a file
with open("token.json", "w") as f:
    f.write(response.text)