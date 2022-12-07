import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/72d65c1449e9038fd546d7a333491172/flightDeals2/users"
SHEETY_ENDPOINT_POST = "https://api.sheety.co/72d65c1449e9038fd546d7a333491172/flightDeals2/users"

TOKEN = "khityu89bduo"

first_name = input(
    "Welcome to Michael's Flight Club.\nWe find the best flight deals and email you.\nWhat is your first name?\n ")

last_name = input("What is your last name?\n ")
first_email = input("What is your email?\n ")
email_confirm = input("Type your email again.\n ")

if first_email == email_confirm:
    print("You're in the Club!")
else:
    second_try = input("Incorrect email.\nTry again!\n ")

id = 5
data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": first_email,
    }
}
SHEETY_PUT = f"{SHEETY_ENDPOINT}/{id}"

response = requests.put(url=SHEETY_PUT, json=data)

print("response.text= ", response.text)
print("Success! Your details have been added.")
