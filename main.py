from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from importlib import reload
from datetime import datetime

now = datetime.now()

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False


from Voxel import *
import maze_create

tald = 1

Qi = 0
QQ = 0
Q2 = 0

music_p = False
music = Audio('assets/BGM', pitch=1, loop=True)
music.stop()


Stage = 0
Count = 0




St = 1
St1 = '■'
St2 = '■'
St3 = '■'
St4 = '■'
St5 = '■'
St6 = '■'
St7 = '■'
St8 = '■'
STAll = St1+St2+St3+St4+St5+St6+St7+St8
name = ''
birth = ''
live = ''
favorite = ''
father = ''
yes_or_no = ''
printscreen = ''
print_temp = ''
Quest = ''
DCount = 5
QCount = 0
N1 = 0

SC = 0

z1 = -1
z2 = 0

def print_print():
    global printscreen,print_temp,STAll,St,Qi
    if St <= 9 and Qi == 0:
        destroy(printscreen)
        STAll = St1+St2+St3+St4+St5+St6+St7+St8
        printscreen = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    if St <= 9 and Qi == 1:
        destroy(printscreen)
        STAll = St1+St2+St3+St4+St5+St6+St7+St8
        printscreen = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

def ST_input(key):
    global St,St1,St2,St3,St4,St5,St6,St7,St8,printscreen,print_temp
    if key == 'a':
        if St==1:
            St1 = 'A'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'A'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'A'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'A'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'A'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'A'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'A'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'A'
            St = St+1
            print_print()
    if key == 'b':
        if St==1:
            St1 = 'B'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'B'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'B'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'B'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'B'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'B'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'B'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'B'
            St = St+1
            print_print()
    if key == 'c':
        if St==1:
            St1 = 'C'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'C'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'C'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'C'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'C'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'C'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'C'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'C'
            St = St+1
            print_print()
    if key == 'd':
        if St==1:
            St1 = 'D'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'D'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'D'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'D'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'D'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'D'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'D'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'D'
            St = St+1
            print_print()
    if key == 'e':
        if St==1:
            St1 = 'E'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'E'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'E'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'E'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'E'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'E'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'E'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'E'
            St = St+1
            print_print()
    if key == 'f':
        if St==1:
            St1 = 'F'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'F'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'F'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'F'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'F'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'F'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'F'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'F'
            St = St+1
            print_print()
    if key == 'g':
        if St==1:
            St1 = 'G'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'G'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'G'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'G'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'G'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'G'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'G'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'G'
            St = St+1
            print_print()
    if key == 'h':
        if St==1:
            St1 = 'H'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'H'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'H'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'H'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'H'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'H'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'H'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'H'
            St = St+1
            print_print()
    if key == 'i':
        if St==1:
            St1 = 'I'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'I'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'I'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'I'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'I'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'I'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'I'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'I'
            St = St+1
            print_print()
    if key == 'j':
        if St==1:
            St1 = 'J'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'J'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'J'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'J'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'J'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'J'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'J'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'J'
            St = St+1
            print_print()
    if key == 'k':
        if St==1:
            St1 = 'K'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'K'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'K'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'K'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'K'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'K'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'K'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'K'
            St = St+1
            print_print()
    if key == 'l':
        if St==1:
            St1 = 'L'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'L'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'L'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'L'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'L'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'L'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'L'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'L'
            St = St+1
            print_print()
    if key == 'm':
        if St==1:
            St1 = 'M'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'M'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'M'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'M'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'M'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'M'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'M'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'M'
            St = St+1
            print_print()
    if key == 'n':
        if St==1:
            St1 = 'N'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'N'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'N'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'N'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'N'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'N'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'N'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'N'
            St = St+1
            print_print()
    if key == 'o':
        if St==1:
            St1 = 'O'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'O'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'O'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'O'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'O'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'O'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'O'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'O'
            St = St+1
            print_print()
    if key == 'p':
        if St==1:
            St1 = 'P'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'P'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'P'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'P'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'P'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'P'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'P'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'P'
            St = St+1
            print_print()
    if key == 'q':
        if St==1:
            St1 = 'Q'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'Q'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'Q'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'Q'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'Q'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'Q'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'Q'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'Q'
            St = St+1
            print_print()
    if key == 'r':
        if St==1:
            St1 = 'R'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'R'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'R'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'R'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'R'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'R'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'R'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'R'
            St = St+1
            print_print()
    if key == 's':
        if St==1:
            St1 = 'S'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'S'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'S'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'S'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'S'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'S'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'S'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'S'
            St = St+1
            print_print()
    if key == 't':
        if St==1:
            St1 = 'T'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'T'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'T'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'T'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'T'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'T'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'T'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'T'
            St = St+1
            print_print()
    if key == 'u':
        if St==1:
            St1 = 'U'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'U'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'U'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'U'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'U'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'U'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'U'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'U'
            St = St+1
            print_print()
    if key == 'v':
        if St==1:
            St1 = 'V'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'V'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'V'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'V'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'V'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'V'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'V'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'V'
            St = St+1
            print_print()
    if key == 'w':
        if St==1:
            St1 = 'W'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'W'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'W'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'W'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'W'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'W'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'W'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'W'
            St = St+1
            print_print()
    if key == 'x':
        if St==1:
            St1 = 'X'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'X'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'X'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'X'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'X'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'X'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'X'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'X'
            St = St+1
            print_print()
    if key == 'y':
        if St==1:
            St1 = 'Y'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'Y'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'Y'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'Y'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'Y'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'Y'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'Y'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'Y'
            St = St+1
            print_print()
    if key == 'z':
        if St==1:
            St1 = 'Z'
            St = St+1
            print_print()
        elif St==2:
            St2 = 'Z'
            St = St+1
            print_print()
        elif St==3:
            St3 = 'Z'
            St = St+1
            print_print()
        elif St==4:
            St4 = 'Z'
            St = St+1
            print_print()
        elif St==5:
            St5 = 'Z'
            St = St+1
            print_print()
        elif St==6:
            St6 = 'Z'
            St = St+1
            print_print()
        elif St==7:
            St7 = 'Z'
            St = St+1
            print_print()
        elif St==8:
            St8 = 'Z'
            St = St+1
            print_print()
    if key == '0':
        if St==1:
            St1 = '0'
            St = St+1
            print_print()
        elif St==2:
            St2 = '0'
            St = St+1
            print_print()
        elif St==3:
            St3 = '0'
            St = St+1
            print_print()
        elif St==4:
            St4 = '0'
            St = St+1
            print_print()
        elif St==5:
            St5 = '0'
            St = St+1
            print_print()
        elif St==6:
            St6 = '0'
            St = St+1
            print_print()
        elif St==7:
            St7 = '0'
            St = St+1
            print_print()
        elif St==8:
            St8 = '0'
            St = St+1
            print_print()
    if key == '1':
        if St==1:
            St1 = '1'
            St = St+1
            print_print()
        elif St==2:
            St2 = '1'
            St = St+1
            print_print()
        elif St==3:
            St3 = '1'
            St = St+1
            print_print()
        elif St==4:
            St4 = '1'
            St = St+1
            print_print()
        elif St==5:
            St5 = '1'
            St = St+1
            print_print()
        elif St==6:
            St6 = '1'
            St = St+1
            print_print()
        elif St==7:
            St7 = '1'
            St = St+1
            print_print()
        elif St==8:
            St8 = '1'
            St = St+1
            print_print()
    if key == '2':
        if St==1:
            St1 = '2'
            St = St+1
            print_print()
        elif St==2:
            St2 = '2'
            St = St+1
            print_print()
        elif St==3:
            St3 = '2'
            St = St+1
            print_print()
        elif St==4:
            St4 = '2'
            St = St+1
            print_print()
        elif St==5:
            St5 = '2'
            St = St+1
            print_print()
        elif St==6:
            St6 = '2'
            St = St+1
            print_print()
        elif St==7:
            St7 = '2'
            St = St+1
            print_print()
        elif St==8:
            St8 = '2'
            St = St+1
            print_print()
    if key == '3':
        if St==1:
            St1 = '3'
            St = St+1
            print_print()
        elif St==2:
            St2 = '3'
            St = St+1
            print_print()
        elif St==3:
            St3 = '3'
            St = St+1
            print_print()
        elif St==4:
            St4 = '3'
            St = St+1
            print_print()
        elif St==5:
            St5 = '3'
            St = St+1
            print_print()
        elif St==6:
            St6 = '3'
            St = St+1
            print_print()
        elif St==7:
            St7 = '3'
            St = St+1
            print_print()
        elif St==8:
            St8 = '3'
            St = St+1
            print_print()
    if key == '4':
        if St==1:
            St1 = '4'
            St = St+1
            print_print()
        elif St==2:
            St2 = '4'
            St = St+1
            print_print()
        elif St==3:
            St3 = '4'
            St = St+1
            print_print()
        elif St==4:
            St4 = '4'
            St = St+1
            print_print()
        elif St==5:
            St5 = '4'
            St = St+1
            print_print()
        elif St==6:
            St6 = '4'
            St = St+1
            print_print()
        elif St==7:
            St7 = '4'
            St = St+1
            print_print()
        elif St==8:
            St8 = '4'
            St = St+1
            print_print()
    if key == '5':
        if St==1:
            St1 = '5'
            St = St+1
            print_print()
        elif St==2:
            St2 = '5'
            St = St+1
            print_print()
        elif St==3:
            St3 = '5'
            St = St+1
            print_print()
        elif St==4:
            St4 = '5'
            St = St+1
            print_print()
        elif St==5:
            St5 = '5'
            St = St+1
            print_print()
        elif St==6:
            St6 = '5'
            St = St+1
            print_print()
        elif St==7:
            St7 = '5'
            St = St+1
            print_print()
        elif St==8:
            St8 = '5'
            St = St+1
            print_print()
    if key == '6':
        if St==1:
            St1 = '6'
            St = St+1
            print_print()
        elif St==2:
            St2 = '6'
            St = St+1
            print_print()
        elif St==3:
            St3 = '6'
            St = St+1
            print_print()
        elif St==4:
            St4 = '6'
            St = St+1
            print_print()
        elif St==5:
            St5 = '6'
            St = St+1
            print_print()
        elif St==6:
            St6 = '6'
            St = St+1
            print_print()
        elif St==7:
            St7 = '6'
            St = St+1
            print_print()
        elif St==8:
            St8 = '6'
            St = St+1
            print_print()
    if key == '7':
        if St==1:
            St1 = '7'
            St = St+1
            print_print()
        elif St==2:
            St2 = '7'
            St = St+1
            print_print()
        elif St==3:
            St3 = '7'
            St = St+1
            print_print()
        elif St==4:
            St4 = '7'
            St = St+1
            print_print()
        elif St==5:
            St5 = '7'
            St = St+1
            print_print()
        elif St==6:
            St6 = '7'
            St = St+1
            print_print()
        elif St==7:
            St7 = '7'
            St = St+1
            print_print()
        elif St==8:
            St8 = '7'
            St = St+1
            print_print()
    if key == '8':
        if St==1:
            St1 = '8'
            St = St+1
            print_print()
        elif St==2:
            St2 = '8'
            St = St+1
            print_print()
        elif St==3:
            St3 = '8'
            St = St+1
            print_print()
        elif St==4:
            St4 = '8'
            St = St+1
            print_print()
        elif St==5:
            St5 = '8'
            St = St+1
            print_print()
        elif St==6:
            St6 = '8'
            St = St+1
            print_print()
        elif St==7:
            St7 = '8'
            St = St+1
            print_print()
        elif St==8:
            St8 = '8'
            St = St+1
            print_print()
    if key == '9':
        if St==1:
            St1 = '9'
            St = St+1
            print_print()
        elif St==2:
            St2 = '9'
            St = St+1
            print_print()
        elif St==3:
            St3 = '9'
            St = St+1
            print_print()
        elif St==4:
            St4 = '9'
            St = St+1
            print_print()
        elif St==5:
            St5 = '9'
            St = St+1
            print_print()
        elif St==6:
            St6 = '9'
            St = St+1
            print_print()
        elif St==7:
            St7 = '9'
            St = St+1
            print_print()
        elif St==8:
            St8 = '9'
            St = St+1
            print_print()
    if key == 'backspace':
        if St==2:
            St1 = '■'
            St = St-1
            print_print()
        elif St==3:
            St2 = '■'
            St = St-1
            print_print()
        elif St==4:
            St3 = '■'
            St = St-1
            print_print()
        elif St==5:
            St4 = '■'
            St = St-1
            print_print()
        elif St==6:
            St5 = '■'
            St = St-1
            print_print()
        elif St==7:
            St6 = '■'
            St = St-1
            print_print()
        elif St==8:
            St7 = '■'
            St = St-1
            print_print()
        elif St==9:
            St8 = '■'
            St = St-1
            print_print()
    if St1 != '■' and key == 'enter':
        enter()


