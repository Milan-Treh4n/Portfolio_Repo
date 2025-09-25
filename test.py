class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        if self.species.lower() == "dog":
            return f"{self.name} says: Woof!"
        elif self.species.lower() == "cat":
            return f"{self.name} says: Meow!"
        else:
            return f"{self.name} makes a sound."

    def __str__(self):
        return f"{self.name} the {self.species}"

# Example usage
if __name__ == "__main__":
    pet1 = Pet("Buddy", "Dog")
    pet2 = Pet("Whiskers", "Cat")
    print(pet1)
    print(pet1.speak())
    print(pet2)
    print(pet2.speak())