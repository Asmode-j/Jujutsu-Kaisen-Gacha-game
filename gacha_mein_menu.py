from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

global valyta, kol_vo
valyta=10000
kol_vo=0

def Main_gacha():
    global window, tabControl, new_game_btn, valyta, kol_vo
    window = Tk()
    window.title("Gacha game")  
    window.geometry('750x550')
    style=ttk.Style(window)
    style.configure('lefttab.TNotebook',tabposition="wn")
        
    def gacha_system():
        global window, valyta, kol_vo
        tabControl.pack_forget()
        new_game_btn.pack_forget()
        
        if valyta == 0:
            mein_okno_gacha()
        
        valyta-=10
        result=[]
        result_index=[]

        def random_cherecter():
            global kol_vo
            file = open("cherecters.txt", "r" , encoding="utf-8")
            lines =file.readlines()
            for i in range(10):
                j=random.randint(1, 1000)
                if j<=10:
                    #5*
                    ran= random.randint(1, 2)
                    if ran == 1:
                        r= random.randint(0, 1)
                        result.append(lines[r].split(';')[1])
                        result_index.append(lines[r].split(';')[0])
                    else:
                        k=random.randint(0, 5)
                        result.append(lines[k].split(';')[1])
                        result_index.append(lines[k].split(';')[0])
                    kol_vo=0
                elif kol_vo>=80:
                    #5*
                    ran= random.randint(1, 2)
                    if ran == 1:
                        r= random.randint(0, 1)
                        result.append(lines[r].split(';')[1])
                        result_index.append(lines[r].split(';')[0])
                    else:
                        k=random.randint(0, 5)
                        result.append(lines[k].split(';')[1])
                        result_index.append(lines[k].split(';')[0])
                    kol_vo=0
                elif j>10 and j<250:
                    #4*
                    kol_vo+=1
                    k=random.randint(6, 17)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                elif j>=250 and j<550:
                    #3*
                    kol_vo+=1
                    k=random.randint(18, 29)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                elif j>=550 and j<850:
                    #2*
                    kol_vo+=1
                    k=random.randint(30, 34)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                else:
                    #1*
                    kol_vo+=1
                    k=random.randint(35, 40)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])

        random_cherecter()
        def okno_s_perekl():
            global index, window, _5, _4, _3, _2, _1
            index = 0
            file = open("cherecters.txt", "r" , encoding="utf-8")
            lines =file.readlines()
            _5=[]
            _4=[]
            _3=[]
            _2=[]
            _1=[]
            for k in range(len(lines)):
                if k<=5:
                    _5.append(lines[k].split(';')[0])
                elif k>=6 and k<=17:
                    _4.append(lines[k].split(';')[0])
                elif k>=18 and k<=29:
                    _3.append(lines[k].split(';')[0])
                elif k>=30 and k<=34:
                    _2.append(lines[k].split(';')[0])
                elif k>=35 and k<=40:
                    _1.append(lines[k].split(';')[0])
                    
            def bg():
                global bag
                if str(result_index[index]) in _5:
                    #5*
                    bag='yellow'
                    return bag
                elif str(result_index[index]) in _4:
                    #4*
                    bag='orange'
                    return bag
                elif str(result_index[index]) in _3:
                    #3*
                    bag='blue'
                    return bag
                elif str(result_index[index]) in _2:
                    #2*
                    bag='green'
                    return bag
                elif str(result_index[index]) in _1:
                    #1*
                    bag='grey'
                    return bag
            def configure():
                global index
                if index <9:
                    index+=1
                    bg()
                    img = PhotoImage(file=f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index]}.png")
                    OP.create_image(400,550,anchor=SE, image=img)
                    LP.configure(bg=bag)
                    LP.configure(text=f'{result[index]}')
                    window.mainloop()
                else:
                    OP.pack_forget()
                    btn.place_forget()
                    btn1.place_forget()
                    LP.place_forget()                  
                    okno()
            def propysk():
                global index
                index+=9
                configure()
                
            bg()       
            OP= Canvas(window,width=400, height=600, bg='grey')
            OP.pack()
            img = PhotoImage(file=f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index]}.png")
            OP.create_image(400,550,anchor=SE, image=img)
            LP= Label(window,width=28, height=2,
                      bg=bag, text = f'{result[index]}')
            LP.place(x=450, y=400)
            btn = Button(window,text='Далее', command = configure)
            btn.place(x=525, y=490)
            btn1 = Button(window,text='Пропустить', command = propysk)
            btn1.place(x=402, y=490)
            window.mainloop()

        def okno():
            global index_1, bag
            index_1=0
            def bg():
                global bag
                if str(result_index[index_1]) in _5:
                    #5*
                    bag='yellow'
                    return bag
                elif str(result_index[index_1]) in _4:
                    #4*
                    bag='orange'
                    return bag
                elif str(result_index[index_1]) in _3:
                    #3*
                    bag='blue'
                    return bag
                elif str(result_index[index_1]) in _2:
                    #2*
                    bag='green'
                    return bag
                elif str(result_index[index_1]) in _1:
                    #1*
                    bag='grey'
                    return bag          
            def ext():
                for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                    i.pack_forget()
                frame_bottom.pack_forget()
                frame_bottom1.pack_forget()
                frame_top.pack_forget()
                frame_top1.pack_forget()
                btn_exit.place_forget()
                btn_restart.place_forget()
                
                mein_okno_gacha()                
            def restart():
                for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                    i.pack_forget()
                frame_bottom.pack_forget()
                frame_bottom1.pack_forget()
                frame_top.pack_forget()
                frame_top1.pack_forget()
                btn_exit.place_forget()
                btn_restart.place_forget()
                gacha_system()
                
            frame_top1 = LabelFrame()
            frame_top1.pack()
            for i in range(1,6):
                globals() [f"OP{i}"] =Canvas(frame_top1,width=138, height=225, bg='grey')
            for i in (OP1,OP2,OP3,OP4,OP5):
                i.pack(side=LEFT, padx=2,pady=2)   
            frame_top = LabelFrame()
            frame_top.pack()
            for i in range(1,6):
                globals() [f"L{i}"] =Label(frame_top, width=20, height=2,
                                           bd=0,bg="grey", text=f'{result[i-1]}')
            for i in (L1,L2,L3,L4,L5):
                i.pack(side=LEFT, padx=2,pady=2)
            frame_bottom1 = LabelFrame()
            frame_bottom1.pack()
            for i in range(6,11):
                globals() [f"OP{i}"] =Canvas(frame_bottom1,width=138, height=225, bg='grey')
            for i in (OP6,OP7,OP8,OP9,OP10):
                i.pack(side=LEFT, padx=2,pady=2)              
            frame_bottom =LabelFrame()
            frame_bottom.pack()
            for i in range(6,11):
                globals() [f"L{i}"] =Label(frame_bottom, width=20, height=2,
                                           bd=0,bg="grey", text=f'{result[i-1]}')
            for i in (L6,L7,L8,L9,L10):
                i.pack(side=LEFT, padx=2,pady=2)
            for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                bg()
                i.configure(bg=bag)
                index_1+=1             
            index_1=0
            images=[]
            for i in (OP1,OP2,OP3,OP4,OP5,OP6,OP7,OP8,OP9,OP10):
                image = Image.open(f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index_1]}.png")
                scaled_image = image.resize((138,225))
                image4canvas = ImageTk.PhotoImage(scaled_image)
                images.append(image4canvas)
                i.create_image(0, 0, anchor=NW, image=image4canvas)
                index_1+=1
            btn_exit = Button(text='Выйти', command = ext)
            btn_exit.place(x=660, y=490)
            btn_restart= Button(text='Заново', command = restart)
            btn_restart.place(x=600, y=490)
            window.mainloop()            
        okno_s_perekl()
        window.mainloop()
