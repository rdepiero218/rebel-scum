import random


dice = {
    'd4': 4,
    'd6': 6,
    'd8': 8,
    'd10': 10
}

outcomes = {  
    'intel' : [2, 3], # mental
    'move': [3, 4, 5], # physical
    'blaster' : [4, 5, 6, 7], # conflict
    'might' : [5, 6, 7, 8, 9], # strength
}  

def roll_die(die_type):

    roll = random.randint(1, dice[die_type])
    
    # store as tuple to store die type (immutable)
    return (roll, die_type)

def check_resolver(action, roll):
    """Check resolver"""

    if roll[0] == dice[roll[1]]:
        result = 'ultimate'
        # print('Your ULTIMATE! Success depends on how BRIGHT or DARK it is')
    elif roll[0] == 1:
        result = 'key'
        # print('Your KEY! Success depends on your character')
    elif roll[0] in outcomes[action]:
        result = True
    else:
        result = False



    #    if roll in outcomes[action]:
    #         # print('Success!')
    #         result = True
    #     elif roll == 1:
    #         result = 'key'
    #     elif roll :
    #         # print('Unsuccessful :(')
    #         result = False


    # if roll in outcomes[action]:
    #     # print('Success!')
    #     result = True
    # elif roll == 1:
    #     result = 'key'
    # else:
    #     # print('Unsuccessful :(')
    #     result = False

    return result

def check_vantage(results, vantage=None):
   
    success = False
    
    if vantage == 'd':
        if False in results:
            # print('Unsuccessful :(')
            success = False
        elif 'key' or 'ultimate' in results:
            success = 'unknown'
        else:
            # print('Unsuccessful :(')
            success = True
    else:
        if True in results:
            # print('Success!')
            success = True
        elif ('key' or 'ultimate') in results:
            success = 'unknown'
        else:
            # print('Unsuccessful :(')
            success = False

    return success


def roll(die_type, action, vantage=None):

    vantage_type = None
    print(45*'-')

    if vantage == None:
        rolls = [roll_die(die_type)] 
        print(f'You are rolling for {action.upper()}')

    elif vantage == 'a' or vantage == 'd':
        rolls = [roll_die(die_type), roll_die(die_type)]
        if vantage == 'a':
            vantage_type = 'ADVANTAGE'
            # print('You are rolling with ADVANTAGE')
        else:
            vantage_type = 'DISADVANTAGE'
            # print('You are rolling with DISADVANTAGE')
        print(f'You are rolling for {action.upper()} with {vantage_type}')
    print(45*'-')
    results = []
    
    for roll in rolls:
        result = check_resolver(action, roll)
        roll_result_msg = f'You rolled a {roll[0]} with a {roll[1]}'

        if result == 'key':
            success_msg = f'\n         Your KEY! Success depends on your character.\n'
        elif result == 'ultimate':
            success_msg = f'\n         Your ULTIMATE! Success depends on how BRIGHT or DARK it is.\n'
        elif result == True:
            success_msg = f'\n         Success \u2714\n'
        elif result == False:
            success_msg = f'\n         Failure \u2715\n'

        print(roll_result_msg + success_msg)
        results.append(result)
        # if roll == 1:
        #     print('Your KEY! Success depends on your character')
        #     results.append(True)

        # elif roll == dice[die_type]:
        #     print('Your ULTIMATE! Success depends on how BRIGHT or DARK it is')
        #     results.append(True)
        # else:
        #     # resolve = resolver(action, roll)
        #     # print('Success?', resolve)
        #     # results.append(resolve)
            # results.append(check_resolver(action, roll))

    success = check_vantage(results, vantage)
    # print(50*'-')
    if success == True:
        print(5*'\u2714 ' + 'You SUCCEEDED ' + 5*'\u2714 ' + '\n')
    elif success == 'unknown':
        # print(f'\uFF1F Success with {vantage_type} cannot be determined')
        print(3*'\uFF1F' + ' Success cannot be determined ' + 3*'\uFF1F' + '\n')
    else:
         print(5*'\u2715 ' + 'You FAILED' + 5*' \u2715' + '\n')
    # print(50*'-')
    return success


def roller():
    actions = {'i': 'intel', 'mo': 'move', 'b': 'blaster', 'mi': 'might'}


    while True:
        
        response = input('Would you like to roll some die? (y) or (n): ')

        if response == 'n':
            break
        # else:
        #     rolling = False

        print('~~~~~~~~~~~~~~~~~~~')
        print('   Roll the dice   ')
        print('~~~~~~~~~~~~~~~~~~~')
        die_type = input("Enter your die (d4, d6, d8, d10): ")
        action_type = actions[input("Enter the action (i)ntel, (mo)ve, (b)laster, (mi)ght): ")]
        vantage_type = input("Enter (a)dvantage, (d)isadvantage, or (n)one: ")
        # print(20*'-')
        # print('action: ', actions[action_type])
        # print(type(action_type))
        # break
        while True: 
            if die_type not in dice.keys():
                print("not a valid die type")
                break

            elif action_type not in outcomes.keys():
                print("not a valid action type")
                break
            
            elif vantage_type == 'a' or vantage_type == 'd':
                this_roll = roll(die_type, action_type, vantage_type)
                # print(this_roll)
                break
            else:
                this_roll = roll(die_type, action_type)
                break

    # return this_roll

### FOR TESTING ONLY

def main():
    # dice_type = input('Choose a die (d4, d6, d8, d10)\n')

    # roll = roll_die(dice_type)
    # roll = roll_die(dice_type)
    # print(roll)
    ## roll some die
    # print(25*'=')
    # print('LET\'S ROLL SOME DICE!')
    # print(25*'=')
    # print('')
    # roll_1 = roll('d4', 'might')
    # # print(20*'-')
    # roll_2 = roll('d6', 'blaster', 'd')
    # # print(20*'-')
    # roll_3 = roll('d10', 'might', 'a')

    roller()


if __name__ == "__main__":
    main()
