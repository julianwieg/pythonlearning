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

# doing it in functions . we pack the operations we wanna do in a function and for each value we can then use it as an expression
def halve(num):
    no_tax = 0.2 * num
    return num/2

halved = [halve(price) for price in prices]

authors = ["Virginia Wolf", "John Steinbeck"]

def add_comma (name):
    parts = name. split(" ")
    return parts [1] + ", " + parts[0]

authors_update = [add_comma(name) for name in authors]
print(authors_update)

# you can do conditional statements. normally started with the expression, the for loop and finished with IF statement
high_prices = [price for price in prices if price > 20 and price < 88]
print(high_prices)

# example with string
websites = ["ab.com", "lom.fr", "other.de"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)