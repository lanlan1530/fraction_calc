from tkinter import *
from fractions import *
from time import *
import tkinter.ttk as ttk
def log_out(a,type='INFO'):
    log_show.insert(INSERT,strftime('%Y-%m-%d %H:%M:%S',localtime(time()))+' '+type+':'+a+'\n') 
    en1.insert(INSERT,'')
    en2.insert(INSERT,'')
def submit():
    fractions_list.append(Fraction(int(en1.get()),int(en2.get())))
    fractions_list.append(choose.get())
    log_out('Submited:'+en1.get()+';'+en2.get()+';'+choose.get())
def calcs():
    s=1
    re=0
    re=fractions_list[s-1]+fractions_list[s+1]
    for i in fractions_list:
        
        if type(i)==Fraction:
            pass
        else:
            if i=='加':
                re=re+fractions_list[s+1]
                log_out('+')
            elif i=='减':
                re=re-fractions_list[s+1]
                log_out('-')
            elif i=='乘':
                re=re*fractions_list[s+1]
                log_out('*')
            elif i=='除':
                re=re/fractions_list[s+1]
                log_out('/')
            else:
                #temp=Fraction(1,1)
                #re=re-temp
                ew.set(Fraction(re))
                log_out('Output:'+str(re))                
    s=s+1
def clear():
    global fractions_list
    fractions_list=[]
    fractions_list.append(Fraction(0,1))
    fractions_list.append('')
    ew.set('')
    en1.delete(0,END)
    en2.delete(0,END)
    log_out('Clear to'+str(fractions_list))
w=Tk()
w.geometry('800x600')
w.config(bg='#C9EEFF')
ew=StringVar()
fractions_list=[]
#Title,font by GNU Unifont(This app font always this)
fractions_list.append(Fraction(0,1))
fractions_list.append('')
f1=Frame(w,bg='#C9EEFF')
f1.place(relx=0,rely=0,relheight=0.2,relwidth=1)
t1=Label(f1,bg='#C9EEFF',text='分数计算器',font='Unifont 18')
t1.pack()
t2=Label(f1,bg='#C9EEFF',text='By lanlan-1530',font='Unifont 12')
t2.pack()
Button(f1,text='clear',command=clear,font='Unifont 10',relief='flat').place(relx=0,rely=0,relheight=0.1,relwidth=0.06)
#For submit fractions to somewhere
inputs=Frame(w,bg='#CCEEFF')
inputs.place(relx=0,rely=0.2,relheight=0.4,relwidth=0.5)
en1=Entry(inputs)
en1.place(relx=0.15,rely=0.3,width=20)
Label(inputs,bg='#C9EEFF',text='/',font='Unifont 15').place(relx=0.25,rely=0.29)
en2=Entry(inputs)
en2.place(relx=0.35,rely=0.3,width=20)
bt1=Button(inputs,command=submit,relief='flat',bg='#C9EEFF',text='提交',font='Unifont 10')
bt1.place(relx=0.25,rely=0.5,relheight=0.1,relwidth=0.15)
choose=StringVar()
list1=['','加','减','乘','除','结束']
ttk.OptionMenu(inputs,choose,*list1).place(relx=0.25,rely=0.7)
#calc button
calc=Button(w,text='计算',command=calcs,relief='flat',bg='#C9EEFF')
calc.place(relx=0.6,rely=0.6,relheight=0.1,relwidth=0.06)
Label(w,textvariable=ew,relief='flat',bg='#C9EEFF').place(relx=0.7,rely=0.6)
#log show
log_show=Text(font='Unifont 12')
log_show.place(relx=0,rely=0.6,relheight=0.4,relwidth=0.5)
#mainloop
w.mainloop()