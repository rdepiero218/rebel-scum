import sys, time
import random

ship_names = [
    'Nebula\'s Edge',
    'Starfire Rapture',
    'Eclipse Voyager',
    'Iron Horizon',
    'Stellar Phoenix',
    'Celestial Fury',
    'Vortex Marauder',
    'Crimson Seraph',
    'Shadow\'s Embrace',
    'Obsidian Vanguard',
    'Galactic Reaver',
    'Titan\'s Wrath',
    'Voidstrider',
    'Astral Tempest',
    'Sunset Requiem',
    'Shadowstorm Cruiser',
    'Endeavor\'s Dawn',
    'Nova\'s Revenge',
    'Phantom Warden',
    'Cosmic Wraith'
]

ship_genders = [
    "Voidborn", 
    "Solarfluid", 
    "Quantumflux", 
    "Plasmatic",
    "Astrosexual", 
    "Unknowable", 
    "Nullgender", 
    "Mechafemme", 
    "Galactomale", 
    "Nebular", 
    "Hyperfluid", 
    "Anomaly", 
    "Singular", 
    "Interdimensional", 
    "Biocosmic", 
    "Spectral", 
    "Cryptoneutral", 
    "Timefluid",
    "Polymorphic"
]

ship_edges = [
    'Armor Plating', 
    'Bombs',
    'Cloaking Device', 
    'Starfighters', 
    'Runabout Shuttle', 
    'Jammers', 
    'Megaputer', 
    'Missiles', 
    'Passenger Amenities', 
    'Self Destruct', 
    'Super Thrusters'
]

ship_sizes = {
    'Yacht' : 'd4',
    'Corvette' : 'd6', 
    'Frigate' : 'd8', 
    'Crusier' : 'd10'
}

def ship_size_selector():
    '''Randomly select a SHIP SIZE'''
    size = random.choice(list(ship_sizes.keys()))
    
    die = ship_sizes[size]

    return [size, die]

def ship_name_selector():
    '''Randomly select a SHIP SIZE'''
    ship_name = random.choice(ship_names)

    return ship_name

def ship_gender_selector():
    '''Randomly select a GENDER'''
    gender = random.choice(ship_genders)

    return gender

def ship_edge_selector(count=3):
    '''Randomly selects SHIP EDGES'''

    ship_edge_list = random.sample(ship_edges, count)

    return ship_edge_list

def ship_generator():
    '''Randomly generates a SHIP'''
    ship = {
        'name' : ship_name_selector(),
        'size' : ship_size_selector()[0],
        'die' : ship_size_selector()[1],
        'gender' : ship_gender_selector(),
        'edges': ship_edge_selector()
    }

    return ship

def print_ship_sheet(ship):
    '''prints the ship character sheet'''
    speed = 0.5
    # print ship name
    border = 31*'-='+'-'
    print(border)
    print(f"▶︎{ship['name'].center(61,' ')}◀︎")
    print(border)
    # print 
    time.sleep(speed)
    print(f"Size:   {ship['size']} ({ship['die']})")
    time.sleep(speed)
    print(f"Gender: {ship['gender']}")

    border = """
╭------------------╮
\u2502   SHIP LOADOUT   \u2502
╰------------------╯
"""
    time.sleep(speed)
    print(border) 
    for edge in ship['edges']:
        time.sleep(speed)  
        print(f"     {edge}")

# Example list of ship features
ship_features = [
    "Laser Cannons", "Photon Shields", "Hyperdrive Engine",
    "Auto-Repair System", "Gravity Stabilizer", "Quantum AI Core", "Energy Deflectors",
    "Cargo Bay Expansion", "Advanced Sensors"
]

# # Progress bar with feature installation
# def build_ship(features):
#     total = len(features)
#     bar_length = 30
    
#     for i, feature in enumerate(features, start=1):
#         # Calculate progress
#         progress = i / total
#         bar = '=' * int(bar_length * progress)
#         spaces = ' ' * (bar_length - len(bar))
        
#         # Display progress bar with feature name
#         sys.stdout.write(f"\rBuilding Ship: [{bar}{spaces}] {int(progress * 100)}% — Installing: {feature}     ")
#         sys.stdout.flush()
        
