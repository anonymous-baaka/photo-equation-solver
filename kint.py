import tkinter as tk
import wolframapi

class Window:
    def __init__(self,root,equation):
        self.root=root
        self.equation=equation

        self.canvas=tk.Canvas(self.root)
        self.canvas.pack()

        self.inputTextBox=tk.Text(self.canvas,height=3,width=50,font=("Arial", 20))
        self.inputTextBox.insert("1.0",self.equation)
        self.inputTextBox.pack()

        self.solveButton=tk.Button(self.canvas,text="solve",height=3,width=6,command=self.evaluate,font=("Arial", 15))
        self.solveButton.pack()

        self.outputTextBox = tk.Text(self.canvas,height=6,width=50,font=("Arial", 30))
        self.outputTextBox.pack()

    def evaluate(self):
        print("called, equation= ",self.equation)
        equation=self.inputTextBox.get("1.0",tk.END)
        result=wolframapi.doit(equation)
        self.setOutputValue(result)

    def setOutputValue(self,results):
        op=""
        print("setop callled")
        print("result= ",results)
        self.outputTextBox.delete("1.0",tk.END)
        for result in results:
            op+=result+"\n"
            print("op= ",op)
        self.outputTextBox.insert("1.0",op)

def createWindow(equation):
    root=tk.Tk()
    window=Window(root,equation)
    root.mainloop()
    return root
    #root.mainloop()
#createWindow("x+1=2")