ttt = 0

blackblock='■'
voidblock='□'
starblock='☆'
triblock='△'
resblock='↔'
randblock='○'

jump = 0



    

def St_clear():
    global St,St1,St2,St3,St4,St5,St6,St7,St8,STAll
    St = 1
    St1 = '■'
    St2 = '■'
    St3 = '■'
    St4 = '■'
    St5 = '■'
    St6 = '■'
    St7 = '■'
    St8 = '■'
    STAll = St1+St2+St3+St4+St5+St6+St7+St8


def enter():
    global tald,Qi,QQ,printscreen
    if Qi == 1 and QQ == 1:
        if St1 == '1' and St2 == '0' and St3 == '0' and St4 == '0' and St5 == '0' and St6 == '1' and St7 == '0' and St8 == '0':
            destroy(printscreen)
            St_clear()
            printscreen = "<cyan>PYTHON"+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
            printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
    if Qi == 1 and QQ == 2:
        if St1 == 'W' and St2 == 'A' and St3 == 'T' and St4 == 'E' and St5 == 'R' and St6 == '■' and St7 == '■' and St8 == '■':
            destroy(printscreen)
            St_clear()
            printscreen = "<cyan>19910220"+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
            printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
    if Qi == 1 and QQ == 3:
        if St1 == 'N' and St2 == 'E' and St3 == 'T' and St4 == 'H' and St5 == '■' and St6 == '■' and St7 == '■' and St8 == '■':
            destroy(printscreen)
            St_clear()
            printscreen = "<cyan>HOLLAND"+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
            printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
    if Qi == 1 and QQ == 4:
        if St1 == 'X' and St2 == 'M' and St3 == 'A' and St4 == 'S' and St5 == '■' and St6 == '■' and St7 == '■' and St8 == '■':
            destroy(printscreen)
            St_clear()
            printscreen = "<cyan>RULE"+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
            printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
    if Qi == 1 and QQ == 5:
        if St1 == 'H' and St2 == 'O' and St3 == 'B' and St4 == 'B' and St5 == 'Y' and St6 == '■' and St7 == '■' and St8 == '■':
            destroy(printscreen)
            St_clear()
            printscreen = "<cyan>ROSSUM"+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
            printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
    if tald == 1 and Qi == 0:
        global name
        name = (STAll)
        St_clear()
        Func(tald2())
        tald = tald + 1
    elif tald == 2 and Qi == 0:
        global birth
        birth = (STAll)
        St_clear()
        Func(tald3())
        tald = tald + 1
    elif tald == 3 and Qi == 0:
        global live
        live = (STAll)
        St_clear()
        Func(tald4())
        tald = tald + 1
    elif tald == 4 and Qi == 0:
        global favorite
        favorite = (STAll)
        St_clear()
        Func(tald5())
        tald = tald + 1
    elif tald == 5 and Qi == 0:
        global father
        father = (STAll)
        St_clear()
        Func(tald6())
        tald = tald + 1
    elif tald == 6 and Qi == 0:
        global yes_or_no
        yes_or_no = (STAll)
        St_clear()
        print(name)
        print(birth)
        print(live)
        print(favorite)
        print(father)
        print(yes_or_no)
        if QCount == 1:
            if name == 'PYTHON■■' and birth == '19910220' and live == 'HOLLAND■' and favorite == 'RULE■■■■' and father == 'ROSSUM■■' and yes_or_no == 'YES■■■■■':
                End1()
            elif name == 'PYTHON■■' and birth == '19910220' and live == 'HOLLAND■' and favorite == 'RULE■■■■' and father == 'ROSSUM■■' and yes_or_no == 'NO■■■■■■':
                End2()
            else:
                destroy(printscreen)
                printscreen = Text("<red>잘못 입력하였습니다.\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다.", position=(0,.1), origin=(0,0),duration=999999)
                global N1
                N1 = 1
        else:
            Func(tuto())


