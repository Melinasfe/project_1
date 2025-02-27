from tkinter import *
win = Tk()
win.geometry('300x400')

#=======Function
def insert():
    name = ent_name.get()
    lst_name.insert(0,name)
    ent_name.delete(0,END)

def delete():
    # lst_name.delete(0,END)
    index = lst_name.curselection()
    lst_name.delete(index)
    # print(index)

#=======Widget
ent_name= Entry (win,font= 'arial 12')
ent_name.pack(pady=20)

lst_name = Listbox(win,font= 'arial 12')
lst_name.pack()

for i in range(20):
    lst_name.insert(END,f'{i+1}- This is a test')

btn_insert = Button(win,text= 'Insert',command=insert)
btn_insert.pack(pady=20)    
btn_delete = Button(win,text= 'Delete',command=delete)
btn_delete.pack(pady=20)    

win.mainloop()











