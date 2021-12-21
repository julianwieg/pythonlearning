# basic of functions.  to use call the function
def age_label(age):
  label = "my age " + age
  return label

results = age_label("22")
print(results)

# functions that start with a boolean often start with a name is

def is_freezing(temp):
  return temperature < 0

# give good names
def sum_score(score, bonus):
    print(score + bonus)

sum_score(100,50)

# the parameter (cart here) in the condition (function) we pass when calling the function -> here 80
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

# while loops with functions
def onboard_passenger(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} added.")
        counter += 1

onboard_passenger(4)

# for loops 
def display_progress(total_files):
    for i in range(total_files):
        print(f"File {i} out of {total_files}")

display_progress(3)




