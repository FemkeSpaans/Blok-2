# Author: Femke Spaans
# Date: 14/01/2020
# Name: afvink 6
# Version: 1

from tkinter import *
from tkinter import messagebox
from random import randint


def main():
    MyGUI()


class MyGUI:

    def __init__(self):
        self.buttons_all_chosen = list()

        master = Tk()
        frame_buttons = Frame(master)
        frame_buttons.grid(column=0, row=0)
        master.title("Tic Tac Toe")
        self.button1 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_1)
        self.button2 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_2)
        self.button3 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_3)
        self.button4 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_4)
        self.button5 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_5)
        self.button6 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_6)
        self.button7 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_7)
        self.button8 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_8)
        self.button9 = Button(frame_buttons, width=10, height=5,
                              command=self.command_button_9)

        self.button_list = [self.button1, self.button2, self.button3,
                            self.button4, self.button5, self.button6,
                            self.button7, self.button8, self.button9]

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)

        mainloop()

    def command_button_1(self):
        self.button1.config(text="x", state="disabled")
        self.ai()

    def command_button_2(self):
        self.button2.config(text="x", state="disabled")
        self.ai()

    def command_button_3(self):
        self.button3.config(text="x", state="disabled")
        self.ai()

    def command_button_4(self):
        self.button4.config(text="x", state="disabled")
        self.ai()

    def command_button_5(self):
        self.button5.config(text="x", state="disabled")
        self.ai()

    def command_button_6(self):
        self.button6.config(text="x", state="disabled")
        self.ai()

    def command_button_7(self):
        self.button7.config(text="x", state="disabled")
        self.ai()

    def command_button_8(self):
        self.button8.config(text="x", state="disabled")
        self.ai()

    def command_button_9(self):
        self.button9.config(text="x", state="disabled")
        self.ai()

    def ai(self):
        button_already_chosen = False
        while button_already_chosen == False:
            numb = randint(0, 8)
            button = self.button_list[numb]
            if button.cget("state") != "disabled":
                button_already_chosen = True
                button = self.button_list[numb]
                button.config(text="O", state="disabled")

            elif button not in self.buttons_all_chosen:
                self.buttons_all_chosen.append(button)
            if len(self.buttons_all_chosen) >= 9:
                keuze = messagebox.askyesno("Game over",
                                            "Game over!\n\n"
                                            "Do you want to play again?")
                if keuze == True:
                    for knop in self.buttons_all_chosen:
                        knop.config(text="", state="normal")
                        self.buttons_all_chosen = list()

                break


main()
