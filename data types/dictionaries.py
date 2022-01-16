# Dictionaries are made of pairs of keys. bit like lists
# key can be string tuple boolean or number. values more
#

locations = {
    "headquarters": "New York",
    "flagship": "Paris",
    "number": 22,
    "list": ["item1", "item2"]
}

print(locations)  ##print all     test

for i in locations:
    print("---- print key ----")
    print(i)   # print key  
    print("---- and now print values in dict ----")
    print(locations[i]) # print values of key
    print("--------------------------------------------------------------")

locations["headquarters"] = "Old York"  ##update value

# check if a key exists use in keyword
print("number" in locations)  #True

#pop aka remove
print("pop number from dic")
if "number" in locations:
    removed = locations.pop("number")
    print(removed)  ##print value of popped item