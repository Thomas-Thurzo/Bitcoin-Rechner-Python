import tkinter as tk
from tkinter import ttk
import requests

root = tk.Tk()
root.geometry("300x150")
root.title("Bitcoin-Preis-Rechner")

COINDESK_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
euro_value = tk.StringVar(value="Hier wird dann der Preis in Euro angezeigt")

def calculate_price():
    try:
        response = requests.get(COINDESK_API_URL)
        response_dict = response.json()
        current_bitcoin_price_euro = response_dict["bpi"]["EUR"]["rate_float"]
        calculated_price_euro = float(bitcoin_entry.get()) * current_bitcoin_price_euro
        euro_value.set("{:.2f}".format(calculated_price_euro))
    except ValueError:
        print("Bitte einen gültigen Zahlenwert eingeben")


bitcoin_label = ttk.Label(root, text="Anzahl Bitcoin:", font=("Arial", 15))
bitcoin_label.pack(side="top", fill="x", padx=5, pady=2)
bitcoin_entry = ttk.Entry(root, font=("Arial", 15))
bitcoin_entry.pack(side="top", fill="x", padx=5, pady=2)

euro_label = ttk.Label(root, text="Preis in Euro:", font=("Arial", 15))
euro_label.pack(side="top", fill="x", padx=5, pady=2)
euro_display = ttk.Label(root, textvariable=euro_value, font=("Arial", 15))
euro_display.pack(side="top", fill="x", padx=5, pady=2)

calculate_button = ttk.Button(root, text="Berechnung durchführen", command=calculate_price)
calculate_button.pack(side="bottom", fill="x", padx=10, pady=10)


root.mainloop()



