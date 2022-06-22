
import tkinter

class CalculatorService():

    def __init__(self):
        self.calculatorTextVariable = None
        self.operator = "DEFAULT"
        self.listOfOperatorButtons = []
        self.inputs = []
        self.currentInput = ""

    def __manageOperatorButtonBindings(self, operator, bg):
        for [op, val] in self.listOfOperatorButtons:
            if op == operator:
                val.canvas.itemconfig("Frame", fill=bg)
                val.canvas.unbind("<Leave>")
                val.canvas.unbind("<Enter>")
            else:
                val.canvas.bind("<Enter>", val.cache["onHover"])
                val.canvas.bind("<Leave>", val.cache["onLeave"])
                val.canvas.itemconfig("Frame", fill="#00d498")

    def setOperator(self, operator, button, bg):
        self.operator = operator
        operators = [op for [op, val] in self.listOfOperatorButtons]

        if operator not in operators:
            self.listOfOperatorButtons.append([operator, button])

        operatorMap = {"ADDITION" : '+', "SUBTRACTION" : '-', "MULTIPLICATION" : '*', "DIVISION" : '/'}

        self.inputs.append(int(self.currentInput))
        self.currentInput = ""
        self.calculatorTextVariable.set(self.calculatorTextVariable.get() + ' ' + operatorMap[operator])

        self.__manageOperatorButtonBindings(operator, bg)

    def clear(self):
        self.calculatorTextVariable.set("0")
        self.currentInput = ""
        
        if self.operator != "DEFAULT":
            self.operator = "DEFAULT"
            self.__manageOperatorButtonBindings("DEFAULT", "")
            return
        
        print('Clicked: Clear')

    def backspace(self):
        #Code here
        print('Clicked: Backspace')

    def evaluate(self):
        print(self.inputs)
        if not self.currentInput:
            return    
        
        self.inputs.append(int(self.currentInput))
        print(self.inputs)
        if len(self.inputs) != 2:
            return
        
        if self.operator == "ADDITION":
            result = self.inputs[0] + self.inputs[1]
        elif self.operator == "SUBTRACTION":
            result = self.inputs[0] - self.inputs[1]
        elif self.operator == "MULTIPLICATION":
            result = self.inputs[0] * self.inputs[1]
        elif self.operator == "DIVISION":
            result = self.inputs[0] / self.inputs[1]
        elif self.operator == "DEFAULT":
            return
        
        self.inputs = [result]
        self.currentInput = ""
        self.calculatorTextVariable.set(str(result))

        self.operator = "DEFAULT"
        self.__manageOperatorButtonBindings("DEFAULT", "")

        #print('Clicked: Evaluate')

    def percentage(self):
        #Code here
        print('Clicked: Percentage')

    def decimal(self):
        #Code here
        print('Clicked: Decimal')

    def positiveNegative(self):
        #Code here
        print('Clicked: Positive Negative')

    def numberClick(self, num):
        self.currentInput += str(num)
        self.calculatorTextVariable.set(self.currentInput)