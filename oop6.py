import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Label1")
label2 = tkinter.Label(main_window, text = "Label2")

tombol1 = tkinter.Button(main_window, text = "tombol1")
tombol2 = tkinter.Button(main_window, text = "tombol2")

label1.pack()
label2.pack()
tombol2.pack()
tombol1.pack()

main_window.mainloop()