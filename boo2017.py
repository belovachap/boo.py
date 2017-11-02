# Happy Halloween 2017!

from colorconsole import terminal

def boo():
    screen = terminal.get_terminal(conEmu=False)
    screen.clear()
    screen.set_color(fg=terminal.colors["RED"], bk=terminal.colors["LGREY"])
    screen.print_at(0, 1, "H A P P Y ")
    screen.print_at(0, 2, "H A L L O W E E N")

    screen.set_color(fg=terminal.colors["LGREY"], bk=terminal.colors["RED"])
    screen.blink()
    screen.print_at(11, 1, "2 0 1 7")

    # Draw the stem and leaf
    screen.reset_colors()
    screen.set_color(fg=terminal.colors["BROWN"], bk=terminal.colors["BLACK"])
    screen.print_at(9, 3, "x")
    screen.print_at(8, 4, "xx")
    screen.set_color(fg=terminal.colors["GREEN"], bk=terminal.colors["BLACK"])
    screen.print_at(10, 3, "x x")
    screen.print_at(11, 4, "x")

    # Draw pumpkin body
    screen.reset_colors()
    screen.set_color(fg=terminal.colors["PURPLE"], bk=terminal.colors["BLACK"])
    screen.print_at(0, 5,  "   xxxxxxxxxxx   ")
    screen.print_at(0, 6,  " xxxxxxxxxxxxxxx ")
    screen.print_at(0, 7,  "xxxxxx xxx xxxxxx")
    screen.print_at(0, 8,  "xxxxxx  xx  xxxxx")
    screen.print_at(0, 9,  "xx xxxxxxxxxxx xx")
    screen.print_at(0, 10, " xx x x x x x xxx")
    screen.print_at(0, 11, "  xxxxxxxxxxxxxx ")
    screen.print_at(0, 12, "   xxx xxx xxx   ")

    # Draw pumpkin glowing bits
    screen.reset_colors()
    screen.set_color(fg=terminal.colors["BLACK"], bk=terminal.colors["CYAN"])
    screen.print_at(7, 7, " ")
    screen.print_at(11, 7, " ")
    screen.print_at(7, 8, "  ")
    screen.print_at(11, 8, "  ")
    screen.print_at(3, 9, " ")
    screen.print_at(15, 9, " ")
    screen.print_at(4, 10, " ")
    screen.print_at(6, 10, " ")
    screen.print_at(8, 10, " ")
    screen.print_at(10, 10, " ")
    screen.print_at(12, 10, " ")
    screen.print_at(14, 10, " ")

    # "Press any key to continue..."
    screen.reset_colors()
    screen.print_at(0, 14, "Press ENTER KEY to continue...")
    screen.getch()
