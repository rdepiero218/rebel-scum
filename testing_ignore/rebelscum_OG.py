
'''Script that generates random characters, ship,
quest prompt, and dice roller for use in Rebel Scum, 
a TTRPG created by Chris O'Neil at 9th Level Games'''

## Written by Regene DePiero, 2025

import sys, time, textwrap
import random


## REBEL SCUM specifc character traits

# The 4 roles and their associated die
roles = {
    'Expert' : 'd4',
    'Vanguard' : 'd6',
    'Fighter' : 'd8',
    'Tank' : 'd10'
}

# Giant fancy nested dictionary that defines specific edges and traits for specific classes.
character_classes = {
    'The Renegade': {
        'flavor text': 'You have turned your back on the Killstar Republick.\n         As a RENEGADE you are considered a TRAITOR by your former compatriots.',
        'shining star' : 'As the RENEGADE, you seek Redemption',
        'burn star' : 'brings justice to the worlds.',
        'edges' : ['Aristocrat', 'Assassin', 'Bureaucrat', 'Driver', 'Intelligence', 'Officer', 'Plutocrat', 'Trooper'],
    },
    'The Revolutionary': {
        'flavor text': 'You are the backbone of the Rebellion.\n         You\'re a soldier invested in the overthrow of the government.',
        'shining star': 'As the REVOLUTIONARY, you fight for CHANGE.',
        'burn star': 'changes the statis quo',
        'edges': ['Academic', 'Aristocrat', 'Commando', 'Firebrand', 'Mechanic', 'Organizer', 'Pilot', 'Spy'],
    },
    'The Robot': {
        'flavor text': 'According to the Killstar Republick, you are just a tool, a possession.\n         You have no rights. You are just a machine.',
        'shining star': 'As the ROBOT, you seek SELF',
        'burn star': 'is an expression of self',
        'edges': ['Assistant', 'Bucket', 'Fixer', 'Killer', 'Lifter', 'Megaputer', 'Spacer', 'Watchdog'],
    },
    'The Rogue': {
        'flavor text': 'You\'re not in this for the revolution - or that\'s what you tell people.\n         You are a free-wheeling, free-dealing individual that got caught up in the fight.',
        'shining star': 'As the ROGUE, you burn for FREEDOM',
        'burn star': 'frees someone',
        'edges': ['Crimer', 'Coyote', 'Duelist', 'Gambler', 'Coder', 'Racer', 'Thief', 'Smuggler'],
    },
    'The Ronin': {
        'flavor text': 'You are an outlaw warrior monk, a member of the fallen Amurai Warriors.\n         You are well trained in the use of LAZER SWORDS and mystical space magic.',
        'shining star': 'As the RONIN, you quest for PEACE.',
        'burn star': 'brings peace to a situation',
        'edges': ['Clairvoyant', 'Diplomat', 'General', 'Historian', 'Swordfighter', 'Teacher', 'Telekinetic', 'Telepath'],
    },
}

#---------------------------------------
## Generic Character Traits for Sci-Fi
#---------------------------------------
## first names
first_names = ['Kael', 'Zyra', 'Orin', 'Vexis', 'Taryn']

## last names
last_names = ['Draven', 'Quen', 'Vorr', 'Syndra', 'Kastix']

# standard genders and some taken from No Man's Sky
genders = ['male', 'female', 'non-binary', 'orthogonal', 'indeterminate', 'unknown']


###-----------------------------
### UTILITY FUNCTIONS
###-----------------------------

## Utility function to slow print to screen
def slow_print(str, sleep_time=3./90):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(sleep_time)



def custom_wrap(text, width=65, indent=5):
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="",  # No indent for the first line
        subsequent_indent=" " * indent  # Indent second and subsequent lines
    )
    return wrapper.fill(text)

def wrap_with_blank_lines(text, width=65):
    wrapped_lines = []
    for paragraph in text.split('\n'):
        if paragraph.strip():  # Wrap non-blank lines
            wrapped_lines.append(textwrap.fill(paragraph, width=width))
        else:  # Preserve blank lines
            wrapped_lines.append('')
    return '\n'.join(wrapped_lines)

