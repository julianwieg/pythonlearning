# split a string by , as seperator
users = "julian/peter/marcos"
user_list = users.split("/")
print(user_list)

users = "julian peter marcos"
new_user = users.replace("marcos", "dada")
print(new_user)