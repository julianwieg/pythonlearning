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

#numbers  min max  and sort numbers  sort strings alphabetical A to z
shares = [12, 3, 5, 10]
print(max(shares))
shares.sort()
print(shares)

#numbers  sum 
shares = [12, 3, 5, 10]
total = sum(shares)
print(total)

#you can combine lists even diff types   joining lists
seats = [1, 2, 3,]
taken = [False, True, False]
print (seats + taken)

#counting elements  count() counts everything
countme = [False, True, False]
#if you want to know if an element exists
print(countme.count(False))

print(True in countme)

# remove duplicates from list is to transform list to set
users = ["julian", "peter", "marcos","julian"]
users_dupsremoved = set(users)