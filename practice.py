import random
print(random.random())
print(int(random.random()*10)+5)
print(random.randint(5,15))


cards = ["Ace", "King", "Queen", "Jack"]
print(random.choice(cards))
print(cards)
random.shuffle(cards)
print(cards)
pos = 0
num_steps=0
while pos> -5 and pos <5:
    coin_flip = random.randint(0,1)
    if coin_flip == 1:
        pos += 1
    else:
        pos -=1
    num_steps += 1
    print("Current Position: ",pos)
print("Num Steps: ", num_steps)