class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui

        self.scale = .025
        self.text_entity = Text(world_parent=self, text='loading...', origin=(0,1.5), color=color.light_gray)
        self.y = -.25

        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

class MenuMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)
        

        self.main_menu = Entity(parent=self, enabled=True)
        self.background = Sprite('shore', color=color.dark_gray, z=1)

        global QCount
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        Stage = int(data[0].rstrip())
        QCount = int(data[1])

        Text("In Maze", parent=self.main_menu, y=0.4, x=0, origin=(0,0))

        def quit_game():
            os.remove('assets\maze.txt') 
            application.quit()            
               
        def maze():
            os.remove('assets\maze.txt') 
            self.main_menu.disable()
            self.background.disable()
            Func(tald1())

        def Continue():
            self.main_menu.disable()
            self.background.disable()
            global music_p
            music_p = True
            if Stage == 1:
                Func(Stage1())      
            if Stage == 2:
                Func(Stage2())     
            if Stage == 3:
                Func(Stage3())  
            if Stage == 4:
                Func(Stage4())  
            if Stage == 5:
                Func(Stage5())  
            if Stage == 6:
                Func(Stage6())  

        if Stage >= 1:
            ButtonList(button_dict={
                "Start": Func(maze),
                "Continue" : Func(Continue),
                "Exit": Func(quit_game)
            },y=0,parent=self.main_menu)
        else:
            ButtonList(button_dict={
                "Start": Func(maze),
                "Exit": Func(quit_game)
            },y=0,parent=self.main_menu)

        for key, value in kwargs.items ():
            setattr (self, key, value)

    def input(self, key):

        if self.main_menu.enabled:
            if key == "escape":
                application.quit()


    def update(self):
        pass




def now_now():
    global now, now2
    now = datetime.now()
def now_temp():
    global now2
    now2 = now.second


def WhiteBlock():
    global z1,z2
    for z in range(z1,z2):
        for x in range(0,1):
            for y in range(1,6):
                voxel = WhiteVoxel(position=(x,y,z))
    z1 = z1 + 2
    z2 = z2 + 2
    music = Audio('assets/Drop.wav', pitch=1, loop=False)





def Stage_i():
    global Stage
    Stage = Stage + 1
def Stage_d():
    global Stage
    Stage = 0
def music_i():
    global music
    music.play()
    global music_p
    music_p = True
def music_d():
    global music
    music.stop()
    global music_p
    music_p = False
def Qi_i():
    global Qi
    Qi = Qi + 1
    print(Qi)
def Q2_i():
    global Q2
    Q2 = Q2 + 1
    now_temp()

def ttt_i():
    global ttt
    ttt = ttt + 1
def ttt_c():
    global ttt
    ttt = 0

def SC_i():
    global SC
    SC = SC + 1

def END_no():
    global printscreen
    if SC == 4:
        printscreen = Text('In Maze', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)
    elif SC == 7:
        destroy(printscreen)
        printscreen = Text('In Maz', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)
    elif SC == 8:
        destroy(printscreen)
        printscreen = Text('In Ma', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)
    elif SC == 9:
        destroy(printscreen)
        printscreen = Text('In M', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)   
    elif SC == 10:
        destroy(printscreen)
        printscreen = Text('In', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999) 
    elif SC == 13:
        destroy(printscreen)
        printscreen = Text('<red>Inde', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999) 
    elif SC == 14:
        destroy(printscreen)
        printscreen = Text('<red>Indeci', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999) 
    elif SC == 15:
        destroy(printscreen)
        printscreen = Text('<red>Indecisi', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)     
    elif SC == 16:
        destroy(printscreen)
        printscreen = Text('<red>Indecisive', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)
    elif SC == 18:
        destroy(printscreen)
        printscreen = Text('<red>Indecisive\n<white>Maze', parent=camera.overlay, position=(0,0,-.1), origin=(0,0), world_scale=100,duration=99999)   
    elif SC >= 27:
            application.quit() 

