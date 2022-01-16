# use negative indexing to retrieve values from end of an index
shares = [12, 3, 5, 10, 22, 33]
shares[-3] = 11
del shares[-1]
latest = shares[-1]
print(latest)

# use del to delete whole data strutcures or objects or key:value pairs
locations = {
    "headquarters": "New York",
    "flagship": "Paris",
    "number": 22,
    "list": ["item1", "item2"]
}
del locations['number']
print(locations)

