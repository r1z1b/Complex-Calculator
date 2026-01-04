from tkinter import *
import math

# ---------------- WINDOW ----------------
var = Tk()
var.title("Complex Calculator")
var.resizable(False, False)

# ---------------- ENTRY ----------------
e = Entry(var, width=25, borderwidth=5, font=("Arial", 18))
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

functionnum = 0.0
mathematics = ""

# ---------------- FUNCTIONS ----------------
def thebutton(num):
    e.insert(END, str(num))

def clear():
    e.delete(0, END)

def set_op(op):
    global functionnum, mathematics
    try:
        functionnum = float(e.get())
        mathematics = op
        e.delete(0, END)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def equal():
    global functionnum
    try:
        num2 = float(e.get()) if e.get() else 0
        e.delete(0, END)

        if mathematics == "add":
            e.insert(0, functionnum + num2)
        elif mathematics == "sub":
            e.insert(0, functionnum - num2)
        elif mathematics == "mul":
            e.insert(0, functionnum * num2)
        elif mathematics == "div":
            e.insert(0, functionnum / num2)
        elif mathematics == "pow":
            e.insert(0, functionnum ** num2)
        elif mathematics == "sqrt":
            e.insert(0, math.sqrt(functionnum))
        elif mathematics == "percent":
            e.insert(0, functionnum / 100)
        elif mathematics == "avg":
            e.insert(0, (functionnum + num2) / 2)
        elif mathematics == "square":
            e.insert(0, functionnum ** 2)
        elif mathematics == "cube":
            e.insert(0, functionnum ** 3)
        elif mathematics == "neg":
            e.insert(0, -functionnum)
        elif mathematics == "abs":
            e.insert(0, abs(functionnum))
        elif mathematics == "fact":
            e.insert(0, math.factorial(int(functionnum)))
        elif mathematics == "inv":
            e.insert(0, 1 / functionnum)
        elif mathematics == "2pow":
            e.insert(0, 2 ** functionnum)

        # Trigonometry (Degrees)
        elif mathematics == "sin":
            e.insert(0, math.sin(math.radians(functionnum)))
        elif mathematics == "cos":
            e.insert(0, math.cos(math.radians(functionnum)))
        elif mathematics == "tan":
            e.insert(0, math.tan(math.radians(functionnum)))
        elif mathematics == "csc":
            e.insert(0, 1 / math.sin(math.radians(functionnum)))
        elif mathematics == "sec":
            e.insert(0, 1 / math.cos(math.radians(functionnum)))
        elif mathematics == "cot":
            e.insert(0, 1 / math.tan(math.radians(functionnum)))

        # Inverse Trigonometry
        elif mathematics == "asin":
            e.insert(0, math.degrees(math.asin(functionnum)))
        elif mathematics == "acos":
            e.insert(0, math.degrees(math.acos(functionnum)))
        elif mathematics == "atan":
            e.insert(0, math.degrees(math.atan(functionnum)))

        # Logs
        elif mathematics == "ln":
            e.insert(0, math.log(functionnum))
        elif mathematics == "log":
            e.insert(0, math.log10(functionnum))
        elif mathematics == "exp":
            e.insert(0, math.exp(functionnum))

    except:
        e.delete(0, END)
        e.insert(0, "Error")

# ---------------- BUTTONS ----------------
btn_cfg = {"width":5, "height":2, "font":("Arial", 10)}

buttons = [
    ("1",1,0),("2",1,1),("3",1,2),("+",1,3,lambda:set_op("add")),
    ("4",2,0),("5",2,1),("6",2,2),("-",2,3,lambda:set_op("sub")),
    ("7",3,0),("8",3,1),("9",3,2),("*",3,3,lambda:set_op("mul")),
    ("=",4,0,equal),("0",4,1),("C",4,2,clear),("/",4,3,lambda:set_op("div")),
    ("x^y",5,0,lambda:set_op("pow")),("√",5,1,lambda:set_op("sqrt")),
    ("%",5,2,lambda:set_op("percent")),("avg",5,3,lambda:set_op("avg")),
    ("sin",6,0,lambda:set_op("sin")),("cos",6,1,lambda:set_op("cos")),
    ("tan",6,2,lambda:set_op("tan")),("csc",6,3,lambda:set_op("csc")),
    ("sec",7,0,lambda:set_op("sec")),("cot",7,1,lambda:set_op("cot")),
    ("x²",7,2,lambda:set_op("square")),("x³",7,3,lambda:set_op("cube")),
    ("ln",8,0,lambda:set_op("ln")),("log",8,1,lambda:set_op("log")),
    ("e^x",8,2,lambda:set_op("exp")),("neg",8,3,lambda:set_op("neg")),
    ("|x|",9,0,lambda:set_op("abs")),("n!",9,1,lambda:set_op("fact")),
    ("2^x",9,2,lambda:set_op("2pow")),("1/x",9,3,lambda:set_op("inv")),
    ("sin⁻¹",10,0,lambda:set_op("asin")),
    ("cos⁻¹",10,1,lambda:set_op("acos")),
    ("tan⁻¹",10,2,lambda:set_op("atan"))
]

for b in buttons:
    if len(b) == 3:
        Button(var, text=b[0], command=lambda x=b[0]: thebutton(x), **btn_cfg)\
            .grid(row=b[1], column=b[2], padx=2, pady=2)
    else:
        Button(var, text=b[0], command=b[3], **btn_cfg)\
            .grid(row=b[1], column=b[2], padx=2, pady=2)

# ---------------- RUN ----------------
var.mainloop()
