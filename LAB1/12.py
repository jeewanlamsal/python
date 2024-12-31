#WAP to find the sum of all items in a dictionary
#Input: {'a': 100, 'b':200, 'c':300}
#Output: 600
#Input: {'x': 25, 'y':18, 'z':45}
#Output: 88

def sum_of_dict_items(input_dict):
 
    return sum(input_dict.values())

input1 = {'a': 100, 'b': 200, 'c': 300}
output1 = sum_of_dict_items(input1)
print(f"Input: {input1}\nOutput: {output1}")

input2 = {'x': 25, 'y': 18, 'z': 45}
output2 = sum_of_dict_items(input2)
print(f"Input: {input2}\nOutput: {output2}")