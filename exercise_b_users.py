from pstats import SortKey


users = {
  "Jonathan" : {
    "twitter" : "jonnyt",
    "lottery_numbers" : [6, 12, 49, 33, 45, 20],
    "home_town" : "Stirling",
    "pets" : [
    {
      "name" : "fluffy",
      "species" : "cat"
    },
    {
      "name" : "fido",
      "species" : "dog"
    },
    {
      "name" : "spike",
      "species" : "dog"
    }
  ]
  },
  "Erik" : {
    "twitter" : "eriksf",
    "lottery_numbers" : [18, 34, 8, 11, 24],
    "home_town" : "Linlithgow",
    "pets" : [
    {
      "name" : "nemo",
      "species" : "fish"
    },
    {
      "name" : "kevin",
      "species" : "fish"
    },
    {
      "name" : "spike",
      "species" : "dog"
    },
    {
      "name" : "rupert",
      "species" : "parrot"
    }
  ]
  },
  "Avril" : {
    "twitter" : "bridgpally",
    "lottery_numbers" : [12, 14, 33, 38, 9, 25],
    "home_town" : "Dunbar",
    "pets" : [
      {
        "name" : "monty",
        "species" : "snake"
      }
    ]
  }
}
# Question 1
print(users["Jonathan"]["twitter"])

#  Question 2
print(users["Erik"]["home_town"])

# Question 3
print(users["Erik"]["lottery_numbers"])

# Question 4
print(users["Avril"]["pets"][0].get("species"))
# or, easier: print(users["Avril"]["pets"][0]["species"])

# Question 5
# sorted_numbers = sorted(users["Erik"]["lottery_numbers"]) why did this not work?
# users["Erik"]["lottery_numbers"].sort()
# print(users["Erik"]["lottery_numbers"][4])
sorted(users["Erik"]["lottery_numbers"])[0]
# for loop --> ask Ed
# min --> ask James
# variable and min --> ask Jenna
# this also works:
# sorted_numbers = sorted(users["Erik"]["lottery_numbers"])
# print(sorted_numbers)
# b = users["Erik"]["lottery_numbers"]
# b.sort()
# print(b)


# # Question 6
users["Avril"]["lottery_numbers"][0]
print(users["Avril"]["lottery_numbers"])
even_numbers = []
for number in users["Avril"]["lottery_numbers"]:
  if number % 2 == 0:
    even_numbers.append(number)
print(even_numbers)
# Instructor's solution:
# lottery_numbers = users["Avril"][lottery_numbers]
# even_numbers = []
# for lottery_number in lottery_numbers:
#    if lottery_number % 2 == 0:
#      even_numbers.append(lottery_number)
# print(even_numbers)

# Question 7
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# Question 8
# users["Erik"]["home_town"].pop("Linlithgow")
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])
# users.get("Erik")["home_town"] = "Edinburgh" --> Cordu

# Question 9 --> appending a dictionary
# users["Erik"]["pets"].append({ "name" : "Fluffy", "species" : "dog" })
# you can also make the dictionary first and store it as a variable --> James
# solution by Richard:
# users["Erik"]["pets"] += [{"name" : "fluffy", "species" : "dog"}]
# print(users["Erik"]["pets"])

# Question 10
# users["ian"] = {
#     "twitter" : "twitter name",
#     "lottery_numbers" : [4,5,6,7,8],
#     "home_town" : "Edinburgh",
#     "pets" : [
#        {
#           "name" : "Dave",
#           "species" : "dog"
#         }
#       ]
# }

