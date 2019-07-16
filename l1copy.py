import Tkinter as tk

def l1copy():
    pass
    return

main = tk.Tk()
ment = tk.StringVar()

main.title("L1 Copy")
main.geometry("450x450+500+300")

label = tk.Label(main,text='My Label').pack()
inputbox = tk.Entry(main, width=20, bg="light grey").pack()
button = tk.Button(main,text = "Submit" , command= l1copy, fg = "red" , bg = "black").pack()
