from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert_miles():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text=f"{km}")



calculate_button = Button(text="Calculate", command=convert_miles)
calculate_button.grid(column=1, row=2)

result = Label(text="")
result.grid(column=1, row=1)


miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)



km_text = Label(text="Km")
km_text.grid(column=2, row=1)


is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

miles_input = Entry()
miles_input.grid(column=1, row=0)

window.mainloop()