#         time.sleep(0.5)  # Simulate time taken to install each feature
    
#     sys.stdout.write("\033[K")  # ANSI escape code to clear the line
#     sys.stdout.flush()
#     # print("\nShip construction complete!")

# # Randomly generate ship features (adjust count as needed)
# selected_features = random.sample(ship_features, k=7)
# build_ship(selected_features)
# sys.stdout.write("\033[K")  # ANSI escape code to clear the line
# sys.stdout.flush()
# print(2*'\n')
# print('print the next line here!')
# # print(2*'\n')

# # Example list of ship features
ship_features = [
    "Laser Cannons", "Photon Shields", "Hyperdrive Engine", "Cloaking Device",
    "Auto-Repair System", "Gravity Stabilizer", "Quantum AI Core", "Energy Deflectors",
    "Cargo Bay Expansion", "Advanced Sensors"
]

# # Funny ship genders inspired by No Man's Sky vibes
# ship_genders = [
#     "Voidborn", "Solarfluid", "Quantumflux", "Plasmatic", "Astrosexual", "Unknowable", 
#     "Nullgender", "Etherbound", "Mechafemme", "Galactomale", "Nebular", "Hyperfluid", 
#     "Cosmoflux", "Anomaly", "Gravitic", "Aetherform", "Photonkind", "Singular", 
#     "Interdimensional", "Biocosmic", "Spectral", "Cryptogender", "Starweaver", 
#     "Dark Matter Enthusiast", "Entropy's Favorite", "Timefluid", "Extradimensional", 
#     "Warpkin", "Echoform", "Polymorphic"
# ]

# Progress bar with feature installation

# def build_ship(features, gender):
#     total = len(features)
#     bar_length = 30
    
#     print(f"Assigning ship gender... ✅ {gender}\n")
#     time.sleep(1)  # Dramatic pause for the gender reveal
    
#     for i, feature in enumerate(features, start=1):
#         # Calculate progress
#         progress = i / total
#         bar = '=' * int(bar_length * progress)
#         spaces = ' ' * (bar_length - len(bar))
        
#         # Display progress bar with feature name
#         sys.stdout.write(f"\rBuilding Ship: [{bar}{spaces}] {int(progress * 100)}% — Installing: {feature}")
#         sys.stdout.flush()
        
#         time.sleep(0.5)  # Simulate time taken to install each feature

#     print("\nShip construction complete!")

# # Randomly generate ship features and gender
# selected_features = random.sample(ship_features, k=7)
# selected_gender = random.choice(ship_genders)

# # Build the ship!
# build_ship(selected_features, selected_gender)


ship_traits = [
    "Turbocharged Ego Core", 
    "AI Personality Matrix", 
    "Infinite Cup Holder Capacity", 
    "Quantum Beard Generator", 
    "Mood-Based Hull Colors", 
    "Celestial Karaoke System", 
    "Gravitationally Confused Thrusters", 
    "Parallel Universe Detector",
    'Profanity Translation Matrix',
    'AI Sarcasm Subroutines'
]

## VERB OPTIONS

building_words = ['Constructing', 'Creating', 'Erecting', 'Assembling', 'Developing', 'Forming', 'Fabricating', 'Establishing']
adjusting_words = ['Modifying', 'Altering', 'Tweaking', 'Calibrating', 'Fine-tuning', 'Swapping', 'Refining', 'Tailoring']
installing_words = ['Implementing', 'Mounting', 'Deploying', 'Integrating', 'Enabling', 'Configuring', 'Positioning']

ship_building_words = [building_words, adjusting_words, installing_words]

