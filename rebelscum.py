import sys, time
import random

import utilities as util
import aspects

import character, quest, ship





def main():

    print_header() 

    while True:
        time.sleep(1)
        # print(40*'-')
        util.printer(util.wrap_text('To obtain your ship and crew assignments, enter a number of players or q to QUIT'))
        time.sleep(1)
        print('')
        response = input('Number of players:  ')
        print(' ')
        util.printer(8*" " + 50*'-','fast')
        print('')
        
        if response == 'q':
            print('')
            util.printer(8*" " + 50*'-','fast')
            util.printer(('Thanks for Playing!').center(65, ' '))
            util.printer(8*" " + 50*'-','fast')
            playing = False
            break
        else:
            num_players = int(response)
            # print(1*'\n')
            # util.printer(50*'-','fast')
            # print(1*'\n')
            time.sleep(3)
            print('')
            # Build the ship!
            player_ship = ship.ship_generator()
            ship.ship_builder(player_ship['gender'], player_ship['edges'])
            ship.print_ship_sheet(player_ship)
            util.printer(8*" " + 50*'-','fast')
            # Recruit your crew!
            player_crew = character.crew_generator(num_players)
            character.recruit_crew(player_crew)
            character.crew_manifest(player_crew)
            # Incoming Transmission!
            prompt = quest.quest_generator()
            quest.print_quest(prompt)

            print(2*'\n')
            util.printer(8*" " + 50*'-','fast')
            util.printer(('Thanks for Playing!').center(65, ' '))
            util.printer(8*" " + 50*'-','fast')

            break


# def main():
#     ## basic testing for functions
#     print_header()
    # print(1*'\n')
    # util.printer(50*'-','fast')
    # print(1*'\n')
    # # character.print_game(int(response))
    # time.sleep(3)
    # num_players = 1
    # print('')
    # # Build the ship!
    # player_ship = ship.ship_generator()
    # ship.ship_builder(player_ship['gender'], player_ship['edges'])
    # ship.print_ship_sheet(player_ship)
    # # Recruit your crew!
    # player_crew = character.crew_generator(num_players)
    # character.recruit_crew(player_crew)
    # character.crew_manifest(player_crew)
    # # Incoming Transmission!
    # prompt = quest.quest_generator()
    # quest.print_quest(prompt)


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
    print(' ')
    border = '\n'+ 16*'--==' + '\n'
    print(border)
    print("A polymorph RPG by Chris O'Neill, 9th Level Games".center(63,' '))
    print(header.center(80,' '))
    print(border)
    util.printer(util.wrap_text(opening_msg, 'blank_lines'))
    util.printer(8*" " + 50*'-','fast')
    print(' ')
if __name__ == '__main__':
    main()