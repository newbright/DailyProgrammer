#------------------------------------------------------------
# Challenge #219: "To-Do List (Part 2)"
# Difficulty: Intermediate
# June 17, 2015
# Brandon Newbright
#------------------------------------------------------------

from collections import defaultdict

my_list = defaultdict(list)

def add_item(item, *categories):
	if categories:
		for c in categories:
			my_list[c].append(item)
			my_list['default'].append(item)
	else:
		my_list['default'].append(item)

def view_list(*categories):
	if categories:
		print("----" + " & ".join(categories) + "----")
		result = set.intersection( *[ set(str(x) for x in my_list[c]) for c in categories ] )
		for item in result:
			print("- {}".format(item))
	else:
		print("----To-Do----")
		for item in my_list['default']:
			print("- {}".format(item))
	print("")

def update_item(item, new_item):
	for c in my_list:
		if item in my_list[c]:
			my_list[c].remove(item)
			my_list[c].append(new_item)

add_item('Go to work','Programming')
add_item('Create Sine Waves in C', 'Music', 'Programming')

view_list('Programming')
view_list('Music')
view_list('Music', 'Programming')

update_item('Create Sine Waves in C', 'Create Sine Waves in Python')

view_list('Music', 'Programming')