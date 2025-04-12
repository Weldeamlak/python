for value in range(1,21 ,2):
   print(value)


# for one_million in range(1,1000001):
   # print(one_million)   
#  print the first mllion numbers is time consumer but geting there min sum or other is done in a msec
# Creating a list of numbers from 1 to 1 million
numbers = list(range(1, 1000001))

# Using min(), max(), and sum() to check the list and sum the numbers
print(f"Min: {min(numbers)}") 
print(f"Max: {max(numbers)}")  
print(f"Sum: {sum(numbers)}") 

multiple_of_3 = list(range(3,31,3))
print(f"a multiple of there between 3 and 30 are:{multiple_of_3}")
# cubes = []
# for value in range(1, 11):
#    cube = value ** 3
#    cubes.append(cube)
# print(cubes) 

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)  