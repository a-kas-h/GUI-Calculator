from tkinter import *

root = Tk()
root.title("GUI Calculator")
root.iconbitmap('GUI-Calculator\calculator_icon-icons.com_72046.ico')
operations = []
def operate(L):
    x = "".join(L)
    result = eval(x)
    return result


def oneClick():
    entryField.insert("end", 1)
    operations.append('1')
def twoClick():
    entryField.insert("end", 2)   
    operations.append('2')
def threeClick():
    entryField.insert("end", 3)
    operations.append('3')
def fourClick():
    entryField.insert("end", 4)
    operations.append('4')    
def fiveClick():
    entryField.insert("end", 5)
    operations.append('5')    
def sixClick():
    entryField.insert("end", 6)
    operations.append('6')
def sevenClick():
    entryField.insert("end", 7)   
    operations.append('7') 
def eightClick():
    entryField.insert("end", 8) 
    operations.append('8')   
def nineClick():
    entryField.insert("end", 9)  
    operations.append('9') 
def zeroClick():
    entryField.insert("end", 0)  
    operations.append('0') 
def plusClick():
    entryField.insert("end", " + ")
    operations.append("+")
def minusClick():
    entryField.insert("end", " - ")
    operations.append("-")
def mulClick():
    entryField.insert("end", " x ")
    operations.append("*")
    
def divClick():
    entryField.insert("end"," ÷ ")
    operations.append("/")

def equalClick():
    global operations
    if len(operations)==0:
        res = entryField.get()
        return eval(res)
    else:
        res = operate(operations)
        entryField.delete(0,'end')
        entryField.insert("end", res)
        operations = [str(res)]

def AllClear():
    global operations
    entryField.delete(0,'end')
    operations = []


entryField = Entry(root, borderwidth=5, width=50, font="Arial 10")
entryField.grid(row=0, columnspan= 4,ipady=10)
myButton1 = Button(root, text="1",command=oneClick,borderwidth=5,padx=40,pady=20)
myButton2 = Button(root, text="2",command=twoClick,borderwidth=5,padx=40,pady=20)
myButton3 = Button(root, text = "3",command=threeClick,borderwidth=5,padx=40,pady=20)
mybutton4 = Button(root, text="4", command=fourClick,borderwidth=5,padx=40,pady=20)
mybutton5 = Button(root, text="5", command=fiveClick,borderwidth=5,padx=40,pady=20)
mybutton6 = Button(root, text="6", command=sixClick,borderwidth=5,padx=40,pady=20)
mybutton7 = Button(root, text="7", command=sevenClick,borderwidth=5,padx=40,pady=20)
mybutton8 = Button(root, text="8", command=eightClick,borderwidth=5,padx=40,pady=20)
mybutton9 = Button(root, text="9", command=nineClick,borderwidth=5,padx=40,pady=20)
mybutton0 = Button(root, text="0", command=zeroClick,borderwidth=5,padx=40,pady=20)
mybuttonPlus = Button(root, text="+", command=plusClick,borderwidth=5,padx=40,pady=20)
myButtonAC = Button(root, text="AC", command=AllClear, borderwidth=5,padx=40,pady=20)
myButtonMinus = Button(root, text="-", command=minusClick, borderwidth=5, padx=40,pady=20)
myButtonMul = Button(root, text="x", command = mulClick, borderwidth=5, padx=40,pady=20)
myButtonDiv = Button(root, text="÷", command=divClick, borderwidth=5,padx=40,pady=20)
equalTo = Button(root, text="=", command=equalClick, borderwidth=5,padx=40,pady=20)
myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2)
mybutton4.grid(row=2, column=0)
mybutton5.grid(row=2, column=1)
mybutton6.grid(row=2, column=2)
mybutton7.grid(row=3, column=0)
mybutton8.grid(row=3, column=1)
mybutton9.grid(row=3, column=2)
mybutton0.grid(row=4, column=0)
mybuttonPlus.grid(row=1, column=3)
myButtonAC.grid(row = 4,column=2)
myButtonMinus.grid(row=2,column=3)
myButtonDiv.grid(row=4,column=3)
myButtonMul.grid(row=3,column=3)
equalTo.grid(row = 4, column=1)
root.mainloop()
