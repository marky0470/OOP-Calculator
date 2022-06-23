
import tkinter
from unittest import result

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

        if self.currentInput:
            self.inputs.append(self.convertToNum(self.currentInput))
        self.currentInput = ""

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
        if self.currentInput == "0" or self.operator != "DEFAULT":
            return
        self.currentInput = self.currentInput[:-1]
        self.calculatorTextVariable.set(self.currentInput)
        print('Clicked: Backspace')

    def evaluate(self):
        if not self.currentInput:
            return    
        
        self.inputs.append(self.convertToNum(self.currentInput))
        
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

        decimalPlace = max([len(str(float(x)).split('.')[1]) for x in self.inputs])
        result = round(result, decimalPlace)
        
        self.inputs = [result]
        self.currentInput = ""
        self.calculatorTextVariable.set(str(result))

        self.operator = "DEFAULT"
        self.__manageOperatorButtonBindings("DEFAULT", "")

        print('Clicked: Evaluate')

    def percentage(self):
        if not self.inputs:
            return
        self.inputs[0] /= 100
        self.calculatorTextVariable.set(str(self.inputs[0]))
        print('Clicked: Percentage')

    def decimal(self):
        if len(self.currentInput.split('.')) == 2:
            return
        self.currentInput += (".")
        self.calculatorTextVariable.set(self.currentInput)
        print('Clicked: Decimal')

    def positiveNegative(self):
        if not self.currentInput:
            return
        self.currentInput = str(self.convertToNum(self.currentInput) * -1)
        self.calculatorTextVariable.set(self.currentInput)
        print('Clicked: Positive Negative')

    def convertToNum(self, num):
        try: 
            return int(num)
        except ValueError:
            return float(num)

    def numberClick(self, num):
        self.currentInput += str(num)
        self.calculatorTextVariable.set(self.currentInput)