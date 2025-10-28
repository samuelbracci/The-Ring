import random
import time

class Stats():
    def __init__(self, base_damage, attack_modifier, health):
        self.base_damage = base_damage
        self.attack_modifier = attack_modifier
        self.health = health

#Players and Enemy stats (Modifiers have to be 10)
#Sorting rule for Stats: Same amount, High rolls, Weak rolls, Miss rolls
fighter = Stats(10, [1, 1, 1, 1, 1, 1.5, 2, 4, 0.8, 0.5, 0], 100) 
dummy = Stats(1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 100) ##Training mode
goblin = Stats(5, [1, 1, 2, 2, 3, 5, 0.5, 0.8, 0, 0], 100) ##Easy enemy
knight = Stats(10, [1, 1, 1, 1, 2, 3, 0.5, 0.8, 0, 0], 100) ##Medium enemy 
dragon = Stats(10,[1, 1, 1, 1, 2, 2, 3, 0.5, 0.5, 0], 100) ##Hard enemy


def attacking(base = int, modifier = list):
    total_damage = base * modifier[random.randint(0, 9)]
    return total_damage

def updating_health(hp, damage):
    hp -= damage
    if hp < 0:
        hp = 0
    return hp


##Menu functions
def menu_option1():
    print("==============================")
    print("|          The Ring          |")
    print("|    O===[)::::::::::::>     |")
    print("==============================\n")
    print("          (Battle) <---")
    print("        (Switch class)")
    print("           (Lore)")
    print("          (Credits)\n")


def menu_option2():
    print("==============================")
    print("|          The Ring          |")
    print("|    O===[)::::::::::::>     |")
    print("==============================\n")
    print("          (Battle)")
    print("        (Switch class) <---")
    print("           (Lore)")
    print("          (Credits)\n")

def menu_option3():
    print("==============================")
    print("|          The Ring          |")
    print("|    O===[)::::::::::::>     |")
    print("==============================\n")
    print("          (Battle)")
    print("        (Switch class)")
    print("           (Lore) <---")
    print("          (Credits)\n")

def menu_option4():
    print("==============================")
    print("|          The Ring          |")
    print("|    O===[)::::::::::::>     |")
    print("==============================\n")
    print("          (Battle)")
    print("        (Switch class)")
    print("           (Lore)")
    print("          (Credits) <---\n")

def error():
    print("")
    print("|| Invalid input. Please try again. ||\n")

def main_menu():
    while True:
        time.sleep(0.5)
        print("")
        menu_option1()
        choice = input("Select or scroll down (y/s): ")
        if choice == "s":
            time.sleep(0.5)
            print("")
            menu_option2()
            choice = input("Select or scroll down (y/s): ")
            if choice == "s":
                time.sleep(0.5)
                print("")
                menu_option3()
                choice = input("Select or scroll down (y/s): ")
                if choice == "s":
                    time.sleep(0.5)
                    print("")
                    menu_option4()
                    choice = input("Select or scroll down (y/s): ")
                    if choice == "y":
                        print("")
                        print("*** Created and programmed by Sam Bracci in 2025 :) ***\n")
                elif choice == "y":
                    print("Lore goes here woah cool lore poggers")
            elif choice == "y":
                print("Fighter")
                print(f"Base attack: {fighter.base_damage}")
                print(f"Modifier: {fighter.attack_modifier}")
                print(f"Health: {fighter.health}")
        elif choice == "y":
            time.sleep(0.5)
            print("You enter the ring...you spot challenge posters on the wall.\n")
            print("|===================|   |===================|   |===================|   |===================|")
            print("|     Slaughter     |   |     Challenge     |   |      Survive      |   |       Train       |")
            print("|    The Goblin     |   |    The Knight     |   |     The Dragon    |   | Against the Dummy |")
            print("|                   |   |                   |   |                   |   |                   |")
            print("| A goblin we found |   | A knight from the |   | A dragon flew in  |   | Hone your skills  |")
            print("| in the forest.    |   | village wanting a |   | from the mountain |   | by fighting a     |")
            print("| Looks crafty but  |   | duel.             |   | Your not expected |   | dummy!            |")
            print("| should be an easy |   | A fair challenge  |   | to survive this   |   | A cakewalk but    |")
            print("| duel.             |   | Stay on guard.    |   | opponent.         |   | good practice.    |")
            print("|===================|   |===================|   |===================|   |===================|")
            print("\n")
            choice = input("Select the foe you wish to battle. (1-4/exit): ")
            if choice == "1":
                goblin_battle_system()
            elif choice == "2":
                knight_battle_system()
            elif choice == "3":
                dragon_battle_system()
            elif choice == "4":
                dummy_battle_system()
            else:
                error()
        else:
            error()


