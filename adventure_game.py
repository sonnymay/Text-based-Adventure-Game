def main():
    print("Welcome to the Forest Adventure Game!")
    print("You find yourself in a dark forest.")
    print("Can you find the treasure without being caught by the monster?")

    playing = True

    while playing:
        choice = input("Would you like to [p]lay or [q]uit? ").lower()

        if choice == "q":
            playing = False
        elif choice == "p":
            play_game()
        else:
            print("Invalid choice. Please enter 'p' or 'q'.")
        
def play_game():
    print("\nYou are at the edge of a dark forest.")
    print("You can see a treasure chest at the top of the hill in the distance.")
    
    action = input("Do you want to go [i]nside the forest or walk [a]round it? ").lower()

    if action == "i":
        inside_forest()
    elif action == "a":
        around_forest()
    else:
        print("Invalid choice.")

def inside_forest():
    print("\nYou find yourself deep inside the forest.")
    print("You don’t see the treasure chest anymore, but you hear growling noises.")
    
    action = input("Do you want to [c]limb a tree or [r]un back? ").lower()

    if action == "c":
        print("\nYou climbed the tree.")
        print("From here you see the treasure chest and a monster guarding it.")
        print("You wait till the monster leaves and then grab the treasure!")
        print("Congratulations! You win!")
    elif action == "r":
        print("\nYou run back to the edge of the forest.")
        play_game()
    else:
        print("Invalid choice.")

def around_forest():
    print("\nYou are walking around the forest.")
    print("The monster sees you and starts chasing.")
    
    action = input("Do you want to [r]un or [f]ight? ").lower()

    if action == "r":
        print("\nYou run as fast as you can.")
        print("The monster is right behind you. Suddenly, you find a sword on the ground.")
        print("You pick it up and fight the monster. You defeat the monster and find the treasure.")
        print("Congratulations! You win!")
    elif action == "f":
        print("\nYou decide to fight, but you have nothing to fight with.")
        print("The monster easily catches you. Game Over!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()