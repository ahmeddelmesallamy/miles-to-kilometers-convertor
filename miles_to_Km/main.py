import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Miles to Km")

miles_entry = tk.Entry(window, width=10)
miles_entry.place(x=200, y = 50)

m_label = tk.Label(window, text="Miles")
m_label.place(x=300, y = 50)

K_label = tk.Label(window, text="Km")
K_label.place(x=300, y = 75)

i_label = tk.Label(window, text="is equal to: ")
i_label.place(x=100, y = 75)

total_label = tk.Label(window, text="0")
total_label.place(x=225, y = 75)



def calculate():
    try:
        miles = float(miles_entry.get())
        new_k = miles * 1.6
        total_label.config(text=new_k)
    except ValueError:
        total_label.config(text="Please enter a number.")






calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.place(x=200, y = 100)

















window.mainloop()