##Battle functions
def dummy_battle_system():
    print("")
    print("")
    print("")

    #Reset health for next battle
    fighter.health = 100
    dummy.health = 100

    print("\033[1mBattle begin!\033[0m\n")
    while True:
        time.sleep(1)
        print("-Your turn-")        
        print("1. Attack")
        print("2. Skill")
        choice = input("Pick a option: ")
        print("")
        if choice == "1":
            #Calculate damage
            attack = attacking(fighter.base_damage, fighter.attack_modifier)
            if attack == 0:
                time.sleep(1)
                print("Miss!")
                print("")
            else:
                #Update enemy health after player attack
                dummy.health = updating_health(dummy.health, attack)
                time.sleep(1)
                print(f"Attack result: {attack}")
                print(f"Enemy health: {dummy.health}")
                print("")
                
                #Victory if enemy health = 0
                if dummy.health == 0:
                    time.sleep(1)
                    print("The opponent has no more health left\n")
                    print("-------------You win!---------------")
                    print("")
                    break
            #Dodge if enemy rolls a 0
            enemy_attack = attacking(dummy.base_damage, dummy.attack_modifier)
            if enemy_attack == 0:
                time.sleep(1)
                print("Dodged the enemy attack!")
                print("")
            else:
                print("-Enemy turn-")
                #Update player health after enemy attack
                fighter.health = updating_health(fighter.health, enemy_attack)
                time.sleep(1)
                print(f"Enemy attack result: {enemy_attack}")
                print(f"Your health: {fighter.health}")
                print("")
                
                #Game over if out of health
                if fighter.health == 0:
                    time.sleep(1)
                    print("You have run out of health and fainted\n")
                    print("-------------Game Over--------------")
                    print("")
                    break
        else:
            error()
            print("")


def goblin_battle_system():
    print("")
    print("")
    print("")

    #Reset health for next battle
    fighter.health = 100
    goblin.health = 100
    
    print("\033[1mBattle begin!\033[0m\n")
    while True:
        time.sleep(1)
        print("-Your turn-")        
        print("1. Attack")
        print("2. Skill")
        choice = input("Pick a option: ")
        print("")
        if choice == "1":
            #Calculate damage
            attack = attacking(fighter.base_damage, fighter.attack_modifier)
            if attack == 0:
                time.sleep(1)
                print("Miss!")
                print("")
            else:
                #Update enemy health after player attack
                goblin.health = updating_health(goblin.health, attack)
                time.sleep(1)
                print(f"Attack result: {attack}")
                print(f"Enemy health: {goblin.health}")
                print("")
                
                #Victory if enemy health = 0
                if goblin.health == 0:
                    time.sleep(1)
                    print("The opponent has no more health left\n")
                    print("-------------You win!---------------")
                    print("")
                    break
            #Dodge if enemy rolls a 0
            enemy_attack = attacking(goblin.base_damage, goblin.attack_modifier)
            if enemy_attack == 0:
                time.sleep(1)
                print("Dodged the enemy attack!")
                print("")
            else:
                print("-Enemy turn-")
                #Update player health after enemy attack
                fighter.health = updating_health(fighter.health, enemy_attack)
                time.sleep(1)
                print(f"Enemy attack result: {enemy_attack}")
                print(f"Your health: {fighter.health}")
                print("")
                
                #Game over if out of health
                if fighter.health == 0:
                    time.sleep(1)
                    print("You have run out of health and fainted\n")
                    print("-------------Game Over--------------")
                    print("")
                    break
        else:
            error()
            print("")

