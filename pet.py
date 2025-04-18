class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # 0 = full, 10 = very hungry
        self.energy = 8  # 0 = tired, 10 = fully rested
        self.happiness = 6  # 0 = sad, 10 = very happy
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 4
            self.happiness += 1
        else:
            print(f"{self.name} is not hungry!")

    def sleep(self):
        if self.energy < 10:
            self.energy += 6
        else:
            print(f"{self.name} is not tired!")

    def play(self):
        if self.energy >= 4:
            self.energy -= 3
            self.happiness += 2
            self.hunger += 1
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        status = (
            f"Name: {self.name}\n"
            f"Hunger: {self.hunger}\n"
            f"Energy: {self.energy}\n"
            f"Happiness: {self.happiness}\n"
        )
        print(status)

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")