import random
from timeit import default_timer as timer
from collections import defaultdict


def answer_slow(heights):
	height_dict = defaultdict(list)
	largest_height = 0

	index = 0
	for h in heights:
		if largest_height < h:
			largest_height = h
		height_dict[h].append(index)
		index += 1

	sum_height = 0
	indexes = set()
	for j in range(largest_height, 0, -1):
		indexes |= set(height_dict[j])
		height_dict[j] = list(indexes)
		height_dict[j].sort()
		for i in range(len(height_dict[j])-1):
			sum_height += height_dict[j][i+1] - height_dict[j][i]-1
	return sum_height


def answer(heights):
	ordered_unique_heights = list(set(heights))
	ordered_unique_heights.sort(reverse=True)
	height_dict = defaultdict(list)

	index = 0
	for h in heights:
		height_dict[h].append(index)
		index += 1

	height_sum = 0
	for i in range(len(heights)):
		j = 1
		if i < height_dict[ordered_unique_heights[0]][0]:
			# tallest is to my right
			while height_dict[ordered_unique_heights[j]][0] > i:
				# Search for largest left bound
				j += 1
		elif i > height_dict[ordered_unique_heights[0]][len(height_dict[ordered_unique_heights[0]]) - 1]:
			# tallest is to my left
			while height_dict[ordered_unique_heights[j]][len(height_dict[ordered_unique_heights[j]]) - 1] < i:
				# Search for largest right bound
				j += 1
		else:
			# I am between the tallest
			j = 0

		height_sum += ordered_unique_heights[j] - heights[i]

	return height_sum


def random_building_heights(howmany, range_limt):
	result = []

	for i in range(howmany):
		result.append(random.randint(1, range_limt))
	return result

building_easy1 = [10, 1, 3, 6, 6, 1, 6, 2]
building_easy2 = [10, 1, 10, 1, 1, 10, 4, 3, 2, 8, 8]
building_easy3 = random_building_heights(100, 100000)
building_easy4 = [1, 4, 2, 5, 1, 2, 3]
building_easy5 = [1, 2, 3, 2, 1]
building_hard1 = random_building_heights(random.randint(1, 9000), 100000)
building_hard2 = random_building_heights(random.randint(1, 9000), 100000)
building_hard3 = random_building_heights(9000, 100000)

print("\nBuilding heights:  " + str(building_easy1))
print("Summed:  " + str(answer_slow(building_easy1)))
print("Summed:  " + str(answer(building_easy1)))

print("\nBuilding heights:  " + str(building_easy2))
print("Summed:  " + str(answer_slow(building_easy2)))
print("Summed:  " + str(answer(building_easy2)))

print("\nBuilding heights:  " + str(building_easy3))
start1 = timer()
print("Summed:  " + str(answer_slow(building_easy3)))
end1 = timer()
start2 = timer()
print("Summed:  " + str(answer(building_easy3)))
end2 = timer()
print(end1-start1)
print(end2-start2)

print("\nBuilding heights:  " + str(building_easy4))
print("Summed:  " + str(answer_slow(building_easy4)))
print("Summed:  " + str(answer(building_easy4)))

print("\nBuilding heights:  " + str(building_easy5))
print("Summed:  " + str(answer_slow(building_easy5)))
print("Summed:  " + str(answer(building_easy5)))

print("\nBuilding heights:  " + str(building_hard1))
print("Summed:  " + str(answer(building_hard1)))

print("\nBuilding heights:  " + str(building_hard2))
print("Summed:  " + str(answer(building_hard2)))

print("\nBuilding heights:  " + str(building_hard3))
start3 = timer()
print("Summed:  " + str(answer(building_hard3)))
end3 = timer()
print(end3-start3)