def knight_battle_system():
    print("")
    print("")
    print("")

    #Reset health for next battle
    fighter.health = 100
    knight.health = 100

    print("\033[1mBattle begin!\033[0m\n")
    while True:
        time.sleep(1)
        print("-Your turn-")        
        print("1. Attack")
        print("2. Skill")
        choice = input("Pick a option: ")
        print("")
        if choice == "1":
            #Calculate damage
            attack = attacking(fighter.base_damage, fighter.attack_modifier)
            if attack == 0:
                time.sleep(1)
                print("Miss!")
                print("")
            else:
                #Update enemy health after player attack
                knight.health = updating_health(knight.health, attack)
                time.sleep(1)
                print(f"Attack result: {attack}")
                print(f"Enemy health: {knight.health}")
                print("")
                
                #Victory if enemy health = 0
                if knight.health == 0:
                    time.sleep(1)
                    print("The opponent has no more health left\n")
                    print("-------------You win!---------------")
                    print("")
                    break
            #Dodge if enemy rolls a 0
            enemy_attack = attacking(knight.base_damage, knight.attack_modifier)
            if enemy_attack == 0:
                time.sleep(1)
                print("Dodged the enemy attack!")
                print("")
            else:
                print("-Enemy turn-")
                #Update player health after enemy attack
                fighter.health = updating_health(fighter.health, enemy_attack)
                time.sleep(1)
                print(f"Enemy attack result: {enemy_attack}")
                print(f"Your health: {fighter.health}")
                print("")
                
                #Game over if out of health
                if fighter.health == 0:
                    time.sleep(1)
                    print("You have run out of health and fainted\n")
                    print("-------------Game Over--------------")
                    print("")
                    break
        else:
            error()
            print("")

def dragon_battle_system():
    print("")
    print("")
    print("")

    #Reset health for next battle
    fighter.health = 100
    dragon.health = 100

    print("\033[1mBattle begin!\033[0m\n")
    while True:
        time.sleep(1)
        print("-Your turn-")        
        print("1. Attack")
        print("2. Skill")
        choice = input("Pick a option: ")
        print("")
        if choice == "1":
            #Calculate damage
            attack = attacking(fighter.base_damage, fighter.attack_modifier)
            if attack == 0:
                time.sleep(1)
                print("Miss!")
                print("")
            else:
                #Update enemy health after player attack
                dragon.health = updating_health(dragon.health, attack)
                time.sleep(1)
                print(f"Attack result: {attack}")
                print(f"Enemy health: {dragon.health}")
                print("")
                
                #Victory if enemy health = 0
                if dragon.health == 0:
                    time.sleep(1)
                    print("The opponent has no more health left\n")
                    print("-------------You win!---------------")
                    print("")
                    break
            #Dodge if enemy rolls a 0
            enemy_attack = attacking(dragon.base_damage, dragon.attack_modifier)
            if enemy_attack == 0:
                time.sleep(1)
                print("Dodged the enemy attack!")
                print("")
            else:
                print("-Enemy turn-")
                #Update player health after enemy attack
                fighter.health = updating_health(fighter.health, enemy_attack)
                time.sleep(1)
                print(f"Enemy attack result: {enemy_attack}")
                print(f"Your health: {fighter.health}")
                print("")
                
                #Game over if out of health
                if fighter.health == 0:
                    time.sleep(1)
                    print("You have run out of health and fainted\n")
                    print("-------------Game Over--------------")
                    print("")
                    break
        else:
            error()
            print("")


"""
Planning Corner heheheheh

###Working on:
- Add one time skills to the game



#Completed functions:
+NPC battles

#High Priority/Function ideas:

- Add a class selector function 

- Finish working on the main menu 

- Add the option to pick between fighting NPC or two player battles

#Low Priority ideas:
-Add unique dialouge whenver a character gets a high roll, example for the knight: "The knight does a jumping slash!" [Can code with array placement]

#Class ideas:
Figher
Archer 
Gambler Mage (A high risk high reward mage that uses magic dice to attack)

"""