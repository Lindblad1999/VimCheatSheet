import time, os, sys
from colorama import init
from termcolor import colored
import shutil
import cursor
import signal

editing_keys = [
    ('r'     , 'replace a single character'), 
    ('cc'    , 'change (replace) entire line'), 
    ('ciw'   , 'change (replace) entire line'),
    ('u'     , 'undo'), 
    ('Ctrl+r', 'redo'), 
    ('.'     , 'repeat last command')
]

cursor_movement_keys = [
    ('h'     , 'move cursor left'),
    ('j'     , 'move cursor down'),
    ('k'     , 'move cursor up'), 
    ('l'     , 'move cursor right'), 
    ('H'     , 'move to top of screen'),
    ('M'     , 'move to middle of screen'), 
    ('L'     , 'move to bottom of screen'), 
    ('w'     , 'jump fwd to start of word'),
    ('e'     , 'jump fwd to end of word'), 
    ('b'     , 'jump bckw wo start of word'),
    ('0'     , 'jump to start of line'), 
    ('$'     , 'jump to end of line'), 
    ('gg'    , 'go to first line of doc'),
    ('G'     , 'go to last line of doc'), 
    ('5gg'   , 'go to line 5'), 
    ('Ctrl+e', 'move screen down one line(w.o. moving cursor)'),
    ('Ctrl+y', 'move screen up one line(w.o. moving cursor)') 
]

cut_and_paste_keys = [
    ('yy'    , 'yank (copy) a line'), 
    ('2yy'   , 'yank (copy) 2 lines'), 
    ('yiw'   , 'yank (copy) the word at cursor'),
    ('Y'     , 'yank (copy) to end of line'), 
    ('p'     , 'put (paste) the clipboard after cursor'), 
    ('P'     , 'put (paste) before cursor'),
    ('dd'    , 'delete (cut) a line'), 
    ('2dd'   , 'delete (cut) 2 lines'), 
    ('diw'   , 'delete (cut) the word at cursor'),
    ('D'     , 'delete (cut) to the end of the line'), 
    ('x'     , 'delete (cut) character')
]

marking_keys = [
    ('v'     , 'start visual mode'), 
    ('V'     , 'start linewise visual mode'), 
    ('o'     , 'move to other end of marked area'),
    ('Ctrl+v', 'start visual block mode'), 
    ('aw'    , 'mark a word'), 
    ('y'     , 'yank (copy) marked text'), 
    ('d'     , 'delete marked text')
]

window_keys = [
    ('Ctrl+wv', 'split screen'), 
    ('Ctrl+ws', 'split screen horizontal'),
    ('Ctrl+wh', 'move to the window on the left'),
    ('Ctrl+wq', 'close current window')
]

custom = [
    ('Space+pv', ':Ex | Go to explorer'),
    ('Ctrl+p'  , 'Search git files'),
    ('Ctrl+e','open harpoon menu'),
    ('Ctrl+a','add file to harpoon'),
    ('Ctrl+e','open harpoon menu'),
]

SLEEP_TIME = 5

def printer(keys, title):
    os.system('clear')
    columns = shutil.get_terminal_size().columns
    lines = shutil.get_terminal_size().lines

    # center in height
    for lines in range(0, int((lines-(len(keys)*2))/2)):
        print('')

    # print commands and descriptions, in center width
    print(colored(title.center(columns), 'white'))
    for pair in keys:
        spaces = ' '*(75-len(pair[0])-len(pair[1]))
        print(colored(f'{pair[0]}{spaces}{pair[1]}\n'.center(columns), 'white'))

def run():
    while True:
        printer(cursor_movement_keys, 'CURSOR MOVEMENT')
        time.sleep(SLEEP_TIME)
        printer(editing_keys, 'EDITING')
        time.sleep(SLEEP_TIME)
        printer(cut_and_paste_keys, 'CUT AND PASTE')
        time.sleep(SLEEP_TIME)
        printer(marking_keys, 'MARKING')
        time.sleep(SLEEP_TIME)
        printer(custom, 'CUSTOM')
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    try:
        cursor.hide()
        run()
    except KeyboardInterrupt:
        # Make sure cursor is set to visible before exiting
        cursor.show()
