# sets collection of values without duplicates. like list but without dups
# sets are unordered and have no indices unlike lists

postcode = {"SE1", "se2", "sr4"}
postcode.add("SW2")

print("se2" in postcode)

for x in postcode:
    print(f"Postcodes: {x}")

# remove an item with .remove   use in first to not get eros
if "se2" in postcode:
    postcode.remove("se2")

# remove duplicates from list is to transform list to set
users = ["julian", "peter", "marcos","julian"]
users_dupsremoved = set(users)
# len of set
print(len(users))
# is admin set a subset of users?
admins={"julian"}
print(admins.issubset(users_dupsremoved))
#union merges but removes duplicates
postcodenew={"SE1", "SE666"}
print(postcodenew.union(postcode))
# intersection() create set that contains values in both sets aka common ones
print(postcodenew.intersection(postcode))
# difference() gives us elements that left set has    but right set does NOT
print(postcodenew.difference(postcode))