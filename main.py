import face_recognition as r
import cv2
import webbrowser
from tkinter import *
import smtplib
import tkinter.messagebox
import pyautogui
import mysql.connector as m
from PIL import ImageTk
from PIL import Image
import time,os
import csv
from datetime import datetime
import requests
import mimetypes

from bs4 import BeautifulSoup
import customtkinter as ctk


ever = []
ever1 = []

#input from webcam
cap = cv2.VideoCapture(0)

# YOLO object detection
config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "frozen_inference_graph.pb"
model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []

file_name = "coco.names"
with open (file_name,'rt') as fpt:
    classLabels=fpt.read().rstrip('\n').split('\n')

model.setInputSize(320,320)
model.setInputScale(1.0/127.5) ##255/2=127.5
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)
g= []
font_scale = 1
font = cv2.FONT_HERSHEY_COMPLEX_SMALL



# connecting database
con = m.connect(user = 'root',host = 'localhost',passwd = '1234',database = 'police_database') # create a database locally and enter your mysql password
cursor = con.cursor()
with open("police_data1.csv", 'r') as f:
    readers = csv.reader(f)

    for fg in readers:

        if fg[0]!='NAME':
            try:
                sql = "INSERT INTO missing_person () VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (fg[0],fg[1],fg[2],fg[3],fg[4],fg[5],fg[6],fg[7],fg[8],fg[9])
                cursor.execute(sql, val)

                con.commit()
            except:
                pass
        else:
            continue




l=[]



width, height= pyautogui.size()

# programme window starts
splash_root = Tk()
splash_root.title('SecureX')
splash_root.geometry(str(width)+'x'+str(height))
size_img1 = Image.open('k9_final-removebg-preview.png')
resized1 = size_img1.resize((375,300), Image.LANCZOS)

img1 = ImageTk.PhotoImage(resized1)
label1 = Label(image = img1).place(x= 772,y=290)
sp_label = Label(splash_root, text = "MAN'S BEST FRIEND, CRIME'S WORST ENEMY", font=('Times', 24))
sp_label.place(x = 550,y = 700)

# opening the links on the urls
def callback(url):
   webbrowser.open_new_tab(url)

# closing the toplevel window
def close1():
    topss.destroy()

# open the window containing web scraping results
def media():
    global topss
    topss = Toplevel()
    topss.title('K9')
    topss.geometry(str(width)+'x'+str(height))
    topss.configure(background='black')

    imagess = Image.open("k9_final-removebg-preview.png")
    resized1ss = imagess.resize((90,75), Image.LANCZOS)
    photoss = ImageTk.PhotoImage(resized1ss)

    
    label = Label(topss, image=photoss)
    label.place(x=8 ,y=8)
    label2s = ctk.CTkLabel(master = topss, text="NO. OF MATCHES : " + str(len(ever1)), font=('Times', 30,'bold'), fg_color="#9797FF",text_color='white',corner_radius=12)
    label2s.place(x=300, y=400 )
    label1 = ctk.CTkLabel(master = topss, text="SOCIAL MEDIA MATCH", font=('Times', 55,'bold'),text_color='white')
    label1.place(x=500 ,y=8)
    for q in range(len(ever1)):
        label2 = ctk.CTkLabel(master = topss, text="URL : " , font=('Times', 30,'bold'),fg_color="#9797FF",text_color='white',corner_radius=12)
        label2.place(x=300 ,y=450+30*q)

        link = ctk.CTkLabel(master = topss, text="link"+str(q+1), font=('Helveticabold', 30,'bold'), fg_color="#9797FF", cursor="hand2",corner_radius=12,text_color='blue')
        link.place(x=410,y=450+30*q)
        link.bind("<Button-1>", lambda e:callback(ever1[q]))



    image1s = Image.open(dataa[0][8])
    resized11s = image1s.resize((220,280), Image.LANCZOS)
    photo1s = ImageTk.PhotoImage(resized11s)


    label112 = Label(topss, image=photo1s)
    label112.place(x=850 ,y=150)
    my_button = ctk.CTkButton(master =topss, text="BACK", font=('Times', 20), command=close1,corner_radius = 15 )

    my_button.grid(row=2, column=10, padx=1300, pady=25)



    topss.mainloop()

def close():
    top23.destroy()

