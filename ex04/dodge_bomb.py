import pygame as pg
import random
import sys


def chec_bound(obj_rct,scr_rct):
    #第一引数：こうかとんrectまたは爆弾ect
    #範囲内:　＋１/範囲外： -1
    yoko,tate =+1,+1
    if obj_rct.left < scr_rct.left or sct_rct.right < obg_rct.right:
        hoge
    if obj_rct.top < scr_rct.top or sct_rct.bottom < obg_rct.bottom:
        fuge
    return yoko,tate
    


def main():
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct=scrn.sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 

    pg.display.update()
    clock.tick(1000)

    bomb_sfc=pg.Surface((20,20)) #正方形の空のSurface
    bomb_sfc.set__colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct=bomb_sfc.get_rect()
    bomb_rct.centerx=random.randint(0,scrn_rct.width)
    bomb_rct.centery=random.randint(scrn_rct.height,0)
    scrn_sfc.blit(bomb_sfc,bomb_rct)

    bomb_sfc.blit(bomb_sfc,bomb_rct)
    


    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dct=pg.key.get_pressed()#辞書型
        if key_dct[pg.K_UP]:
            tori_rct.ventery -= 1

        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -=1

        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx +=1

        vx,vy= +1,+1
        bomb_rct.move_ip(vx,vy)
        yoko,tate=check_bound(bomb_rct,scrn_rct)
        vx *=yoko
        vy *=tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()