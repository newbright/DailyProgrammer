#------------------------------------------------------------
# Challenge #219: "To-Do List (Part 1)"
# Difficulty: Easy
# June 15, 2015
# Brandon Newbright
#------------------------------------------------------------

# Very straightforward; To-Do list is modelled as a list
my_list = []

# All functions of this challenge are existing list operations in Python

# Add (append) a new item to the list
def add_item(item):
	my_list.append(item)

# Delete (remove) an item from the list
def delete_item(item):
	if item in my_list:
		my_list.remove(item)

# Print the items in the list; formatted for readability
def view_list():
	print("____TO-DO____")
	for item in my_list:
		print("- {}".format(item))
	print("")

# Challenge inputs
add_item('Take a shower')
add_item('Go to work')
view_list()

add_item('Buy a new phone')
delete_item('Go to work')
view_list()