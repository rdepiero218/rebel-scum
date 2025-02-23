import sys,time
import textwrap


# def indented_wrap(text, width=65, first=0, indent=5):
#     wrapper = textwrap.TextWrapper(
#         width=width,
#         initial_indent=""*first,  # No indent for the first line
#         subsequent_indent=" " * indent  # Indent second and subsequent lines
#     )
#     return wrapper.fill(text)

def indent_all_lines(text, width=65, indent=5):
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=" " * indent,
        subsequent_indent=" " * indent
    )
    return wrapper.fill(text)

def first_line_indent_wrap(text, width=65, indent=5):
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

def wrap_text(text, method='indent_all', width=65, indent=5):
    if method == 'indent_all':
        return indent_all_lines(text, width, indent)
    elif method == 'first_line':
        return first_line_indent_wrap(text, width, indent)
    elif method == 'blank_lines':
        return wrap_with_blank_lines(text, width)
    else:
        raise ValueError("Invalid method. Choose 'indent_all', 'indented_wrap', or 'wrap_with_blank_lines'.")

def printer(str, speed=None):
   '''Prints text to screen one character at a time'''
   if speed == 'fast':
       sleep_time=1./90
   elif speed == 'slow':
       sleep_time=5./90
   else:
       sleep_time=3./90
       
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(sleep_time)

def main():

    width = 70


    opening_msg = """
It is a dark time. BARON DEATHRAY and his KILLTROOPERS hunt down all dissenion from the evil KILLSTAR REPUBLICK. Fascism and terror rule the star system!

In the darkness, a motley band of revolutionaries, traitors, criminals, robots, and other REBEL SCUM are trying to fight back.

You are are our only hope...
    """


    text = """
A distress signal flickers across your ship's comms—an urgent plea from a old monk stranded near Persephone. They need you to steal the plans to a secret base before the Killtroopers close in. Time is running out, and the fate of the galaxy hangs in the balance. If you succeed, you will be rewarded with a shiny medal.
    """



    # printer(text_wrapper(opening_msg, width ))
    # printer(text_wrapper(opening_msg, width=70, initial=0, indent=0, blank_lines=True))
    # print(text_wrapper(opening_msg, width=70, first=0, indent=0))
    # printer(indented_wrap(opening_msg))
    # printer(wrap_with_blank_lines(opening_msg, width=50))
    # print(indented_wrap(opening_msg, initial=4))

    # print(wrap_text(opening_msg))

    printer(text, 'fast')


if __name__ == "__main__":
    main()