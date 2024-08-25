def closest_key(input_dict, value):
    closest_key = None
    closest_index = float('inf')  # Start with a large value for comparison
    
    for key, values_list in input_dict.items():
        if value in values_list:
            index = values_list.index(value)
            if index < closest_index:
                closest_index = index
                closest_key = key
                
    return closest_key

# Test the function
test_dict = {
    'a': ['x', 'y', 'z'],
    'b': ['v', 'w', 'x'],
    'c': ['y', 'x', 'w']
}
print(closest_key(test_dict, 'x'))  # Output: 'a'
