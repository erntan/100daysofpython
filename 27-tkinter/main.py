from tkinter import *

KM_TO_MI = 1.609344

# window = Tk()
# window.title("My first GUI program")
# window.minsize(500, 300)
#
# # Label
# label = Label(text="I am a Label", font=("Arial", 24))
# label.place(x=0,y=100)
# label["text"] = "new text"
# label.config(text="new new text")
#
# # Button
# def button_clicked():
#     label.config(text=input.get())
#
#
# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=2)
#
# # Entry
# input = Entry(width=10)
# input.grid(column=2, row=2)
#
#
# window.mainloop()

window = Tk()
window.title("Mile to KM Converter")

lbl_mi = Label(text="Miles")
lbl_km = Label(text="KM")
lbl_convert = Label(text="is equal to")

textb_mi = Entry()
textb_mi.insert(END, string="0")
textb_km = Entry()
textb_km.insert(END, string="0")


def mikm(dist, convert_to):
    dist = float(dist)
    if convert_to == "mile":
        return dist*KM_TO_MI
    else:
        return dist*1/KM_TO_MI

def button_mikm():
    if textb_mi.get() == "0":
        miles = round(mikm(textb_km.get(),"mile"), 4)
        textb_mi.insert(END, str(miles))
    else:
        kms = round(mikm(textb_mi.get(),"kilometer"), 4)
        textb_km.insert(END, str(kms))

btn_convert = Button(text="Calculate", command=button_mikm)


lbl_mi.grid(column=3, row=1)
lbl_convert.grid(column=1, row=2)
lbl_km.grid(column=3, row=2)
textb_mi.grid(column=2, row=1)
textb_km.grid(column=2, row=2)
btn_convert.grid(column=2, row=3)


window.mainloop()