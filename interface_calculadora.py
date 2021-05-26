import PySimpleGUI as sg
from projeto_calculadora import Calculadora

#Vamos Criar uma Classe que vai conter nosso app
class App():
    def __init__(self):
        self.theme = sg.theme('Reddit')
        self.window = sg.Window('PyCalculator',layout=layout,margins=(0,0),resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1,5):
            for button in layout[i]:
                button.expand(expand_x = True, expand_y = True)

    ## Aqui serão definidas as funçoes do nosso menu_layout
    def menu(self):
        sg.popup('About','Just an example','Contact me')

    ##definir a função que mostra o resultado no visor da calculadora
    def resulter(self):
        if self.oper == '+':
            return Calculadora.soma(float(self.result),float(self.values['-BOX-']))
        if self.oper == '-':
            return Calculadora.subtracao(float(self.result),float(self.values['-BOX-']))
        if self.oper == '*':
            return Calculadora.multiplicacao(float(self.result),float(self.values['-BOX-']))
        if self.oper == '/':
            return Calculadora.divisao(float(self.result),float(self.values['-BOX-']))

    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None,'Exit',sg.WIN_CLOSED):
                break

            self.eventos_do_menu(event)

            self.eventos_dos_numeros(event)

            self.evento_do_clear(event)

            self.eventos_do_backarrow(event)

            self.eventos_dos_operadores(event)

    def eventos_do_menu(self,event):
        if event in ('About'):
            self.menu()

    def eventos_dos_numeros(self,event):
        codigos_dos_eventos = {'-ONE-': '1', '-TWO-': '2', '-THREE-': '3', '-FOUR-': '4', '-FIVE-': '5',
                               '-SIX-': '6', '-SEVEN-': '7', '-EIGHT-': '8', '-NINE-': '9', '-ZERO-': '0'}

        if event in (codigos_dos_eventos):
            if self.values['-BOX-'] == '0':
                self.window['-BOX-'].Update(value=codigos_dos_eventos[event])
            else:
                self.window['-BOX-'].update(value=self.values['-BOX-'] + codigos_dos_eventos[event])

    def evento_do_clear(self,event):
        if event in ('-CLEAR-'):
            self.result = 0
            self.window['-BOX-'].update(value=self.result)

    def eventos_do_backarrow(self,event):
        if event in ('-BACKARROW-'):
            self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

    def eventos_dos_operadores(self,event):
        if event in ('-PLUS-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '+'
                self.result = self.values['-BOX-']
            self.window['-BOX-'].update(value='')

        if event in ('-MINUS-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '-'
                self.result = self.values['-BOX-']
            self.window['-BOX-'].update(value='')

        if event in ('-DIV-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '/'
                self.result = self.values['-BOX-']
            self.window['-BOX-'].update(value='')

        if event in ('-TIMES-'):
            if self.oper != '':
                self.result = self.resulter()
            else:
                self.oper = '*'
                self.result = self.values['-BOX-']
            self.window['-BOX-'].update(value='')

        if event in ('-RESULT-'):
            self.result = self.resulter()
            self.window['-BOX-'].update(value=self.result)
            self.result = 0
            self.oper = ''







#menu layout
menu_layout = [
               ['File',['Save','Exit']],
               ['Tools',['Waiting']],
               ['Help',['About']]
               ]
#Elementos dentro da nossa tela
layout =[[sg.Menu(menu_layout)],
         [sg.Input('0',size =(int(15),1), font=('Consolas',20),key='-BOX-'), #visor da calculadora
          sg.Button('<-',font=('Consolas',20),key='-BACKARROW-'), #Botao de apagar ultimo digitado
          sg.Button('C',font=('Consolas',20),key = '-CLEAR-')], #Botao para limpar tudo
         #ROW 2
         [sg.Button('7',font=('Consolas',20),key='-SEVEN-'),
          sg.Button('8',font=('Consolas',20),key='-EIGHT-'),
          sg.Button('9',font=('Consolas',20),key='-NINE-'),
          sg.Button('+',font=('Consolas',20),key='-PLUS-'),
          sg.Button('*',font=('Consolas',20),key='-TIMES-')],
         #ROW 3
         [sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
          sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
          sg.Button('6', font=('Consolas', 20), key='-SIX-'),
          sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
          sg.Button('/', font=('Consolas', 20), key='-DIV-')],
         #ROW 4
         [sg.Button('1', font=('Consolas', 20), key='-ONE-'),
          sg.Button('2', font=('Consolas', 20), key='-TWO-'),
          sg.Button('3', font=('Consolas', 20), key='-THREE-'),
          sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
          sg.Button('=', font=('Consolas', 20), key='-RESULT-')]
         ]
App().start()
'''

'''
