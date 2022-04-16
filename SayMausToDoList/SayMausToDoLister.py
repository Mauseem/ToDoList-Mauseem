from asyncio import tasks
import tkinter
import tkinter.messagebox
from turtle import bgcolor
import pickle

# Create the mainframe
root = tkinter.Tk()
root.title("SayMaus ToDoList")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title = "Warning!", message = "You must enter as task.")

def delete_tasks():
    try:
        task_index = listbox_tasks.curselection()
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title = "Warning!", message = "You must select a task.")

def load_tasks():
    tasks = pickle.load(open("tasks.dat","rb"))
    for task in tasks:
        listbox_tasks.insert(tkinter.END , task)

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("task.dat","wb"))

# Create the GUI
#Create the frame
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

# Create the listbox
listbox_tasks = tkinter.Listbox(frame_tasks,height = 10, width = 50)
listbox_tasks.pack(side=tkinter.LEFT)

#Create scroll bar

Scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
Scrollbar_tasks.pack(side=tkinter.RIGHT, fill = tkinter.Y)

listbox_tasks.config(yscrollcommand = Scrollbar_tasks.set)
Scrollbar_tasks.config(command = listbox_tasks.yview)
# Create entry widget
entry_task = tkinter.Entry(root, width = 50)
entry_task.pack()

#create button
button_add_task = tkinter.Button(root, text = "Add Task", width = 45 , command = add_task)
button_add_task.pack()
button_delete_task = tkinter.Button(root, text = "Delete Task", width = 45 , command = delete_tasks)
button_delete_task.pack()
button_load_task = tkinter.Button(root, text = "Load Task", width = 45 , command = load_tasks)
button_load_task.pack()
button_save_task = tkinter.Button(root, text = "Save Task", width = 45 , command = save_tasks)
button_save_task.pack()




root.mainloop()
