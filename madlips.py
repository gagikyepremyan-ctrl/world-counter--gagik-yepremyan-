import random

def get_valid_input(prompt, validation_type):
    """
    Helper function to ensure user input meets specific criteria.
    """
    # Allowed list for measures of time
    allowed_time = [
        "millisecond", "milliseconds", "second", "seconds", "minute", "minutes", 
        "hour", "hours", "day", "days", "week", "weeks", "month", "months", 
        "year", "years", "decade", "decades", "century", "centuries"
    ]

    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        # 1. Time Measure Validation
        if validation_type == "time":
            if user_input.lower() in allowed_time:
                return user_input
            print("Invalid measure! Use units like millisecond, minute, hour, year, or century.")

        # 2. Number Validation
        elif validation_type == "number":
            if user_input.isdigit():
                return user_input
            print("Invalid input. Please enter a number (digits only).")

        # 3. Suffix Validation (-ing)
        elif validation_type == "ing":
            if user_input.lower().endswith("ing") and user_input.replace(" ", "").isalpha():
                return user_input
            print("Invalid input. The word must end in '-ing'.")

        # 4. Suffix Validation (-ly)
        elif validation_type == "ly":
            if user_input.lower().endswith("ly") and user_input.replace(" ", "").isalpha():
                return user_input
            print("Invalid input. The word must end in '-ly'.")

        # 5. General Text Validation (Nouns, Adjectives, etc.)
        elif validation_type == "alpha":
            if all(x.isalpha() or x.isspace() for x in user_input):
                return user_input
            print("Invalid input. Please use letters only.")

def madlibs_story(template):
    print(f"\n--- Starting Template {template} ---\n")
    
    if template == 1:
        number = get_valid_input("Type a number: ", "number")
        measure_of_time = get_valid_input("Type a measure of time (ex. minute, hour, year): ", "time")
        mode_of_transportation = get_valid_input("Type a mode of transportation: ", "alpha")
        adjective = get_valid_input("Type an adjective: ", "alpha")
        adjective2 = get_valid_input("Type another adjective: ", "alpha")
        noun = get_valid_input("Type a noun: ", "alpha")
        color = get_valid_input("Type a color: ", "alpha")
        part_of_the_body = get_valid_input("Type a part of the body: ", "alpha")
        verb = get_valid_input("Type a verb: ", "alpha")
        number2 = get_valid_input("Type another number: ", "number")
        noun2 = get_valid_input("Type another noun: ", "alpha")
        noun3 = get_valid_input("Type another noun: ", "alpha")
        verb2 = get_valid_input("Type another verb: ", "alpha")
        noun4 = get_valid_input("Type another noun: ", "alpha")
        adjective3 = get_valid_input("Type another adjective: ", "alpha")
        silly_word = get_valid_input("Type a silly word: ", "alpha")
        noun5 = get_valid_input("Type another noun: ", "alpha")

        print(f"""
        It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. 
        The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. 
        There are nurses here who have {color} {part_of_the_body}. If someone wants to come into my room I told them 
        that they have to {verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor 
        and they were wearing a {noun3} on their {part_of_the_body}. I heard that all doctors {verb2} {noun4} every 
        day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!
        """)

    elif template == 2:
        proper_noun = get_valid_input("Type a proper noun: ", "alpha")
        noun = get_valid_input("Type a noun: ", "alpha")
        adjective_feeling = get_valid_input("Type an adjective feeling: ", "alpha")
        feeling = get_valid_input("Type a feeling: ", "alpha")
        animal = get_valid_input("Type an animal: ", "alpha")
        verb2 = get_valid_input("Type another verb: ", "alpha")
        color = get_valid_input("Type a color: ", "alpha")
        ending_in_ing = get_valid_input("Type a word ending in -ing: ", "ing")
        adverb = get_valid_input("Type an adverb: ", "alpha")
        ending_in_ly = get_valid_input("Type a word ending in -ly: ", "ly")
        measure_of_time = get_valid_input("Type a measure of time (ex. minute, hour, year): ", "time")
        number = get_valid_input("Type a number: ", "number")
        silly_word = get_valid_input("Type a silly word: ", "alpha")
        noun2 = get_valid_input("Type another noun: ", "alpha")

        print(f"""
        This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. 
        I am so {adjective_feeling} to {feeling} in a tent. I am worried we might see a(n) {animal}, 
        I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. 
        I have heard that the {color} lake is great for {ending_in_ing}. Then we will {adverb} hike through 
        the forest for {ending_in_ly} {measure_of_time}. At night we will tell {number} {silly_word} stories 
        and roast {noun2} around the campfire!!
        """)

    elif template == 3:
        proper_noun = get_valid_input("Type a proper noun: ", "alpha")
        persons_name = get_valid_input("Type a person's name: ", "alpha")
        color = get_valid_input("Type a color: ", "alpha")
        animal = get_valid_input("Type an animal: ", "alpha")
        place = get_valid_input("Type a place: ", "alpha")
        adjective2 = get_valid_input("Type another adjective: ", "alpha")
        magical_creature = get_valid_input("Type a magical creature: ", "alpha")
        plural = get_valid_input("Type a plural noun: ", "alpha")
        magical_creature2 = get_valid_input("Type another magical creature: ", "alpha")
        plural2 = get_valid_input("Type another plural noun: ", "alpha")
        room_in_a_house = get_valid_input("Type a room in a house: ", "alpha")
        noun2 = get_valid_input("Type another noun: ", "alpha")
        plural3 = get_valid_input("Type another plural noun: ", "alpha")
        adjective4 = get_valid_input("Type another adjective: ", "alpha")
        plural4 = get_valid_input("Type another plural noun: ", "alpha")
        number = get_valid_input("Type a number: ", "number")
        measure_of_time = get_valid_input("Type a measure of time (ex. minute, hour, year): ", "time")
        ending_in_ing = get_valid_input("Type a word ending in -ing: ", "ing")
        adjective5 = get_valid_input("Type another adjective: ", "alpha")
        noun5 = get_valid_input("Type another noun: ", "alpha")

        print(f"""
        Dear {proper_noun}, I am writing to you from {persons_name}'s castle in an enchanted forest. 
        I found myself here one day after going for a ride on a {color} {animal} in {place}. 
        There are {adjective2} {magical_creature} and {plural} {magical_creature2} here! 
        In the {plural2} there is a pool full of {room_in_a_house}. I fall asleep each night on a 
        {noun2} of {plural3} and dream of {adjective4} {plural4}. It feels as though I have lived here 
        for {number} {measure_of_time}. I hope one day you can visit, although the only way to get 
        here now is {ending_in_ing} on a {adjective5} {noun5}!!
        """)

# --- Main Selection Logic ---
user_selection = input("Type 1, 2, or 3 to select a template (or any other key for random): ").strip()

if user_selection in ['1', '2', '3']:
    final_template = int(user_selection)
else:
    final_template = random.randint(1, 3)
    print(f"Non-numeric or invalid input detected. Randomly selected template: {final_template}")

madlibs_story(final_template)
