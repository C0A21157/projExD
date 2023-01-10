import pygame as pg
import sys
import time, random
import tkinter

scene = 0
font1 =("Century",30) #初期画面で使用する文字フォント
font2 =("Century",20)
font3 =("Century",15)

key=""
def key(e):
    global key
    key=e.keysym


def main():
    global scene, jid

    if scene == 0:#初期画面
        canvas.create_text(300,100,text="食べろにょろにょろ",fill="black",font=font1,tag="スタート画面")#タイトル
        canvas.create_text(300,200,text="[操作説明]",fill="black",font=font2,tag="スタート画面")#操作説明
        canvas.create_text(300,250,text="・十字キーで操作してね",fill="black",font=font3,tag="スタート画面")
        canvas.create_text(300,270,text="・アイテムのリンゴを食べたら加速するよ",fill="black",font=font3,tag="スタート画面")
        canvas.create_text(300,290,text="・黄色い■は敵！あたったらライフが減るよ",fill="black",font=font3,tag="スタート画面")
        canvas.create_text(300,310,text="・リンゴを５個あつめたらclear！",fill="black",font=font3,tag="スタート画面")    
        canvas.create_text(300,380,text="スペースキーでスタート",fill="lime",font=font2,tag="スタート画面")
            
        if key == "space": #スペースがおされたらゲーム開始
            #print(0)
            root.after_cancel(jid)#スタート画面削除
            scene = 1
            root.destroy()
        else:
            jid = root.after(100,main)
    
    if scene ==1:
        color_red = pg.Color(255, 0, 0)
        color_white = pg.Color(255, 255, 255)
        color_green = pg.Color(0, 255, 0)
        screen = pg.display.set_mode((600, 400))#ディスプレイのサイズ
        screen.fill(color_white)
        pg.display.set_caption("蛇")
        arr = [([0] * 41) for i in range(61)]  
        x = 10  # 蛇の初期x座標
        y = 10  # 蛇の初期y座標
        foodx = random.randint(1, 60)  # 食べ物のx座標
        foody = random.randint(1, 40)  # 食べ物のy座標
        arr[foodx][foody] = -1
        snake_lon = 3  # 蛇の長さ
        way = 1  # 蛇の運動方向

        while True:
            screen.fill(color_white)
            time.sleep(0.1)
            for event in pg.event.get():  # 监听器
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if (event.key == pg.K_RIGHT) and (way != 2):  # 右
                        way = 1
                    if (event.key == pg.K_LEFT) and (way != 1):  # 左
                        way = 2
                    if (event.key == pg.K_UP) and (way != 4):  # 上
                        way = 3
                    if (event.key == pg.K_DOWN) and (way != 3):  # 下に移動
                        way = 4
            if way == 1:
                x += 1
            if way == 2:
                x -= 1
            if way == 3:
                y -= 1
            if way == 4:
                y += 1
            if (x > 60) or (y > 40) or (x < 1) or (y < 1) or (arr[x][y] > 0):  # 死亡(壁、自分の体をぶつかったら)
                sys.exit()
            arr[x][y] = snake_lon
            for a, b in enumerate(arr, 1):
                for c, d in enumerate(b, 1):
                    # 食べ物は-1，空地は0，蛇の位置は正数
                    if (d > 0):
                        # print(a,c) #蛇の座標を表示
                        arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                        pg.draw.rect(screen, color_green, ((a - 1) * 10, (c - 1) * 10, 10, 10))
                    if (d < 0):
                        pg.draw.rect(screen, color_red, ((a - 1) * 10, (c - 1) * 10, 10, 10))
            if (x == foodx) and (y == foody):   #蛇が食べ物を食べったら
                snake_lon += 1    #長さ+1
                while (arr[foodx][foody] != 0):    #新しい食べ物を表示
                    foodx = random.randint(1, 60)
                    foody = random.randint(1, 40)
                arr[foodx][foody] = -1
            pg.display.update()
        
        
if __name__ == "__main__":
    pg.init()
    root = tkinter.Tk()
    root.title("スタート") #初期画面タイトル
    root.bind("<KeyPress>", key)
    canvas = tkinter.Canvas(width=600, height=400, bg="white") #初期画面の画面サイズ設定
    canvas.pack()
    main()
    root.mainloop()
    pg.quit()
    sys.exit()
           
