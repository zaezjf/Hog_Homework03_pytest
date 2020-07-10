class Calculator:

    def isstr(self, a, b):
        if isinstance(a, str):
            return 0
        if isinstance(b, str):
            return 0

    def add(self, a, b):
        if self.isstr(a, b) == 0:
            return "非法输入，只能进行数字运算"
        else:
            return a + b

    def red(self, a, b):
        if self.isstr(a, b) == 0:
            return "非法输入，只能进行数字运算"
        else:
            return a - b

    def mul(self, a, b):
        if self.isstr(a, b) == 0:
            return "非法输入，只能进行数字运算"
        else:
            return a * b

    def div(self, a, b):
        if self.isstr(a, b) == 0:
            return "非法输入，只能进行数字运算"
        elif b == 0:
            return "非法输入，除数不能为0"
        else:
            return a / b