## Block of functions to randomly select character traits



def name_generator():
    '''Randomly selects a first and last name'''
    character_name = random.choice(first_names) + ' ' + random.choice(last_names)

    return character_name

def role_selector():
    '''Randomly select a ROLE'''
    role = random.choice(list(roles.keys()))
    
    die = roles[role]

    return [role, die]

def gender_selector():
    '''Randomly select a GENDER'''
    gender = random.choice(genders)

    return gender

def class_selector():

    char_class = random.choice(list(character_classes.keys()))

    return char_class

def edge_selector(char_class, count=3):
    '''Randomly select edges from selected class'''
    
    edge_list = random.sample(list(character_classes[char_class]['edges']), count)

    return edge_list

def character_generator():
    # randomly select initial traits
    character = {
        'name' : name_generator(),
        'role' : role_selector()[0],
        'class' : class_selector(),
        'die' : role_selector()[1],
        'gender' : gender_selector(),
    }

    # add additional traits that depend on the class
    character['edges'] = edge_selector(character['class'])
    character['profile'] = character_classes[character['class']]['flavor text']
    character['shining star'] = character_classes[character['class']]['shining star']
    character['burn star'] = character_classes[character['class']]['burn star']
    
    return character
    
def print_character_sheet(character):
    '''prints the character sheet'''
    print(30*'~')
    print(f"{character['name']} - {character['class']}")
    print(30*'~')
    print(f"Role:   {character['role']} ({character['die']})")
    print(f"Gender: {character['gender']}")
    print('')
    print(f"PROFILE: { character['profile'] }")
    print('')
    print(f"STAR: {character['shining star']}")
    print(f"      Burn a star to succeed whenever the result {character['burn star']}")
    print()
    print(f"EDGES: ")

    for edge in character['edges']:
        print(f"    {edge}")


def crew_generator(player_count):
    '''Generates multiple characters to form a crew'''
    # num_players = int(input('Enter the number of players'))

    crew = []
    
    if player_count < 5:
        
        class_list = []
        
        while len(crew) < player_count:
            # for i in range(player_count):
            crew_member = character_generator()
            
            if crew_member['class'] not in class_list:
                crew.append(crew_member)
                class_list.append(crew_member['class'])
    else:
        # if more than 5 players, no one cares if there are repeats
        for i in range(player_count):
            
            crew.append(character_generator())
            
    for member in crew:
        
        print_character_sheet(member)
        time.sleep(1)
        print('')
        
    return crew

# SHIP BUILDER

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

def ship_edge_selector(count=3):
    '''Randomly selects SHIP EDGES'''

    ship_edge_list = random.sample(ship_edges, count)

    return ship_edge_list

def ship_builder():
    '''Randomly generates a SHIP'''
    ship = {
        'name' : ship_name_selector(),
        'size' : ship_size_selector()[0],
        'die' : ship_size_selector()[1],
        'gender' : gender_selector(),
        'edges': ship_edge_selector()
    }

    return ship

def print_ship_sheet(ship):
    '''prints the ship character sheet'''
    border = 31*'-='+'-'
    print(border)
    # print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    # print(30*'▶︎◀︎')
    print(f"▶︎{ship['name'].center(61,' ')}◀︎")
    print(border)
    # print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f"Size:   {ship['size']} ({ship['die']})")
    print(f"Gender: {ship['gender']}")

    for edge in ship['edges']:
        print(f"     {edge}")

###===============================
### QUEST GENERATOR
###===============================

## Create a template statement
adjectives = [
    'mysterious', 'grizzled', 'enigmatic', 'robotic', 'ancient', 'fierce', 'honorable',
    'stoic', 'galactic', 'alien', 'wounded', 'intelligent', 'charming', 'ruthless', 'shrewd'
]

