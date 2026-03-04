class npc:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, amount):
        """
        Reduces the character's health by the specified amount and checks for defeat.
        """
        self.current_health -= amount
        # Ensure health does not drop below zero
        if self.current_health < 0:
            self.current_health = 0
        print(f"{self.name} took {amount} damage! Current health: {self.current_health}/{self.max_health}")
        if self.current_health == 0:
            print(f"{self.name} has been defeated!")

    def attack(self, target):
        """
        Performs an attack on a target character.
        The damage calculation logic is within the damage_calculation function.
        """
        # A simple base damage value or a roll can be used
        base_damage = self.attack_power
        actual_damage = base_damage - target.defense
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(actual_damage)
# Class for the main character
class player:
    def __init__(self, name, health, attack_power, defense, items):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.items = items

    def take_damage(self, amount):
        """
        Reduces the character's health by the specified amount and checks for defeat.
        """
        self.current_health -= amount
        # Ensure health does not drop below zero
        if self.current_health < 0:
            self.current_health = 0
        print(f"{self.name} took {amount} damage! Current health: {self.current_health}/{self.max_health}")
        if self.current_health == 0:
            print(f"{self.name} has lost the game.")

    def attack(self, target):
        """
        Performs an attack on a target character.
        The damage calculation logic is within the damage_calculation function.
        """
        # A simple base damage value or a roll can be used
        base_damage = self.attack_power
        actual_damage = base_damage - target.defense
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(actual_damage)
