import sys, time
import random
import aspects as a
import utilities as util


##------------------------------
## METHOD DEFINITIONS
##------------------------------
def ship_size_selector():
    '''Randomly select a SHIP SIZE'''
    size = random.choice(list(a.ship_sizes.keys()))
    
    die = a.ship_sizes[size]

    return [size, die]

def ship_name_selector():
    '''Randomly select a SHIP SIZE'''
    ship_name = random.choice(a.ship_names)

    return ship_name

def ship_gender_selector():
    '''Randomly select a GENDER'''
    gender = random.choice(a.ship_genders)

    return gender

def ship_profile_selector():
    '''Randomly select a PROFILE'''
    profile = random.choice(a.ship_backstories)

    return profile

def ship_edge_selector(count=3):
    '''Randomly selects SHIP EDGES'''

    ship_edge_list = random.sample(a.ship_edges, count)

    return ship_edge_list

def ship_generator():
    '''Randomly generates a SHIP'''
    ship = {
        'name' : ship_name_selector(),
        'size' : ship_size_selector()[0],
        'die' : ship_size_selector()[1],
        'gender' : ship_gender_selector(),
        'edges': ship_edge_selector(),
        'profile': ship_profile_selector()
    }

    return ship

def print_ship_sheet(ship):
    '''prints the ship character sheet'''
    speed = 0.5
    # print ship name
    border = 31*'-='+'-'
    # print(border)
    # print(f"▶︎{ship['name'].center(61,' ')}◀︎")
    # print(border)
    util.printer(border, 'fast')
    util.printer(f"▶︎{ship['name'].center(61,' ')}◀︎", 'fast')
    util.printer(border, 'fast')
    # print 
    sheet_string = f"""
SIZE:   {ship['size']} ({ship['die']})

GENDER: {ship['gender']}

"""
    util.printer(sheet_string)
    util.printer(util.wrap_text(f"PROFILE: {ship['profile']}", 'first_line', indent=9))
    # time.sleep(speed)
    # print(f"Size:   {ship['size']} ({ship['die']})")
    # time.sleep(speed)
    # print(f"Gender: {ship['gender']}")
    border = """
╭------------------╮
\u2502   SHIP LOADOUT   \u2502
╰------------------╯
"""
    time.sleep(speed)
    # print(border) 
    util.printer(border, 'fast')
    for edge in ship['edges']:
        time.sleep(speed)  
        util.printer(f">     {edge}")

    print(' ')


# def ship_builder(gender, edges):

#     traits = random.sample(a.ship_traits, k=3)

#     features = a.ship_extras + edges # adds ship edges for extra fun in screen printout

#     total = len(features)

#     bar_length = 30
    
#     for i, feature in enumerate(features, start=1):
#         # Calculate progress
#         progress = i / total
#         bar = '=' * int(bar_length * progress)
#         spaces = ' ' * (bar_length - len(bar))
        
#         # Display progress bar with feature name
#         sys.stdout.write(f"\rBuilding Ship: [{bar}{spaces}] {int(progress * 100)}% — Installing: {feature} {8*' '}")
#         sys.stdout.flush()
        
#         time.sleep(0.5)  # Simulate time taken to install each feature

#     print('\n\n')
#     # Assign gender and other funny traits
#     print(f"....Assigning ship gender... ✅ {gender}")
#     time.sleep(1)
    
#     # print("Assigning additional quirky features:")
#     i = 0
#     for trait in random.sample(traits, k=3):
        
#         print(f"{4*'.'}{random.choice(a.ship_building_words[i])} {trait}")
#         i += 1
#         time.sleep(0.5)

def ship_builder(gender, edges):

    traits = random.sample(a.ship_traits, k=3)

    features = a.ship_extras + edges # adds ship edges for extra fun in screen printout

    total = len(features)

    bar_length = 30

    util.printer('....Initializing Ship Building Protocol', 'slow')
    time.sleep(1)
    print('')
    util.printer('....Building Ship', 'slow')
    print(' ')
    
    for i, feature in enumerate(features, start=1):
        # Calculate progress
        progress = i / total
        bar = '=' * int(bar_length * progress)
        spaces = ' ' * (bar_length - len(bar))
        
        # Display progress bar with feature name
        sys.stdout.write(f"\r{1*' '}[{bar}{spaces}] {int(progress * 100)}% — Installing: {feature} {8*' '}")
        sys.stdout.flush()
        
        time.sleep(0.5)  # Simulate time taken to install each feature

    print('\n\n')
    # Assign gender and other funny traits
    util.printer(f"....Assigning ship gender... ✅ {gender}")
    print(' ')

    time.sleep(1)
 
    # print("Assigning additional quirky features:")
    i = 0
    for trait in random.sample(traits, k=3):
        util.printer(f"{4*'.'}{random.choice(a.ship_building_words[i])} {trait}")
        # print(' ')
        i += 1
        time.sleep(0.5)
        print(' ')

    util.printer('....Loading Ship Profile', 'slow')
    # util.printer('....', 'slow')
    time.sleep(2)
    print(' ')

##------------------------------
## TESTING
##------------------------------

def main():
    print('This is for testing only')
    
    ship = ship_generator()
    print(2*'\n')
    # Build the ship!
    # ship_builder(ship['gender'], ship['edges'])
    print(2*'\n')
    # print('Another line here')
    # print(2*'\n')
    print_ship_sheet(ship)
    print(2*'\n')
    

if __name__ == "__main__":
    main()
