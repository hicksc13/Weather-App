import requests
import tkinter as tk

API_KEY = "83536a95d4dd86b3883578912f0f2d0f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class MyGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Weather Look-up")

        self.location_var = tk.StringVar()
        self.location_var.set("")

        self.label = tk.Label(self.root, text="Please Enter a city name or zipcode", font=('Arial', 20))
        self.label.pack(padx=20, pady=20)

        self.char_name = tk.Entry(self.root, textvariable = self.location_var, font = ('calibre',10,'normal'))
        self.char_name.pack()

        self.sub_btn=tk.Button(self.root,text = 'Submit', command = self.search)
        self.sub_btn.pack()
        self.root.mainloop()


    def search(self, *args):
        name_entered = self.location_var.get()
        request_url = f"{BASE_URL}?appid={API_KEY}&q={name_entered}"
        response = requests.get(request_url)
        data = response.json()
        weather = data['weather'][0]['description']
        temperature_kelvin = round(data["main"]["temp"] - 273.15, 2)
        temperature = round(temperature_kelvin*1.8+32, 2)
        return temperature


MyGui()

