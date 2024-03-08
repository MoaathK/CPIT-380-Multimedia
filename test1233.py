import tkinter as tk

def scaleUpPic(entry):
    x_value = int(entry.get())
    
    print("Scaling up with X value:", x_value)

Scale2 = tk.Tk()
Scale2.geometry("500x300")
Scale2.title('Scalling Up using number of X')

label2 = tk.Label(Scale2, text="Enter the X value you want to scale-up")
label2.grid(row=0, column=0)

e1 = tk.Entry(Scale2)
e1.grid(row=0, column=1)

button = tk.Button(Scale2, text="Scale-Up", command=lambda: scaleUpPic(e1))
button.grid(row=1, column=0, columnspan=2)

buttonExit = tk.Button(Scale2, text="Exit", command=Scale2.destroy)
buttonExit.grid(row=2, column=0, columnspan=2)

Scale2.mainloop()