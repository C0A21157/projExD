import tkinter as tk

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():#常時起動するリアルタイム処理関数
    global cx,cy
    if key=="Up":cy -=20
    if key=="Down":cy+=20
    if key=="Right":cx+=20
    if key=="Left":cx-=20
    canvas.coords("koukaton",cx,cy)#工科とん座標が動く
    root.after(1000,main_proc)


if __name__=="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")
    #root.geometry("1500x900")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    koukaton=tk.PhotoImage(file="fig/4.png")
    cx,cy=300,400
    canvas.create_image(cx,cy,image=koukaton,tag="koukaton")
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyPress>",key_up)
    main_proc()
    root.mainloop()

