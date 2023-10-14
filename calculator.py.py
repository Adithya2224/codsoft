#importing tkinter 
import tkinter as tk

#button click
def b_click(event):
    t=event.widget.cget('text')
    
    if t=='=':
        try:
            res= eval(ent.get())
            ent.delete(0, tk.END)         #Entry 
            ent.insert(tk.END, str(res))
        except Exception:
            ent.delete(0, tk.END)
            ent.insert(tk.END, 'Error')
    elif t=='C':
        ent.delete(0, tk.END)
    else:
        ent.insert(tk.END, t)

#window creation for the Calculator

x = tk.Tk()
x.title("Calculator")

ent = tk.Entry(x, font=('Times New Roman',16))
ent.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

#seperate Frame for buttons

buttons_f= tk.Frame(x)
buttons_f.pack()
#button elements
buttons_t = ['7','8', '9', '+', '4', '5', '6', '-','1', '2', '3', '*','C', '0', '=', '/']
row, col = 0, 0
for t in buttons_t:
    button = tk.Button(buttons_f, text=t, padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind('<Button-1>', b_click)
    col += 1
    #button placement
    if col > 3:
        col = 0
        row += 1
#window mainloop
x.mainloop()