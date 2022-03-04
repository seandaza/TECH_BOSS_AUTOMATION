import requests    

#Returns a specific booking based upon the booking id provided


url = 'https://restful-booker.herokuapp.com/booking'  #Setting the route


#Setting the request header
headers = {'Content-Type': 'application/json'}


#using GET method to get the booking and saving it in response
response = requests.get(url,headers)

#Printing the status code of the response
print(response.status_code)

#Assert for successful get
assert response.status_code == 200, "Error in getting all booking ids"

#Printing the response in json format
print(response.json())

#Saving the booking ids in a json file
with open("all_booking_ids.json", "w") as f:
    f.write(response.text)