##################
    def gacha_system_2():
        global window, valyta, kol_vo
        tabControl.pack_forget()
        new_game_btn.pack_forget()
        
        if valyta == 0:
            mein_okno_gacha()
        
        valyta-=10
        result=[]
        result_index=[]
        
        def random_cherecter_2():
            global kol_vo
            file = open("cherecters.txt", "r" , encoding="utf-8")
            lines =file.readlines()
            for i in range(10):
                j=random.randint(1, 1000)
                if j<=10:
                    #5*
                    ran= random.randint(1, 2)

                    if ran == 1:
                        r= 5
                        result.append(lines[r].split(';')[1])
                        result_index.append(lines[r].split(';')[0])
                    else:
                        k=random.randint(0, 5)
                        result.append(lines[k].split(';')[1])
                        result_index.append(lines[k].split(';')[0])
                    kol_vo=0
                elif kol_vo>=80:
                    #5*
                    ran= random.randint(1, 2)
                    if ran == 1:
                        r= 5
                        result.append(lines[r].split(';')[1])
                        result_index.append(lines[r].split(';')[0])
                    else:
                        k=random.randint(0, 5)
                        result.append(lines[k].split(';')[1])
                        result_index.append(lines[k].split(';')[0])
                    kol_vo=0
                elif j>10 and j<250:
                    #4*
                    kol_vo+=1
                    k=random.randint(6, 17)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                elif j>=250 and j<550:
                    #3*
                    kol_vo+=1
                    k=random.randint(18, 29)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                elif j>=550 and j<850:
                    #2*
                    kol_vo+=1
                    k=random.randint(30, 34)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])
                else:
                    #1*
                    kol_vo+=1
                    k=random.randint(35, 40)
                    result.append(lines[k].split(';')[1])
                    result_index.append(lines[k].split(';')[0])


        random_cherecter_2()
        def okno_s_perekl_2():
            global index, window, _5, _4, _3, _2, _1
            index = 0
            file = open("cherecters.txt", "r" , encoding="utf-8")
            lines =file.readlines()
            _5=[]
            _4=[]
            _3=[]
            _2=[]
            _1=[]
            for k in range(len(lines)):
                if k<=5:
                    _5.append(lines[k].split(';')[0])
                elif k>=6 and k<=17:
                    _4.append(lines[k].split(';')[0])
                elif k>=18 and k<=29:
                    _3.append(lines[k].split(';')[0])
                elif k>=30 and k<=34:
                    _2.append(lines[k].split(';')[0])
                elif k>=35 and k<=40:
                    _1.append(lines[k].split(';')[0])
                    
            def bg():
                global bag
                if str(result_index[index]) in _5:
                    #5*
                    bag='yellow'
                    return bag
                elif str(result_index[index]) in _4:
                    #4*
                    bag='orange'
                    return bag
                elif str(result_index[index]) in _3:
                    #3*
                    bag='blue'
                    return bag
                elif str(result_index[index]) in _2:
                    #2*
                    bag='green'
                    return bag
                elif str(result_index[index]) in _1:
                    #1*
                    bag='grey'
                    return bag
            def configure():
                global index
                if index <9:
                    index+=1
                    bg()
                    img = PhotoImage(file=f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index]}.png")
                    OP.create_image(400,550,anchor=SE, image=img)
                    LP.configure(bg=bag)
                    LP.configure(text=f'{result[index]}')
                    window.mainloop()
                else:
                    OP.pack_forget()
                    btn.place_forget()
                    btn1.place_forget()
                    LP.place_forget()                  
                    okno_2()
            def propysk():
                global index
                index+=9
                configure()
                
            bg()       
            OP= Canvas(window,width=400, height=600, bg='grey')
            OP.pack()
            img = PhotoImage(file=f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index]}.png")
            OP.create_image(400,550,anchor=SE, image=img)
            LP= Label(window,width=28, height=2,
                      bg=bag, text = f'{result[index]}')
            LP.place(x=450, y=400)
            btn = Button(window,text='Далее', command = configure)
            btn.place(x=525, y=490)
            btn1 = Button(window,text='Пропустить', command = propysk)
            btn1.place(x=402, y=490)
            window.mainloop()

        def okno_2():
            global index_1, bag
            index_1=0
            def bg():
                global bag
                if str(result_index[index_1]) in _5:
                    #5*
                    bag='yellow'
                    return bag
                elif str(result_index[index_1]) in _4:
                    #4*
                    bag='orange'
                    return bag
                elif str(result_index[index_1]) in _3:
                    #3*
                    bag='blue'
                    return bag
                elif str(result_index[index_1]) in _2:
                    #2*
                    bag='green'
                    return bag
                elif str(result_index[index_1]) in _1:
                    #1*
                    bag='grey'
                    return bag          
            def ext():
                for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                    i.pack_forget()
                frame_bottom.pack_forget()
                frame_bottom1.pack_forget()
                frame_top.pack_forget()
                frame_top1.pack_forget()
                btn_exit.place_forget()
                btn_restart.place_forget()
                
                mein_okno_gacha()                
            def restart():
                for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                    i.pack_forget()
                frame_bottom.pack_forget()
                frame_bottom1.pack_forget()
                frame_top.pack_forget()
                frame_top1.pack_forget()
                btn_exit.place_forget()
                btn_restart.place_forget()
                gacha_system_2()
                
            frame_top1 = LabelFrame()
            frame_top1.pack()
            for i in range(1,6):
                globals() [f"OP{i}"] =Canvas(frame_top1,width=138, height=225, bg='grey')
            for i in (OP1,OP2,OP3,OP4,OP5):
                i.pack(side=LEFT, padx=2,pady=2)   
            frame_top = LabelFrame()
            frame_top.pack()
            for i in range(1,6):
                globals() [f"L{i}"] =Label(frame_top, width=20, height=2,
                                           bd=0,bg="grey", text=f'{result[i-1]}')
            for i in (L1,L2,L3,L4,L5):
                i.pack(side=LEFT, padx=2,pady=2)
            frame_bottom1 = LabelFrame()
            frame_bottom1.pack()
            for i in range(6,11):
                globals() [f"OP{i}"] =Canvas(frame_bottom1,width=138, height=225, bg='grey')
            for i in (OP6,OP7,OP8,OP9,OP10):
                i.pack(side=LEFT, padx=2,pady=2)              
            frame_bottom =LabelFrame()
            frame_bottom.pack()
            for i in range(6,11):
                globals() [f"L{i}"] =Label(frame_bottom, width=20, height=2,
                                           bd=0,bg="grey", text=f'{result[i-1]}')
            for i in (L6,L7,L8,L9,L10):
                i.pack(side=LEFT, padx=2,pady=2)
            for i in (L1,L2,L3,L4,L5,L6,L7,L8,L9,L10):
                bg()
                i.configure(bg=bag)
                index_1+=1             
            index_1=0
            images=[]
            for i in (OP1,OP2,OP3,OP4,OP5,OP6,OP7,OP8,OP9,OP10):
                image = Image.open(f"C:/Users/Asmodej/Desktop/Programming/Игра гача/CherectersFoto/{result_index[index_1]}.png")
                scaled_image = image.resize((138,225))
                image4canvas = ImageTk.PhotoImage(scaled_image)
                images.append(image4canvas)
                i.create_image(0, 0, anchor=NW, image=image4canvas)
                index_1+=1
            btn_exit = Button(text='Выйти', command = ext)
            btn_exit.place(x=660, y=490)
            btn_restart= Button(text='Заново', command = restart)
            btn_restart.place(x=600, y=490)
            window.mainloop()            
        okno_s_perekl_2()
        window.mainloop()
            

