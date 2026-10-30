import sys
import time
import random


def type_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def press_enter():
    input("\n[Press Enter to continue...]\n")


def play_game():
    inventory = []

    # --- RANDOM KILLER SELECTION ---
    # Options: "Thomas", "Victoria", "Evelyn", or "Detective"
    suspects = ["Thomas", "Victoria", "Evelyn", "Detective"]
    actual_killer = random.choice(suspects)

    # --- INTRO ---
    type_text("==================================================")
    type_text("         THE MIDNIGHT MASK: RANDOMIZED            ")
    type_text("==================================================")
    type_text("A torrential downpour isolates Blackwood Manor from the outside world.")
    type_text("Lord Arthur Blackwood has just been found dead in his locked study.")
    type_text("As Lead Detective, you must investigate the estate and uncover the truth.")

    if actual_killer == "Detective":
        type_text("\n[Note: You have a throbbing headache and a strange gap in your memory from earlier tonight...]")

    press_enter()

    # --- INVESTIGATION PHASE ---
    investigation_points = 3

    while investigation_points > 0:
        print(f"\n--- INVESTIGATION PHASE ({investigation_points} actions remaining) ---")
        print("1. Search the Locked Study (Crime Scene)")
        print("2. Search the Servants' Quarters (Butler's Domain)")
        print("3. Inspect the Greenhouse (Lady Victoria's Spot)")
        print("4. Check the Wine Cellar (Dr. Evelyn's Spot)")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            if "Study Scanned" not in inventory:
                type_text("\nYou examine the study. Lord Blackwood was struck down at his desk.")

                if actual_killer == "Thomas":
                    type_text("You find a bloody apron thread caught on the desk drawer.")
                    inventory.append("Bloody Thread")
                elif actual_killer == "Victoria":
                    type_text("You find a torn inheritance ledger cutting Victoria out of the will.")
                    inventory.append("Torn Ledger")
                elif actual_killer == "Evelyn":
                    type_text("You smell bitter almonds on Lord Blackwood's glass—cyanide poison.")
                    inventory.append("Poison Residue")
                elif actual_killer == "Detective":
                    type_text("You find a spare key to the locked door tucked into your OWN coat pocket!")
                    inventory.append("Spare Study Key")

                inventory.append("Study Scanned")
                investigation_points -= 1
            else:
                type_text("\nYou've already thoroughly searched the study.")

        elif choice == "2":
            if "Butler Checked" not in inventory:
                type_text("\nYou search the servants' quarters.")
                if actual_killer == "Thomas":
                    type_text("In Thomas's locker, you find a hidden stash of stolen manor jewels and a heavy club.")
                    inventory.append("Stolen Jewels")
                else:
                    type_text(
                        "Thomas's quarters are tidy. You find a letter showing his unwavering loyalty to the estate.")
                inventory.append("Butler Checked")
                investigation_points -= 1
            else:
                type_text("\nYou've already searched the servants' quarters.")

        elif choice == "3":
            if "Greenhouse Checked" not in inventory:
                type_text("\nYou inspect the greenhouse.")
                if actual_killer == "Victoria":
                    type_text("You find Victoria's muddy gloves hidden beneath a stack of flower pots.")
                    inventory.append("Muddy Gloves")
                else:
                    type_text("The greenhouse is quiet. Just rare orchids and gardening tools.")
                inventory.append("Greenhouse Checked")
                investigation_points -= 1
            else:
                type_text("\nYou've already searched the greenhouse.")

        elif choice == "4":
            if "Cellar Checked" not in inventory:
                type_text("\nYou check the wine cellar.")
                if actual_killer == "Evelyn":
                    type_text("You find an empty vial of medical-grade poison hidden behind a wine rack.")
                    inventory.append("Empty Vial")
                else:
                    type_text("Dr. Evelyn is sipping wine. Her hands are steady and calm.")
                inventory.append("Cellar Checked")
                investigation_points -= 1
            else:
                type_text("\nYou've already checked the wine cellar.")
        else:
            print("Invalid input. Choose a number between 1 and 4.")

        press_enter()

    # --- THE CLIMAX ---
    type_text("\n--- THE FINAL ACCUSATION ---")
    type_text("The grand clock strikes midnight. Lightning flashes outside.")
    type_text("You gather everyone in the parlor to announce your final verdict.")

    print("\nWho do you accuse?")
    print("1. Accuse Butler Thomas")
    print("2. Accuse Lady Victoria")
    print("3. Accuse Dr. Evelyn")
    print("4. Confess: Accuse YOURSELF (The Detective)")
    print("5. Refuse to accuse anyone (Give Up)")

    final_choice = input("\nEnter your choice (1-5): ").strip()

    # Mapping choices to suspect tags
    choice_map = {
        "1": "Thomas",
        "2": "Victoria",
        "3": "Evelyn",
        "4": "Detective"
    }

    accused = choice_map.get(final_choice, "None")

    # --- ENDING LOGIC ---
    if accused == "Detective":
        if actual_killer == "Detective":
            type_text("\n[BAD ENDING 1: THE TWIST - YOU ARE THE KILLER]")
            type_text("Memories flood back to you... Lord Blackwood was blackmailing you over a past case.")
            type_text("You used the spare key in your pocket to enter his room, commit the act, and lock up.")
            type_text("You place your badge on the table and surrender yourself to the authorities.")
        else:
            type_text("\n[BAD ENDING 2: MADNESS & FALSE CONFESSION]")
            type_text("Overwhelmed by exhaustion and paranoia, you confess to a crime you didn't commit.")
            type_text("The real killer watches silently in relief as you are led away in handcuffs.")

    elif accused == actual_killer:
        if actual_killer == "Thomas":
            type_text("\n[GOOD ENDING 1: THE BUTLER DID IT]")
            type_text(
                "You present your evidence. Thomas breaks down, admitting he killed Lord Blackwood over stolen estate wealth.")
            type_text("Great work, Detective! Case solved.")
        elif actual_killer == "Victoria":
            type_text("\n[GOOD ENDING 2: ARISTOCRATIC GREED]")
            type_text(
                "Confronted with the evidence, Lady Victoria's facade collapses. She confesses to taking out her uncle before he disinherited her.")
            type_text("Justice is served!")
        elif actual_killer == "Evelyn":
            type_text("\n[GOOD ENDING 3: MEDICAL MALPRACTICE]")
            type_text(
                "Dr. Evelyn attempts to bluff, but your findings corner her. She admits to poisoning Blackwood to cover up a medical scandal.")
            type_text("Flawless deduction!")

    elif final_choice in ["1", "2", "3"]:
        type_text("\n[BAD ENDING 3: WRONGFUL ACCUSATION]")
        type_text(f"You accuse {accused}, but your argument lacks solid proof!")
        type_text(
            "They produce an airtight defense. The true killer slips away into the night while your reputation is destroyed.")

    else:
        type_text("\n[BAD ENDING 4: INDECISION]")
        type_text(
            "You fail to make a decision. The lights flicker out, chaos erupts, and the killer escapes in the storm.")


if __name__ == "__main__":
    play_game()