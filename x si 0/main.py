from player_vs_player import *
from player_vs_pc import *


# main play function - initialise the GUI and gamemodes
def play():
    menu = Tk()
    menu.geometry("500x500")
    menu.title("X si 0")

    button_color = "tomato"
    button_font = "summer"
    text_color = "honeydew"

    def play_with_pc():
        player_versus_pc(menu)

    def play_with_player():
        player_versus_player(menu)

    # define buttons by calling the Button(params) function
    title_button = Button(menu,
                  text="Bun venit la X si 0",  # button text
                  activeforeground=button_color,  # foreground color when mouse is over the button
                  activebackground=text_color,  # background color when mouse is over the button
                  bg=button_color,  # background color
                  fg=text_color,  # foreground color
                  width=500,  # button width
                  font=button_font,  # button font text
                  bd=15  # button border width
                  )

    B1 = Button(menu,
                text="Contra computer",
                command=play_with_pc,
                activeforeground=button_color,
                activebackground=text_color,
                bg=button_color,
                fg=text_color,
                width=500,
                font=button_font,
                bd=5)

    B2 = Button(menu, text="Doi jucatori",
                command=play_with_player,
                activeforeground=button_color,
                activebackground=text_color,
                bg=button_color,
                fg=text_color,
                width=500,
                font=button_font,
                bd=5)

    B3 = Button(menu, text="Iesire",
                command=menu.quit,
                activeforeground=button_color,
                activebackground=text_color,
                bg=button_color,
                fg=text_color,
                width=500,
                font=button_font,
                bd=5)
    # arranges buttons on the top of the menu
    title_button.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    # loops infinitely the GUI, so that it never closes
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()
