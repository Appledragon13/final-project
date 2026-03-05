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


