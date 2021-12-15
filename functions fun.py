# basic of functions
def age_label(age):
  label = "my age " + age
  return label

results = age_label("22")
print(results)

# functions that start with a boolean often start with a name is

def is_freezing(temp):
  return temperature < 0

def sum_score(score, bonus):
    print(score + bonus)

sum_score(100,50)

# the parameter in the condition (function) we pass when calling the function like 80
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")  #returns Total: 90

add_shipping(80)

# of course you can nest code in functions
def calculator(operator, x, y):
    if operator == "+":
        print(x+y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")

calculator("-", 30, 20)