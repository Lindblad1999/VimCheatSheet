import time, os
from colorama import init
from termcolor import colored
import shutil

def cursor_movement():
    os.system('clear')
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines
    keys = [('h', 'move cursor left'), ('j', 'move cursor down'),
        ('k', 'move cursor up'), ('l', 'move cursor right'), ('H', 'move to top of screen'),
        ('M', 'move to middle of screen'), ('L', 'move to bottom of screen'), ('w', 'jump fwd to start of word'),
        ('e', 'jump fwd to end of word'), ('b', 'jump bckw wo start of word'),
        ('0', 'jump to start of line'), ('$', 'jump to end of line'), ('gg', 'go to first line of doc'),
        ('G', 'go to last line of doc'), ('5gg', 'go to line 5'), ('Ctrl+e', 'move screen down one line(w.o. moving cursor)'),
        ('Ctrl+y', 'move screen up one line(w.o. moving cursor)') 
    ]

    # center in height
    for lines in range(0, lines-(len(keys)*2)-5):
        print('')

    print(colored('CURSOR MOVEMENT'.center(columns), 'white'))
    for pair in keys:
        spaces = ' '*(75-len(pair[0])-len(pair[1]))
        print(colored(f'{pair[0]}{spaces}{pair[1]}\n'.center(columns), 'white'))

def run():
    while True:
        cursor_movement()
        time.sleep(5)

if __name__ == "__main__":
    run()

