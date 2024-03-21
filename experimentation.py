from dataclasses import dataclass
import math
import random

@dataclass
class Stats:
    # Points
    experience: int
    level: int
    hitpoints: int
    magicpoints: int
    
    # Primary Attributes
    strength: int
    dexterity: int
    vitality: int
    magic: int
    spirit: int
    luck: int
    
    # Derived Attributes
    attack: int
    hit_chance: int
    defense: int
    evade: int
    magic_attack: int
    magic_defense: int
    magic_dodge: int
    
    def __str__(self):
    # Format the output string to display the stats in a readable way
        return f"Level: {self.level}\nHP: {self.hitpoints}\nMP: {self.magicpoints}\n" \
               f"STR: {self.strength}\nDEX: {self.dexterity}\nVIT: {self.vitality}\n" \
               f"MAG: {self.magic}\nSPI: {self.spirit}\nLCK: {self.luck}"    
    
    def level_up(self):
        """https://gamedev.stackexchange.com/questions/82583/rpg-like-hit-points-growth-algorithms-help"""
        x = 0.07
        y = 2
        max_level = 10
        max_value = 9999
        
        while self.experience >= self._experience_required(x, y, max_level, max_value):
            self.experience -= self._experience_required(x, y, max_level, max_value)
            self.level += 1
            self._increase_stats()
            
    def _experience_required(self, x, y, max_level, max_value):
        if self.level < max_level:
            return round (((self.level + 1) /x )** y)
        else:
            return round(-y ** -(self.level - max_level) + max_value)
                
    def _increase_stats(self):
        point_bonus = random.randint(15,20)
        
        """
        Learning time: 
        Assume point_bonus = 20 and level is 2
        math.floor: rounds to DOWN to the nearest int value | math.exp = 2.71828
        hp_bonus = math.floor(20 * 2.71828**(0.25*2))
        hp_bonus = math.floor(20 * 2.71828**(0.5))
        hp_bonus = math.floor(20 * 1.64872)
        hp_bonus = math.floor(32.9744)
        hp_bonus = 33
        """
        hp_bonus = math.floor(point_bonus * math.exp(0.25 * self.level))  # 25%
        mp_bonus = math.floor(point_bonus * math.exp(0.05 * self.level))  # 5%
        
        # Points
        self.hitpoints += hp_bonus
        self.magicpoints += mp_bonus
        
        # Primary
        self.strength += random.randint(0,5)
        self.dexterity += random.randint(0,5)
        self.vitality += random.randint(0,5)
        self.magic += random.randint(0,5)
        self.spirit += random.randint(0,5)
        self.luck += random.randint(0,5)
    
# Example usage
player_stats = Stats(experience=0, level=1, hitpoints=100, magicpoints=50,
                     strength=25, dexterity=10, vitality=25, magic=15,
                     spirit=5, luck=5, attack=10,hit_chance=10, defense=10,
                     evade=10, magic_attack=10, magic_defense=10, magic_dodge=10)

print(player_stats)
player_stats.experience = 817
player_stats.level_up()
print()
print(player_stats)
# player_stats.experience = 1838
# player_stats.level_up()
# print()
# print(player_stats)
# player_stats.experience = 3267
# player_stats.level_up()
# print()
# print(player_stats)
# player_stats.experience = 5103
# player_stats.level_up()
# print()
# print(player_stats)
    
def experience_table():
    """
    Keeping this for my sanity.
 
    (level/x**y) is the formula.
    x = more xp required per level (lower x = more xp required per level)
    y = how quickly required xp per level should increase 
    (higher y = larger gaps between levels)
    
    https://blog.jakelee.co.uk/converting-levels-into-xp-vice-versa/#:~:text=First%2C%20come%20up%20with%20a,%3D%20larger%20gaps%20between%20levels).
    """
    experience_requirement = {}
    x = 0.07 
    y = 2  
    max_level = 10

    # Default level
    experience_requirement[1] = 0
    
    for level in range(2, max_level + 1):
        experience_requirement[level] = round((level / x) ** y)
        # experience_requirement[level] = round(((level - 1) ** y) / x)
        
    for level, experience in experience_requirement.items():
        formatted_experience = "{:,}".format(experience)
        print(f'Level {level}: {formatted_experience} experience')
    
    total = sum(experience_requirement.values())
    format_total = "{:,}".format(total)
    print(f'You need: {format_total} total experience')

# experience_table()
