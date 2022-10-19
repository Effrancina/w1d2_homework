#Question 1
stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
print(stops)
#Question 2
stops.insert(0, "Glasgow Queen St")
print(stops)
#Question 3
stops.insert(4, "Polmont")
print(stops)
#Question 4
index = stops.index('Linlithgow')
print(index)
#Question 5
stops.remove('Linlithgow')
print(stops)
#Question 6
stops.pop(2)
print(stops)
# stops.pop(stops.index("Cumbernauld")) also works
# del stops[stops.index("Cumbernauld")] also works
#Question 7
num_items = len(stops)
print(num_items)
#Question 8
print(sorted(stops))
#Question 9
stops.sort(reverse=True)
# stops.reverse()
print(stops)
#Question 10
for stop in stops:
    print(stop)
    