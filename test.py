# Accept Values
number_of_values = int(input())
my_list = []
my_dict = {}
mean = 0.0
median = 0.0
mode = 0
mode_value = 0
my_list = input().split(' ')

# Convert list members to integers
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

# Sort list
my_list.sort(reverse = True)

# Calculate and print mean
for number in my_list:
    mean += number
mean /= len(my_list)

print('%0.1f' % mean)

# Calculate and print median
if (len(my_list) % 2 == 0):
    median = (my_list[len(my_list) // 2] + my_list[(len(my_list) - 2) // 2]) / 2
else:
    median = my_list[len(my_list) //2]

print('%0.1f' % median)

# Calculate and print mode
for number in my_list:
    if number not in my_dict:
        my_dict[number] = 1
    else:
        my_dict[number] = my_dict[number] + 1
        
mode = max(my_list)

for key in my_dict:
    if (my_dict[key] >= mode_value) and (key < mode):
        mode_value = my_dict[key]
        mode = key

print('%d' % mode)


























    
