import tkinter
import customtkinter
import requests

### CHANGE API KEY #####
API_KEY = ""
BASE_URL = ""

def search():
    
    city_name = entry_1.get()
    if not city_name:
        text_1.delete(1.0, tkinter.END)
        text_1.insert(tkinter.END, "Please enter a city name")
        return

    params = {
        "q": city_name,
        "appid": API_KEY
    }

    unit = optionmenu_1.get()
    if unit == "F":
        params["units"] = "imperial"
    else:
        params["units"] = "metric"
        
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if unit == "F":
        unit_text = "Fahrenheit"
    else:
        unit_text = "Celsius"


    if data["cod"] == "404":
        text_1.delete(1.0, tkinter.END)
        text_1.insert(tkinter.END, "City not found")
        return

    text_1.delete(1.0, tkinter.END)
    text_1.insert(tkinter.END, f"Current temperature in {city_name}: {data['main']['temp']} {unit_text}")
    text_1.insert(tkinter.END, f"\nDescription: {data['weather'][0]['description']}")
    text_1.insert(tkinter.END, f"\nHumidity: {data['main']['humidity']}%")
    text_1.insert(tkinter.END, f"\nWind speed: {data['wind']['speed']} {unit_text}")
    text_1.insert(tkinter.END, f"\nLow: {data['main']['temp_min']} {unit_text}")
    text_1.insert(tkinter.END, f"\nHigh: {data['main']['temp_max']} {unit_text}")
    text_1.insert(tkinter.END, f"\nPressure: {data['main']['pressure']} hpa")
    text_1.insert(tkinter.END, f"\nVisibility: {data['visibility']} meters")

app = customtkinter.CTk()
app.geometry("500x880")
app.title("Weather Look-up")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Weather Look up",justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Search", command=search)
button_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter City Name:")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["F", "C"])
optionmenu_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=450, height=300)
text_1.pack(pady=10, padx=10)

### Default Settings ###
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
optionmenu_1.set("F")

app.mainloop()