import requests
from Auth import token

#Returns the ids of all the bookings that exist within the API. Can take optional query strings to search and return a subset of booking ids.

url = 'https://restful-booker.herokuapp.com/booking/22'   #Setting the booking id to update

#Setting the request header
headers = {'Content-Type': 'application/json','Accept': 'application/json', 'Cookie': 'token='+f'{token}'}

#Using DELETE method to delete the booking
response = requests.delete(url,headers=headers)

#Printing the status code of the response
print(response.status_code)

#Assert for successful delete
assert response.status_code == 201, "Error in deleting booking"