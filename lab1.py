def max_list_iter(int_list):

# Straightforward function that finds the maximum value in a function by itteraton.
# Continuously updates variable max on each itteration and returns it at the end of the loop.
# Raises a ValueError if the list is None Type and returns None if the list is empty. 

	if int_list is None:

		raise ValueError('ValueError: int_list == None')

		return	

	elif len(int_list) == 0:

		return None

	else:
		max = int_list[0]

		for int in int_list:

			if int > max:

				max = int
		return max
	pass

def reverse_rec(int_list):  

# Reverses a list int_list by recursively calling reverse_rec. Checks base cases first.
# Returns a ValueError is the list is None type.

	if int_list == None:

		raise ValueError("ValueError: int_list == None")

		return

	elif len(int_list) == 0 or len(int_list) == 1:

		return int_list

	else:

		return [int_list[-1]] + reverse_rec(int_list[:-1])

	pass


def bin_search(target, low, high, int_list):


# Recirsive binary search that searches for a target in int_list in a range between low and high.
# Checks base cases and raises a ValueError if the list is None Type.
# If the target is not found, returns None, otherwise returns the index of the value.

	if int_list == None:

		raise ValueError("ValueError: int_list == None")

		return

	elif len(int_list) == 0:

		return None


	else:
		mid = (low + high) // 2
#		print(mid)
#		print(int_list[mid])

		if (mid == low or mid == high) and int_list[mid] != target:
#			print("Hi I am returning None")
			return None

		elif int_list[mid] == target:

			return mid

		elif int_list[mid] > target:

#			print("Hi I am greater than my target; lowering search")
			return bin_search(target, low, mid, int_list)


		elif int_list[mid] < target:
#			print("Hi I am greater than my target; lowering search")
			return bin_search(target, mid, high, int_list)


