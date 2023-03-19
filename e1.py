# import glob
#
# myFiles = glob.glob('*.txt')
#
# print(myFiles)

import PySimpleGUI as sg

layout = [[sg.InputText(key='input')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
          [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/')]]

window = sg.Window('Calculator', layout)

equation = ''
while True:
    event, values = window.Read()
    if event == 'C':
        equation = ''
    elif event == '=':
        try:
            result = eval(equation)
        except:
            result = 'Error'
        window['input'].Update(result)
        equation = ''
    elif event in ['+', '-', '*', '/']:
        equation += values['input'] + event
        window['input'].Update(equation)
    else:
        equation += event
        window['input'].Update(equation)

window.Close()
