import tkinter
import random
window = tkinter.Tk()
window.title('моё окно')
window.geometry('600x500')
lable = tkinter.Label(text='0', fg='black', bg='red', font = 'Arial 22')
lable.place(x=200,y=200)
def random_colors():
    colors=['red', 'green', 'black', 'brown', 'blue']
    lable['bg'] = random.choice(colors)
def count():
    random_colors()
    num = int(lable['text'])
    num = num +1 
    lable['text'] = str(num)
button = tkinter.Button(text='кнопка', command = count)
button.place(x=10,y=10)

window.mainloop()
