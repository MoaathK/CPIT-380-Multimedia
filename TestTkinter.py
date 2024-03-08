import tkinter as tk
r = tk.Tk()
r.geometry("500x300")
r.title('test')
button = tk.Button(r,text='Does it work?',width=25,command=r.destroy)
button.pack(side='bottom', padx=10, pady=10)
button.pack()
r.mainloop()

#### this is How to get the value from a scrollbar ####
'''
def show_value():
    print(scale.get())

root = tk.Tk()
root.geometry("200x150")
# Create a Scale widget
scale = tk.Scale(root, from_=1, to=100, orient='horizontal')
scale.pack(padx=20, pady=20)

 #Button to print the current value of the scale
button = tk.Button(root, text="Get Value", command=show_value)
button.pack()

root.mainloop()

'''
