from fpdf import FPDF
from natsort import natsorted 
from PIL import Image,ImageFont,ImageDraw
from os import listdir
from os.path import isfile, join

class case:
    def __init__(self, name, path,pos):
        self.name = name
        self.path = path
        self.pos = (pos[0],pos[1])
        self.pos_on_board = (pos[0],pos[1])

    def calculate_pos_on_board(self,board_size):
        self.pos_on_board = (self.pos[0]*board_size[0],self.pos[1]*board_size[1])

mypath = "../../assets/aruco/6X6_50/"

qr_code_zombie = "../../assets/qrcode/qrcode_zombie.png"
qr_code_zombie_logo = "../../assets/qrcode/qrcode_zombie_logo.png"
data_matric_door = "../../assets/datamatrix/dmtxmanoirdoor1.png"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = natsorted(onlyfiles)
arucos = []
aruco_size = 200
aruco_size_on_pdf = 15
board_size = (12,12)
black_aruco = ""
i = 0
for f in onlyfiles:
    if i == 0:
        black_aruco = mypath+f
    else:
        arucos.append(mypath+f)
    i = i + 1
print(onlyfiles)

dungeon_case = "../../assets/dungeon/dungeon_case.png"

pdf = FPDF(format="A4",orientation = 'P')
pdf.add_page()
i = 0
j = 0
aruco_counter = 0
aruco_counter2 = 0
aruco_counter_global = 0
count_pair_x = 0
count_pair_y = 1
while i < board_size[0]:
    while j < board_size[1]:
        if i== 0 or i ==board_size[0]-1:
            if i == board_size[0]-1:
                count_pair_x = 1
            if aruco_counter%2 ==count_pair_x:
                pdf.image(black_aruco, x = j*aruco_size_on_pdf, y = i*aruco_size_on_pdf, w = aruco_size_on_pdf, h = aruco_size_on_pdf)
            else:
                pdf.image(arucos[aruco_counter_global], x = j*aruco_size_on_pdf, y = i*aruco_size_on_pdf, w = aruco_size_on_pdf, h = aruco_size_on_pdf)
                aruco_counter_global += 1
            aruco_counter += 1
            

        elif j == 0 or j == board_size[1]-1:
            if aruco_counter2%2 ==count_pair_y:
                pdf.image(black_aruco, x = j*aruco_size_on_pdf, y = i*aruco_size_on_pdf, w = aruco_size_on_pdf, h = aruco_size_on_pdf)
            else:
                pdf.image(arucos[aruco_counter_global], x = j*aruco_size_on_pdf, y = i*aruco_size_on_pdf, w = aruco_size_on_pdf, h = aruco_size_on_pdf)
                aruco_counter_global += 1
            aruco_counter2 += 1
            if aruco_counter2%2 == 0:
                if count_pair_y == 0:
                    count_pair_y=1
                else:
                    count_pair_y=0

        j = j + 1
    i = i + 1
    j = 0


i = 0
j = 0
pos_start_x =aruco_size_on_pdf
pos_start_y =aruco_size_on_pdf
while i < board_size[0]-2:
    j= 0
    while j < board_size[1]-2:
        pdf.image(dungeon_case, x = i*aruco_size_on_pdf+pos_start_x, y = j*aruco_size_on_pdf+pos_start_y, w = aruco_size_on_pdf, h = aruco_size_on_pdf)
        j = j + 1
    i = i + 1


liste_case = []

liste_case.append(case("case1",qr_code_zombie,(2,2)))
liste_case.append(case("case2",qr_code_zombie_logo,(4,4)))
liste_case.append(case("case3",data_matric_door,(8,8)))

for case_spe in liste_case:
    case_spe.calculate_pos_on_board((aruco_size_on_pdf,aruco_size_on_pdf))
    pdf.image(case_spe.path, x = case_spe.pos_on_board[0]+pos_start_x, y = case_spe.pos_on_board[1]+pos_start_y, w = aruco_size_on_pdf, h = aruco_size_on_pdf)


#pdf.image(black_aruco, x=20, y=20, w=20, h=20)
pdf.output("../../assets/board/plank_test.pdf", "F")