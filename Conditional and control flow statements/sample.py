'''
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.completed_quests = []
        self.attack_power = 15 if name.upper() in ["SIVA", "FLYNN RIDER"] else 10

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount

    def complete_quest(self, quest):
        self.completed_quests.append(quest)

    def attack(self):
        return random.randint(self.attack_power // 2, self.attack_power)

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

def combat(player, enemy):
    print(f"You've encountered a {enemy.name} with {enemy.health} health!")
    while player.is_alive() and enemy.is_alive():
        action = input("What will you do? (attack/heal): ")
        if action == "attack":
            player_damage = player.attack()
            enemy_damage = random.randint(5, 15)
            enemy.take_damage(player_damage)
            print(f"You attack the {enemy.name} for {player_damage} damage!")
            print(f"{enemy.name}'s health: {enemy.health}")
            if enemy.is_alive():
                player.take_damage(enemy_damage)
                print(f"The {enemy.name} attacks you for {enemy_damage} damage!")
                print(f"Your health: {player.health}")
        elif action == "heal":
            heal_amount = random.randint(10, 20)
            player.heal(heal_amount)
            print(f"You heal yourself for {heal_amount} health points!")
            print(f"Your health: {player.health}")
            enemy_damage = random.randint(5, 15)
            player.take_damage(enemy_damage)
            print(f"The {enemy.name} attacks you for {enemy_damage} damage!")
            print(f"Your health: {player.health}")
    if player.is_alive():
        print("You defeated the enemy!")
    else:
        print("You were defeated.")

def quiz_challenge():
    questions = [
        ("What has keys but can't open locks?", "keyboard"),
        ("What has a head, a tail, is brown, and has no legs?", "penny"),
        ("What has to be broken before you can use it?", "egg"),
        ("What can be caught but never thrown?", "cold"),
        ("What belongs to you but others use it more than you do?", "name"),
        ("What comes once in a minute, twice in a moment, but never in a thousand years?", "m"),
        ("What has a neck but no head?", "bottle"),
        ("What has legs but can't walk?", "table"),
        ("What can travel around the world while staying in a corner?", "stamp"),
        ("What has a face and two hands but no arms or legs?", "clock")
    ]
    question1, answer1 = random.choice(questions)
    questions.remove((question1, answer1))
    question2, answer2 = random.choice(questions)
    print("You encounter a mysterious scroll with two riddles on it:")
    print("1.", question1)
    print("2.", question2)
    selected_question = input("Select a question (1/2): ")
    if selected_question == "1":
        question, answer = question1, answer1
    elif selected_question == "2":
        question, answer = question2, answer2
    else:
        print("Invalid selection.")
        return False
    user_answer = input("Your answer: ").lower()
    if user_answer == answer:
        print("Correct! You found a hidden treasure!")
        return True
    else:
        print("Incorrect! You are attacked by a trap!")
        combat(Player("You"), Enemy("DEVIL_GOD_SHIVA", 50, 5))  # Player forced into battle
        return False

def rescue_princess(player, princess_name):
    sorcerer = Enemy("Evil Sorcerer", 60, 10)
    print(f"You embark on a quest to rescue Princess {princess_name} from the clutches of an {sorcerer.name} with {sorcerer.health} health.")
    challenges = [
        ("Sneak Past the Guards", "Successfully sneak past the sorcerer's guards without being detected."),
        ("Free Princess", f"Release Princess {princess_name} from her chains and gain her trust."),
        ("Return Princess to the Kingdom", f"Escort Princess {princess_name} safely back to her kingdom and face {sorcerer.name} in the final confrontation.")
    ]
    for challenge, description in challenges:
        print(f"\nChallenge: {challenge}")
        print(description)
        if input("Press enter to continue..."):
            print("Challenge completed!")
        else:
            print("You failed the challenge and must face a stronger enemy!")
            combat(player, sorcerer)  # Stronger enemy
            break
    else:
        print(f"\nCongratulations! You have successfully rescued Princess {princess_name}!")
        player.complete_quest("Rescue Princess")
        print("You are hailed as a hero by the kingdom and rewarded with riches and glory.")

def start_quest(player):
    if player.name.upper() in ["SIVA", "FLYNN RIDER"]:
        princess_name = "RUPANZEL"
        rescue_princess(player, princess_name)
    else:
        print("What type of quest would you like to start?")
        print("1. Quiz Challenge")
        print("2. Rescue Princess")
        quest_choice = input("Enter your choice (1/2): ")

        if quest_choice == "1":
            quiz_challenge()
        elif quest_choice == "2":
            princess_name = input("Enter the name of the princess: ")
            rescue_princess(player, princess_name)
        else:
            print("Invalid choice.")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Start combat")
        print("2. Start quest")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            combat(player, random.choice([Enemy("DEVIL_KING", 50, 10), Enemy("DEVIL_GOD_SHIVA", 50, 10)]))
        elif choice == "2":
            start_quest(player)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__=="__main__":
    main()
'''
print('''OK, now this is the new option in the coding We can write the code by saying in the mic.    ''')
print("python")