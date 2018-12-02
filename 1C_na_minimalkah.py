from sys import exit
from tkinter import *

def add_key(event):
    key = ent.get()
    l = Label(bg='black', fg='white', width=50)
    with open("test.txt", "r+") as file:
        for line in file:
            if key == "":
                l['text'] = ' '.join("You can't create empty key")
                l.pack()
                return "You can't create empty key"
            if line.split(":")[0] == key:
                l['text'] = ' '.join("This key already exists")
                l.pack()
                return "This key already exists"
        file.write(f'{key}:\n')
        l['text'] = ' '.join(f'Кеу "{key}" created')
    l.pack()

def get_value(key: str):
    with open("test.txt", "r") as file:
        for line in file:
            if line.split(":")[0] == key and line.split != "":
                return (line.split(":")[1])
            else:
                return "Key with this name don't exist\nCheck key name"


def search_of_line(key: str):
    with open("test.txt", "r") as file:
        i = -1
        lines = file.readlines()
        try:
            while True:
                i = i + 1
                if lines[i].split(":")[0] == key:
                    return i
        except IndexError:
            print("CHECK KEY NAME")
            exit()


def search_of_byte(key: str):
    with open("test.txt", "r") as file:
        file.read()
        x = file.tell()
    with open("test.txt", "r") as file:
        i = 0
        count = 0
        for line in file:
            if i <= search_of_line(key):
                count = count + len(line)
                i = i + 1
        if count is None == True:
            return x
        else:
            return count


def add_value(event):
    x=0
    entered=ent.get()
    key=entered.split(" ")[0]
    value=entered.split(" ")[1]
    l = Label(bg='black', fg='white', width=50)
    with open("test.txt", "r") as file:
        for line in file:
            if len(line)==len(key)+2:
                if line.split(":")[0] == key:
                    with open("test.txt", "r+") as file:
                        file.seek(search_of_byte(key))
                        remaining = file.read()
                    with open("test.txt", "r+") as file:
                        file.seek(search_of_byte(key) - 1)
                        file.write(f' {value}\n')
                        file.write(remaining)
                        x=1
            else:
                if line.split(":")[0] == key:
                    with open("test.txt", "r+") as file:
                        file.seek(search_of_byte(key))
                        remaining = file.read()
                    with open("test.txt", "r+") as file:
                        file.seek(search_of_byte(key)-1)
                        file.write(f', {value}\n')
                        file.write(remaining)
                        x=1
    if x==0:
        l['text'] = ' '.join("No key with this name")
    else:
        l['text'] = ' '.join("Value added")
    l.pack()

root = Tk()
ent = Entry(width=50)
add_key_Button = Button(text="Add new key")
add_value_Button = Button(text="Add new value")

add_key_Button.bind('<Button-1>', add_key)
add_value_Button.bind('<Button-1>', add_value)

ent.pack()
add_key_Button.pack()
add_value_Button.pack()
root.mainloop()
