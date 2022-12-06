import tkinter as tk
import maze_maker as mm
import random





def count_up(): #sキーが押されたらカウントダウン開始
    global tmr 
    global jid
    label["text"]=tmr #ラベルのテキストにカウントダウンを表示させる
    tmr=tmr+1
    jid=root.after(1000,count_up) #１００ミリ秒ごと（１秒）にカウントアップ関数を呼び出される
    


def key_down(event):
    global key
    key=event.keysym
    

def key_up(event):
    global key
    key=""




   



def main_proc():#常時起動するリアルタイム処理関数
    global cx,cy,mx,my
    if key=="Up":my -=1
    if key=="Down":my+=1
    if key=="Right":mx+=1
    if key=="Left":mx-=1

    if maze_lst[mx][my]==1: #移動先がかべだったら
        if key=="Up":my +=1
        if key=="Down":my-=1
        if key=="Right":mx-=1
        if key=="Left":mx+=1

    cx=mx*100+50
    cy=my*100+50
    canvas.coords("koukaton",cx,cy)#工科とん座標が動く
    
    root.after(100,main_proc)


if __name__=="__main__":
    root=tk.Tk()
    label=tk.Label(root,text="-",font=("",80))
    label.pack()
    tmr=0
    jid=None
    count_up()
    root.bind("<KeyPress>",key_down)#何かのキーが押されたらキーダウンに移動

    

    root.title("友達を探すこうかとん")#タイトル
    #root.geometry("1500x900")
    canvas=tk.Canvas(root,width=1500,height=900,bg="skyblue") #ウィンドウの初期設定
    canvas.pack()


    maze_lst=mm.make_maze(15,9) #15*9のマス目
    #print(maze_lst)
    mm.show_maze(canvas,maze_lst)
    mx,my=1,1
    dx,dy=13,5
    cx,cy=mx*100+50,my*100+50
    ex,ey=dx*100+50,dy*100+50

    

    koukaton=tk.PhotoImage(file="fig/4.png")
    tomodati=tk.PhotoImage(file="fig/2.png")
    canvas.create_image(cx,cy,image=koukaton,tag="koukaton")
    canvas.create_image(ex,ey,image=tomodati,tag="friend")
    key=""
    root.bind("<s>",key_down)
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    

 

    main_proc()
    
    
    
    root.mainloop()

