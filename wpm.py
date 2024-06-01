import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0, "Welcome to the speed Typing test!",curses.color_pair(2))
    stdscr.addstr("\nPress any key to begin!",curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target_text,current_text,wpm=0):
    stdscr.addstr(target_text)

    for i,char in enumerate(current_text):
        stdscr.addstr(0,i,char,curses.color_pair(1))


def wpm_test(stdscr):
    target_text= "Hello World this is some text for this app"
    current_text = []
    # stdscr.clear()
    # stdscr.addstr(target_text)
    # stdscr.refresh()
    # stdscr.getkey()

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        key = stdscr.getkey()

        if ord(key) == 27:  # ESC key to exit
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)

        stdscr.refresh()
        

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED , curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE , curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)
wrapper(main)
