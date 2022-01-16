travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,numvisits,cities):
    addtodict = {}
    addtodict["country"] = country
    addtodict["visits"] = numvisits
    addtodict["cities"] = cities
    travel_log.append(addtodict)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#i broke the rules and added this for clarity
for entry in travel_log:
    print(entry)
