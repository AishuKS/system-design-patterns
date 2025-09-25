from abc import ABC, abstractmethod
import copy
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Enemy(Prototype):
    def __init__(self, name, health, speed, weapon):
        self.name = name
        self.health = health
        self.speed = speed
        self.weapon = weapon
    
    def clone(self):
        return copy.deepcopy(self)
    # it ensures nested objects are cloned too

    def __str__(self):
        return (f"Enemy: {self.name}, Health: {self.health}, Speed: {self.speed}, Weapon: {self.weapon}")
    #special method in python to tell how to represent an object 
    #without str the output will be like <__main__.Enemy object at 0x00000123>

orc_prototype = Enemy("Orc", 100, 5, "Axe")
fast_arc = orc_prototype.clone()
fast_arc.name = "Fast Orc"
fast_arc.speed = 7

strong_arc = orc_prototype.clone()
strong_arc.name = "Strong Orc"
strong_arc.health = 120

print("Fast Orc:", fast_arc)