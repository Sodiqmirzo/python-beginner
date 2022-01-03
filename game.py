from random import randint

t = ["Quduq", "Qog\'oz", "Qaychi"]


computer = t[randint(0, 2)]


player = False

computer_count = 0
player_count = 0
tie_count = 0

while player == False:

    player = input("Quduq, Qog\'oz, Qaychi ? \n")
    if player == computer:
        print("Durrang!")
        tie_count += 1
    elif player == "Quduq":
        if computer == "Qog\'oz":
            print("Yutqazdiz!", computer, "Yopdi", player)
            computer_count += 1
        else:
            print("Yutdiz!", player, "Cho\'kdi", computer)
            player_count += 1
    elif player == "Qog\'oz":
        if computer == "Qaychi":
            print("Yutqazdiz!", computer, "Kesdi", player)
            computer_count += 1
        else:
            print("Yutdiz!", player, "Yopdi", computer)
            player_count += 1
    elif player == "Qaychi":
        if computer == "Quduq":
            print("Yutqazdiz...", computer, "Kesdi", player)
            computer_count += 1
        else:
            print("Yutdiz!", player, "Kesdi", computer)
            player_count += 1
    elif player == "quit" or player == "q":
        break
    else:
        print("Boshqa harfni bosdiz. Qayta uruning!")

    player = False
    computer = t[randint(0, 2)]
print(f"""  
            O\'yin tugadi.
            Siz {player_count} marta yutdiz. 
            {computer_count} marta yutqazdiz. 
            {tie_count} marta durrang o\'ynadiz. 
            Umumiy o\'yin esa {player_count + computer_count + tie_count} marta o\'ynaldi. 
        """)
