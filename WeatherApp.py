from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox

def data_get():
    city = city_name.get().title()

    # API correction for city names
    if city == "Chattogram":
        city_api = "Chittagong"
    elif city == "Barishal":
        city_api = "Barisal"
    else:
        city_api = city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_api},BD&appid=15f734a3ad982dc6ef8ae2d143a87732"
    
    try:
        data = requests.get(url).json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", "Check your internet connection.")
        return

    if data.get("cod") == 200:
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=f"{data['main']['temp'] - 273.15:.2f} °C")
        pre_label1.config(text=f"{data['main']['pressure']} hPa")
        hum_label1.config(text=f"{data['main']['humidity']} %")
        rain = data.get("rain", {}).get("1h")
        rain = f"{rain} mm" if rain else "No recent rain"
        precep_label1.config(text=rain)
    else:
        messagebox.showerror("Error", f"City '{city}' not found or API error.")
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        pre_label1.config(text="N/A")
        hum_label1.config(text="N/A")
        precep_label1.config(text="N/A")

win = Tk()
win.title("Sajid Weather App")
win.config(bg="red")
win.geometry("500x670")

# Update to Poppins font
name_label = Label(win, text="Sajid Weather App", font=("Poppins", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Dhaka", "Chattogram", "Khulna", "Rajshahi", "Barishal", "Sylhet", "Rangpur", "Mymensingh"]
com = ttk.Combobox(win, values=list_name, font=("Poppins", 20), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

done_button = Button(win, text="Done", font=("Poppins", 20, "bold"), command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

w_label = Label(win, text="Weather Climate", font=("Poppins", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Poppins", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Poppins", 17))
wb_label.place(x=25, y=320, height=50, width=210)

wb_label1 = Label(win, text="", font=("Poppins", 17))
wb_label1.place(x=250, y=320, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Poppins", 20))
temp_label.place(x=25, y=380, height=50, width=210)

temp_label1 = Label(win, text="", font=("Poppins", 20))
temp_label1.place(x=250, y=380, height=50, width=210)

pre_label = Label(win, text="Pressure", font=("Poppins", 20))
pre_label.place(x=25, y=440, height=50, width=210)

pre_label1 = Label(win, text="", font=("Poppins", 20))
pre_label1.place(x=250, y=440, height=50, width=210)

hum_label = Label(win, text="Humidity", font=("Poppins", 20))
hum_label.place(x=25, y=500, height=50, width=210)

hum_label1 = Label(win, text="", font=("Poppins", 20))
hum_label1.place(x=250, y=500, height=50, width=210)

precep_label = Label(win, text="Precipitation (1h)", font=("Poppins", 18))
precep_label.place(x=25, y=560, height=50, width=210)

precep_label1 = Label(win, text="", font=("Poppins", 18))
precep_label1.place(x=250, y=560, height=50, width=210)

win.mainloop()


