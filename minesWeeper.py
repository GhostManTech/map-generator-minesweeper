try:
	import random
except Exception as error:
	print("[ERROR] -> %s" % error)
else:
	def create_map(size: int, data = None) -> list:
		try:
			size = int(size)
		except Exception as error:
			print("[ERROR] -> %s" % error)
		else:
			if 10 <= size <= 100:
				result = list()
				for k in range(size):
					result.append(list())
					for _ in range(size):
						result[k].append(data)
				return result
			else:
				return "[ERROR] -> Your value is too big or too small !"

	def create_map_bomba(array: list, number: int, value = 9) -> list:
		try:
			array = list(array)
			number = int(number)
			value = int(value)
		except Exception as error:
			print("[ERROR] -> %s" % error)
		else:
			size = len(array)
			if size == len(array[0]) and number <= size:
				while number > 0:
					number -= 1
					test = [random.randint(0, size-1), random.randint(0, size-1)]
					while array[test[0]][test[1]] == value:
						test = [random.randint(0, size-1), random.randint(0, size-1)]
					array[test[0]][test[1]] = value
				return array
			else:
				return "There are one or several mistakes in your data !"

	def count_map_replace(array, table_position, value, x, y):
		count = 0
		for k in range(len(table_position)):
			if array[table_position[k][0]][table_position[k][1]] == value:
				count += 1
		array[x][y] = count
		return array

	def create_map_indication(array: list, value: int) -> list:
		try:
			array = list(array)
			value = int(value)
		except Exception as error:
			print("[ERROR] -> %s" % error)
		else:
			test = []
			size = len(array)
			for k in range(size):
				for c in range(size):
					if array[k][c] != value:
						test.append([k, c])
			for k in range(len(test)):
				if 1 <= test[k][0] <= size-2 and 1 <= test[k][1] <= size-2:
					table_position = [[test[k][0], test[k][1]-1], [test[k][0], test[k][1]+1], [test[k][0]-1, test[k][1]], [test[k][0]+1, test[k][1]], [test[k][0]-1, test[k][1]+1], [test[k][0]+1, test[k][1]+1], [test[k][0]-1, test[k][1]-1], [test[k][0]+1, test[k][1]-1]]
				if test[k][0] == 0 and test[k][1] == 0:
					table_position = [[test[k][0]+1, test[k][1]], [test[k][0],test[k][1]+1], [test[k][0]+1, test[k][1]+1]]
				if test[k][0] == size-1 and test[k][1] == 0:
					table_position = [[test[k][0]-1, test[k][1]], [test[k][0]-1,test[k][1]+1], [test[k][0], test[k][1]+1]]
				if test[k][0] == 0 and test[k][1] == size-1:
					table_position = [[test[k][0], test[k][1]-1], [test[k][0]+1,test[k][1]-1], [test[k][0]+1, test[k][1]]]
				if test[k][0] == size-1 and test[k][1] == size-1:
					table_position = [[test[k][0]-1, test[k][1]-1], [test[k][0]-1,test[k][1]], [test[k][0], test[k][1]-1]]
				if 1 <= test[k][0] <= size-2 and test[k][1] == 0:
					table_position = [[test[k][0]-1, test[k][1]], [test[k][0]-1,test[k][1]+1], [test[k][0], test[k][1]+1], [test[k][0]+1, test[k][1]+1], [test[k][0]+1, test[k][1]]]
				if 1 <= test[k][0] <= size-2 and test[k][1] == size-1:
					table_position = [[test[k][0]-1, test[k][1]], [test[k][0]-1,test[k][1]-1], [test[k][0], test[k][1]-1], [test[k][0]+1, test[k][1]-1], [test[k][0]+1, test[k][1]]]
				if test[k][0] == 0 and 1 <= test[k][1] <= size-2:
					table_position = [[test[k][0], test[k][1]-1], [test[k][0],test[k][1]+1], [test[k][0]+1, test[k][1]-1], [test[k][0]+1, test[k][1]+1], [test[k][0]+1, test[k][1]]]
				if test[k][0] == size-1 and 1 <= test[k][1] <= size-2:
					table_position = [[test[k][0], test[k][1]-1], [test[k][0],test[k][1]+1], [test[k][0]-1, test[k][1]-1], [test[k][0]-1, test[k][1]+1], [test[k][0]-1, test[k][1]]]
				array = count_map_replace(array, table_position, value, test[k][0], test[k][1])
			return array

	def display_map(array: list):
		try:
			array = list(array)
		except Exception as error:
			print("[ERROR] -> %s" % error)
		else:
			size = len(array)
			string = ""
			for k in range(size):
				for c in range(size):
					string += f"{array[k][c]} "
				print(string)
				string = ""

	if __name__ == "__main__":
		map_1 = create_map(50)
		map_2 = create_map_bomba(map_1, 40, 9)
		map_3 = create_map_indication(map_2, 9)
		display_map(map_3)