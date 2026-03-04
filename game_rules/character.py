import random  # Imported in case you later want crits or randomness


# =====================================================
# Weapon Class
# Represents a weapon the player can equip
# =====================================================
class Weapon:
    def __init__(self, name, attack_bonus, price):
        # Name of the weapon (ex: "Iron Sword")
        self.name = name
        
        # How much extra attack damage this weapon adds
        self.attack_bonus = attack_bonus
        
        # Cost of the weapon in gold
        self.price = price

    def __str__(self):
        # Controls how the weapon is displayed when printed
        return f"{self.name} (+{self.attack_bonus} ATK) - {self.price} gold"


# =====================================================
# Armor Class
# Represents armor the player can equip
# =====================================================
class Armor:
    def __init__(self, name, defense_bonus, price):
        # Name of the armor (ex: "Steel Armor")
        self.name = name
        
        # How much extra defense this armor adds
        self.defense_bonus = defense_bonus
        
        # Cost of the armor in gold
        self.price = price

    def __str__(self):
        # Controls how armor is displayed when printed
        return f"{self.name} (+{self.defense_bonus} DEF) - {self.price} gold"


# =====================================================
# HealingItem Class
# Represents consumable healing items like potions
# =====================================================
class HealingItem:
    def __init__(self, name, heal_amount, price):
        # Name of the item (ex: "Health Potion")
        self.name = name
        
        # Amount of health this item restores
        self.heal_amount = heal_amount
        
        # Cost of the item in gold
        self.price = price

    def __str__(self):
        # Controls how healing items are displayed
        return f"{self.name} (Heals {self.heal_amount}) - {self.price} gold"


# =====================================================
# Enemy Class
# Represents generic enemies the player fights
# =====================================================
class Enemy:
    def __init__(self, name, max_health, attack_power, defense):
        # Enemy name (ex: "Goblin")
        self.name = name
        
        # Maximum health the enemy can have
        self.max_health = max_health
        
        # Current health starts equal to max health
        self.current_health = max_health
        
        # How much base damage the enemy deals
        self.attack_power = attack_power
        
        # How much damage reduction the enemy has
        self.defense = defense

    def is_alive(self):
        # Returns True if the enemy still has health remaining
        return self.current_health > 0

    def attack(self, target):
        # Calculate damage dealt after subtracting target's defense
        damage = max(0, self.attack_power - target.get_defense())
        
        # Apply damage to the target
        target.take_damage(damage)
        
        # Print combat message
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def take_damage(self, damage):
        # Reduce current health by damage taken
        self.current_health -= damage
        
        # Prevent health from going below 0
        self.current_health = max(0, self.current_health)

    def __str__(self):
        # Controls how enemy status is displayed
        return f"{self.name} HP: {self.current_health}/{self.max_health}"


# =====================================================
# Player Class (Main Character)
# More advanced than Enemy because of equipment & inventory
# =====================================================
class Player:
    def __init__(self, name, max_health):
        # Player name
        self.name = name
        
        # Maximum health
        self.max_health = max_health
        
        # Current health starts full
        self.current_health = max_health
        
        # List storing all items the player owns
        self.inventory = []
        
        # Currently equipped weapon (starts as None)
        self.equipped_weapon = None
        
        # Currently equipped armor (starts as None)
        self.equipped_armor = None

    def is_alive(self):
        # Returns True if player still has health
        return self.current_health > 0

    def get_attack_power(self):
        # Base attack damage every player has
        base_attack = 5
        
        # If a weapon is equipped, add its bonus
        if self.equipped_weapon:
            return base_attack + self.equipped_weapon.attack_bonus
        
        # If no weapon equipped, return base attack
        return base_attack

    def get_defense(self):
        # Base defense every player has
        base_defense = 2
        
        # If armor is equipped, add its defense bonus
        if self.equipped_armor:
            return base_defense + self.equipped_armor.defense_bonus
        
        # If no armor equipped, return base defense
        return base_defense

    def attack(self, target):
        # Calculate damage after subtracting target defense
        damage = max(0, self.get_attack_power() - target.defense)
        
        # Apply damage to the target
        target.take_damage(damage)
        
        # Print combat result
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def take_damage(self, damage):
        # Reduce player health
        self.current_health -= damage
        
        # Prevent health from dropping below 0
        self.current_health = max(0, self.current_health)

    def heal(self, healing_item):
        # Check if item exists in inventory
        if healing_item in self.inventory:
            
            # Increase health by heal amount
            self.current_health += healing_item.heal_amount
            
            # Prevent health from exceeding max health
            self.current_health = min(self.max_health, self.current_health)
            
            # Remove used item from inventory
            self.inventory.remove(healing_item)
            
            # Print result
            print(f"{self.name} used {healing_item.name} and healed {healing_item.heal_amount} HP!")
        else:
            print("Item not in inventory!")

    def equip_weapon(self, weapon):
        # Equip a weapon
        self.equipped_weapon = weapon
        print(f"{self.name} equipped {weapon.name}.")

    def equip_armor(self, armor):
        # Equip armor
        self.equipped_armor = armor
        print(f"{self.name} equipped {armor.name}.")

    def add_to_inventory(self, item):
        # Add any item to inventory
        self.inventory.append(item)

    def __str__(self):
        # Displays player status information
        return (f"{self.name} HP: {self.current_health}/{self.max_health}\n"
                f"Weapon: {self.equipped_weapon.name if self.equipped_weapon else 'None'}\n"
                f"Armor: {self.equipped_armor.name if self.equipped_armor else 'None'}")
