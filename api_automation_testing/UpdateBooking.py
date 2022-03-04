import requests
import json
from Auth import token

#Updates a current booking

url = 'https://restful-booker.herokuapp.com/booking/14'   #Setting the booking id to update



#Setting the request header
headers = {'Content-Type': 'application/json','Accept': 'application/json', 'Cookie': 'token='+f'{token}'}

#Loading the new booking data for the update
payload = open("update_request.json", "r").read()

#using PUT method to update the booking and saving it in response
response = requests.put(url,data=payload, headers=headers)

#Printing the status code of the response
print(response.status_code)

#Assert for successful update
assert response.status_code == 200, "Error in updating booking"

#Showing the token
print(response.json())

#Saving the update response in a json file
with open("update_response.json", "w") as f:
    f.write(response.text)