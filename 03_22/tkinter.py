import tkinter as tk

root = tk.Tk() # Создание окна

root.title("App")
root.geometry("500x500")
root.resizable(False,False)
pole = tk.Label(root, text="Hello world!")
pole.pack(side=tk.RIGHT)

right_label = tk.Label(root, text="(- _ -)")
right_label.pack(side=tk.RIGHT)



pole2 = tk.Label(root, text="Привет мир!")
pole2.pack(side=tk.LEFT)

left_label = tk.Label(root, text="(- _ -)")
left_label.pack(side=tk.LEFT)

pole3 = tk.Label(root, text="How are you?")
pole3.pack(side=tk.TOP)

top_label = tk.Label(root, text="(- _ -)")
top_label.pack(side=tk.TOP)

pole4 = tk.Label(root, text="Как дела?")
pole4.pack(side=tk.BOTTOM)

bottom_label = tk.Label(root, text="(- _ -)")
bottom_label.pack(side=tk.BOTTOM)

open = False

def print_hi() :
    global open
    print("Hi")

    if open:
        top_label.config(text="(- _ -)")
        open = False
    else:
        top_label.config(text="(0 _ 0)")
        open = True
        bottom_label.config(text=user_input.get())

button = tk.Button(root, text="Нажми на меня!", command=print_hi)
button.pack(side=tk.BOTTOM)

user_input = tk.Entry(root)
user_input.pack(side=tk.TOP)


root.mainloop() # Запуск
