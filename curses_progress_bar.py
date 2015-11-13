import curses
import time
import math

# init new screen
stdscr = curses.initscr()

# init colors
curses.start_color()
curses.use_default_colors()

# define colors
curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_YELLOW, -1)
curses.init_pair(3, curses.COLOR_MAGENTA, -1)
curses.init_pair(4, curses.COLOR_GREEN, -1)
curses.init_pair(5, curses.COLOR_BLUE, -1)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(7, curses.COLOR_WHITE, -1)
curses.init_pair(8, curses.COLOR_CYAN, -1)


for i in range(0, 1001):
    number = i
    width = 20

    bar_color = None
    if i/10.0 < 25.0:
        bar_color = curses.color_pair(1)
    elif 25.0 <= i/10.0 and i/10.0 < 75.0:
        bar_color = curses.color_pair(2)
    else:
        bar_color = curses.color_pair(4)

    # clear the screen
    stdscr.clear()

    # progress bar
    stdscr.addstr(" [")
    stdscr.addstr("".ljust(int(math.floor(number/10.0/100.0*20.0)), "#").ljust(width, " "), bar_color)
    stdscr.addstr("] ")

    # add the percent/number
    stdscr.addstr("[")
    stdscr.addstr("{:.1f}%".format(number/10.0).rjust(6, " "))
    stdscr.addstr("] ")

    # display new data
    stdscr.refresh()

    # pause a while
    time.sleep(0.01)


curses.endwin()