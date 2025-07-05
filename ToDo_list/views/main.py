import tkinter as tk 
from views.resources import PRIMARY_COLOR
from views.activities.create_activity import show_create_activity

main_window = tk.Tk()
main_window.state("zoomed")
main_window.config(bg=PRIMARY_COLOR)
show_create_activity(main_window)


