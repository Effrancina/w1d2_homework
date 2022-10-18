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
# or: print(users["Avril"]["pets"][0]["species"])
# Question 5
# sorted_numbers = sorted(users["Erik"]["lottery_numbers"]) why did this not work?
users["Erik"]["lottery_numbers"].sort()
print(users["Erik"]["lottery_numbers"][4])
# # Question 6
users["Avril"]["lottery_numbers"]