##############

    def vozvrat_v_menu():
            pass
    
    def mein_okno_gacha():
        global window, tabControl, new_game_btn, valyta
        
        tabControl = ttk.Notebook(window, style='lefttab.TNotebook')
        
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Классическая гача')
        tabControl.add(tab2, text='Временная гача     ')
        tabControl.pack(expand=1, fill = 'both')
####
        canvas = Canvas(tab1,height=480, width=620, bg='grey')
        canvas.place(x=0,y=5)
        imag=PhotoImage(file='gacha1_foto.png')
        canvas.create_image(0, 0, anchor=NW, image=imag)
        canvas.create_text(275, 50, text="Сугуру Гето", fill="Black",font=("Arial", 14))
        canvas.create_text(345, 165, text="Годжо Сатору", fill="Black",font=("Arial", 14))


        valyta_label=ttk.Label(tab1,width=30,
                     font=("Arial", 14),
                     text=f'Валюта: {valyta}')
        valyta_label.place(x=30, y = 490)
        b1=ttk.Button(tab1,width=30,
                      text='Крутить гачу',
                      command= gacha_system)
        b1.place(x=400, y=490)

####
        canvas_2 = Canvas(tab2,height=480, width=620, bg='grey')
        canvas_2.place(x=0,y=5)
        imag_2=PhotoImage(file='gacha2_foto.png')
        canvas_2.create_image(0, 0, anchor=NW, image=imag_2)
        canvas_2.create_text(310, 80, text="Сукуна", fill="white",font=("Arial", 16))
        
        valyta_label_2=ttk.Label(tab2,width=30,
                     font=("Arial", 14),
                     text=f'Валюта: {valyta}')
        valyta_label_2.place(x=30, y = 490)
        b1_2=ttk.Button(tab2,width=30,
                      text='Крутить гачу',
                      command= gacha_system_2)
        b1_2.place(x=400, y=490)
        
####

        new_game_btn = Button(text = 'Вернуться в главное меню', command=vozvrat_v_menu)
        new_game_btn.pack(anchor=W)

        window.mainloop()
            
    mein_okno_gacha()
Main_gacha()
