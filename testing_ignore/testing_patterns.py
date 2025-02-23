import sys, time

# ship_loadout_str = '\u3014 '+'SHIP LOADOUT'+' \u3015 '
# ship_loadout_str = '\u3018  '+'SHIP LOADOUT'+'  \u3019 '

# # print('  ' + 15*'_')
# print(ship_loadout_str)
# print((14*'‾').center(len(ship_loadout_str),' '))

# # border = """
# # \u2501
# #  /              ∕⎹
# # |⎹⏐    SHIP LOADOUT
# #  \
# # """

# border = """
# ╰┈┈┈┈╯⃛
# ╭------------------╮
# \u2502   SHIP LOADOUT   \u2502
# ╰------------------╯
# \u3018 
# """

# # # border = """
# # # ╰---------------╮◝
# # # """
# print(border)
# # print('⎿⏌⌜----')

# # print('╰┈┈┈┈┈┈┈┈┈╮')


# # for i in range(1000,1100):
# #     print(i, chr(i))

# # print('\u3014')
# pattern = 20*'-=='
# # \u25CE
# pattern = 10*'\u2022\u29BE\u2022\u2734'

# print(pattern)

# header = """ 
#         .______       _______ .______    _______  __         
#         |   _  \     |   ____||   _  \  |   ____||  |        
#         |  |_)  |    |  |__   |  |_)  | |  |__   |  |        
#         |      /     |   __|  |   _  <  |   __|  |  |        
#         |  |\  \----.|  |____ |  |_)  | |  |____ |  `----.   
#         | _| `._____||_______||______/  |_______||_______|   
#              _______.  ______  __    __  .___  ___.          
#             /       | /      ||  |  |  | |   \/   |          
#            |   (----`|  ,----'|  |  |  | |  \  /  |          
#             \   \    |  |     |  |  |  | |  |\/|  |          
#         .----)   |   |  `----.|  `--'  | |  |  |  |          
#         |_______/     \______| \______/  |__|  |__|                                                    
# """

# print('')
# print(16*'--==')
# border = '\n'+ 16*'--==' + '\n'
# print(border)
# print(header.center(80,' '))
# print(border)
# print('')
# print(16*'-.-')
# print(16*'--==')
# # print(54*'=')
# print('')

crew_string = '\u25CB \u25CB \u25CB \u25CB \u25C9'

crew_string = 5*'\u25CB '

crew_size = 5
for i in range(1,crew_size+1):
    # print(crew_string)
    sys.stdout.write(f"\r{i*' \u25C9'} {(crew_size-i)*'\u25CB '}")
    sys.stdout.flush()
    time.sleep(1)

print(2*'\n')
# print(crew_string)
# print(2*'\n')