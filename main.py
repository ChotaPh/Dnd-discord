import random

act = input ("dice action: ")



# Advantage

# Roll 2 times
# Save roll result each time
# use Max function to pick highest

# List  rolls
# Value [3] [ ] [7]
# Index  0   1   2
# rolls[1] = 7
# => [3] [7] [7]
# rolls.append(99)
# => [3] [7] [7] [99]







if act == "droll":
    rolles = 2
    def dis_roll(rolles):
        rolls = []
        for x in range(rolles):
            rolls.append(random.randint(1, 20))
            print(x + 1, ":", rolls)
        min = rolls[0]
        for num in rolls:
            if num < min:
                min = num
        return min
    print("rolled",dis_roll(rolles))
elif act== "adroll":
    rolles = 2
    def ad_roll(rolles):
        rolls = []
        for x in range(rolles):
            rolls.append(random.randint(1, 20))
            print(x + 1, ":", rolls)
        return max(rolls)
    print("rolled",ad_roll(rolles))
elif act == "atkroll":
    input_str = input('sides, roll: ')  # sides, roll: 4 2
    input_split = input_str.split(' ')  # '4 2'
    sides = int(input_split[0])
    roll = int(input_split[1])
    def total_roll(sides, roll):
        total = 0
        for x in range(roll):
            roll = random.randint(1, sides)
            total = total + roll
            print(x + 1, ":", roll)
        return total
    print("total",total_roll(sides,roll))

print("\n")
