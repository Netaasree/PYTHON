import random

class Player:
    def __init__(self, name, race, character_class):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.hp = 100
        self.gold = 0
        self.level = 1

    def __str__(self):
        return f"{self.name} - Race: {self.race}, Class: {self.character_class}, Level: {self.level}, HP: {self.hp}, Gold: {self.gold}"

class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward

    def __str__(self):
        return f"{self.name}: {self.description}, Reward: {self.reward} gold"

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def __str__(self):
        return f"{self.name}\n{self.description}\nQuests Available: {[quest.name for quest in self.quests]}"

def create_player():
    name = input("Enter your character's name: ")
    race = input("Choose your race (Human, Elf, Dwarf, Orc): ")
    character_class = input("Choose your class (Warrior, Mage, Rogue, Priest): ")
    return Player(name, race, character_class)

def create_quest():
    name = input("Enter quest name: ")
    description = input("Enter quest description: ")
    reward = random.randint(10, 50)
    return Quest(name, description, reward)

def explore_location(player, location):
    print(location)
    choice = input("Would you like to explore (E) or leave (L)? ").upper()
    if choice == "E":
        quest_choice = input("Would you like to take on a quest? (Y/N) ").upper()
        if quest_choice == "Y" and location.quests:
            selected_quest = random.choice(location.quests)
            print("You've accepted the quest:", selected_quest)
            player.gold += selected_quest.reward
            print("Quest completed! You've earned", selected_quest.reward, "gold.")
            location.quests.remove(selected_quest)
        elif not location.quests:
            print("There are no quests available here.")
        else:
            print("No quest selected.")
    elif choice == "L":
        print("Leaving the location.")

def main():
    player = create_player()
    print("\nWelcome to the Text-Based RPG!\n")

    locations = [
        Location("Forest", "A dense forest filled with towering trees."),
        Location("Cave", "A dark and mysterious cave."),
        Location("Town", "A bustling town filled with merchants and adventurers.")
    ]

    # Adding quests to locations
    locations[0].add_quest(Quest("Collect Herbs", "Gather medicinal herbs for the town healer.", 20))
    locations[2].add_quest(Quest("Deliver Package", "Deliver a package to a merchant in the neighboring village.", 30))

    while True:
        print("\nPlayer Info:")
        print(player)

        print("\nLocations:")
        for i, location in enumerate(locations):
            print(f"{i + 1}. {location.name}")

        choice = int(input("Select a location to explore: "))
        if 1 <= choice <= len(locations):
            explore_location(player, locations[choice - 1])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
