import tkinter as tk
import requests

# Variablen
COINDESK_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


# Funktionen
def preis_berechnen():
    try:
        bitcoin = requests.get(COINDESK_API_URL)
        bitcoin_dict = bitcoin.json()
        aktueller_preis = bitcoin_dict["bpi"]["EUR"]["rate_float"]
        preis = float(bitcoin_entry.get()) * aktueller_preis
        euro_wert.set("€{:.2f}".format(preis))
    except ValueError:
        fehler_label = tk.Label(fenster, text="Bitte einen gültigen Zahlenwert eingeben!")
        fehler_label.pack()


# Hauptfenster Einstellungen
fenster = tk.Tk()
fenster.geometry("500x500")
fenster.title("Bitcoin Preis Rechner")
foto = tk.PhotoImage(file="logo.png")
fenster.iconphoto(False, foto)
fenster.configure(background="#4C6793")
fenster.minsize(width=500, height=500)
fenster.maxsize(width=1000, height=1000)

# Variablen
euro_wert = tk.StringVar()

# Widgets Platzieren
bicoin_label = tk.Label(fenster, text="Bitte die Anzahl der Bitcoin eingeben", font=("Arial", 15), background="#8BBCCC")
bicoin_label.pack(side="top", fill="x", padx=10, pady=5)

bitcoin_entry = tk.Entry(fenster, font=("Arial", 15), text="0")
bitcoin_entry.pack(side="top", fill="x", padx=10, pady=5)

euro_label = tk.Label(fenster, text="Ausgabe Preis in Euro", font=("Arial", 15), background="#8BBCCC")
euro_label.pack(side="top", fill="x", padx=10, pady=5)

euro_display = tk.Entry(fenster, font=("Arial", 15), textvariable=euro_wert)
euro_display.pack(side="top", fill="x", padx=10, pady=5)

quit_button = tk.Button(fenster, text="Beenden", font=("Arial", 15), command=fenster.destroy, background="#5C2E7E")
quit_button.pack(side="bottom", fill="x", padx=10, pady=10)

calculate_button = tk.Button(fenster, text="Berechnung durchführen", font=("Arial", 15), command=preis_berechnen, background="#5C2E7E")
calculate_button.pack(side="bottom", fill="x", padx=10, pady=10)

# Mainloop
fenster.mainloop()
