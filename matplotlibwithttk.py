#погрешность!!!!
from tkinter import *
import tkinter.ttk as ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Functions import *
from Methods import *
import matplotlib.pyplot as plt



def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Лаборатоная работа 3")
        self.minsize(640, 400)
        nb = ttk.Notebook(self)
        self.answer_label = Label(self, text="Здесь появится ответ")
        self.answer_label.pack()
        validation = (self.register(self.onValidate), '%P')
        nb.pack(fill='both', expand='yes')
        child = ttk.Frame(self)
        self.var_for_methods = IntVar()
        self.var_for_methods.set(0)
        method1 = Radiobutton(child, text="Метод касательных", variable=self.var_for_methods, value=0)
        method1.pack()
        method2 = Radiobutton(child, text="Метод простой итерации", variable=self.var_for_methods, value=1)
        method2.pack()
        self.a = StringVar()
        self.b = StringVar()
        a_label = Label(child, text="Введите левую границу:")
        a_label.pack()
        border_a = ttk.Entry(child, textvariable=self.a,  validate="key", validatecommand=validation)
        border_a.pack()
        b_label = Label(child, text="Введите правую границу:")
        b_label.pack()
        border_b = ttk.Entry(child, textvariable=self.b, validate="key", validatecommand=validation)
        border_b.pack()
        equation_label = Label(child, text="Выберите уравнение:")
        equation_label.pack()
        self.var = IntVar()
        self.var.set(0)
        equation1 = Radiobutton(child, text="x^3 + x + 2 = 0", variable=self.var, value=0)
        equation1.pack()
        equation2 = Radiobutton(child, text="x^2 - 2 = 0", variable=self.var, value=1)
        equation2.pack()
        equation3 = Radiobutton(child, text="2x + 1 = 0", variable=self.var, value=2)
        equation3.pack()
        self.accuracy = StringVar()
        accuracy_label = Label(child, text="Введите точность:")
        accuracy_label.pack()
        accuracy_entry = ttk.Entry(child, textvariable=self.accuracy, validate="key",  validatecommand=validation)
        accuracy_entry.pack()
        button = Button(child, text="Посчитать", command=self.do_equation)
        button.pack()

        child2 = ttk.Frame(self)
        name_label = Label(child2, text="Метод простой итерации")
        name_label.pack()
        x_label = Label(child2, text="Введите начальное приближение для x:")
        x_label.pack()
        border_x = ttk.Entry(child2, textvariable=self.a,  validate="key", validatecommand=validation)
        border_x.pack()
        y_label = Label(child2, text="Введите начальное приближение для y:")
        y_label.pack()
        border_y = ttk.Entry(child2, textvariable=self.b, validate="key", validatecommand=validation)
        border_y.pack()
        equation2_label = Label(child2, text="Выберите уравнение:")
        equation2_label.pack()
        self.checkbox_var1 = BooleanVar()
        self.checkbox_var1.set(0)
        self.checkbox_var2 = BooleanVar()
        self.checkbox_var2.set(0)
        self.checkbox_var3 = BooleanVar()
        self.checkbox_var3.set(0)
        self.checkbox_var4 = BooleanVar()
        self.checkbox_var4.set(0)
        equation_check1 = Checkbutton(child2, text="3x^2 + 1 - y = 0", variable=self.checkbox_var1,
                                      onvalue=1, offvalue=0)
        equation_check1.pack()
        equation_check2 = Checkbutton(child2, text="6sin(x) - y = 0", variable=self.checkbox_var2,
                                      onvalue=1, offvalue=0)
        equation_check2.pack()
        equation_check3 = Checkbutton(child2, text="-3x^2 + 1 = y", variable=self.checkbox_var3,
                                      onvalue=1, offvalue=0)
        equation_check3.pack()
        equation_check4 = Checkbutton(child2, text="3x^3 = y", variable=self.checkbox_var4,
                                      onvalue=1, offvalue=0)
        equation_check4.pack()
        accuracy2_label = Label(child2, text="Введите точность:")
        accuracy2_label.pack()
        accuracy2_entry = ttk.Entry(child2, textvariable=self.accuracy, validate="key", validatecommand=validation)
        accuracy2_entry.pack()
        button2 = Button(child2, text="Посчитать", command=self.do_system)
        button2.pack()

        nb.add(child, text='Уравнения')
        nb.add(child2, text='Системы')

    def do_system(self):
        checkbox = self.checkbox_var1.get() + self.checkbox_var2.get() + self.checkbox_var3.get()\
                   + self.checkbox_var4.get()
        if checkbox != 2:
            self.answer_label.config(text="Выберите 2 функции")
        else:
            if self.checkbox_var1.get() and self.checkbox_var2.get():
                function = s
                function_y = sin_y
                function_for_graph = sin
            elif self.checkbox_var1.get() and self.checkbox_var3.get():
                function = s
                function_y = minus_s_y
                function_for_graph = minus_s
            elif self.checkbox_var1.get() and self.checkbox_var4.get():
                function = cube
                function_y = s_y
                function_for_graph = s
            elif self.checkbox_var3.get() and self.checkbox_var4.get():
                function = cube
                function_y = minus_s_y
                function_for_graph = minus_s
            elif self.checkbox_var2.get() and self.checkbox_var4.get():
                function = cube
                function_y = sin_y
                function_for_graph = sin
            else:
                function = minus_s
                function_y = sin_y
                function_for_graph = sin
            if (function_y == sin_y) and ((float(self.b.get()) < -6) or (float(self.b.get()) > 6)):
                self.answer_label.config(text="Для лучшей точности была выбрана функция arcsin, "
                                              "пожалуйста введите -6 <= y <= 6 ")
            else:
                method = SimpleIterationForSystems(float(self.a.get()), float(self.b.get()), float(self.accuracy.get()),
                                                   function, function_y)
                answer = method.get_answer()
                if answer == 400000:
                    answer = "Превышено максимальное число допустимых операций. Промежуточный результат" + \
                                "x = " + str(method.result[0]) + " y = " + str(method.result[1])
                else:
                    if (type(answer) != list) and (type(answer) != bool) and (answer < 400000):
                        answer = "Не выполнилось условие сходимости метода"
                    elif type(answer) == bool:
                        answer = "Компьютер не может такое посчитать, произошло переполнение в питоне0_o"
                    else:
                        answer = "x = " + str(method.result[0]) + " y = " + str(method.result[1])
                self.answer_label.config(text=answer)
                plt.title("График")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.grid()
                x = np.linspace(method.result[0]-5, method.result[0]+5, 50)
                plt.plot(x, [function(i) for i in x])
                plt.plot(x, [function_for_graph(i) for i in x])
                plt.plot(x, [0 for i in x], "r--")
                plt.scatter(method.result[0], method.result[1], color='red', s=20, marker='o')
                plt.show()

    def do_equation(self):
        if self.var.get() == 0:
            function = f
            derived_function = derived_f
            second_derived_function = second_derived_f
        elif self.var.get() == 1:
            function = g
            derived_function = derived_g
            second_derived_function = second_derived_g
        else:
            function = z
            derived_function = derived_z
            second_derived_function = second_derived_z
        if self.var_for_methods.get() == 0:
            method = NewtonMethod(float(self.a.get()), float(self.b.get()), float(self.accuracy.get()), function,
                                 derived_function, second_derived_function)
            method.find_answer()
            if method.result:
                self.answer_label.config(text=method.result)
                plt.title("График")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.grid()
                x = np.linspace(float(self.a.get()), float(self.b.get()), 50)
                plt.plot(x, [function(i) for i in x])
                plt.plot(x, [0 for i in x], "r--")
                plt.scatter(method.result, function(method.result), color='red', s=20, marker='o')
                plt.show()
            else:
                self.answer_label.config(text="Не выполнено условие сходимости")
        else:
            method = SimpleIteration(float(self.a.get()),
                                     float(self.b.get()),
                                     float(self.accuracy.get()),
                                     function,
                                 derived_function)
            method.find_answer()
            if method.result:
                self.answer_label.config(text=method.result)
                plt.title("График")
                plt.xlabel("x")
                plt.ylabel("y")
                plt.grid()
                x = np.linspace(float(self.a.get()), float(self.b.get()), 50)
                plt.plot(x, [function(i) for i in x])
                plt.plot(x, [0 for i in x], "r--")
                plt.scatter(method.result, function(method.result), color='red', s=20, marker='o')
                plt.show()
            else:
                self.answer_label.config(text="Слишком большой интервал, возьмите расстояние не больше 0.2 "
                                              "либо на этом интервале нет корней")

    def onValidate(self, P):
        return is_digit(P)

    def draw_graphic(self):
        return True

    def matplot_canvas(self):
        f = Figure(figsize=(1, 1), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)



root = Root()
root.mainloop()