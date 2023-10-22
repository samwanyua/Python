#Random module

import random
x=random.randint(1,6)
print(x)
y=random.random()
print(y)

my_list=["Rock", "Paper", "Scissors"]
z=random.choice(my_list)
print(z)

cards= ['A', 2,3,4,5,6,7,8,9,10,'J','Q','K']
random.shuffle(cards)
print(cards)