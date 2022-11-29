import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    num=btn["text"]
    if num=="=":
        pass
    else: #「=」以外

    #tkm.showinfo("",f"{num}ボタンがクリックされました")
        entry.insert(tk.END,num)


root=tk.Tk() #Pythonで大文字から始まるものはクラス名これをrootという変数に代入

root.geometry("300x500")

entry=tk.Entry(root,justify="right",width=10,font=("",40))#代替半角３０文字くらいはいるよって意味

entry.grid(row=0,column=0,columnspan=3)


r=1
c=0


for num in range(9,-1,-1):
    button=tk.Button(root,text=f"{num}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%3==0:
        r+=1
        c=0

operators=["+","="]
for ope in operators:
    button=tk.Button(root,text=f"{ope}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%3==0:
        r+=1
        c=0


root.mainloop() #ウィンドウ表示