class End1(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        lines = '''

            파이썬(<blue>Python<white>)은
            <yellow>1991년 2월 20일
            <white>발표된 프로그래밍 언어이며
            굉장히 <lime>규칙<white>을 중시하는 언어이다.
            만든이는 네덜란드 <olive>노르트홀란트<white>주 출신의
            <peach>귀도 반 로섬<white>으로
            그는 1989년 <cyan>크리스마스<white>에
            자신이 가질만한 <orange>취미<white>를 찾았고
            파이썬이 제작되었다.

            '''.split('\n')
        lines = [l.strip() for l in lines if l != '']
        # print(lines)
        lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
        for l in lines:
            l.enabled = False
            l.world_scale = 50
        
        self.seq = Sequence()
        self.seq.append(Wait(2))
        self.seq.append(Wait(.5))
        speed = 0.1


        for l in lines:
            self.seq.append(Wait(1))
            self.seq.append(Func(l.appear, speed))
            self.seq.append(Wait((len(l.text) * speed) + 1))
            self.seq.append(Func(setattr, l, 'enabled', False))
        
        self.seq.append(Func(setattr, window.exit_button, 'enabled', True))
        self.seq.append(Func(setattr, window.exit_button, 'position', (0,0)))
        self.seq.append(Func(setattr, window.exit_button.text_entity, 'text', 'exit'))
        self.seq.append(Wait(5))
        self.seq.append(Func(application.quit))

        self.seq.start()

        self.disabled = True


        global input
        def input(key):
            pass

class End2(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        Func(now_temp())

        global input
        def input(key):
            pass
        
        global update
        def update():
            now_now()
            if (now.second - now2) >= 1 or (now.second - now2) < 0:
                SC_i()
                END_no()
                now_temp()

class tald1(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Quest
        if QCount == 0:
            Quest = '이름을 입력해 주세요.'
        elif QCount == 1:
            Quest = '<red>언어의 <white>이름을 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)
        

    global input
    def input(key):
        ST_input(key)
        


class tald2(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global name2
        for x in range(len(blackblock)):
            name2 = name.replace(blackblock[x],"")

        global Quest
        if QCount == 0:
            Quest = name2+'의 생년월일을 입력해 주세요.'
        elif QCount == 1:
            Quest = '<red>파이썬<white>의 발표일을 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    global input
    def input(key):
        ST_input(key)
      

class tald3(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Quest
        if QCount == 0:
            Quest = name2+'의 탄생지를 입력해 주세요.'
        elif QCount == 1:
            Quest = '<red>파이썬<white>의 탄생지를 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    global input
    def input(key):
        ST_input(key)
      
    

class tald4(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Quest
        if QCount == 0:
            Quest = name2+'이 중요시 하는 것을 입력해 주세요.'
        elif QCount == 1:
            Quest = '<red>파이썬<white>이 중요시 하는 것을 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    global input
    def input(key):
        ST_input(key)
      
    

class tald5(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Quest
        if QCount == 0:
            Quest = name2+'이 좋아하는 것을 입력해 주세요.'
        elif QCount == 1:
            Quest = '<red>파이썬<white>의 제작자 이름을 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    global input
    def input(key):
        ST_input(key)
      
    

class tald6(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        global Stage
        f = open('assets\Stage.txt')
        Stage = f.readline()
        f.close()
        super().__init__(parent=camera.ui, ignore_paused=True)
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Quest
        if QCount == 1:
            Quest = '확실한가요?\n　YES 혹은 NO로 대답해주세요.'
        else:
            Quest = '마지막으로 아무거나 입력해 주세요.'
        global print_temp
        print_temp = Quest.center(30,' ')+"\n\n\n<green>"+STAll.center(30,' ')
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

    global input
    def input(key):
        if N1 == 0:
            ST_input(key)
        if key == 'control':
            St_clear()
            Func(tuto())
      
    

class Stage_in():
    def __init__(self):
        lines = '''
            '''.split('\n')
        lines = [l.strip() for l in lines if l != '']
        # print(lines)
        lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
        for l in lines:
            l.enabled = False
            l.world_scale = 50
        

        self.seq = Sequence()
        speed = .05

        for l in lines:
            self.seq.append(Wait(.5))
            self.seq.append(Func(l.appear, speed))
            self.seq.append(Wait((len(l.text) * speed) + 0.5))
            self.seq.append(Func(setattr, l, 'enabled', False))
        Func(LoadingWheel())
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()[0].rstrip()
        if data == "0":
            self.seq.append(Func(Stage1))
        elif data == '1':
            self.seq.append(Func(Stage2))
        elif data == '2':
            self.seq.append(Func(Stage3))
        elif data == '3':
            self.seq.append(Func(Stage4))
        elif data == '4':
            self.seq.append(Func(Stage5))
        elif data == '5':
            self.seq.append(Func(Stage6))

        self.seq.start()

        self.disabled = True

class Quest_in():
    def __init__(self):
        lines = '''
            '''.split('\n')
        lines = [l.strip() for l in lines if l != '']
        # print(lines)
        lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
        for l in lines:
            l.enabled = False
            l.world_scale = 50
        

        self.seq = Sequence()
        speed = .05

        for l in lines:
            self.seq.append(Wait(.5))
            self.seq.append(Func(l.appear, speed))
            self.seq.append(Wait((len(l.text) * speed) + 0.5))
            self.seq.append(Func(setattr, l, 'enabled', False))
        Func(LoadingWheel())
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()[0].rstrip()
        if data == '1':
            self.seq.append(Func(Quest1))
        elif data == '2':
            self.seq.append(Func(Quest2))
        elif data == '3':
            self.seq.append(Func(Quest3))
        elif data == '4':
            self.seq.append(Func(Quest4))
        elif data == '5':
            self.seq.append(Func(Quest5))

        self.seq.start()

        self.disabled = True

class tuto(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content
        scene.clear()

        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "0\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)
        
        for z in range(-1,108):
            for x in range(0,1):
                voxel = BlackVoxel(position=(x,0,z))
        for z in range(108,109):
            for x in range(0,1):
                voxel = clear_ground(position=(x,0,z))
        for z in range(109,110):
            for x in range(0,1):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(-1,0):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(-1,0):
            for x in range(-1,2):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(1,2):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(0,1):
                voxel = BlackVoxel(position=(x,6,z))
        player = FirstPersonController()
        player.original_speed = player.speed

        Func(music_i())

        camera.clip_plane_far = 8

        player.position = Vec3(0,2,0)


        global Stage
        Stage = 0

        

        global input
        def input(key):
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 2, 0)
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
        global update
        def update():
            if player.position.z > 0 and player.position.z < 1 and Stage == 0:
                print_on_screen("Mind maze", position=(0,.1), origin=(0,0))
                Func(Stage_i())
            if player.position.z > 12 and player.position.z < 13 and Stage == 0:
                print_on_screen("Ctrl, r 키를 동시에 누르면 시작 지점으로 돌아옵니다. ", position=(0,.1), origin=(0,0), duration=2.3)
                Func(Stage_i())
            if player.position.z > 32 and player.position.z < 33 and Stage == 0:
                print_on_screen("Shift 키를 눌러 달릴 수 있습니다.", position=(0,.1), origin=(0,0), duration=2.3)
                Func(Stage_i())
            if player.position.z > 54 and player.position.z < 55 and Stage == 0:
                print_on_screen("F2와 F3키로 음악을 재생, 멈출 수 있습니다.", position=(0,.1), origin=(0,0), duration=2.3)
                Func(Stage_i())
            if player.position.z > 84 and player.position.z < 85 and Stage == 0:
                print_on_screen("간단한 미로 게임을 해봅시다.", position=(0,.1), origin=(0,0), duration=2.3)
                Func(Stage_i())
            if player.position.z > 1 and player.position.z < 12 and Stage == 1:
                Func(Stage_d())
            if player.position.z > 13 and player.position.z < 32 and Stage == 1:
                Func(Stage_d())
            if player.position.z > 33 and player.position.z < 54 and Stage == 1:
                Func(Stage_d())
            if player.position.z > 55 and player.position.z < 84 and Stage == 1:
                Func(Stage_d())
            if player.position.z > 85 and player.position.z < 90 and Stage == 1:
                Func(Stage_d())
            if player.position.y < -2 and player.position.y > -3 and Stage == 1:
                Func(Stage_d())
            if player.position.z > 107.4 and Stage == 0:
                Stage_i()
                Func(Stage_in())
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())


class Stage1(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content

        scene.clear()

        reload(maze_create)

        sky = Entity(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/sky.jpg'),
            scale=500,
            double_sided=True
            )

        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "1\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)


        for z in range(0,29):
            for x in range(0,29):
                voxel = BlackVoxel2(position=(x,0,z))


        r = open('assets\maze.txt', 'r')
        lines = r.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                        for y in range(1,6):
                            voxel = BlackVoxel2_entt(position=(x,y,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == voidblock:
                zline1 += 1
                zline2 += 1
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                del lineline[0]
        r.close()  

        os.remove('assets\maze.txt') 

        for z in range(28,29):
            for x in range(28,29):
                voxel = clear_ground(position=(x,0,z))

        
        global tald
        tald = 0

        player = FirstPersonController(speed=2.5)
        player.original_speed = player.speed

        camera.clip_plane_far = 5.4

        if music_p == True:
            music.stop()
            music.play()
        
        

        global Stage
        Stage = 0


        player.position = Vec3(0,3,0)

        
        global input
        def input(key):
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 3, 0)
            if held_keys['alt'] and key == 'c':
                player.position = Vec3(28, 2, 28)
            if Stage == 0 and key == 'w':   
                lines = '''
                    In maze
                    1
                    '''.split('\n')
                lines = [l.strip() for l in lines if l != '']
                # print(lines)
                lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
                for l in lines:
                    l.enabled = False
                    l.world_scale = 50

                self.seq = Sequence()
                speed = .05

                for l in lines:
                    self.seq.append(Wait(.3))
                    self.seq.append(Func(l.appear, speed))
                    self.seq.append(Wait((len(l.text) * speed) + 1))
                    self.seq.append(Func(setattr, l, 'enabled', False))

                self.seq.start()

                self.disabled = True
                Func(Stage_i())
        
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())
            if player.position.y < -2:
                camera.clip_plane_far = 1000
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
            if player.position.z > 27.6 and player.position.x > 27.6:
                player.position = Vec3(0,2,0)
                Func(Quest_in())


class Quest1(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        global QQ
        QQ = 1
        
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Qi
        Qi = 1
        global Quest
        Quest = '<orange>Record 1\n\n<white>우리들이 보는 것은 <green>같으나 서로 다르다.\n<white>나는 두번째, 형은 열번째, 동생은 여덟번째를 담당한다.\n그리고 형이 관측한 별의 수는 132개다.'

        global print_temp
        print_temp = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

        if music_p == True:
            music.stop()
            music.play()


        global input
        def input(key):
            ST_input(key)
            if key == 'control':
                St_clear()
                Func(Stage_in())
        
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())

        

class Stage2(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        scene.clear()


        sky = Entity(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/sky.jpg'),
            scale=500,
            double_sided=True
            )

        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "2\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)

        for z in range(-19,6):
            for x in range(0,1):
                voxel = BlackVoxel3(position=(x,0,z))
        for z in range(-20,4):
            for x in range(-1,0):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(-20,4):
            for x in range(1,2):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(-20,5):
            for x in range(0,1):
                voxel = BlackVoxel3(position=(x,6,z))
        for z in range(5,6):
            for x in range(-8,0):
                voxel = BlackVoxel3(position=(x,0,z))
        for z in range(5,6):
            for x in range(1,7):
                voxel = BlackVoxel3(position=(x,0,z))
        for z in range(4,5):
            for x in range(-9,0):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(4,5):
            for x in range(1,8):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(6,7):
            for x in range(-9,8):
                voxel = BlackVoxel3(position=(x,1,z))
        for z in range(6,7):
            for x in range(0,1):
                voxel = Left_Block(position=(x,1.75,z))
        for z in range(6,7):
            for x in range(0,1):
                voxel = Right_Block(position=(x,2.75,z))
        for z in range(6,7):
            for x in range(-9,0):
                for y in range(1,4):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(6,7):
            for x in range(1,8):
                for y in range(1,4):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(6,7):
            for x in range(-9,8):
                for y in range(4,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(5,6):
            for x in range(-9,8):
                voxel = BlackVoxel3(position=(x,6,z))
        for z in range(-20,-19):
            for x in range(0,1):
                voxel = clear_ground_Entt(position=(x,0,z))
        for z in range(-21,-20):
            for x in range(0,1):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(5,6):
            for x in range(-9,-8):
                voxel = clear_ground(position=(x,0,z))
        for z in range(5,6):
            for x in range(7,8):
                voxel = clear_ground(position=(x,0,z))
        for z in range(5,6):
            for x in range(-10,-9):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(5,6):
            for x in range(8,9):
                for y in range(1,6):
                    voxel = BlackVoxel3(position=(x,y,z))
        for z in range(-2,-1):
            for x in range(0,1):
                for y in range(1,6):
                    voxel = EnttBlackVoxel(position=(x,y,z))





        player = FirstPersonController(speed=2.5)
        player.original_speed = player.speed
        player.position = Vec3(0, 1, 0)

        camera.clip_plane_far = 30


        if music_p == True:
            music.stop()
            music.play()   

        global Stage
        Stage = 0
        
        global input
        def input(key):
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 2, 0)
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
            if Stage == 0 and key == 'w':   
                lines = '''
                    In maze
                    2
                    '''.split('\n')
                lines = [l.strip() for l in lines if l != '']
                # print(lines)
                lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
                for l in lines:
                    l.enabled = False
                    l.world_scale = 50

                self.seq = Sequence()
                speed = .05

                for l in lines:
                    self.seq.append(Wait(.3))
                    self.seq.append(Func(l.appear, speed))
                    self.seq.append(Wait((len(l.text) * speed) + 1))
                    self.seq.append(Func(setattr, l, 'enabled', False))

                self.seq.start()

                self.disabled = True
                Func(Stage_i())
            if key != 'shift' and player.position.z < -1 and player.position.z > -1.2:
                if held_keys['shift']:
                    pass
                else:
                    player.position = Vec3(0,0,-1)
        
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())
            if player.position.y < -1.8 and player.position.y > -2:
                camera.clip_plane_far = 500
            if player.position.y < -240:
                Func(Quest_in())


class Quest2(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)

        global QQ
        QQ = 2
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Qi
        Qi = 1
        global Quest
        Quest = '<orange>Record 2\n\n<salmon>D <white>- <gray>M <white>- <red>F <white>- <blue>? <white>... - <salmon>D\n<blue>?<white>에 들어갈 단어를 쓰시오.'
        
        global print_temp
        print_temp = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

        if music_p == True:
            music.stop()
            music.play()


        global input
        def input(key):
            ST_input(key)
            if key == 'control':
                St_clear()
                Func(Stage_in())

        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())



class Stage3(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content

        scene.clear()

        reload(maze_create)

        sky = Entity(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/sky.jpg'),
            scale=500,
            double_sided=True
            )

        for z in range(28,29):
            for x in range(28,29):
                voxel = clear_ground(position=(x,0,z))
                
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "3\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)

        ir = 0
        ib = 0
        r = open('assets\maze.txt', 'r')
        h = open('assets\maze1.txt', 'w')
        lines = r.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                        for y in range(1,6):
                            voxel = BlackVoxel4(position=(x,y,z))
                zline1 += 1
                zline2 += 1
                h.write(blackblock)
                ib = 1
                i = randint(1,2)
                del lineline[0]
            elif lineline[0] == voidblock:
                if i > 950 and ir < 15:
                    if ib < 2:
                        h.write(starblock)
                        ir += 1
                        ib = 3
                    else:
                        h.write(voidblock)
                        ib = 1
                else:
                    h.write(voidblock)
                    ib = 1
                zline1 += 1
                zline2 += 1
                i = randint(1,1000)
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                i = randint(1,1000)
                h.write('\r')
                del lineline[0]
        r.close() 
        h.close()  

        

        r = open('assets\maze1.txt', 'r')
        lines = r.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel4(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == voidblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel4(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == starblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel4_Entt(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                del lineline[0]
        r.close() 

        os.remove('assets\maze.txt') 
        os.remove('assets\maze1.txt') 

        
        global player
        player = FirstPersonController(speed=2.5)
        player.original_speed = player.speed


        global Stage
        Stage = 0
        

        if music_p == True:
            music.stop()
            music.play()

        camera.clip_plane_far = 5

        global input
        def input(key):
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 2, 0)
                Func(ttt_c())
                camera.clip_plane_far = 5
            if held_keys['alt'] and key == 'c':
                player.position = Vec3(28, 2, 28)
            if Stage == 0 and key == 'w':   
                lines = '''
                    In maze
                    3
                    '''.split('\n')
                lines = [l.strip() for l in lines if l != '']
                # print(lines)
                lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
                for l in lines:
                    l.enabled = False
                    l.world_scale = 50

                self.seq = Sequence()
                speed = .05

                for l in lines:
                    self.seq.append(Wait(.3))
                    self.seq.append(Func(l.appear, speed))
                    self.seq.append(Wait((len(l.text) * speed) + 1))
                    self.seq.append(Func(setattr, l, 'enabled', False))

                self.seq.start()

                self.disabled = True
                Func(Stage_i())
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())
            if player.position.y < -2:
                camera.clip_plane_far = 1000
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
                Func(Stage_i())
                Func(ttt_i())
            if ttt > 333:
                Func(ttt_c())
                camera.clip_plane_far = 5
                player.position = Vec3(0, 3, 0)
                player.position = Vec3(0, 2, 0)
                player.position = Vec3(0, 1, 0)
                player.position = Vec3(0, 2, 0)
            if player.position.z > 27.6 and player.position.x > 27.6:
                player.position = Vec3(0,2,0)
                Func(Quest_in())

class Quest3(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)

        global QQ
        QQ = 3
        
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Qi
        Qi = 1
        global Quest
        Quest = '<orange>Record 3\n\n<red>이<white>나<blue>라<light_gray>를 구성하는 대다수의 주에 거주하는 사람들은 자신들의 국가가 이 별칭으로 불리는 것을 좋아하지 않는다.\n그러나 그것은 대중적이며 딱히 비하의 의미를 가지진 않는다.\n이 나라의 스펠링 <yellow>앞글자 <light_gray>4자리.'
        global print_temp
        print_temp = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

        if music_p == True:
            music.stop()
            music.play()


        global input
        def input(key):
            ST_input(key)
            if key == 'control':
                St_clear()
                Func(Stage_in())

        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())

class jump_block(Button):
    def __init__(self, position=(0,0,0), texture='assets/up.png'):
        super().__init__(
            parent = scene,
            position = position,
            model='assets/block',
            origin_y = .5,
            texture=texture,
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            scale=0.5
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down' or key == 'right mouse down':
                player.jump_height = 500
                camera.clip_plane_far = 9900
                global jump
                jump=1
                Func(Stage_i())

class Stage4(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content

        scene.clear()

        reload(maze_create)

        sky = Entity(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/sky.jpg'),
            scale=300,
            double_sided=True
            )

        Sky(texture='assets/castaway_sky.jpg')

        for z in range(28,29):
            for x in range(28,29):
                voxel = clear_ground(position=(x,0,z))
                
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "4\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)

        ir = 0
        ie = 0
        ib = 0
        r = open('assets\maze.txt', 'r')
        h = open('assets\maze1.txt', 'w')
        lines = r.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                        for y in range(1,6):
                            voxel = BlackVoxel5(position=(x,y,z))
                zline1 += 1
                zline2 += 1
                h.write(blackblock)
                ib = 1
                i = randint(1,2)
                ii = randint(1,1000)
                del lineline[0]
            elif lineline[0] == voidblock:
                if i > 950 and ir < 15:
                    if ib < 2:
                        h.write(starblock)
                        ir += 1
                        ib = 3
                        ii = randint(1,1000)
                    else:
                        h.write(voidblock)
                        ib = 1
                elif ii > 950 and ie < 25:
                    h.write(triblock)
                    ie += 1
                    i = randint(1,1000)
                else:
                    h.write(voidblock)
                    ib = 1
                zline1 += 1
                zline2 += 1
                i = randint(1,1000)
                ii = randint(1,1000)
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                i = randint(1,1000)
                ii = randint(1,1000)
                h.write('\r')
                del lineline[0]
        r.close() 
        h.close()  
        
        
        f = open('assets\maze1.txt', 'r')
        lines = f.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel5(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == voidblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel5(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == starblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel4_Entt(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == triblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = jump_block(position=(x,2,z))
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel5(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                del lineline[0]
        f.close() 

        os.remove('assets\maze.txt') 
        os.remove('assets\maze1.txt') 
        
        
        global player
        player = FirstPersonController(speed=2.5)
        player.original_speed = player.speed

        camera.clip_plane_far = 5

        
        global Stage
        Stage = 0


        if music_p == True:
            music.stop()
            music.play()

        global input
        def input(key):
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 2, 0)
                Func(ttt_c())
                player.jump_height = 2
                camera.clip_plane_far = 5
                global jump
                jump = 0

            if jump == 1 and key == 'w':   
                player.jump()
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
            if held_keys['alt'] and key == 'c':
                player.position = Vec3(28, 2, 28)
            if Stage == 0 and key == 'w':   
                lines = '''
                    In maze
                    4
                    '''.split('\n')
                lines = [l.strip() for l in lines if l != '']
                # print(lines)
                lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
                for l in lines:
                    l.enabled = False
                    l.world_scale = 50

                self.seq = Sequence()
                speed = .05

                for l in lines:
                    self.seq.append(Wait(.3))
                    self.seq.append(Func(l.appear, speed))
                    self.seq.append(Wait((len(l.text) * speed) + 1))
                    self.seq.append(Func(setattr, l, 'enabled', False))

                self.seq.start()

                self.disabled = True
                Func(Stage_i())
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())
            if player.position.y < -2:
                camera.clip_plane_far = 1000
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
                Func(ttt_i())
            if player.position.y > 100:
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
            if ttt > 300:
                Func(ttt_c())
                camera.clip_plane_far = 5
                player.position = Vec3(0, 3, 0)
                player.position = Vec3(0, 2, 0)
                player.position = Vec3(0, 1, 0)
                player.position = Vec3(0, 2, 0)
            if player.position.z > 27.6 and player.position.x > 27.6:
                player.position = Vec3(0,2,0)
                Func(Quest_in())


class Quest4(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)

        global QQ
        QQ = 4
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Qi
        Qi = 1
        global Quest
        Quest = '<orange>Record 4\n\n<yellow>기름 부음\n<gold>기리사독\n<magenta>파견'
        global print_temp
        print_temp = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

        if music_p == True:
            music.stop()
            music.play()


        global input
        def input(key):
            ST_input(key)
            if key == 'control':
                St_clear()
                Func(Stage_in())

        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())


class reset_block(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.rgb(10,250,130),
        )
    def input(self, key):
        if self.hovered:
            if held_keys['w'] or held_keys['s'] or held_keys['a']or held_keys['d']:
                player.position = Vec3(0, 2, 0)




class Stage5(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content

        scene.clear()

        reload(maze_create)

        sky = Entity(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/sky.jpg'),
            scale=300,
            double_sided=True
            )

        Sky(texture='assets/castaway_sky.jpg')

        for z in range(28,29):
            for x in range(28,29):
                voxel = clear_ground(position=(x,0,z))
                
        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "5\r"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)

        ir = 0
        ie = 0
        ib = 0
        ig = 0
        r = open('assets\maze.txt', 'r')
        h = open('assets\maze1.txt', 'w')
        lines = r.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                        for y in range(1,6):
                            voxel = BlackVoxel6(position=(x,y,z))
                zline1 += 1
                zline2 += 1
                h.write(blackblock)
                ib = 1
                i = randint(1,2)
                ii = randint(1,1000)
                del lineline[0]
            elif lineline[0] == voidblock:
                if i > 950 and ir < 15:
                    if ib < 2:
                        h.write(starblock)
                        ir += 1
                        ib = 3
                        ii = randint(1,1000)
                    else:
                        h.write(voidblock)
                        ib = 1
                elif ii > 950 and ie < 25:
                    h.write(triblock)
                    ie += 1
                    i = randint(1,1000)
                elif i > 250 and i < 330 and ig < 10:
                    h.write(resblock)
                    ig += 1
                    i = randint(1,1000)
                else:
                    h.write(voidblock)
                    ib = 1
                zline1 += 1
                zline2 += 1
                i = randint(1,1000)
                ii = randint(1,1000)
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                i = randint(1,1000)
                ii = randint(1,1000)
                h.write('\r')
                del lineline[0]
        r.close() 
        h.close()  
        
        
        f = open('assets\maze1.txt', 'r')
        lines = f.readlines()
        lineline = ''.join(lines)
        lineline = list(lineline)
        zline1 = -1
        zline2 = 0
        xline1 = -1
        xline2 = 0
        while lineline:
            if lineline[0] == blackblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel6(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == voidblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel6(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == starblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel4_Entt(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == triblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = jump_block(position=(x,2,z))
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = BlackVoxel6(position=(x,0,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            elif lineline[0] == resblock:
                for z in range(zline1,zline2):
                    for x in range(xline1,xline2):
                            voxel = reset_block(position=(x,1,z))
                zline1 += 1
                zline2 += 1
                del lineline[0]
            else:
                zline1 = -1
                zline2 = 0
                xline1 += 1
                xline2 += 1
                del lineline[0]
        f.close() 


        os.remove('assets\maze.txt') 
        os.remove('assets\maze1.txt') 
        
        
        global player
        player = FirstPersonController(speed=2.5)
        player.original_speed = player.speed

        camera.clip_plane_far = 5


        if music_p == True:
            music.stop()
            music.play()
        
        global Stage
        Stage = 0
        

        global input
        def input(key):
            if key == 'shift':   
                player.speed = player.original_speed * 1.5
            elif key == 'shift up':
                player.speed = player.original_speed
            if held_keys['control'] and key == 'r':
                player.position = Vec3(0, 2, 0)
                Func(ttt_c())
                player.jump_height = 2
                camera.clip_plane_far = 5
                global jump
                jump = 0

            if jump == 1 and key == 'w':   
                player.jump()
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
            if held_keys['alt'] and key == 'c':
                player.position = Vec3(28, 2, 28)
            if Stage == 0 and key == 'w':   
                lines = '''
                    In maze
                    5
                    '''.split('\n')
                lines = [l.strip() for l in lines if l != '']
                # print(lines)
                lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
                for l in lines:
                    l.enabled = False
                    l.world_scale = 50

                self.seq = Sequence()
                speed = .05

                for l in lines:
                    self.seq.append(Wait(.3))
                    self.seq.append(Func(l.appear, speed))
                    self.seq.append(Wait((len(l.text) * speed) + 1))
                    self.seq.append(Func(setattr, l, 'enabled', False))

                self.seq.start()

                self.disabled = True
                Func(Stage_i())
        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())
            if player.position.y < -2:
                camera.clip_plane_far = 1000
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
                Func(ttt_i())
            if player.position.y > 100:
                print_on_screen("Press Ctrl and r", position=(0,.1), origin=(0,0))
            if ttt > 280:
                Func(ttt_c())
                camera.clip_plane_far = 5
                player.position = Vec3(0, 3, 0)
                player.position = Vec3(0, 2, 0)
                player.position = Vec3(0, 1, 0)
                player.position = Vec3(0, 2, 0)
            if player.position.z > 27.6 and player.position.x > 27.6:
                player.position = Vec3(0,2,0)
                Func(Quest_in())


class Quest5(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)

        global QQ
        QQ = 5
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400
        global Qi
        Qi = 1
        global Quest
        Quest = '<orange>Record 5\n\n<white>대다수의 인간은 <turquoise>이것 <white>없이는 삶을 영위하지 못한다.\n<turquoise>이것<white>이 없는 인간은 병들기 쉽다.\n<turquoise>이것<white>은 물질적인 것일 수도 있고 무형적인 것일 수도 있다.'
        global print_temp
        print_temp = Quest+"\n\n\n\n<cyan>Answer : "+STAll+"\n\n\n\n<red>Ctrl 버튼으로 넘길 수 있습니다."
        global printscreen
        printscreen = print_temp
        printscreen = Text(printscreen, position=(0,.1), origin=(0,0),duration=999999)

        if music_p == True:
            music.stop()
            music.play()


        global input
        def input(key):
            ST_input(key)
            if key == 'control':
                St_clear()
                Func(Stage_in())

        global update
        def update():
            if held_keys['f3'] and music_p == True:
                Func(music_d())
            if held_keys['f2'] and music_p == False:
                Func(music_i())

def DCount_():
    global DCount, printscreen, z2
    if DCount == 5:
        destroy(printscreen)
        printscreen = Text("<yellow>4", position=(0,.1), origin=(0,0),duration=999999)
        DCount = 4
    elif DCount == 4:
        destroy(printscreen)
        printscreen = Text("<blue>3", position=(0,.1), origin=(0,0),duration=999999)
        DCount = 3
    elif DCount == 3:
        destroy(printscreen)
        printscreen = Text("<red>2", position=(0,.1), origin=(0,0),duration=999999)
        DCount = 2
    elif DCount == 2:
        destroy(printscreen)
        printscreen = Text("<red>1", position=(0,.1), origin=(0,0),duration=999999)
        DCount = 1
    elif DCount == 1:
        application.quit()

class Stage6(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content
        scene.clear()
        
        for z in range(-1,108):
            for x in range(0,1):
                voxel = BlackVoxel(position=(x,0,z))
        for z in range(108,109):
            for x in range(0,1):
                voxel = clear_ground(position=(x,0,z))
        for z in range(109,110):
            for x in range(0,1):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(-1,0):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(-1,0):
            for x in range(-1,2):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(1,2):
                for y in range(1,7):
                    voxel = BlackVoxel(position=(x,y,z))
        for z in range(0,110):
            for x in range(0,1):
                voxel = BlackVoxel(position=(x,6,z))
        player = FirstPersonController()
        player.speed = 1


        player.position = Vec3(0,2,0)


        global Stage
        Stage = 0

        if music_p == True:
            music.stop()

        camera.clip_plane_far = 20

        
        global printscreen
        printscreen = Text("<white>5", position=(0,.1), origin=(0,0),duration=999999)

        global input
        def input(key):
            if held_keys['alt'] and key == 'c':
                player.position = Vec3(0, 2, 107)

        global update
        def update():
            now_now()
            if Q2 == 0:
                Q2_i()
            if (now.second - now2) > 2 or (now.second - now2) < 0 and player.position.z < 106:
                WhiteBlock()
                now_temp()
                if player.position.z < (z2 - 2):
                    DCount_()
                    player.position = Vec3(0,2,z2)
            if player.position.z > 70:
                player.speed = 0.5
            if player.position.z > 107.4 and Stage == 0:
                Func(Quest6())
            
class Quest6(Entity):
    def __init__(self, **kwargs):
        scene.clear()
        super().__init__(parent=camera.ui, ignore_paused=True)
        
        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        with open('assets/Stage.txt', 'r') as file:
            data = file.readlines()
        data[0] = "0\r"
        data[1] = "1"
        with open('assets/Stage.txt', 'w') as file:
            file.writelines(data)


        lines = '''
            <smoke>Reset

            '''.split('\n')
        lines = [l.strip() for l in lines if l != '']
        # print(lines)
        lines = [Text(l, parent=camera.overlay, position=(0,0,-.1), origin=(0,0), enabled=False, world_scale=2) for l in lines]
        for l in lines:
            l.enabled = False
            l.world_scale = 50
        
        self.seq = Sequence()
        self.seq.append(Wait(3))
        self.seq.append(Wait(.5))
        speed = 0.7


        for l in lines:
            self.seq.append(Wait(1))
            self.seq.append(Func(l.appear, speed))
            self.seq.append(Wait((len(l.text) * speed) + 1))
            self.seq.append(Func(setattr, l, 'enabled', False))
        
        self.seq.append(Func(setattr, window.exit_button, 'enabled', True))
        self.seq.append(Func(setattr, window.exit_button, 'position', (0,0)))
        self.seq.append(Func(setattr, window.exit_button.text_entity, 'text', 'exit'))
        self.seq.append(Wait(5))
        self.seq.append(Func(application.quit))

        self.seq.start()

        self.disabled = True


        global input
        def input(key):
            pass

        global update
        def update():
            pass




# Setup window title
window.title = "In Maze"

# Call our menu
main_menu = MenuMenu()


# Run application
app.run()