npc_types = [
    'Bounty Hunter', 
    'Holo-Engineer', 
    'Smuggler', 
    'Rebel Spy', 
    'Space Pirate', 
    'Amurai Warrior',
    'Imperial Officer', 
    'Mercenary', 
    'Diplomat', 
    'Pilot', 
    'Warlord',
    'Scientist', 
    'Hacker', 
    'Droid', 
    'Merchant'
]

objectives = [
    'retrieve the lost artifact', 
    'infiltrate an enemy base', 
    'disable a space station defenses',
    'negotiate with an alien faction', 
    'repair a damaged ship', 
    'steal secret blueprints',
    'rescue a kidnapped senator', 
    'extract a valuable resource', 
    'deliver crucial data',
    'defend a convoy from pirates', 
    'capture a fugitive', 
    'decrypt an ancient text',
    'retrieve a prototype weapon', 
    'investigate a mysterious distress signal', 
    'escort a diplomat'
]

locations = [
    'an Abandoned Space Station',
    'an Alien Ruins',
    'an Asteroid Belt',
    'a Bio-Dome Colony',
    'a Black Hole Perimeter',
    'a Cryo-Lab Facility',
    'a Deep Space Relay',
    'a Deserted Moon Base',
    'a Dimensional Rift',
    'a Floating Megacity',
    'a Galactic Core',
    'a Hidden Rebel Outpost',
    'a Hyperdrive Repair Yard',
    'an Intergalactic Marketplace',
    'a Lost Planet',
    'a Nebula Research Station',
    'an Orbital Defense Platform',
    'a Quarantine Zone',
    'a Radiation Zone',
    'a Remote Mining Colony',
    'a Secret Military Bunker',
    'a Sentient AI Mainframe',
    'a Solar Observatory',
    'a Starship Graveyard',
    'a Subterranean Alien Hive',
    'a Terraforming Hub',
    'a Time Distortion Field',
    'an Underwater Research Lab',
    'a Warp Gate Nexus',
    'an Xeno-Biology Lab'
]

obstacles = [
    'a deadly asteroid field', 
    'an ambush by rival bounty hunters', 
    'a malfunctioning hyperdrive',
    'a treacherous pirate gang', 
    'an alien warlord', 
    'the Empire\'s heavy patrols', 
    'a dangerous nebula',
    'hostile wildlife', 
    'a malfunctioning droid', 
    'a deadly trap set by enemies', 
    'a collapsing space station',
    'a faction of rebels who oppose your mission', 
    'a fleet of Imperial Star Destroyers', 
    'a deadly bounty placed on your head', 
    'a deadly virus outbreak'
]

rewards = [
    'a large sum of credits', 
    'a rare starship upgrade', 
    'the location of a hidden planet',
    'an ancient relic of immense power', 
    'a valuable piece of technology', 
    'a fleet of loyal soldiers',
    'an exclusive contract', 
    'a dangerous weapon prototype', 
    'information about the galaxy\'s secrets',
    'a rare artifact with unknown abilities', 
    'access to a prestigious military rank', 
    'the promise of future alliances',
    'a mysterious alien ally', 
    'a powerful energy crystal', 
    'a high-ranking position in a faction'
]


def quest_generator():
    ## Create a template statement
    adjective=random.choice(adjectives)
    npc_type=random.choice(npc_types)
    objective=random.choice(objectives)
    location=random.choice(locations)
    obstacle=random.choice(obstacles)
    reward=random.choice(rewards)

    quest_prompt = f'''
A {adjective} {npc_type} has contacted you with an urgent request. They need you to {objective} in {location}, but beware — you will need to deal with {obstacle}. If you succeed, you will be rewarded with {reward}.
'''
    
    print(50*'-')
    print('INCOMING TRANSMISSION')
    print(50*'-')
    # return quest_prompt
    print(custom_wrap(quest_prompt, indent=0))
    # slow_print(wrap_with_blank_lines(quest_prompt, indent=5))

### Add dice roller

