import random

# defining the order
def player_order(p1,p2):
      
    print("Player 1 rolled ", p1)
    print("Player 2 rolled ", p2)
    
    if p1 == "rock" and p2 == "scissors":
        print("Player 1 goes first!")
        return 1
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 goes first!")
        return 2
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 goes first!")
        return 2
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 goes first!")
        return 1
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 goes first!")
        return 1
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 goes first!")
        return 2
    elif p1 == p2:
        print("It's a draw! One more time:")
        p1 = random.choice(("rock", "scissors", "paper",))
        p2 = random.choice(("rock", "scissors", "paper",))
        player_order(p1, p2)

# counting damage amount dealt after one attack 
def damage_caused(chosen_weap):

    # damage modifier for each weapon
    SW_DMG = 1
    HAM_DMG = 1
    CR_DMG = 1.2
    SB_DMG = 1.4
    damage = {
                 "sword": SW_DMG*random.randint(1, 15),
                 "hammer": HAM_DMG*random.randint(1, 15),
                 "crossbow": CR_DMG*random.randint(1, 20),
                 "spell book": SB_DMG*random.randint(1, 23)
             }
    return damage.get(chosen_weap, 0)

# counting hit points based on the chosen race and class
def race_and_class_hp(chosen_race, chosen_class):

    # basic hit points depending on the race
    ORC_HP = 55
    HUMAN_HP = 50
    ELF_HP = 47
    GNOLL_HP = 49

    # hit points modifier for each class
    TANK_MOD = 1.1
    BERS_MOD = 1.2
    SHOOT_MOD = 1
    WIZ_MOD = 0.9

    # hit points formula for each race/class combination
    class_hp = {
                    ("orc", "tank"): ORC_HP*TANK_MOD,
                    ("orc", "berserker"): ORC_HP*BERS_MOD,
                    ("orc", "shooter"): ORC_HP*SHOOT_MOD,
                    ("orc", "wizard"): ORC_HP*WIZ_MOD,
                    ("human", "tank"): HUMAN_HP*TANK_MOD,
                    ("human", "berserker"): HUMAN_HP*BERS_MOD,
                    ("human", "shooter"): HUMAN_HP*SHOOT_MOD,
                    ("human", "wizard"): HUMAN_HP*WIZ_MOD,
                    ("elf", "tank"): ELF_HP*TANK_MOD,
                    ("elf", "berserker"): ELF_HP*BERS_MOD,
                    ("elf", "shooter"): ELF_HP*SHOOT_MOD,
                    ("elf", "wizard"): ELF_HP*WIZ_MOD,
                    ("gnoll", "tank"): GNOLL_HP*TANK_MOD,
                    ("gnoll", "berserker"): GNOLL_HP*BERS_MOD,
                    ("gnoll", "shooter"): GNOLL_HP*SHOOT_MOD,
                    ("gnoll", "wizard"): GNOLL_HP*WIZ_MOD
               }
    return class_hp.get((chosen_race, chosen_class), 0)
    
# describing races, classes, weapons, hit points and damage
RACE = ("orc",
        "human",
        "elf",
        "gnoll")
BATTLE_CLASS = ("tank",
                "berserker",
                "shooter",
                "wizard")
WEAPONS = ("sword",
           "hammer",
           "crossbow",
           "spell book")

while True:

    print("Greetings! Let the fate decide who goes first: ")

    p1 = random.choice(("rock", "scissors", "paper",))
    p2 = random.choice(("rock", "scissors", "paper",))
    order = player_order(p1,p2)
    print("Let the fun begin!")
    
    #creating the character
    p1_race = input("Player 1, choose your race {}: ".format(RACE))
    while p1_race not in RACE:
        p1_race = input("Please try again: ")
    p1_class = input("Your class {}: ".format(BATTLE_CLASS))
    while p1_class not in BATTLE_CLASS:
        p1_class = input("Please try again: ")
    p1_weap = input("And your weapon {}: ".format(WEAPONS))
    while p1_weap not in WEAPONS:
        p1_weap = input("Please try again: ")
    p2_race = input("Player 2, choose your race {}: ".format(RACE))
    while p2_race not in RACE:
        p2_race = input("Please try again: ")
    p2_class = input("Your class {}: ".format(BATTLE_CLASS))
    while p2_class not in BATTLE_CLASS:
        p2_class = input("Please try again: ")
    p2_weap = input("And your weapon {}: ".format(WEAPONS))
    while p2_weap not in WEAPONS:
        p2_weap = input("Please try again: ")

    #player 1 and 2 hit points
    p1_hp = race_and_class_hp(p1_race, p1_class)
    p2_hp = race_and_class_hp(p2_race, p2_class)
    
    # starting the fight if Player 1 should go first
    if order == 1:
        while True:
            print("Player 1 has {0} HP and Player 2 has {1} HP".format(p1_hp, p2_hp))

            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                p2_hp -= damage_caused(p1_weap)
                
            attack_2 = input("Player 2, describe your attack to your opponent and enter 'go!': ")
            while attack_2 not in ("go!",):
                attack_2 = input("Please try again: ")
            if attack_2 == "go!":
                p1_hp -= damage_caused(p2_weap)   

            if p1_hp <= 0 or p2_hp <= 0:
                print("Player 1 has {0} HP and Player 2 has {1} HP, congratulations to the winner!".format(p1_hp, p2_hp))
                break
            else:
                continue

    # starting the fight if Player 2 should go first
    if order == 2:
        while True:
            print("Player 1 has {0} HP and Player 2 has {1} HP".format(p1_hp, p2_hp))

            attack_2 = input("Player 2, describe your attack to your opponent and enter 'go!': ")
            while attack_2 not in ("go!",):
                attack_2 = input("Please try again: ")
            if attack_2 == "go!":
                p1_hp -= damage_caused(p2_weap)

            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                p2_hp -= damage_caused(p1_weap)   

            if p1_hp <= 0 or p2_hp <= 0:
                print("Player 1 has {0} HP and Player 2 has {1} HP, congratulations to the winner!".format(p1_hp, p2_hp))
                break
            else:
                continue
    
    # asking if players want to start the game again
    repeat = input("Would you like to play again? Enter 'y' for another game or 'n' to quit: ")
    while repeat not in ("y","n"):
        repeat = input("Please make a valid choice ('y' or 'n'): ")
    if repeat == "y":
        continue
    else:
        print("Good bye!")
        break