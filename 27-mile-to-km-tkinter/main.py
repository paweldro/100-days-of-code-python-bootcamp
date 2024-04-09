import tkinter


def calc_button_clicked():
    miles = miles_input.get()
    if miles.replace(".", "").isnumeric() and miles.count(".") <= 1:
        km = float(miles) * 1.609344
        conversion_label.config(text=str(km))
    else:
        conversion_label.config(text="input error")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=600)
window.config(padx=10, pady=10)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

conversion_label = tkinter.Label(text="0", font=("Arial", 15))
conversion_label.grid(column=1, row=1)
conversion_label.config(padx=10, pady=10)

calc_button = tkinter.Button(text="Calculate", command=calc_button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
