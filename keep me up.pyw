import time
import pyautogui
import PySimpleGUI as sg
import multiprocessing

def KeepUI():
    
    sg.theme('Dark')
    layout = [
       # [sg.Button('X', button_color=('white', 'red',), size=(3, 2), font=('Wingdings', 7), pad=(0,0))],
        [sg.Text('Keep-Me-Up is now running.\nClose it to disable it.')],
    ]
    window = sg.Window('Keep-Me-Up', layout, size=(200,50), element_justification='right', finalize=True) #no_titlebar=True

    
    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'X'):
            if p2.is_alive(): 
                p2.terminate()
            break

def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = KeepUI)
    p1.start()
