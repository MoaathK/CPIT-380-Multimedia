import tkinter as tk

def getScale(scale,x):
    selectValue = int(scale.get())
    
    print(type(selectValue))
    print("test!")
    print(selectValue)

r =tk.Tk()
r.geometry("200x150")
scale = tk.Scale(r , from_=1 ,to=100,orient='horizontal')
scale.pack(pady=10)
button = tk.Button(r, text="Get Value" ,command=lambda: getScale(scale,1))
button.pack(pady=10)

r.mainloop()