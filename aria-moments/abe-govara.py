import pygame
import tkinter as tk
import time
pygame.init()
pygame.mixer.init()
def play():
    pygame.mixer.music.load("holywater.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
        time.sleep(1)
root = tk.Tk()
root.geometry('400x200')
root.resizable(False,False)
tk.Label(root , text="click for abe govara").pack()
tk.Button(root , text= "..." , command=play).pack()
root.mainloop()