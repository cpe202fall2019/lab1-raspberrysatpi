def max_list_iter(int_list):  # must use iteration not recursion

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

 # must use recursion

	if int_list == None:

		raise ValueError("ValueError: int_list == None")

		return

	elif len(int_list) == 0 or len(int_list) == 1:

		return int_list

	else:
		return [int_list[-1]] + reverse_rec(int_list[:-1])
	pass


def bin_search(target, low, high, int_list):  # must use recursion


	if int_list == None:

		raise ValueError("ValueError: int_list == None")

		return

	elif len(int_list) == 0 or (len(int_list) == 1 and int_list[0] == target):

		return None

	else:
		mid = (low + high) // 2

		if int_list[mid] == target:

			return mid

		elif int_list[mid] > target:

			bin_search(target, low, mid, int_list)


		elif int_list[mid] < target:
			bin_search(target, mid, high, int_list)

	pass
