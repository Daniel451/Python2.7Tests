import curses


stdscr = curses.initscr()

curses.start_color()
curses.use_default_colors()

curses.init_pair(1, 0, -1)

stdscr.addstr("terminal has colors: {}\n".format(curses.has_colors()))

curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_YELLOW, -1)
curses.init_pair(3, curses.COLOR_MAGENTA, -1)
curses.init_pair(4, curses.COLOR_GREEN, -1)
curses.init_pair(5, curses.COLOR_BLUE, -1)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(7, curses.COLOR_WHITE, -1)
curses.init_pair(8, curses.COLOR_CYAN, -1)

stdscr.addstr("1 Red: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(1))

stdscr.addstr("2 Yellow: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(2))

stdscr.addstr("3 Magenta: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(3))

stdscr.addstr("4 Green: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(4))

stdscr.addstr("5 Blue: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(5))

stdscr.addstr("6 Black: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(6))

stdscr.addstr("7 White: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(7))

stdscr.addstr("8 Cyan: ".ljust(13, " "))
stdscr.addstr("this is a test text\n", curses.color_pair(8))

stdscr.refresh()