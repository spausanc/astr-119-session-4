#python exceptions let you dela with unexpected results

try:		#???
	print(a)	#this ill throw an exception since a is not defined
except:
	print("a is not defined!")
	
	
#there are specific error to help with cases
try:
	print(a)	#this will throw an exception since a is not defined
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")


print(a)		#this will break our program since a is not defined
