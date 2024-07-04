import tkinter as tk

from tkinter import messagebox

#add fun
def add_task():
    task = ent.get()
    if task:
        lb.insert(tk.END,task)
        ent.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning",'Please enter a task')

#del fun
def del_task():
    try:
        tasks_list=lb.curselection()[0]
        lb.delete(tasks_list)
    except IndexError:
        messagebox.showwarning("Warning",'Select a task to delete')
        
#main window
x=tk.Tk()
x.title('To-Do List')

#adding Entry of the tasks
ent=tk.Entry(x,font=('Times New Roman', 16))
ent.pack(pady=10)

#buttons for adding and deleting the tasks.
b1=tk.Button(x,text='Add Task',command=add_task)
b1.pack()
b2=tk.Button(x,text='Delete Task',command=del_task)
b2.pack()

#displaying tasks in the mentioned font
lb=tk.Listbox(x,font=("Times New Roman", 16))
lb.pack()

#mainloop() to return and continue
x.mainloop()
