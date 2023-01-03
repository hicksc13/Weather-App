import tkinter
import customtkinter

API_KEY = "83536a95d4dd86b3883578912f0f2d0f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x780")
app.title("Weather Look-up")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Weather Look up",justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Search")#, command=search)
button_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter City Name:")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["F", "C"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("F")
text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=200)
text_1.pack(pady=10, padx=10)


def search(self,*ars):
	print(entry_1)




app.mainloop()