from tkinter import *
import time
import random


def Play(player, ai):
    global Draw
    global AI_Score
    global Player_Score
    global Player_State
    # Rock
    if player == 'Rock' and ai == 'Rock':
        Draw += 1
        Player_State = 'Draw'
    elif player == 'Rock' and ai == 'Paper':
        AI_Score += 1
        Player_State = 'Lose'
    elif player == 'Rock' and ai == 'Scissor':
        Player_Score += 1
        Player_State = 'Win'
    # Paper
    elif player == 'Paper' and ai == 'Rock':
        Player_Score += 1
        Player_State = 'Win'
    elif player == 'Paper' and ai == 'Paper':
        Draw += 1
        Player_State = 'Draw'
    elif player == 'Paper' and ai == 'Scissor':
        AI_Score += 1
        Player_State = 'Lose'
    # Scissor
    elif player == 'Scissor' and ai == 'Rock':
        AI_Score += 1
        Player_State = 'Lose'
    elif player == 'Scissor' and ai == 'Paper':
        Player_Score += 1
        Player_State = 'Win'
    elif player == 'Scissor' and ai == 'Scissor':
        Draw += 1
        Player_State = 'Draw'
    RPS = {'Rock': Rock_img,
           'Paper': Paper_img,
           'Scissor': Scissor_img}

    return RPS[player], RPS[ai]


def random_ai():
    AI = random.choice(['Rock', 'Paper', 'Scissor'])
    return AI


def eye(element):
    global eye_observer
    RE_active = []
    # /
    eye_observer.append(element)
    if len(eye_observer) > 14:
        eye_observer.remove(eye_observer[0])
    re2 = eye_observer[len(eye_observer) - 4:len(eye_observer)]
    re3 = eye_observer[len(eye_observer) - 6:len(eye_observer)]
    re4 = eye_observer[len(eye_observer) - 8:len(eye_observer)]
    re5 = eye_observer[len(eye_observer) - 10:len(eye_observer)]
    re6 = eye_observer[len(eye_observer) - 12:len(eye_observer)]
    re7 = eye_observer[len(eye_observer) - 14:len(eye_observer)]
    # //
    if re2[:2] == re2[2:4]:
        print('re2', re2)
        RE_active = re(re2[2:4])
    elif re3[:3] == re3[3:6]:
        print('re3', re3)
        RE_active = re(re3[3:6])
    elif re4[:4] == re4[4:8]:
        print('re4', re4)
        RE_active = re(re4[4:8])
    elif re5[:5] == re5[5:10]:
        print('re5', re5)
        RE_active = re(re5[5:10])
    elif re6[:6] == re6[6:12]:
        print('re6', re6)
        RE_active = re(re6[6:12])
    elif re7[:7] == re7[7:14]:
        print('re7', re7)
        RE_active = re(re7[7:14])
    return RE_active


def re(active_re):
    print('predict', active_re[0])
    if active_re[0] == 'Rock':
        active_re = 'Paper'
    elif active_re[0] == 'Paper':
        active_re = 'Scissor'
    elif active_re[0] == 'Scissor':
        active_re = 'Rock'
    return active_re


# 'Rock', 'Paper'
# Paper', 'Rock
# 'Rock', 'Paper', 'Scissor',
# 'Paper', 'Scissor', 'Rock'
# 'Scissor', 'Rock', 'Paper'


def data():
    global Draw
    global AI_Score
    global Player_Score
    global Player_State
    Data = Label(text=f'   {Player_State}   \n'
                      f'   Player = {Player_Score}   \n'
                      f'   AI = {AI_Score}   \n'
                      f'   Draw = {Draw}   ')
    Data.grid(row=1, column=1)


def player_ai_show(player_img, ai_img):
    Player_img = Label(image=player_img)
    Player_img.grid(row=1, column=0)
    data()
    AI_img = Label(image=ai_img)
    AI_img.grid(row=1, column=2)


def player_ai_ch(player_ch):
    AI = ai_ch(player_ch)
    show = Play(player_ch, AI)
    player_ai_show(show[0], show[1])


def ai_ch(player_ch):
    global AI_predict
    AI = AI_predict
    if not AI_predict:
        AI = random.choice(['Rock', 'Paper', 'Scissor'])
    AI_predict = eye(player_ch)
    print(AI)
    return AI


if __name__ == '__main__':
    # \\
    Draw = 0
    AI_Score = 0
    Player_Score = 0
    Player_State = ''
    eye_observer = []
    AI_predict = ''
    # \\
    window = Tk()
    Rock_img = PhotoImage(file='rock.gif')
    Paper_img = PhotoImage(file='paper.gif')
    Scissor_img = PhotoImage(file='scissor.gif')
    bm = Menubutton(text='choose')
    bm.menu = Menu(bm)
    bm["menu"] = bm.menu
    bm.menu.add_command(image=Rock_img, command=lambda: player_ai_ch('Rock'))
    bm.menu.add_command(image=Paper_img, command=lambda: player_ai_ch('Paper'))
    bm.menu.add_command(image=Scissor_img, command=lambda: player_ai_ch('Scissor'))
    bm.grid(row=0, column=0)

    window.mainloop()
