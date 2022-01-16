#support the slice notation that allows you to get a sublist from a list:
# sub_list = list[begin: end: step]#
#end item is not included. count from 0. steps can be negative
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[6:])
sub_colors = colors[1:4]

print(sub_colors)
#if not start given will start from BACK if negative step given
print(colors[:3:-2])