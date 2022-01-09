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