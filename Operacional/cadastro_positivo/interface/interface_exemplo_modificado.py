import tkinter as tk
from time import sleep

class classe_teste():
    def __init__(self):
        print('hellos')
    

teste = classe_teste()


# def say_hi():
#     print('hi')

root = tk.Tk()
botao = tk.Button(root)
botao['text'] = 'print say hi'
# botao['command'] = say_hi()
# botao.pack(side='bottom')
root.mainloop()
