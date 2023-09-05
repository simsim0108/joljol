import tkinter


root = tkinter.Tk()
root.title("Canvas에 화면 그리기")
create_image = tkinter.Canvas(width=480, height=300)
create_image.pack()
img_bg = tkinter.PhotoImage(file="park.png")
create_image.create_image(240, 150, image=img_bg)
root.mainloop()
