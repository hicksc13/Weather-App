import tkinter.messagebox
import customtkinter

from osrs_api.const import AccountType
from osrs_api import Hiscores


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        NAME_ENTERED = "N/A"
        # configure window
        self.title("OSRS Highscores Lookup")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
  
        # create sidebar frame with widgets
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkLabel(self.sidebar_frame, text=f"Current Player:{NAME_ENTERED}")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="New Search", command=self.open_input_dialog_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Compare", command=self.compare)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter OSRS name here")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.search_button = customtkinter.CTkButton(self, text="Search", command=self.search_name)
        self.search_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        self.textbox = customtkinter.CTkTextbox(self, width=300)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")


        ####### set default values ###########
        self.appearance_mode_optionemenu.set("Dark")
        self.textbox.insert("0.0", "Hello and Welcome to OSRS-Lookup. Please enter your name below and your skills and levels will replace this text box.")



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Please ether a new name: ", title="New Search")
        new_player = dialog.get_input()
        NAME_ENTERED = new_player
        self.sidebar_button_1 = customtkinter.CTkLabel(self.sidebar_frame, text=f"Current Player:{NAME_ENTERED}")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.search_new_name(new_player)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def compare(self):
        print("compare")


    def search_name(self, *args):
        NAME_ENTERED = self.entry.get()
        self.sidebar_button_1 = customtkinter.CTkLabel(self.sidebar_frame, text=f"Current Player:{NAME_ENTERED}")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        input_player = Hiscores(NAME_ENTERED)
        self.textbox.delete('1.0','end')
        for skill, level in input_player.skills.items():
            self.textbox.insert('1.0', text=f'{skill}: {level}\n')


    def search_new_name(self, *args):
        input_player = Hiscores(*args)
        self.textbox.delete('1.0','end')
        for skill, level in input_player.skills.items():
            self.textbox.insert('1.0', text=f'{skill}: {level}\n')



#### TO-DO ####
#Need to add compare module

 

if __name__ == "__main__":
    app = App()
    app.mainloop()