# open window showing cctv captured feed and info
def cctv():
    global top23
    tim = str(today)
    timee = tim.split()
    top23 = Toplevel()
    top23.title('K9')
    top23.geometry(str(width)+'x'+str(height))
    top23.configure(background='black')

    image = Image.open("k9_final-removebg-preview.png")
    resized1 = image.resize((90,75), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized1)


    label = Label(top23, image=photo)
    label.place(x=8 ,y=8)

    label1 = ctk.CTkLabel(master = top23, text="CCTV MATCH", font=('Times', 55),text_color	= "white" )
    label1.place(x=650 ,y=8)

    label2 = ctk.CTkLabel(master = top23, text="TIME : " + timee[1], font=('Times', 40),fg_color="#9797FF",corner_radius=12)
    label2.place(x=300 ,y=500)

    label4 =ctk.CTkLabel(master = top23, text="DATE: " + timee[0], font=('Times', 40),fg_color="#9797FF",corner_radius=12)
    label4.place(x=300, y=580)

    label3 = ctk.CTkLabel(master = top23, text="SOURCE : CAM1", font=('Times', 40),fg_color="#9797FF",corner_radius=12)
    label3.place(x=300 ,y=660)

    image1 = Image.open(ever[0])
    resized11 = image1.resize((220,280), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(resized11)

    # Create a label with the image
    label1 = Label(top23, image=photo1)
    label1.place(x=850 ,y=150)
    my_button = ctk.CTkButton(master = top23, text="BACK", font=('Times', 20), command = close,corner_radius=10)

    my_button.grid(row=2, column=10, padx=1300, pady=25)



    top23.mainloop()


def send_mail():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('k9hackathon115@gmail.com','bybeesnvmpkxbnxm')
    s.sendmail('k9hackathon115@gmail.com','sumanyu198@gmail.com','ALERT ! ! !\n'+dataa[0][0]+' location found')


def data2():
    global root2
    send_mail()
    top.destroy()
    root2 = Toplevel()
    root2.geometry(str(width) + 'x' + str(height))
    root2.configure(background='black')

    image56 = Image.open("k9_final-removebg-preview.png")
    resized56 = image56.resize((90, 75), Image.LANCZOS)
    photo56 = ImageTk.PhotoImage(resized56)


    label = Label(root2, image=photo56)
    label.grid(row=5, column=0, padx=1, pady=5)


    font1 = ("Helvetica", 17, "bold")
    name_label = ctk.CTkLabel(master=root2, text="NAME:", font=font1, text_color="blue")

    age_label = ctk.CTkLabel(master=root2, text="AGE:", font=font1, text_color="blue")

    gender_label = ctk.CTkLabel(master=root2, text="GENDER:", font=font1, text_color="blue")

    dob_label = ctk.CTkLabel(master=root2, text="DOB:", font=font1, text_color="blue")

    height_label = ctk.CTkLabel(master=root2, text="HEIGHT:", font=font1, text_color="blue")
    complexion_label = ctk.CTkLabel(master=root2, text="COMPLEXION:", font=font1, text_color="blue")
    physique_label = ctk.CTkLabel(master=root2, text="PHYSIQUE:", font=font1, text_color="blue")
    name_dbb = ctk.CTkLabel(master=root2, text=dataa[0][0], font=font1, fg_color="black")
    age_dbb = ctk.CTkLabel(master=root2, text=dataa[0][9], font=font1, fg_color="black")
    gender_dbb = ctk.CTkLabel(master=root2, text=dataa[0][3], font=font1, fg_color="black")
    dob_dbb = ctk.CTkLabel(master=root2, text=dataa[0][2], font=font1, fg_color="black")
    height_dbb = ctk.CTkLabel(master=root2, text=dataa[0][5], font=font1, fg_color="black")
    complexion_dbb = ctk.CTkLabel(master=root2, text=dataa[0][6], font=font1, fg_color="black")
    physique_dbb = ctk.CTkLabel(master=root2, text=dataa[0][7], font=font1, fg_color="black")

    # place labels and entry widgets in the window
    name_label.grid(row=7, column=0)
    age_label.grid(row=8, column=0)
    gender_label.grid(row=9, column=0)
    dob_label.grid(row=10, column=0)
    height_label.grid(row=11, column=0)
    complexion_label.grid(row=12, column=0)
    physique_label.grid(row=13, column=0)
    name_dbb.grid(row=7, column=1, pady=15)
    age_dbb.grid(row=8, column=1, pady=15)
    gender_dbb.grid(row=9, column=1, pady=15)
    dob_dbb.grid(row=10, column=1, pady=15)
    height_dbb.grid(row=11, column=1, pady=15)
    complexion_dbb.grid(row=12, column=1, pady=15)
    physique_dbb.grid(row=13, column=1, pady=15)

    canvas = Canvas(root2, width=8, height=1080)
    canvas.place(x=400)


    canvas.create_line(1, 0, 1, 1080, fill="black", width=20)

    image1 = Image.open(dataa[0][8])
    resized11 = image1.resize((350, 450), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(resized11)


    label = Label(root2, image=photo1)
    label.place(x=1000, y=50)

    my_button = ctk.CTkButton(master=root2, text="CCTV MATCH", font=("Times", 35), command=cctv, corner_radius=10)
    my_button.grid(row=20, column=150, padx=450, pady=10)

    my_button = ctk.CTkButton(master=root2, text="SOCIAL MEDIA MATCH", font=('Times',35), command=media, corner_radius=10)
    my_button.grid(row=21, column=150, padx=450, pady=10)

    root2.mainloop()

# gives the warning window for invalid data
def onClick():
    tkinter.messagebox.showinfo('warning',"Invalid FIR_ID")

# window comparing faces of missing person
def data():
    global top
    global knownn ,dataa

    f = my_text1.get()
    j = my_text2.get()
    k = my_text3.get()

    try:
        cursor.execute("select * from missing_person where FIR_ID = '{}' ;".format(j))
        dataa = cursor.fetchall()
        knownn = dataa[0][8]
        top = Toplevel()

        top.title("K9")

        top.geometry(str(width) + 'x' + str(height))
        top.configure(background="black")
        image123 = Image.open("k9_final-removebg-preview.png")
        resized123 = image123.resize((75, 75), Image.LANCZOS)
        photo123 = ImageTk.PhotoImage(resized123)


        label = Label(top, image=photo123)
        label.grid(row=2, column=0, padx=1, pady=5)


        font1 = ("Helvetica", 17, "bold")
        name_label = ctk.CTkLabel(top, text="Name :", font=font1, text_color="blue")
        name_db = ctk.CTkLabel(top, text=dataa[0][0], font=font1, fg_color="black")
        age_label = ctk.CTkLabel(top, text="Age :", font=font1, text_color="blue")
        age_db = ctk.CTkLabel(top, text=dataa[0][9], font=font1, fg_color="black")
        gender_label = ctk.CTkLabel(top, text="Gender :", font=font1, text_color="blue")
        gender_db = ctk.CTkLabel(top, text=dataa[0][3], font=font1, fg_color="black")
        dob_label = ctk.CTkLabel(top, text="DOB :", font=font1, text_color="blue")
        dob_db = ctk.CTkLabel(top, text=dataa[0][2], font=font1, fg_color="black")
        height_label = ctk.CTkLabel(top, text="Height :", font=font1, text_color="blue")
        height_db = ctk.CTkLabel(top, text=dataa[0][5], font=font1, fg_color="black")
        complexion_label = ctk.CTkLabel(top, text="Complexion :", font=font1, text_color="blue")
        complexion_db = ctk.CTkLabel(top, text=dataa[0][6], font=font1, fg_color="black")
        physique_label = ctk.CTkLabel(top, text="Physique :", font=font1, text_color="blue")
        physique_db = ctk.CTkLabel(top, text=dataa[0][7], font=font1, fg_color="black")


        name_label.grid(row=5, column=0, pady=15)
        name_db.grid(row=5, column=1, pady=15)
        age_label.grid(row=6, column=0, pady=15)
        age_db.grid(row=6, column=1, pady=15)
        gender_label.grid(row=7, column=0, pady=15)
        gender_db.grid(row=7, column=1, pady=15)
        dob_label.grid(row=8, column=0, pady=15)
        dob_db.grid(row=8, column=1, pady=15)
        height_label.grid(row=9, column=0, pady=15)
        height_db.grid(row=9, column=1, pady=15)
        complexion_label.grid(row=10, column=0, pady=15)
        complexion_db.grid(row=10, column=1, pady=15)
        physique_label.grid(row=11, column=0, pady=15)
        physique_db.grid(row=11, column=1, pady=15)

        canvas = Canvas(top, width=8, height=1080)
        canvas.place(x=420)


        canvas.create_line(1, 0, 1, 1080, fill="black", width=20)

        image23 = Image.open(dataa[0][8])
        resized23 = image23.resize((350, 400), Image.LANCZOS)
        photo23 = ImageTk.PhotoImage(resized23)
        label23 = Label(top, image=photo23)
        label23.place(x=950, y=160)

        ctk.CTkLabel(master = top, text="Processing...", font=("Bahnschrift 15", 17,'bold'), text_color="#76EE00").place(x=900, y=660)

        for i in range(16):
            Label(top, bg="#1F2732", width=3, height=2).place(x=(i + 30) * 30, y=700)

        top.update()
        play_animation(top)
        top.mainloop()
        print(dataa)
    except:
        onClick()


# facial recognition algorithm
def face_rec(x):

    known_img = r.load_image_file(knownn)
    known_encoding = r.face_encodings(known_img)[0]

    unknown_img = r.load_image_file(x)
    unknown_encoding = r.face_encodings(unknown_img)

    if unknown_encoding == []:
        return 1
    else:
        for person in unknown_encoding:
            result = r.compare_faces([known_encoding], person)
            if result[0] == True:
                print("found the person")
                return 0
            else:
                g.append(person)
                continue
        if g==unknown_encoding:
            return 1
        else:
            pass

# saving cctv feed and web scraping images logcally on the system
def createimg(x,ut):
    responsee = requests.get(x)
    content_type = responsee.headers["Content-Type"]

    img_ext = mimetypes.guess_extension(content_type)


    file_name =  ut + img_ext


    with open(file_name, "wb") as f_imag:
        f_imag.write(responsee.content)
    return file_name




# web scraping for finding image src from the url
def find_img():
    global yyy
    ggh = dataa[0][0]
    list1 = ggh.split()
    inn = list1[0] + "+" +list1[1]

    url = "https://www.google.com/search?q=" + inn + "&tbm=isch&ved=2ahUKEwiv8vqPyd79AhVENrcAHYDOAYIQ2-cCegQIABAA&oq=" + inn + "&gs_lcp=CgNpbWcQAzIFCAAQgAQyBwgAEIAEEBgyBwgAEIAEEBg6BAgjECc6BAgAEEM6CAgAEIAEELEDOgYIABAIEB46CQgAEIAEEAoQGFD3B1iPHWDQH2gBcAB4AIABhAGIAfYMkgEEMC4xNJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=TQ8SZO-XGMTs3LUPgJ2HkAg&bih=714&biw=1536&rlz=1C1SQJL_enIN914IN914&hl=en-GB"


    response = requests.get(url)


    soup = BeautifulSoup(response.content, "html.parser")
    done = soup.find_all("img")
    for ii in done:

        l.append(ii.get("src"))

    for k in range(len(l)):

        for j in range(16):
            Label(top, bg="#76EE00", width=3, height=2).place(x=(j + 30) * 30, y=700)
            time.sleep(0.04)
            top.update_idletasks()
            Label(top, bg="#1F2732", width=3, height=2).place(x=(j + 30) * 30, y=700)
        if k != 0:
            ut = str(k+1)
            fileee = createimg(l[k], ut)
            ans = face_rec(fileee)

            if ans == 0:
                yyy = l[k]
                ever1.append(fileee)
                print("found", l[k])
            else:
                os.remove(fileee)
                continue
        else:
            pass


# loading bar animation
def play_animation(top):
    global today

    find_img()
    tu = 1
    while tu == 1:
        ret, frame = cap.read()
        ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)

        print(ClassIndex)
        if (len(ClassIndex) != 0):
            for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
                if (ClassInd == 1):
                    cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                    cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font,
                                fontScale=font_scale, color=(0, 255, 0), thickness=2)
                    cv2.imwrite("temp.jpg", frame)

                    h = face_rec("temp.jpg")

                    if h == 0:

                        ever.append("temp.jpg")
                        tu = 0
                        today = datetime.now()

                        break
                    else:
                        os.remove("temp.jpg")
                        continue
                else:
                    pass
        cv2.imshow("Object detection tutorial", frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
        else:
            pass


        for j in range(16):
            Label(top, bg="#76EE00", width=3, height=2).place(x=(j + 30) * 30, y=700)
            time.sleep(0.04)
            top.update_idletasks()
            Label(top, bg="#1F2732", width=3, height=2).place(x=(j + 30) * 30, y=700)



    cap.release()
    data2()


# the main window of the programme
def main_window():
    global my_text1, my_text2, my_text3

    splash_root.destroy()


    ctk.set_default_color_theme("green")

    root = Tk()
    root.geometry(str(width) + 'x' + str(height))
    root.title("K9")
    root.configure(background="black")



    label1 = ctk.CTkLabel(master=root, text="EXPLORE DATABASE", font=('Times', 50), corner_radius=12,
                          text_color="#FFFFE4")
    label1.pack(pady=30)

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=40, fill='both', expand=True)

    my_text1 = ctk.CTkEntry(master=frame, placeholder_text="Name", font=("Arial", 23), height=50, width=300)
    my_text1.place(x=600, y=60)

    my_text2 = ctk.CTkEntry(master=frame, placeholder_text="FIR ID", font=("Arial", 23), height=50, width=300)
    my_text2.place(x=600, y=160)

    my_text3 = ctk.CTkEntry(master=frame, placeholder_text="Date of Birth", font=("Arial", 23), height=50, width=300)
    my_text3.place(x=600, y=260)

    button = ctk.CTkButton(frame, text='SEARCH', font=("Times", 28), command=data)
    button.place(x=675, y=400)

splash_root.after(3000, main_window)
mainloop()
