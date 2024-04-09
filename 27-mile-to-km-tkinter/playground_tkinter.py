import tkinter


def button_clicked():
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("Gui")
window.minsize(width=600, height=600)
window.config(padx=100, pady=100)  #can be used with widgets
#Label

my_label = tkinter.Label(text="label", font=("Arial", 25, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text 2")

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.place(x=100, y=100)

#input = tkinter.Entry(width=10)
#input.grid(column=1, row=1)  #grid can't be used with place/pack




window.mainloop()
