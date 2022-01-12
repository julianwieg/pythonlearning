# to create a list based on another you need to create empty list
prices = [10, 20, 44, 88]
halvedprice = []

for price in prices:
    half_price = price/2
    halvedprice.append(half_price)

print(halvedprice)
    
# you can do this easier with 'list comprehension' 
# create a new list by applying an expression on each element of existing list
# to create a copy of a list remove /2  aka copy each element
# works with all types like booleans types or strings
halvednew = [price/2 for price in prices]
print(halvednew)

users = ["julian", "peter", "marcos"]
prefix = ["Mr. " + name for name in users]
print(prefix)

#you can do all kinds of stuff
counte = [name.count("e") for name in users]
print(counte)

# doing it in functions 
