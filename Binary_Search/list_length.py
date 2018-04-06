def list_length(a_list=[]):

	"""
	Returns the length of a given list.

	Assumes the list only can be asked for an element at
	a certain position. (So list cannot be looped over).
	"""

	if not isinstance(a_list, list):
		return 0

	lower_idx = -1
	current_idx = 1
	upper_idx = 1

	while True:
		try:
			a_list[current_idx]
			found = True
		except IndexError:
			found = False

		if found:
			if (current_idx - lower_idx == 1 and last_found == False) or current_idx == lower_idx:
				return current_idx + 1

			lower_idx = current_idx

			if upper_idx > current_idx:
				current_idx = current_idx + int((upper_idx - current_idx) / 2)
			else:
				current_idx = int(current_idx * 2)

			last_found = True

		else:
			if current_idx - lower_idx == 1:
				return current_idx

			upper_idx = current_idx
			current_idx = lower_idx + int((current_idx - lower_idx) / 2)

			last_found = False
