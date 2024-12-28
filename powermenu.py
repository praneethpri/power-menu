import tkinter
import customtkinter

customtkinter.set_appearance_mode('light')

root = customtkinter.CTk()

root.geometry("300x400")

button = customtkinter.CTkButton(master=root, text='Hello')

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()