def ship_builder(gender, edges):

    traits = random.sample(ship_traits, k=3)

    features = ship_features + edges # adds ship edges for extra fun in screen printout

    total = len(features)

    bar_length = 30
    
    for i, feature in enumerate(features, start=1):
        # Calculate progress
        progress = i / total
        bar = '=' * int(bar_length * progress)
        spaces = ' ' * (bar_length - len(bar))
        
        # Display progress bar with feature name
        sys.stdout.write(f"\rBuilding Ship: [{bar}{spaces}] {int(progress * 100)}% — Installing: {feature} {8*' '}")
        sys.stdout.flush()
        
        time.sleep(0.5)  # Simulate time taken to install each feature
    print('\n\n')
    # Assign gender and other funny traits
    print(f"....Assigning ship gender... ✅ {gender}")
    time.sleep(1)
    
    # print("Assigning additional quirky features:")
    i = 0
    for trait in random.sample(traits, k=3):
        
        print(f"{4*'.'}{random.choice(ship_building_words[i])} {trait}")
        i += 1
        time.sleep(0.5)


def main():
    ship = ship_generator()
    print(2*'\n')
    # Build the ship!
    ship_builder(ship['gender'], ship['edges'])
    print(2*'\n')
    # print('Another line here')
    # print(2*'\n')
    print_ship_sheet(ship)
    print(2*'\n')
    

if __name__ == "__main__":
    main()



### -----------------------------------------

###### TESTING GARBAGE

# def overwrite_message(message, sleep_time=0.5):
#     sys.stdout.write(message)
#     sys.stdout.flush()
#     time.sleep(sleep_time)
#     # Move the cursor back to the start of the message and clear it
#     sys.stdout.write('\r' + ' ' * len(message) + '\r')
#     sys.stdout.flush()

# # # Example usage
# # overwrite_message('Loading...')
# # time.sleep(1)
# # overwrite_message('Still loading...')
# # time.sleep(1)
# # overwrite_message('Done!')

# for i in range(101):
#     overwrite_message(f'Progress: {i}%')
#     time.sleep(0.1)
# overwrite_message('Finished!')

# def blink_cursor(stdscr):
#     curses.curs_set(1)  # Make cursor visible initially
#     while True:
#         time.sleep(0.5)
#         curses.curs_set(0)  # Hide cursor
#         stdscr.refresh()
#         time.sleep(0.5)
#         curses.curs_set(1)  # Show cursor
#         stdscr.refresh()

# if __name__ == '__main__':
#     curses.wrapper(blink_cursor)

# import sys
# import time

# def overwrite_part_of_message(message, overwrite_text, start_pos, sleep_time=0.5):
#     sys.stdout.write(message)
#     sys.stdout.flush()
#     time.sleep(sleep_time)
#     # Move the cursor to the start position
#     sys.stdout.write('\r' + message[:start_pos])
#     # Write the new text
#     sys.stdout.write(overwrite_text)
#     sys.stdout.flush()

# # Example usage
# message = 'Building your ship . . . .'
# start = 18
# print('Building your ship . . .')
# for i in range(3):
#     overwrite_part_of_message(message, '. . . .', start_pos=start)
#     print(i)
#     time.sleep(1)
#     overwrite_part_of_message(message, 5*' ', start_pos=start)
#     # overwrite_part_of_message(message, '. . . .', start_pos=start)
#     # time.sleep(1)
#     # overwrite_part_of_message(message, '. . . .', start_pos=start)

# print(5*'\n')

# def overwrite_part_of_message(message, overwrite_text, start_pos, sleep_time=0.5):
#     sys.stdout.write(message)
#     sys.stdout.flush()
#     time.sleep(sleep_time)
#     # Move the cursor to the start position
#     sys.stdout.write('\r' + message[:start_pos] )
#     # Write the new text
#     sys.stdout.write(overwrite_text)
#     sys.stdout.flush()

# # Example usage
# message = 'Loading... Please wait.'
# overwrite_part_of_message(message, 'Working........', 10)
# time.sleep(1)
# overwrite_part_of_message(message, 'Almost there...', 10)
# time.sleep(1)
# overwrite_part_of_message(message, 'Complete!......', 10)


# for i in range(5):
#     sys.stdout.write(f"Building your ship{'.' * (i+1)}\r")
#     sys.stdout.flush()
#     time.sleep(1)

# sys.stdout.write("\033[K")  # ANSI escape code to clear the line
# sys.stdout.flush()
# # sys.stdout.flush()
# print(2*'\n')
# print('print the next line here!')
# # print(2*'\n')

# import random