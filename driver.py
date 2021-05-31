import kint
import tkinter as tk
import test

def main():
    equation=test.test('1.jpg')
    root=tk.Tk()
    Window=kint.Window(root,equation)
    root.mainloop()
main()