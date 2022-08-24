import tkinter as tk
import tkinter.simpledialog as sd
import math as m
import os

class my_calculator():
    def __init__(self, root):
        print(os.getcwd())
        self.root=root
        self.root.title('My_calculator')
        self.root.resizable(False, False)
        self.text_results=[]
        self.special_functions_var=tk.StringVar()
        self.mode_var=tk.StringVar()
        self.mode_var.set('radians')
        self.constants=tk.Menubutton(self.root, text='Constants', activebackground='yellow')
        self.constants.grid(row=0, column=0, columnspan=2)
        self.constants.menu=tk.Menu(self.constants, tearoff=0)
        self.constants['menu']=self.constants.menu
        self.constants.menu.add_command(label='add', activebackground='blue', command=self.add_constant)
        self.constants.menu.add_command(label='delete', activebackground='red', command=self.delete_constant)
        self.mode=tk.Menubutton(self.root, text='Mode', activebackground='yellow')
        self.mode.grid(row=0, column=2, columnspan=1)
        self.mode.menu=tk.Menu(self.mode, tearoff=0)
        self.mode['menu']=self.mode.menu
        self.mode.menu.add_radiobutton(label='radians', activebackground='green', variable=self.mode_var, value='radians', command=self.change_mode)
        self.mode.menu.add_radiobutton(label='degrees', activebackground='green', variable=self.mode_var, value='degrees', command=self.change_mode)
        self.more_functions=tk.Menubutton(self.root, text='More\nfunctions', activebackground='yellow')
        self.more_functions.grid(row=0, column=3, columnspan=1)
        self.more_functions.menu=tk.Menu(self.more_functions, tearoff=0)
        self.more_functions['menu']=self.more_functions.menu
        self.more_functions.menu.add_command(label='numbers arithmetic bases', activebackground='green', command=self.run_arithmetic_bases_program)
        self.more_functions.menu.add_command(label='solve arithmetic systems', activebackground='green', command=self.run_arithmetic_systems_program)
        self.history=tk.Menubutton(self.root, text='History', activebackground='yellow')
        self.history.grid(row=0, column=4, columnspan=2)
        self.history.menu=tk.Menu(self.history, tearoff=0)
        self.history['menu']=self.history.menu
        self.history.menu.add_command(label='show previous result', activebackground='blue', command=self.show_previous_result)
        self.history.menu.add_command(label='clear constants_file', activebackground='red', command=self.clear_constants_file)
        self.input_bar=tk.Entry(self.root, font='Calibri 25')
        self.input_bar.grid(row=1, column=0, columnspan=6, sticky=tk.NW)
        self.input_bar_eye=tk.Label(self.root, text='◉')
        self.input_bar_eye.grid(row=1, column=5, sticky=tk.NE)
        self.input_bar_eye.bind('<Enter>', self.show_input_bar_context)
        self.input_bar_eye.bind('<Leave>', self.hide_input_bar_context)
        self.constants_descriptions_label=tk.Label(self.root, text='', font='Calibri 10')
        self.constants_descriptions_label.grid(row=2, column=0, columnspan=5, sticky=tk.N)
        self.mode_label=tk.Label(self.root, text='{}'.format(self.mode_var.get()), font='Arial 10')
        self.mode_label.grid(row=2, column=2, sticky=tk.S)
        self.plus_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='+', text='+', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.plus_sign.grid(row=3, column=0)
        self.minus_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='-', text='-', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.minus_sign.grid(row=4, column=0)
        self.multiplication_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='*', text='*', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.multiplication_sign.grid(row=5, column=0)
        self.division_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='/', text='/', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.division_sign.grid(row=6, column=0)
        self.power_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='**', text='^', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.power_sign.grid(row=3, column=1)
        self.open_bracket=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='(', text='(', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.open_bracket.grid(row=5, column=1)
        self.close_bracket=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value=')', text=')', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.close_bracket.grid(row=6, column=1)
        self.factorial_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='!', text='!', font='Calibri 20', width=1, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.factorial_sign.grid(row=4, column=1, sticky=tk.W)
        self.square_root_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='√', text='√', font='Calibri 20', width=2, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.square_root_sign.grid(row=4, column=1, sticky=tk.E)
        self.asin_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='asin', text='a', font='Calibri 20', width=1, height=1, bg='lightgreen', fg='black', command=self.special_functions_result)
        self.asin_sign.grid(row=3, column=2, sticky=tk.W)
        self.acos_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='acos', text='a', font='Calibri 20', width=1, height=1, bg='lightgreen', fg='black', command=self.special_functions_result)
        self.acos_sign.grid(row=4, column=2, sticky=tk.W)
        self.atan_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='atan', text='a', font='Calibri 20', width=1, height=1, bg='lightgreen', fg='black', command=self.special_functions_result)
        self.atan_sign.grid(row=5, column=2, sticky=tk.W)
        self.sin_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='sin', text='sin', font='Calibri 20', width=2, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.sin_sign.grid(row=3, column=2, sticky=tk.E)
        self.cos_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='cos', text='cos', font='Calibri 20', width=2, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.cos_sign.grid(row=4, column=2, sticky=tk.E)
        self.tan_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='tan', text='tan', font='Calibri 20', width=2, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.tan_sign.grid(row=5, column=2, sticky=tk.E)
        self.ln_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='ln', text='ln', font='Calibri 20', width=3, height=1, bg='lightblue', fg='black', command=self.special_functions_result)
        self.ln_sign.grid(row=6, column=2)
        self.point_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='.', text='.', font='Calibri 20', width=3, height=1, bg='green', fg='black', command=self.write_EntryBox)
        self.point_sign.grid(row=6, column=3)
        self.equal_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='=', text='=', font='Calibri 20', width=3, height=1, bg='red', fg='black', command=self.result)
        self.equal_sign.grid(row=6, column=5)
        self.clear_sign=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='C', text='C', font='Calibri 20', width=3, height=1, bg='brown', fg='black', command=self.clear_EntryBox)
        self.clear_sign.grid(row=2, column=5)
        self.num1=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='1', text='1', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num1.grid(row=5, column=3)
        self.num2=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='2', text='2', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num2.grid(row=5, column=4)
        self.num3=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='3', text='3', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num3.grid(row=5, column=5)
        self.num4=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='4', text='4', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num4.grid(row=4, column=3)
        self.num5=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='5', text='5', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num5.grid(row=4, column=4)
        self.num6=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='6', text='6', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num6.grid(row=4, column=5)
        self.num7=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='7', text='7', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num7.grid(row=3, column=3)
        self.num8=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='8', text='8', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num8.grid(row=3, column=4)
        self.num9=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='9', text='9', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num9.grid(row=3, column=5)
        self.num0=tk.Radiobutton(self.root, indicator=False, variable=self.special_functions_var, value='0', text='0', font='Arial 20', width=3, height=1, bg='yellow', fg='black', command=self.write_EntryBox)
        self.num0.grid(row=6, column=4)
        self.root.bind('<Return>', self.result)
    def write_EntryBox(self):
        self.input_bar.insert('end', self.special_functions_var.get())
    def clear_EntryBox(self):
        self.input_bar.delete('0', 'end')
    def show_input_bar_context(self, event):
        self.text_context=''
        for i in range(len(self.input_bar.get())//56+1):
            self.text_context=self.text_context+self.input_bar.get()[56*i:56*(i+1)]+'\n'
        self.context_label=tk.Label(self.root, text=self.text_context)
        self.context_label.grid(row=2, column=0, columnspan=6, sticky=tk.NW)
    def hide_input_bar_context(self, event):
        try:
            self.context_label.destroy()
        except:
            pass
    def result(self, event=None):
        try:
            self.result=eval(self.input_bar.get())
            self.text_results.append(self.result)
            self.clear_EntryBox()
            self.input_bar.insert('end', self.result)
            print(self.result)
        except:
            pass
    def special_functions_result(self):
        try:
            self.number_radians=float(self.input_bar.get())
            if self.mode_var.get()=='radians':
                self.number=float(self.input_bar.get())
            elif self.mode_var.get()=='degrees':
                self.number=m.pi*float(self.input_bar.get())/180  
            if self.special_functions_var.get()=='√':
                self.result=m.sqrt(float(self.input_bar.get()))
            elif self.special_functions_var.get()=='!':
                self.result=m.factorial(float(self.input_bar.get()))
            elif self.special_functions_var.get()=='sin':
                self.result=m.sin(self.number)
            elif self.special_functions_var.get()=='cos':
                self.result=m.cos(self.number)
            elif self.special_functions_var.get()=='tan':
                self.result=m.tan(self.number)
            elif self.special_functions_var.get()=='asin':
                self.result=m.asin(self.number_radians)
                if self.mode_var.get()=='degrees':
                    self.result=180*self.result/m.pi
            elif self.special_functions_var.get()=='acos':
                self.result=m.acos(self.number_radians)
                if self.mode_var.get()=='degrees':
                    self.result=180*self.result/m.pi
            elif self.special_functions_var.get()=='atan':
                self.result=m.atan(self.number_radians)
                if self.mode_var.get()=='degrees':
                    self.result=180*self.result/m.pi
            elif self.special_functions_var.get()=='ln':
                self.result=m.log(float(self.input_bar.get()))
            self.clear_EntryBox()
            self.input_bar.insert('end', self.result)
            self.text_results.append(self.result)
            print(self.result)   
        except:
            pass
    def add_constant(self):
        constants_buttons.constants_file_controlvar=0
        self.ask_constant_symbol=sd.askstring(parent=self.root, title='Add a constant', prompt='Give the symbol:')
        self.ask_constant_value=sd.askstring(parent=self.root, title='Add a constant', prompt='Give the value:')
        self.ask_constant_description=sd.askstring(parent=self.root, title='Add a constant', prompt='Give the description:')
        if type(self.ask_constant_symbol) is str and type(self.ask_constant_value) is str and type(self.ask_constant_description) is str and self.ask_constant_symbol!='' and self.ask_constant_value!='' and self.ask_constant_description!='':
            constants_buttons(self.root, self.ask_constant_symbol, self.ask_constant_value, self.ask_constant_description)
    def delete_constant(self):
        self.ask_delete_constant=sd.askstring(parent=self.root, title='Delete a constant', prompt='Give the symbol of the constant you want to delete:')
        try:
            self.constant_index=constants_buttons.list_constants_symbols.index(self.ask_delete_constant)
            constants_buttons.list_constants[self.constant_index].destroy()
            constants_buttons.list_constants[self.constant_index]=0
            constants_buttons.list_constants_symbols[self.constant_index]=0
            self.text_constants=[]
            with open(os.getcwd()+'\my_calculator_constants.txt', 'r') as constants_file:
                for line in constants_file:
                    self.text_constants.append(line[:-1])
            constants_file.close()
            for i in range(len(self.text_constants)):
                if self.ask_delete_constant in self.text_constants[i] and '(deleted)' not in self.text_constants[i]:
                    self.text_constants[i]=self.text_constants[i]+' (deleted)'
                    break
            constants_file=open(os.getcwd()+'\my_calculator_constants.txt', 'w')
            for item in self.text_constants:
                constants_file.write(item+'\n')
            constants_file.close()
        except:
            pass
    def change_mode(self):
        self.mode_label.configure(text=self.mode_var.get())
    def run_arithmetic_bases_program(self):
        os.system(r"python C:\Users\prila\Desktop\Python_projects\calculator\arithmetic_bases_program.py")
    def run_arithmetic_systems_program(self):
        os.system(r"python C:\Users\prila\Desktop\Python_projects\calculator\arithmetic_systems_program.py")
    def show_previous_result(self):
        try:
            self.input_bar.insert('end', self.text_results[-1])
            self.text_results.pop(-1)
        except:
            pass
    def clear_constants_file(self):
        self.message_clear_constants_file=sd.messagebox.askokcancel(parent=self.root, title='Clear constants_file', message='Are you sure you want to delete all stored constants from the constants_file?')
        if self.message_clear_constants_file==True:
            constants_file=open(os.getcwd()+'\my_calculator_constants.txt', 'w')
            constants_file.close()

class constants_buttons(my_calculator):
    list_constants=[]
    list_constants_symbols=[]
    constants_file_controlvar=0
    def __init__(self, root, constant_symbol, constant_value, constant_description):
        self.root=root
        self.constant_symbol=constant_symbol
        self.constant_value=constant_value
        self.constant_description=constant_description
        if constants_buttons.constants_file_controlvar==0:
            constants_file=open(os.getcwd()+'\my_calculator_constants.txt', 'a')
            constants_file.seek(2)
            constants_file.write(self.constant_symbol+'|||'+self.constant_value+'|||'+self.constant_description+'\n')
            constants_file.close()
        if 0 in constants_buttons.list_constants_symbols:
            self.constant_index=constants_buttons.list_constants_symbols.index(0)
            constants_buttons.list_constants_symbols[self.constant_index]=self.constant_symbol
        else:
            constants_buttons.list_constants_symbols.append(self.constant_symbol)
            self.constant_index=len(constants_buttons.list_constants_symbols)-1
        self.constant_button=tk.Radiobutton(self.root, indicator=False, variable=calculator.special_functions_var, value='{}'.format(self.constant_value), text='{}'.format(self.constant_symbol), font='Calibri 20', width=3, height=1, bg='blue', fg='black', command=calculator.write_EntryBox)
        self.constant_button.grid(row=7+self.constant_index//6, column=self.constant_index%6)
        try:
            constants_buttons.list_constants[self.constant_index]=self.constant_button
        except:
            constants_buttons.list_constants.append(self.constant_button)
        self.constant_button.bind('<Enter>', self.show_constant_description)
        self.constant_button.bind('<Leave>', self.hide_constant_description)
    def show_constant_description(self, event):
        if '\\n' in self.constant_description:
            calculator.constants_descriptions_label.configure(text=self.constant_description.split('\\n')[0]+'\n'+self.constant_description.split('\\n')[1])
        else:
            calculator.constants_descriptions_label.configure(text=self.constant_description)
    def hide_constant_description(self, event):
        calculator.constants_descriptions_label.configure(text='')

def create_start_constants():
        constants_buttons.constants_file_controlvar=1
        with open(os.getcwd()+'\my_calculator_constants.txt', 'r') as constants_file:
            for line in constants_file:
                if '(deleted)' not in line:
                    try:
                        constants_features=line.split('|||')
                        constants_buttons(calculator.root, constants_features[0], constants_features[1], constants_features[2][:-1])
                    except:
                        pass
        constants_file.close()
        
root=tk.Tk()
calculator=my_calculator(root)
create_start_constants()
root.mainloop()
