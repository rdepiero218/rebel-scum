import sys,time, textwrap
# import curses




def indented_wrap(text, width=65, initial=0, indent=5):
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=" " * initial,  # No indent for the first line
        subsequent_indent=" " * indent  # Indent second and subsequent lines
    )
    return wrapper.fill(text)


def wrap_with_blank_lines(text, width=50):
    wrapped_lines = []
    for paragraph in text.split('\n'):
        if paragraph.strip():  # Wrap non-blank lines
            wrapped_lines.append(textwrap.fill(paragraph, width=width))
        else:  # Preserve blank lines
            wrapped_lines.append('')
    return '\n'.join(wrapped_lines)

def slow_print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)



def main():

    width = 70


    opening_msg = """
    It is a dark time. BARON DEATHRAY and his KILLTROOPERS hunt down all dissenion from the evil KILLSTAR REPUBLICK. Fascism and terror rule the star system!

    In the darkness, a motley band of revolutionaries, traitors, criminals, robots, and other REBEL SCUM are trying to fight back.

    You are are our only hope...
    """

    # print(opening_msg)
    # slow_print(textwrap.fill(opening_msg, width))
    slow_print(wrap_with_blank_lines(opening_msg, width))
    # slow_print(custom_wrap(opening_msg))

    # print(indented_wrap(opening_msg, initial=4))

    # print('')

    # print(len('        .______       _______ .______    _______  __  '))


if __name__ == "__main__":
    main()

##---------------------
## SLOW PRINTING
##---------------------
## V1
# def slow_print(str):
#    for c in str + '\n':
#      sys.stdout.write(c)
#      sys.stdout.flush()
#      time.sleep(3./90)

## V2 - adding time option to slow or speed up
# (should maybe make a function like printer that prints text

# def slow_print(str, sleep_time=3./90):
#    for c in str + '\n':
#      sys.stdout.write(c)
#      sys.stdout.flush()
#      time.sleep(sleep_time)


# def slow_print(str, sleep_time=3./90, remove_after=False):
#     for c in str + '\n':
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(sleep_time)
    
#     if remove_after:
#         # Move the cursor up one line and clear the line
#         sys.stdout.write('\033[F\033[K')
#         sys.stdout.flush()

# # Example usage
# import sys
# import time

# def slow_print(message, sleep_time=3./90, remove_after=False):

#     building_msg = 'Building your ship'

#     for c in building_msg:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(sleep_time)
    
#     if remove_after:
#         # Move the cursor back to the start of the message and clear it
#         sys.stdout.write('\r' + ' ' * len(message) + '\r')
#         sys.stdout.flush()

# Example usage
# print(5*'\n')
# slow_print('Building your ship. . . . . ', sleep_time=10./90, remove_after=True)
# print(5*'\n')
# slow_print(f'Building your ship. . . . . ', sleep_time=10./90, remove_after=True)
# print(5*'\n')
# print('another line here for testing')
# time.sleep(3)
# slow_print(f'Building your ship. . . . . ', sleep_time=10./90)
# import curses
# import time

print(5*'\n')
