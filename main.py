# main.py

from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet(name="fluffy")

    # Display initial status
    my_pet.get_status()

    # Interact with the pet
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    # Display status after interactions
    my_pet.get_status()

    # Train the pet
    my_pet.train("sit")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
