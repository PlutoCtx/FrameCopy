#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.ttk import *


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('460x519')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='文件[F]', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0., rely=0.046, relwidth=0.124, relheight=0.048)

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='操作[O]', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.122, rely=0.046, relwidth=0.124, relheight=0.048)

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='升级[U]', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.243, rely=0.046, relwidth=0.124, relheight=0.048)

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='语言[L]', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.365, rely=0.046, relwidth=0.124, relheight=0.048)

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='帮助[H]', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.487, rely=0.046, relwidth=0.124, relheight=0.048)

        self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
        self.Command1 = Button(self.top, text='CRC', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.609, rely=0.046, relwidth=0.124, relheight=0.048)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0., rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.087, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.191, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.278, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.383, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.487, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.591, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.696, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.8, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Picture1 = Canvas(self.top)
        self.Picture1.place(relx=0.904, rely=0.108, relwidth=0.089, relheight=0.125)

        self.Combo1List = ['Add items in design or code!', ]
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体', 9))
        self.Combo1.place(relx=0.035, rely=0.277, relwidth=0.228, relheight=0.039)
        self.Combo1.set(self.Combo1List[0])

        self.style.configure('Line1.TSeparator', background='#000000')
        self.Line1 = Separator(self.top, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0.017, rely=0.324, relwidth=0.261, relheight=0.0019)

        self.style.configure('Line2.TSeparator', background='#000000')
        self.Line2 = Separator(self.top, orient='vertical', style='Line2.TSeparator')
        self.Line2.place(relx=0.017, rely=0.262, relwidth=0.0022, relheight=0.062)

        self.style.configure('Line3.TSeparator', background='#000000')
        self.Line3 = Separator(self.top, orient='vertical', style='Line3.TSeparator')
        self.Line3.place(relx=0.278, rely=0.324, relwidth=0.0022, relheight=0.062)

        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='芯片选择', style='Label1.TLabel')
        self.Label1.place(relx=0.104, rely=0.247, relwidth=0.107, relheight=0.033)

        self.style.configure('Line4.TSeparator', background='#000000')
        self.Line4 = Separator(self.top, orient='horizontal', style='Line4.TSeparator')
        self.Line4.place(relx=0.017, rely=0.262, relwidth=0.087, relheight=0.0019)

        self.style.configure('Line5.TSeparator', background='#000000')
        self.Line5 = Separator(self.top, orient='horizontal', style='Line5.TSeparator')
        self.Line5.place(relx=0.209, rely=0.262, relwidth=0.07, relheight=0.0019)

        self.Combo2List = ['Add items in design or code!', ]
        self.Combo2 = Combobox(self.top, values=self.Combo2List, font=('宋体', 9))
        self.Combo2.place(relx=0.33, rely=0.277, relwidth=0.228, relheight=0.039)
        self.Combo2.set(self.Combo2List[0])

        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='编程区域', style='Label1.TLabel')
        self.Label1.place(relx=0.383, rely=0.247, relwidth=0.107, relheight=0.033)

        self.style.configure('Line6.TSeparator', background='#000000')
        self.Line6 = Separator(self.top, orient='horizontal', style='Line6.TSeparator')
        self.Line6.place(relx=0.313, rely=0.324, relwidth=0.261, relheight=0.0019)

        self.style.configure('Line7.TSeparator', background='#000000')
        self.Line7 = Separator(self.top, orient='vertical', style='Line7.TSeparator')
        self.Line7.place(relx=0.313, rely=0.324, relwidth=0.0022, relheight=0.062)

        self.style.configure('Line8.TSeparator', background='#000000')
        self.Line8 = Separator(self.top, orient='horizontal', style='Line8.TSeparator')
        self.Line8.place(relx=0.313, rely=0.262, relwidth=0.07, relheight=0.0019)

        self.style.configure('Line9.TSeparator', background='#000000')
        self.Line9 = Separator(self.top, orient='vertical', style='Line9.TSeparator')
        self.Line9.place(relx=0.574, rely=0.324, relwidth=0.0022, relheight=0.062)

        self.style.configure('Line10.TSeparator', background='#000000')
        self.Line10 = Separator(self.top, orient='horizontal', style='Line10.TSeparator')
        self.Line10.place(relx=0.487, rely=0.262, relwidth=0.087, relheight=0.0019)

        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.top, text='保存项目', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.609, rely=0.247, relwidth=0.193, relheight=0.048)

        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.top, text='载入项目', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.609, rely=0.293, relwidth=0.193, relheight=0.048)

        self.style.configure('Command3.TButton', font=('宋体', 9))
        self.Command3 = Button(self.top, text='当前：常规烧录', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.817, rely=0.247, relwidth=0.159, relheight=0.094)

        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='设置', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.035, rely=0.355, relwidth=0.211, relheight=0.064)

        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='Option', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.261, rely=0.355, relwidth=0.211, relheight=0.064)

        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='代码', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.487, rely=0.355, relwidth=0.211, relheight=0.064)

        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='EEPROM', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.713, rely=0.355, relwidth=0.211, relheight=0.064)

        self.style.configure('Frame1.TLabelframe', font=('宋体', 9))
        self.Frame1 = LabelFrame(self.top, text='Frame1', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.017, rely=0.447, relwidth=0.976, relheight=0.418)

        self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
        self.Option1 = Radiobutton(self.top, text='16', value=0, style='Option1.TRadiobutton')
        self.Option1.place(relx=0.087, rely=0.601, relwidth=0.089, relheight=0.023)

        self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
        self.Option2 = Radiobutton(self.top, text='递减', value=0, style='Option2.TRadiobutton')
        self.Option2.place(relx=0.087, rely=0.709, relwidth=0.124, relheight=0.023)

        self.Combo3List = ['Add items in design or code!', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.417, rely=0.601, relwidth=0.211, relheight=0.039)
        self.Combo3.set(self.Combo3List[0])

        self.Combo3List = ['Add items in design or code!', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.417, rely=0.663, relwidth=0.211, relheight=0.039)
        self.Combo3.set(self.Combo3List[0])

        self.Combo3List = ['Add items in design or code!', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.417, rely=0.709, relwidth=0.211, relheight=0.039)
        self.Combo3.set(self.Combo3List[0])

        self.style.configure('Line11.TSeparator', background='#000000')
        self.Line11 = Separator(self.Frame1, orient='vertical', style='Line11.TSeparator')
        self.Line11.place(relx=0.018, rely=0.111, relwidth=0.0022, relheight=0.627)

        self.style.configure('Line12.TSeparator', background='#000000')
        self.Line12 = Separator(self.Frame1, orient='vertical', style='Line12.TSeparator')
        self.Line12.place(relx=0.018, rely=0.774, relwidth=0.0022, relheight=0.184)

        self.style.configure('Line13.TSeparator', background='#000000')
        self.Line13 = Separator(self.Frame1, orient='horizontal', style='Line13.TSeparator')
        self.Line13.place(relx=0.018, rely=0.959, relwidth=0.624, relheight=0.0046)

        self.style.configure('Line14.TSeparator', background='#000000')
        self.Line14 = Separator(self.Frame1, orient='vertical', style='Line14.TSeparator')
        self.Line14.place(relx=0.641, rely=0.959, relwidth=0.0022, relheight=0.184)

        self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
        self.Label2 = Label(self.Frame1, text='序列号选项', style='Label2.TLabel')
        self.Label2.place(relx=0.232, rely=0.074, relwidth=0.145, relheight=0.078)

        self.style.configure('Line15.TSeparator', background='#000000')
        self.Line15 = Separator(self.Frame1, orient='horizontal', style='Line15.TSeparator')
        self.Line15.place(relx=0.018, rely=0.111, relwidth=0.196, relheight=0.0046)

        self.style.configure('Line16.TSeparator', background='#000000')
        self.Line16 = Separator(self.Frame1, orient='horizontal', style='Line16.TSeparator')
        self.Line16.place(relx=0.018, rely=0.737, relwidth=0.624, relheight=0.0046)

        self.style.configure('Line17.TSeparator', background='#000000')
        self.Line17 = Separator(self.Frame1, orient='vertical', style='Line17.TSeparator')
        self.Line17.place(relx=0.641, rely=0.737, relwidth=0.0022, relheight=0.627)

        self.style.configure('Line18.TSeparator', background='#000000')
        self.Line18 = Separator(self.Frame1, orient='horizontal', style='Line18.TSeparator')
        self.Line18.place(relx=0.374, rely=0.111, relwidth=0.267, relheight=0.0046)

        self.style.configure('Label3.TLabel', anchor='w', font=('宋体', 9))
        self.Label3 = Label(self.Frame1, text='烧录次数', style='Label3.TLabel')
        self.Label3.place(relx=0.249, rely=0.737, relwidth=0.109, relheight=0.078)

        self.style.configure('Line19.TSeparator', background='#000000')
        self.Line19 = Separator(self.Frame1, orient='horizontal', style='Line19.TSeparator')
        self.Line19.place(relx=0.018, rely=0.774, relwidth=0.214, relheight=0.0046)

        self.style.configure('Line20.TSeparator', background='#000000')
        self.Line20 = Separator(self.Frame1, orient='horizontal', style='Line20.TSeparator')
        self.Line20.place(relx=0.374, rely=0.774, relwidth=0.267, relheight=0.0046)

        self.style.configure('Line21.TSeparator', background='#000000')
        self.Line21 = Separator(self.Frame1, orient='vertical', style='Line21.TSeparator')
        self.Line21.place(relx=0.677, rely=0.111, relwidth=0.0022, relheight=0.848)

        self.style.configure('Label4.TLabel', anchor='w', font=('宋体', 9))
        self.Label4 = Label(self.Frame1, text='烧录选项', style='Label4.TLabel')
        self.Label4.place(relx=0.766, rely=0.074, relwidth=0.127, relheight=0.078)

        self.style.configure('Line22.TSeparator', background='#000000')
        self.Line22 = Separator(self.Frame1, orient='horizontal', style='Line22.TSeparator')
        self.Line22.place(relx=0.677, rely=0.111, relwidth=0.071, relheight=0.0046)

        self.style.configure('Line23.TSeparator', background='#000000')
        self.Line23 = Separator(self.Frame1, orient='horizontal', style='Line23.TSeparator')
        self.Line23.place(relx=0.891, rely=0.111, relwidth=0.089, relheight=0.0046)

        self.style.configure('Line24.TSeparator', background='#000000')
        self.Line24 = Separator(self.Frame1, orient='vertical', style='Line24.TSeparator')
        self.Line24.place(relx=0.98, rely=0.111, relwidth=0.0022, relheight=0.848)

        self.Check1Var = StringVar(value='0')
        self.style.configure('Check1.TCheckbutton', font=('宋体', 9))
        self.Check1 = Checkbutton(self.Frame1, text='Check1', variable=self.Check1Var, style='Check1.TCheckbutton')
        self.Check1.place(relx=0.713, rely=0.184, relwidth=0.02, relheight=0.055)

        self.Check2Var = StringVar(value='0')
        self.style.configure('Check2.TCheckbutton', font=('宋体', 9))
        self.Check2 = Checkbutton(self.Frame1, text='Check2', variable=self.Check2Var, style='Check2.TCheckbutton')
        self.Check2.place(relx=0.036, rely=0.147, relwidth=0.038, relheight=0.078)

        self.style.configure('Label5.TLabel', anchor='w', font=('宋体', 9))
        self.Label5 = Label(self.Frame1, text='使用序列号', style='Label5.TLabel')
        self.Label5.place(relx=0.089, rely=0.147, relwidth=0.163, relheight=0.078)

        self.style.configure('Line25.TSeparator', background='#000000')
        self.Line25 = Separator(self.Frame1, orient='vertical', style='Line25.TSeparator')
        self.Line25.place(relx=0.036, rely=0.258, relwidth=0.0022, relheight=0.184)

        self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
        self.Option1 = Radiobutton(self.Frame1, text='10', value=0, style='Option1.TRadiobutton')
        self.Option1.place(relx=0.071, rely=0.295, relwidth=0.091, relheight=0.055)

        self.style.configure('Line26.TSeparator', background='#000000')
        self.Line26 = Separator(self.Frame1, orient='horizontal', style='Line26.TSeparator')
        self.Line26.place(relx=0.036, rely=0.442, relwidth=0.196, relheight=0.0046)

        self.style.configure('Line27.TSeparator', background='#000000')
        self.Line27 = Separator(self.Frame1, orient='vertical', style='Line27.TSeparator')
        self.Line27.place(relx=0.232, rely=0.442, relwidth=0.0022, relheight=0.184)

        self.style.configure('Label6.TLabel', anchor='w', font=('宋体', 9))
        self.Label6 = Label(self.Frame1, text='进制', style='Label6.TLabel')
        self.Label6.place(relx=0.107, rely=0.221, relwidth=0.109, relheight=0.115)

        self.style.configure('Line28.TSeparator', background='#000000')
        self.Line28 = Separator(self.Frame1, orient='horizontal', style='Line28.TSeparator')
        self.Line28.place(relx=0.036, rely=0.258, relwidth=0.071, relheight=0.0046)

        self.style.configure('Line29.TSeparator', background='#000000')
        self.Line29 = Separator(self.Frame1, orient='horizontal', style='Line29.TSeparator')
        self.Line29.place(relx=0.16, rely=0.258, relwidth=0.071, relheight=0.0046)

        self.style.configure('Line30.TSeparator', background='#000000')
        self.Line30 = Separator(self.Frame1, orient='vertical', style='Line30.TSeparator')
        self.Line30.place(relx=0.036, rely=0.516, relwidth=0.0022, relheight=0.184)

        self.style.configure('Line31.TSeparator', background='#000000')
        self.Line31 = Separator(self.Frame1, orient='horizontal', style='Line31.TSeparator')
        self.Line31.place(relx=0.036, rely=0.7, relwidth=0.196, relheight=0.0046)

        self.style.configure('Line32.TSeparator', background='#000000')
        self.Line32 = Separator(self.Frame1, orient='vertical', style='Line32.TSeparator')
        self.Line32.place(relx=0.232, rely=0.7, relwidth=0.0022, relheight=0.184)

        self.style.configure('Label7.TLabel', anchor='w', font=('宋体', 9))
        self.Label7 = Label(self.Frame1, text='计数方式', style='Label7.TLabel')
        self.Label7.place(relx=0.089, rely=0.479, relwidth=0.109, relheight=0.078)

        self.style.configure('Line33.TSeparator', background='#000000')
        self.Line33 = Separator(self.Frame1, orient='horizontal', style='Line33.TSeparator')
        self.Line33.place(relx=0.036, rely=0.516, relwidth=0.053, relheight=0.0046)

        self.style.configure('Line34.TSeparator', background='#000000')
        self.Line34 = Separator(self.Frame1, orient='horizontal', style='Line34.TSeparator')
        self.Line34.place(relx=0.196, rely=0.516, relwidth=0.036, relheight=0.0046)

        self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
        self.Option2 = Radiobutton(self.Frame1, text='递增', value=0, style='Option2.TRadiobutton')
        self.Option2.place(relx=0.071, rely=0.553, relwidth=0.127, relheight=0.055)

        self.Combo3List = ['Add items in design or code!', ]
        self.Combo3 = Combobox(self.Frame1, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.41, rely=0.221, relwidth=0.216, relheight=0.092)
        self.Combo3.set(self.Combo3List[0])

        self.style.configure('Label8.TLabel', anchor='w', font=('宋体', 9))
        self.Label8 = Label(self.Frame1, text='长度（位）', style='Label8.TLabel')
        self.Label8.place(relx=0.267, rely=0.221, relwidth=0.145, relheight=0.078)

        self.style.configure('Label9.TLabel', anchor='w', font=('宋体', 9))
        self.Label9 = Label(self.Frame1, text='步进', style='Label9.TLabel')
        self.Label9.place(relx=0.267, rely=0.369, relwidth=0.127, relheight=0.078)

        self.style.configure('Label10.TLabel', anchor='w', font=('宋体', 9))
        self.Label10 = Label(self.Frame1, text='起始值', style='Label10.TLabel')
        self.Label10.place(relx=0.267, rely=0.516, relwidth=0.127, relheight=0.078)

        self.style.configure('Label11.TLabel', anchor='w', font=('宋体', 9))
        self.Label11 = Label(self.Frame1, text='起始地址', style='Label11.TLabel')
        self.Label11.place(relx=0.267, rely=0.627, relwidth=0.109, relheight=0.078)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass
