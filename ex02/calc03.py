import tkinter as tk
from tkinter import ttk
 
# Define
BUTTON = [
    ['AC', '', '', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]
 
SYMBOL = ['+', '-', '*', '/']
 
class CaluGui(object):
    def __init__(self, root=None):
        # Define
        self.calc_str = '' # 計算用の文字列
 
        # Window Setting
        root.title('授業用電卓') # Window のタイトル
        #root.geometry('300x450') # Window のサイズ
 
        # Frame Setting
        calc_frame = ttk.Frame(root, width=300, height=100) 
        calc_frame.pack(side=tk.TOP, padx=10, pady=20) # 余白の設定
        button_frame = ttk.Frame(root, width=300, height=400) # 計算ボタン用のフレーム
        button_frame.pack(side=tk.BOTTOM) # 余白の設定
 
        # Parts Setting
        self.calc_var = tk.StringVar() # 計算式用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, font=("",20)) # 計算式用のLabel
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, font=("",15)) # 結果用のLabel
        calc_label.pack(anchor=tk.E) # 右揃えに設定
        ans_label.pack(anchor=tk.E) # 右揃えに設定
 
        for y, row in enumerate(BUTTON, 1): # 
            for x, num in enumerate(row):
                button = tk.Button(button_frame, text=num, font=('', 15),width=6,height=3,bg="#696969", fg='#ffffff')
                                     
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.click_button) #

            

        
            
    
    def click_button(self, event):#演算の設定
        check = event.widget['text'] # 押したボタンのCheck
 
        if check == '=': # イコールの場合
            if self.calc_str[-1:] in SYMBOL: # 記号よりも前で計算
                self.calc_str = self.calc_str[:-1]
 
            res = '= ' + str(eval(self.calc_str)) # eval関数の利用
            self.ans_var.set(res)
        elif check == 'AC': # ACが押されたら計算式を消す様に設定
            self.calc_str = ''
            self.ans_var.set('')
       
        elif check in SYMBOL: # 記号の場合
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL: # 
                self.calc_str = self.calc_str[:-1] + check
        else: # 数字などの場合
            self.calc_str += check
 
        self.calc_var.set(self.calc_str)
    
 
 
def main():
    # Window Setting
    root = tk.Tk()
    # Window size non resizable
    root.resizable(width=False, height=False)
    CaluGui(root)
    # Display
    root.mainloop() 
 
if __name__ == '__main__':
    main()