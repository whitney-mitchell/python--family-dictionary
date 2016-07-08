# Define a dictionary that contains information about several members of your family.
my_family = { 'cat': { 'name': 'Georgia', 'age': 13 },
							'mother': { 'name': 'Mary', 'age': 66 },
							'boyfriend': { 'name': 'Jesse', 'age': 30 }
						}
# Using a dictionary comprehension, produce output that looks like the following example.
# Krista is my sister and is 42 years old.
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

# for key, value in my_family.items():
# 	name = value['name']
# 	age = value['age']

	# output = ['{0} is my {1} and is {2} years old'.format(name, key, age)]

output = {value['name']+" is my "+key+" and is "+str(value['age'])+" years old." for key, value in my_family.items()}
print(output)

import code
code.interact(local=locals())
