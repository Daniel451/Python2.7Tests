import curses
import time


stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()

curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_YELLOW, -1)
curses.init_pair(3, curses.COLOR_MAGENTA, -1)
curses.init_pair(4, curses.COLOR_GREEN, -1)
curses.init_pair(5, curses.COLOR_BLUE, -1)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(7, curses.COLOR_WHITE, -1)
curses.init_pair(8, curses.COLOR_CYAN, -1)

#stdscr.addstr("1 Red: ".ljust(13, " "))
#stdscr.addstr("this is a test text\n", curses.color_pair(1))


for i in range(0, 1001):
    stdscr.clear()
    stdscr.addstr("Loading: ")
    stdscr.addstr(str(i/10.0))
    stdscr.addstr("%")
    stdscr.refresh()
    time.sleep(0.01)