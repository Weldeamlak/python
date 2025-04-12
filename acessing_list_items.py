magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#    print(magician)
# print(f"{"Hello"} , magician") # works well but it prints once for all magisian so it is logical error
# for magician in magicians:
#    print(magician)
#    print(f"Hello , {magician}")  # right way

# pizzas = ['pepperoni', 'mushrooms', 'extra cheese']
# for pizza in pizzas:
#    print(f"i love {pizza}")
# print("i realy love pizza")   
squares = []
for value in range(1, 11):
  square = value ** 2
  squares.append(square)
print(squares)

for value in range(1, 11):
  print(value)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))


# list comprehension: used to write simple and short code 
# squares = []
# for value in range(1, 11):
#   square = value ** 2
#   squares.append(square)
# print(squares) ......... give the same result as below
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# it is just one line code
# what we done in the above 
# 1. creating list name =>squres
# 2.open the square bracket
# 3. write the code that you want to execute

# 4. write the for loop
# 5. write the value that you want to use in the for loop

