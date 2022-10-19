united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]
# Question 1
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom[1]["capital"])
# Question 2
dict = {
    "name" : "Northern_Ireland",
    "capital" : "Belfast",
    "population" : 1811000
}
united_kingdom.append(dict)
print(united_kingdom)

# Question 3
# for country in united_kingdom:
#   print(country["name"])

# Question 4
total_population = 0  
# --> do this first cause you'll need somewhere to add your result
for country in united_kingdom:
# += --> add it to the stuff on the end
   total_population += country["population"]
print(total_population)
