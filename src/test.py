import tkinter as tk

root = tk.Tk()
root.title('Hello world')
root.geometry("500x500")

my_canvas = tk.Canvas(root, width=500, height=500, bg='red')
my_canvas.pack()


def create_line(x1, y1, x2, y2): 
  return lambda: my_canvas.create_line(x1, y1, x2, y2, fill='white')


my_canvas.after(2000, create_line(0, 0, 500, 500))
my_canvas.after(3000, create_line(0, 500, 500, 0))

root.mainloop()