def print_header():
    header = """ 
        .______       _______ .______    _______  __         
        |   _  \     |   ____||   _  \  |   ____||  |        
        |  |_)  |    |  |__   |  |_)  | |  |__   |  |        
        |      /     |   __|  |   _  <  |   __|  |  |        
        |  |\  \----.|  |____ |  |_)  | |  |____ |  `----.   
        | _| `._____||_______||______/  |_______||_______|   
             _______.  ______  __    __  .___  ___.          
            /       | /      ||  |  |  | |   \/   |          
           |   (----`|  ,----'|  |  |  | |  \  /  |          
            \   \    |  |     |  |  |  | |  |\/|  |          
        .----)   |   |  `----.|  `--'  | |  |  |  |          
        |_______/     \______| \______/  |__|  |__|          
                                               
    """
    opening_msg = """
It is a dark time. BARON DEATHRAY and his KILLTROOPERS hunt down all dissenion from the evil KILLSTAR REPUBLICK. Fascism and terror rule the star system!

In the darkness, a motley band of revolutionaries, traitors, criminals, robots, and other REBEL SCUM are trying to fight back.

You are are our only hope...
"""
    
    border = '\n'+ 16*'--==' + '\n'
    print(border)
    print(header.center(80,' '))
    print(border)
    # print(10*'\u2022\u29BE\u2022\u2734')
    slow_print(wrap_with_blank_lines(opening_msg))
    # print('The adventures of the crew of the '.center(80,' '))
    print('')

def print_game(num_players):

    print('')
    # slow_print(f'Your ship and crew of {num_players} is ready!')
    print('')

    slow_print(f'Building your ship. . . . . ', sleep_time=5./90)
    time.sleep(1)
    print_ship_sheet(ship_builder())
    
    print('')
    # # print(70*'=')
    # print('CREW MANIFEST'.center(33, ' ').center(70,'='))
    # # print(70*'=')
    print(62*'-')
    # print('|'+62*' '+'|')
    print('|'+'CREW MANIFEST'.center(60, ' ')+'|')
    # print('|'+62*' '+'|')
    print(62*'-')
    print('')
    
    crew_generator(num_players)
    
    print('')

def main():

    print_header() 

    # print(quest_generator()) 
    

    
    # starting = True
    while True:
        time.sleep(1)
        print(40*'-')
        print('To obtain your ship and crew assignments,\nenter a number of players or q to QUIT')
        time.sleep(1)
        print('')
        response = input('Number of players: ')
        print(40*'-')
        print('')
        
        if response == 'q':
            print('')
            print(40*'-')
            print('See you next time!'.center(30, '*').center(30,' '))
            print(40*'-')
            playing = False
            break
        else:
            print_game(int(response))
            time.sleep(5)
            print(quest_generator())
            break


    # while playing:
        
    
    #     if response == 'q':
    #         print('')
    #         print(40*'-')
    #         print('See you next time!'.center(30, '*').center(30,' '))
    #         print(40*'-')
    #         playing = False
    #         break
    #     else:
    #         print_game(int(response))
    #         time.sleep(5)
    #         print(quest_generator())

    # while playing:
        
    #     time.sleep(1)
    #     print(40*'-')
    #     print('To obtain your ship and crew assignments,\nenter a number of players or q to QUIT')
    #     time.sleep(1)
    #     print('')
    #     response = input('Number of players: ')
    #     print(40*'-')
    #     print('')

    #     if response == 'q':
    #         print('')
    #         print(40*'-')
    #         print('See you next time!'.center(30, '*').center(30,' '))
    #         print(40*'-')
    #         playing = False
    #         break
    #     else:
    #         print_game(int(response))
    #         time.sleep(5)
    #         print(quest_generator())
        
#             msg_1 = """
# Are you happy with this ship & crew?
# (y) - Yes! Let's play
# (n) - No. I want a different ship and crew
# (q) - Quit. I don't want to play anymore
# """
#             response_2 = input(msg_1)

#             if response_2 == 'n':
#                 continue
#             elif response_2 == 'q':

#             else:

            

        # print('Would you like another crew? (y or n)')
        # response = int(input('Would you like another crew? (y or n): '))
    




if __name__ == '__main__':
    main()