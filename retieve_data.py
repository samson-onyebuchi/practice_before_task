from pymongo import MongoClient
from mongoDB_URL import mongodb_url

# Connect to the MongoDB Atlas cluster
client = MongoClient(mongodb_url())
db = client["mydatabase"]
users_collection = db["Test"]

def validate_pin(phone_number, pin):
  # Find the user with the matching phone number
  user = users_collection.find_one({"phone_number": phone_number})
  
  # If a user with the specified phone number was found
  if user:
    # Check if the provided PIN matches the user's stored PIN
    if user["pin"] == pin:
      return True
    else:
      return False
  else:
    return False

# Test the function with a sample phone number and PIN
pin = "2347038157217"
password = "1234"

if validate_pin(pin, password):
  print("The provided PIN is valid!")
else:
  print("The provided PIN is not valid.")
