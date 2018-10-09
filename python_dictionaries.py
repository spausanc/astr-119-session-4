#define a dictionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class"			:	"Astr 119",
	"prof"			:	"Brant",
	"awesomeness"	:	10
}
print(type(example_dict))	#will say dict

#get a value via key
course = example_dict["class"]	#Given the key, the program will print the value
print(course)					#"course" is just a nickname :)

#change a value via key
example_dict["awesomeness"] += 1	#increase awesomeness. only for numerical values

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])	#it's looping through keys to do line 12
	