
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
my_friends_name = ['mesfin', 'siltanu', 'natnael', 'hailemichael']

for name in my_friends_name:
    message = f"My friend's name is {name.title()}."
    print(message)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
guest_list = ['jhon' , 'daneal' , 'santos']
print(f"{guest_list[1]} ,can't come in the party!")
del guest_list[1]
print(guest_list)
guest_list.insert(0 ,'kinda')
print('\n')
# guest_list.insert((len(guest_list)/2) ,'doe')  
# this will give an error because it must be like the below or line number 29
guest_list.insert(len(guest_list) // 2, 'doe')

guest_list.append('wark')
print(f"{guest_list.pop().title()} i can't invitted to my party")
print(f"{guest_list.pop().title()} i can't invitted to my party")
print(f"{guest_list.pop().title()} i can't invitted to my party")
print('\n')
for guest in guest_list:
 del guest_list[1]
 del guest_list[0] # this is not del the first element how , i do not know i will see next

print(f"{guest.title()}, you are invited to the party.")
 