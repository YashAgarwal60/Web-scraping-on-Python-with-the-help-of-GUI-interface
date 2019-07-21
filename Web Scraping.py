import requests as rt
import bs4
from tkinter import *
def scrap(name):
    dt=rt.request('get','https://www.1mg.com/search/all?name={}'.format(name))
    s=bs4.BeautifulSoup(dt.text,'html.parser')
    for i in s.findAll('div',{'class':'col-md-3 col-sm-4 col-xs-6 style__container___jkjS2'}):
        x=i.find('a')
        dts=rt.request('get','https://www.1mg.com'+x.get('href'))
        s1=bs4.BeautifulSoup(dts.text,'html.parser')
        mn=s1.find('div',{'class':'ProductDescription__product-description___1PfGf'})
        yield mn.text
def get(name,mess):
    global obj
    try:
        obj=scrap(name)
        mess.config(text=next(obj))
    except:
        mess.config(text='invalid name')
def datas(mess):
    global obj
    try:
        mess.config(text=next(obj))
    except:
        mess.config(text='end')
def mygui():
    scr=Tk()
    scr.geometry('1200x600+0+0')
    l=Label(scr,text='MEDICAL INFORMATION SYSTEM',font=('times',20,'bold'),bg='yellow')
    l.pack(fill=X,side=TOP)
    f=Frame(scr,bg='blue')
    f.pack(fill=BOTH,expand=12)
    e=Entry(f,font=('times',20,'bold'),bg='yellow')
    e.place(x=500,y=100)
    l=Label(f,text='Name',font=('times',20,'bold'),bg='yellow')
    l.place(x=400,y=100)
    b=Button(f,text='get',font=('times',20,'bold'),bg='yellow',command=lambda :get(e.get(),m))
    b.place(x=400,y=200)
    m=Message(f,bg='yellow',font=('times',15,'bold'))
    m.place(x=0,y=250)
    b1=Button(f,text='next',font=('times',20,'bold'),bg='yellow',command=lambda :datas(m))
    b1.place(x=600,y=250)
    scr.mainloop()
mygui()
