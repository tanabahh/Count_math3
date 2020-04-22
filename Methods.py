from Functions import *


class NewtonMethod:
    def __init__(self, a, b, accuracy, function, derived_function, second_derived_function):
        self.a = a
        self.b = b
        self.accuracy = accuracy
        self.function = function
        self.derived_function = derived_function
        self.second_derived_function = second_derived_function
        self.result = False

    def is_convergence(self):
        a = self.a
        previous = self.derived_function(a)
        while a < self.b:
            if self.derived_function(a)*previous < 0:
                return False
            previous = self.derived_function(a)
            a += (self.b-self.a)/10000
        return self.function(self.a)*self.function(self.b) < 0

    def first_approach(self):
        a = self.a
        while a < self.b:
            if self.derived_function(a)*self.second_derived_function(a) > 0:
                return a
            a += (self.b - self.a) / 10000
        return a

    def second_approach(self, first_x):
        return first_x - self.function(first_x)/self.derived_function(first_x)

    def find_answer(self):
        if self.is_convergence():
            first_x = self.first_approach()
            second_x = self.second_approach(first_x)
            while abs(first_x - second_x) > self.accuracy:
                first_x = second_x
                second_x = self.second_approach(first_x)
            self.result = second_x


class SimpleIteration:
    def __init__(self, a, b, accuracy, function, derived_function):
        self.a = a
        self.b = b
        self.accuracy = accuracy
        self.function = function
        self.derived_function = derived_function
        self.result = False
        maximum = max(self.derived_function(self.a), self.derived_function(self.b), self.derived_function(0))
        minimum = min(self.derived_function(self.a), self.derived_function(self.b), self.derived_function(0))
        self.const = 2 / (maximum + minimum)

    def is_convergence(self):
        return (self.function(self.a)*self.function(self.b) < 0) and (self.a - self.b < 0.2)

    def first_approach(self):
        return self.a

    def second_approach(self, first_x):
        print(first_x)
        return first_x - self.const*self.function(first_x)

    def find_answer(self):
        if self.is_convergence():
            first_x = self.first_approach()
            second_x = self.second_approach(first_x)
            while abs(first_x - second_x) > self.accuracy:
                first_x = second_x
                second_x = self.second_approach(first_x)
                self.result = second_x


class SimpleIterationForSystems:
    def __init__(self, x, y, accuracy, function, function_y):
        self.accuracy = accuracy
        self.function = function
        self.function_y = function_y
        self.result = [x, y]  # x, y

    def is_convergence(self):
        try:
            if (self.function == s) and (self.function_y == sin_y):
                return abs(derived_s_x(self.result[0])) + abs(derived_sin_y(self.result[1])) < 1
            if (self.function == s) and (self.function_y == minus_s_y):
                return abs(derived_s_x(self.result[0])) + abs(derived_minus_s_y(self.result[1])) < 1
            if (self.function == minus_s) and (self.function_y == sin_y):
                return abs(derived_minus_s_x(self.result[0])) + abs(derived_sin_y(self.result[1])) < 1
            if (self.function == minus_s) and (self.function_y == sin_y):
                return abs(derived_minus_s_x(self.result[0])) + abs(derived_sin_y(self.result[1])) < 1
            if (self.function == cube) and (self.function_y == sin_y):
                return abs(derived_cube_x(self.result[0])) + abs(derived_sin_y(self.result[1])) < 1
            if (self.function == cube) and (self.function_y == s_y):
                return abs(derived_cube_x(self.result[0])) + abs(derived_s_y(self.result[1])) < 1
            if (self.function == cube) and (self.function_y == minus_s_y):
                return abs(derived_cube_x(self.result[0])) + abs(derived_minus_s_y(self.result[1])) < 1
        except:
            return False


    def next_approach(self):
        return [self.function_y(self.result[1]), self.function(self.result[0])]

    def get_answer(self):
        iteration = 1
        if not self.is_convergence():
            print("Yes")
            return iteration
        try:
            print(self.result)
            next_it = self.next_approach()
            print(next_it)
            while(iteration < 400000) and (max(abs(self.result[0] - next_it[0]), abs(self.result[1] - next_it[1])) >
                                           self.accuracy):
                self.result[0] = next_it[0]
                self.result[1] = next_it[1]
                next_it = self.next_approach()
                iteration += 1
            if iteration >= 400000:
                return iteration
            else:
                return self.result
        except:
            return False
