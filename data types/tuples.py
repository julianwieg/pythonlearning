# tuples vs strings
# tuples use ()    and lists []   tuples need a , at the end
# tuples are IMMUTABLE  
# you can store tuples inside a list

score = [("mia", 75), ("lee", 90)]
print(score)
print(len(score))  #cause it is two tuples in the list it is 2
mia_score = score[0] #access tuple 1 (0)
print(mia_score)

for user_score in score:        #or iterate through
    print(f"Result {user_score}")

# to store a tuple returned by a function assign a function calls result to variable like results
def get_highlow(values_list):
    high_value = max(values_list)
    low_value = min(values_list)
    return high_value, low_value

values = [32, 13, 90,222]
results = get_highlow(values)
print(results)
print(type(results))
#but to return individual values use indices
highest = results[0]
print(F"highest value {highest}")