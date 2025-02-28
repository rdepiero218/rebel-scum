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

    # print('You rolled a', roll)
    
    return roll

def check_core_resolver(action, roll):

    if roll in outcomes[action]:
        # print('Success!')
        result = True
    elif roll == 1:
        result = 'key'
    else:
        # print('Unsuccessful :(')
        result = False

    return result

def check_vantage(results, vantage=None):
    """Check core resolver (not key or crown)"""
    success = False
    
    if vantage == 'd':
        if False in results:
            # print('Unsuccessful :(')
            success = False
        else: 
            # print('Success!')
            success = True
    else:
        if True in results:
            # print('Success!')
            success = True
        else:
            # print('Unsuccessful :(')
            success = False

    return success


def roll(die_type, action, vantage=None):

    vantage_type = None

    if vantage == 'a' or vantage == 'd':

        rolls = [roll_die(die_type), roll_die(die_type)]

        if vantage == 'a':
            vantage_type = 'ADVANTAGE'
            # print('You are rolling with ADVANTAGE')
        else:
            vantage_type = 'DISADVANTAGE'
            # print('You are rolling with DISADVANTAGE')
        print(f'You are rolling for {action.upper()} with {vantage_type}')
        

    else:
        rolls = [roll_die(die_type)]
        print(f'You are rolling for {action.upper()}')

    results = []
    
    
    
    for roll in rolls:
        print('You rolled a ', roll)
        if roll == 1:
            print('Your KEY! Success depends on your character')
            results.append(True)
        elif roll == dice[dice_type]:
            print('Your ULTIMATE! Success depends on how BRIGHT or DARK it is')
            results.append(True)
        else:
            # resolve = resolver(action, roll)
            # print('Success?', resolve)
            # results.append(resolve)
            results.append(check_core_resolver(action, roll))

    success = check_vantage(results, vantage)
     
    if success == True:
        print('A successful roll :)')
    else:
        print('An unsuccessful roll :(')
        
    return success

### FOR TESTING ONLY

def main():
    # dice_type = input('Choose a die (d4, d6, d8, d10)\n')

    # roll = roll_die(dice_type)
    # roll = roll_die(dice_type)
    # print(roll)
    # roll some die
    print(25*'=')
    print('LET\'S ROLL SOME DICE!')
    print(25*'=')
    print('')
    roll_1 = roll('d4', 'move')
    print(20*'-')
    roll_2 = roll('d6', 'blaster', 'd')
    print(20*'-')
    roll_3 = roll('d10', 'might', 'a')
if __name__ == "__main__":
    main()
