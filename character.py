import sys, time
import random
import aspects as a
import utilities as util


##------------------------------
## METHOD DEFINITIONS
##------------------------------

def name_generator():
    '''Randomly selects a first and last name'''
    character_name = random.choice(a.first_names) + ' ' + random.choice(a.last_names)

    return character_name

def role_selector():
    '''Randomly select a ROLE'''
    role = random.choice(list(a.roles.keys()))
    
    die = a.roles[role]

    return [role, die]

def gender_selector():
    '''Randomly select a GENDER'''
    gender = random.choice(a.genders)

    return gender

def class_selector():

    char_class = random.choice(list(a.character_classes.keys()))

    return char_class

def edge_selector(char_class, count=3):
    '''Randomly select edges from selected class'''
    
    edge_list = random.sample(list(a.character_classes[char_class]['edges']), count)

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
    character['profile'] = a.character_classes[character['class']]['flavor text']
    character['shining star'] = a.character_classes[character['class']]['shining star']
    character['burn star'] = a.character_classes[character['class']]['burn star']
    
    return character
    
def print_character_sheet(character):
    '''prints the character sheet'''
    util.printer(30*'~', 'fast')
    util.printer(f"{character['name']} - {character['class']}", 'fast')
    util.printer(30*'~', 'fast')

    time.sleep(0.5)
    sheet_string = f"""
Role:   {character['role']} ({character['die']})
Gender: {character['gender']}

PROFILE: { character['profile'] }

STAR: {character['shining star']}
      Burn a star to succeed whenever the result {character['burn star']}

EDGES: 
"""
    util.printer (sheet_string, 'fast')
    for edge in character['edges']:
        util.printer(f">    {edge}")
        time.sleep(0.5)
    print(' ')


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
        
    return crew

def recruit_crew(crew):

    search_msgs = random.sample(a.search_methods, 4)
    util.printer("\n....AI Initiating recruitment protocol\n")
    time.sleep(1)

    for msg in search_msgs:

        util.printer(f"....{msg}")
        time.sleep(1)
   
    print(' ')
    util.printer(f"....Processing candidates ")
    print(' ')
    # util.printer(f"....processing candidates ")
    recruited_crew = []
    
    for member in crew:
        recruited_crew.append(member['name'])

    crew_size = len(recruited_crew)

    crew_roles = random.sample(a.crew_roles, crew_size)

    methods = random.sample(a.recruitment_methods, crew_size)
    for i in range(1,crew_size+1):
        sys.stdout.write(f"\r{i*' \u25C9'} {(crew_size-i)*'\u25CB '} Recruited - {crew_roles[i-1]:16s}: {methods[i-1]:55s}")
        sys.stdout.flush()
        time.sleep(3)
    
    util.printer("\n\n....Crew recruitment complete", 'slow')
    time.sleep(0.5)
    print(' ')
    util.printer('....Loading Crew Manifest', 'slow')
    # util.printer('....', 'slow') 
    time.sleep(2)
    print(' ')


def crew_manifest(crew):

# """
    border = 62*'-'
    util.printer(border, 'fast')
    # print('|'+62*' '+'|')
    util.printer('|'+'CREW MANIFEST'.center(60, ' ')+'|', 'fast')
    util.printer(border, 'fast')
    print('')
    time.sleep(0.5)

    for member in crew:
        print_character_sheet(member)
        time.sleep(1)
    
    print(' ')
##------------------------------
## TESTING
##------------------------------

def main():
    print('This is for testing only')
    print(2*'\n')

    # print(character_generator())
    # character = character_generator()
    # print_character_sheet(character)

    num_players = 2
    crew = crew_generator(num_players)
    # # print(crew)
    # print(2*'\n')
    # print(50*'-')
    # recruit_crew(num_players)

    recruit_crew(crew)
    # print(2*'\n')
    # print(50*'-')
    # print(2*'\n')
    # crew_manifest(crew)



if __name__ == "__main__":
    main()