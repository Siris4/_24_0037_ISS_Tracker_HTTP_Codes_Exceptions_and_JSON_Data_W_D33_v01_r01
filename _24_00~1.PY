import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.raise_for_status())  #handles all the Exception Handling

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(f"The longitude is: {longitude}")
print(f"The latitude is: {latitude}")

#tuple created:
iss_position = (longitude, latitude)
print(iss_position)

# then go to:
# https://www.latlong.net