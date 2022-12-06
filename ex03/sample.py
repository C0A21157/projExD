import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr 
    global jid
    label["text"]=tmr #ラベルのテキストにカウントダウンを表示させる
    tmr=tmr+1
    jid=root.after(1000,count_up) #１００ミリ秒ごと（１秒）にカウントアップ関数を呼び出される


def key_down(event):#eventをとるのが約束
    global jid #書き換えるからグローバル変数

    if jid is not None:#カウントアップ中にキーが押されたら.カウントアップ中でない時はjid is none
        root.after_cancel(jid)
        jid=None
    else:   
        key=event.keysym#どのキーがおされたかを保持する
    #jid=root.after_cancel
        jid=root.after(1000,count_up)
    #tkm.showinfo("キー押下",f"{key}キーが押されました")


if __name__=="__main__":
    root=tk.Tk()
    label=tk.Label(root,text="-",font=("",80))#カウントアップさせる前に”－”が出される
    label.pack() #配置用メソッド
    

    tmr=0
    jid=None
    #count_up() #タイプアップ関数の呼び出し
    root.bind("<KeyPress>",key_down)#何かのキーが押されたらキーダウンに移動
    root.mainloop()

