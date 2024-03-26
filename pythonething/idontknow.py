"""
fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric
"""
class pokemon:
    def __init__(self, element, attack, defense, hp):
        self.element = element
        self.attack = attack
        self.defence = defense
        self.hp = hp

def calculate_damage(atk_element, def_element, atk_damage, def_points):
    effectiveness = 1
    
    if(atk_element == "fire" and def_element == "grass"):
        effectiveness = 2
    elif (atk_element == "grass" and def_element == "fire"):
        effectiveness = 0.5
    elif (atk_element == "fire" and def_element == "water"):
        effectiveness = 0.5
    elif (atk_element == "water" and def_element == "fire"):
        effectiveness = 2
    elif (atk_element == "water" and def_element == "grass"):
        effectiveness = 0.5
    elif (atk_element == "grass" and def_element == "water"):
        effectiveness = 2
    elif (atk_element == "water" and def_element == "electric"):
        effectiveness = 0.5
    elif (atk_element == "electric" and def_element == "water"): 
        effectiveness = 2
    
    damage = 50 * (atk_damage / def_points) * effectiveness

    return damage

pikatchu = pokemon("electric", 100, 80, 200)
squirtle = pokemon("water", 100, 80, 200)

calculate_damage(pikatchu.element, squirtle.element, pikatchu.attack, squirtle.attack)

calculate_damage("fire", "water", 100, 100) > 25

calculate_damage("grass", "fire", 35, 5) > 175

calculate_damage("electric", "fire", 100, 100) > 50

print(pikatchu.attack, squirtle.attack)
