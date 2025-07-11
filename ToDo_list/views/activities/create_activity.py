import tkinter as tk
from tkinter import messagebox as mb
from db.operations import ToDo
from tkcalendar import DateEntry
from views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, FOURTH_COLOR, TITLE, TEXT, TEXT_COLOR


def show_create_activity(w: tk.Tk):
    for widget in w.winfo_children():
        widget.destroy()

    w.columnconfigure(0,weight=1)
    w.columnconfigure(1,weight=1)
    w.columnconfigure(2,weight=1)

    for i in range(6):
        w.rowconfigure(i,pad=10)

    title = tk.Label(w,text="VISTA PARA CREAR ACTIVIDADES", font= TITLE, fg=FOURTH_COLOR,bg=PRIMARY_COLOR)
    title.grid(column=0,row=0,columnspan=3,sticky="n",pady=20)

    text_labels =["Titulo:", "Descripción:", "Fecha de la actividad:"]

    for i in range(3):
        tk.Label(w,text=text_labels[i], font=TEXT, bg=PRIMARY_COLOR, fg=TEXT_COLOR).grid(column=0, row=i+1, sticky="en")

    entry_title = tk.Entry(w,font=TEXT)
    entry_title.grid(column=1, row=1, columnspan=3,sticky="nw", ipadx=70, padx=10)
    entry_description = tk.Entry(w,font=TEXT)
    entry_description.grid(column=1, row=2, columnspan=3,sticky="nw", ipadx=70, padx=10)
    entry_date = DateEntry(w, width= 20, year = 2025, month = 7, day = 1, selectmode ='day')
    entry_date.grid(column=1, row=3, columnspan=3,sticky="nw", ipadx=70, padx=10)

    def enviar():
        data={}
        data["title"] = entry_title.get()
        data["description"] = entry_description.get()
        data["date"] = entry_date.get_date()
        status, msg = ToDo(data)
        if not status:
            mb.showerror("Ocurrió un error: ", msg)
            return
        mb.showinfo("Actividad creada!", msg)
        show_create_activity(w)
        

    tk.Button (w,font=TEXT, text= "GUARDAR", fg= TEXT_COLOR, bg=SECONDARY_COLOR ,relief="flat",command=enviar).grid(column=0,row=4,columnspan=3,sticky="n")


