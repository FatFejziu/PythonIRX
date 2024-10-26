class Vertebrate:
    def __init__(self, backbone=True): #Backbone is true by default
        self.has_backbone=backbone
    def vertebrate_info(self):
        print(f"Vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat="Water"):
        self.habitat=habitat
    def aquatic_info(self):
        print(f"Aquatic animals live in water")


class Fish(Vertebrate, Aquatic):
    def __init__(self, species, backbone=True, habitat="Water"):
        super().__init__(backbone=backbone)
        self.habitat=habitat
        self.species=species

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print(f"The fish is swimming")

goldfish=Fish("Gold Fish")
print(goldfish.has_backbone)
goldfish.swim()