import tkinter

TEXT1 = "is equal to"
TEXT2 = "0"
TEXT3 = "Miles"
TEXT4 = "Km"


def convert_to_km():
    in_miles = float(mile_entry.get())
    in_km = round(1.6 * in_miles, 3)
    label2.config(text=str(in_km))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=250)
window.config(pady=20, padx=20)

mile_entry = tkinter.Entry(width=11)
mile_entry.insert(tkinter.END, string="0")
mile_entry.grid(row=0, column=1)

label1 = tkinter.Label(text=TEXT1)
label1.grid(row=1, column=0)

label2 = tkinter.Label(text=TEXT2)
label2.config(padx=5, pady=5)
label2.grid(row=1, column=1)

label3 = tkinter.Label(text=TEXT3)
label3.grid(row=0, column=2)

label4 = tkinter.Label(text=TEXT4)
label4.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", width=11, command=convert_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()