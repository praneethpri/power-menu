from tkinter import PhotoImage
import customtkinter
import subprocess
from PIL import Image, ImageTk

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

    image_shutdown = customtkinter.CTkImage(light_image=Image.open('./assets/shutdown-button.jpg'), dark_image=Image.open('./assets/shutdown-button.jpg'), size=(150, 150))
    image_restart = customtkinter.CTkImage(light_image=Image.open('./assets/restart-button.jpg'), dark_image=Image.open('./assets/restart-button.jpg'),size=(150, 150))

    button_shutdown = customtkinter.CTkButton(master=root, image=image_shutdown, command=shutdown_process, text='', fg_color="transparent", hover_color="#551ae5")
    button_shutdown.grid(row=0, column=0, padx=1, pady=1)
    button_restart = customtkinter.CTkButton(master=root, image=image_restart, text='', fg_color="transparent", hover_color="#551ae5")
    button_restart.grid(row=0, column=1, padx=1, pady=1)
    root.mainloop()

def shutdown_process():
    subprocess.run("echo 'hello'", shell=True)

def restart_process():
    subprocess.run("sudo reboot", shell=True)

if __name__ == "__main__":
    main()
