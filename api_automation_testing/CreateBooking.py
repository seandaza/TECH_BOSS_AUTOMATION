import requests
import json

#Creates a new booking in the API

url = 'https://restful-booker.herokuapp.com/booking'  #Setting the route


#Setting the request header
headers = {'Content-Type': 'application/json'}

#Loading the data for the new booking
payload = open("post_request.json", "r").read()

#using POST method to get the booking and saving it in response
response = requests.post(url,data=payload, headers=headers)


#Printing the status code of the response
print(response.status_code)

#Printing the response in json format
print(response.json())

#Assert for successful post
assert response.status_code == 200, "Error in creating booking"

#Saving the post response in a json file
with open("post_response.json", "w") as f:
    f.write(response.text)