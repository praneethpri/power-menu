import customtkinter

def main():
    customtkinter.set_appearance_mode('light')
    root = customtkinter.CTk()
    root.title("Power Options")
    root.geometry("600x200")
    root.attributes('-topmost', True)
    root.attributes('-type', 'dialog')
    root.grid_rowconfigure(0, weight=1, minsize=50)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    button_shutdown = customtkinter.CTkButton(master=root, text='Shutdown')
    button_shutdown.grid(row=0, column=0, padx=1, pady=1)
    button_restart = customtkinter.CTkButton(master=root, text='Restart')
    button_restart.grid(row=0, column=1, padx=1, pady=1)
    root.mainloop()

main()
