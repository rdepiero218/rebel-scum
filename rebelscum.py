import sys, time
import random

import utilities as util
import aspects

import character, quest, ship





# def main():

#     print_header() 

#     while True:
#         time.sleep(1)
#         print(40*'-')
#         print('To obtain your ship and crew assignments,\nenter a number of players or q to QUIT')
#         time.sleep(1)
#         print('')
#         response = input('Number of players: ')
#         print(40*'-')
#         print('')
        
#         if response == 'q':
#             print('')
#             print(40*'-')
#             print('See you next time!'.center(30, '*').center(30,' '))
#             print(40*'-')
#             playing = False
#             break
#         else:
#             # character.print_game(int(response))
#             time.sleep(5)
#             # Build the ship!
#             the_ship = ship.ship_generator()
#             the_ship.ship_builder(ship['gender'], ship['edges'])
#             # Recruit your crew!
#             character.crew_manifest(int(response))
#             # Incoming Transmission!
#             quest = quest.quest_generator()
#             quest.print_quest()

            
#             print(2*'\n')

#             break

def main():
    ## basic testing for functions
    print_header()
    print(1*'\n')
    util.printer(50*'-','fast')
    print(1*'\n')
    # character.print_game(int(response))
    time.sleep(3)
    num_players = 1
    print('')
    # Build the ship!
    player_ship = ship.ship_generator()
    ship.ship_builder(player_ship['gender'], player_ship['edges'])
    ship.print_ship_sheet(player_ship)
    # Recruit your crew!
    player_crew = character.crew_generator(num_players)
    character.recruit_crew(num_players)
    character.crew_manifest(player_crew)
    # Incoming Transmission!
    prompt = quest.quest_generator()
    quest.print_quest(prompt)


# def print_game(num_players):

#     print('')
#     # slow_print(f'Your ship and crew of {num_players} is ready!')
#     print('')

#     # printer(f'Building your ship. . . . . ', sleep_time=5./90)
#     time.sleep(1)
#     print_ship_sheet(ship_builder())
    
#     print('')
#     # # print(70*'=')
#     # print('CREW MANIFEST'.center(33, ' ').center(70,'='))
#     # # print(70*'=')
#     print(62*'-')
#     # print('|'+62*' '+'|')
#     print('|'+'CREW MANIFEST'.center(60, ' ')+'|')
#     # print('|'+62*' '+'|')
#     print(62*'-')
#     print('')
    
#     crew_generator(num_players)
    
#     print('')


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
    util.printer(util.wrap_text(opening_msg, 'blank_lines'))
    # print('The adventures of the crew of the '.center(80,' '))

if __name__ == '__main__':
    main()