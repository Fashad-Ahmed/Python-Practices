cleanest_cities = ["Karachi", "Peshawar", "Quetta"]
value = input("Enter city: ")
for city in cleanest_cities:
    if value in cleanest_cities:
        print("Cleanest city")
        break
    else:
        print("Not Cleanest city")
        break
