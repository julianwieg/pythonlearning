#Lists

#Lists   add elements to a list. use indices from 0 to pull add amend data in lists
users = ["julian", "peter", "marcos"]
users.append("niklas")
users.insert(0, "firstusernow")
print(users)
removed = users.pop(2)
print(users)
print(removed)
print(len(users))

#numbers  min max 
shares = [12,3, 5, 10]
print(max(shares))