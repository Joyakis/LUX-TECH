#square of numbers
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# For even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#Flattening a list of list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

