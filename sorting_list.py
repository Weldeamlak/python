#   sorting arrays using sort() and sorted() and  reverse()

my_fav_cities =['Aksum' , 'AddisAbaba' , 'DireDawa' , 'Hawassa' ,'Gondar']
# sort() permanet sorting
# help memory manegment
my_fav_cities.sort()

print(my_fav_cities)

# sorted() temporary sorting
# does not change the original list

my_favo_cities =['Aksum' , 'AddisAbaba' , 'DireDawa' , 'Hawassa' ,'Gondar']

sorted_cities = sorted(my_favo_cities)
print(my_favo_cities)   # orginal list is dispaly
print(sorted_cities)  # emporary sorted list will display
my_favo_cities.reverse()
print(my_favo_cities)  # reverse the list
my_favo_cities.reverse() # back to the original

# Sorting a Dictionary
student_scores = {
    "Nati": 90,
    "Haile": 75,
    "Betty": 85
}
# Sort by Keys
# for name in sorted(student_scores):
#     print(name ,"->", student_scores[name])
 

#  sort by value

# for name in sorted(student_scores , key = student_scores.get):
#     print(name ,"->", student_scores[name])

   #  to make it reverse
for name in sorted(student_scores , key = student_scores.get , reverse = True):
    print(name ,"->", student_scores[name])