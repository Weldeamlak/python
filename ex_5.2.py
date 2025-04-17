fruits = ['apple', 'banana', 'cherry', 'orange']

if 'apple' in fruits:
    print("Is 'apple' in fruits? I predict True.")
else:
    print("Is 'apple' in fruits? I predict False.")

if 'Apple'.lower() == 'apple':
    print("Is 'Apple'.lower() == 'apple'? I predict True.")
else:
    print("Is 'Apple'.lower() == 'apple'? I predict False.")

if 'grape' not in fruits:
    print("Is 'grape' not in fruits? I predict True.")
else:
    print("Is 'grape' not in fruits? I predict False.")

temperature = 15
humidity = 60
if temperature < 20 and humidity > 50:
    print("Is temperature < 20 and humidity > 50? I predict True.")
else:
    print("Is temperature < 20 and humidity > 50? I predict False.")

day = 'Monday'
time = 'afternoon'
if day == 'Monday' or time == 'morning':
    print("Is day == 'Monday' or time == 'morning'? I predict True.")
else:
    print("Is day == 'Monday' or time == 'morning'? I predict False.")

num1 = 10
num2 = 20
if num1 != num2:
    print("Is num1 != num2? I predict True.")
else:
    print("Is num1 != num2? I predict False.")

score = 85
if score > 80 and score < 90:
    print("Is score > 80 and score < 90? I predict True.")
else:
    print("Is score > 80 and score < 90? I predict False.")

age = 30
if age == 30:
    print("Is age == 30? I predict True.")
else:
    print("Is age == 30? I predict False.")

balance = 500
withdrawal = 600
if withdrawal > balance:
    print("Is withdrawal > balance? I predict True.")
else:
    print("Is withdrawal > balance? I predict False.")

numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Is 3 in numbers? I predict True.")
else:
    print("Is 3 in numbers? I predict False.")
