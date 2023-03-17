# Code to set ride tiers, ride prices, per mile price, what 
# credit user has and output total ride price

# Change ride_type's in LINE 5 to desired titles.
print("Ride Options: Normal, Mid Range or Luxury.")
ride_type = input("What Type of Ride are you looking for?: ")
print("How many Credits are in your account?")
credits = float(input("Credits: "))
print("How many Miles to Destination?:")
miles = float(input("Miles: "))

# Change LINE 13's price to desired price.
per_mile = 1.25
ride_price = 0
final_price = 0

# Can change LINES 20, 22 & 24 to deired price for
# each ride_type.
if ride_type == "Mid Range":
  ride_price = 25.00
elif ride_type == "Luxury":
  ride_price = 50.50
else:
  ride_price = 15.50

print("Ride Price:")
print(ride_price)

print("Per Mile Price:")
print(per_mile)

if credits > 0:
  final_price = ride_price + (miles * per_mile)  - credits
else:
  final_price = ride_price + (miles * per_mile)

print("Final Price after Credit: ")
print(final_price)
