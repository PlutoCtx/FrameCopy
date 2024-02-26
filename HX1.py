#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Version: python3.10
# @Time: 2024/1/30 9:34
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: copy03.py
# @Software: PyCharm
# @User: chent

import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk


def loading(progressbarOne=None, maxbyte=None):
    # 改变变量属性
    global byte
    # 每次运行500B
    byte += 500
    # 设置指针
    progressbarOne['value'] = byte
    if byte < maxbyte:
        # 经过100ms后再次调用loading方法
        progressbarOne.after(100, loading)

def show(progressbarOne=None, maxbyte=None):
    # 设置进度条的目前值
    progressbarOne['value'] = 0
    # 设置进度条的最大值
    progressbarOne['maximum'] = maxbyte
    # 调用loading方法
    loading(progressbarOne, maxbyte)

def open_progress_window():
    progress_window = ProgressWindow(top)

class Application_ui(Frame):

    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    # def __init__(self, master=None):
    #     Frame.__init__(self, master)
    #     self.master.title('SJ1 SJVH V1.0')
    #     self.master.geometry('462x481')


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('HX1 HXIIA2 V1.0')
        self.master.geometry('462x481')
        self.createWidgets()


    def click_action_open(self):
        # tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')
        r = tkinter.filedialog.askopenfilename(title='Python tkinter',
                                               filetypes=[('All files', '*')])
        print(r)

    def click_action_save(self):
        tkinter.messagebox.showinfo('消息', '保存成功')

    def click_action_download(self):
        tkinter.messagebox.showinfo('消息', '下载成功')

    def click_action_difference(self):
        tkinter.messagebox.showinfo('消息', '对比成功：\n无区别')

    def click_action_coding(self):
        tkinter.messagebox.showinfo('消息', '正在跳转到编程界面')

    def click_action_check(self):
        tkinter.messagebox.showinfo('消息', '检验中，请稍后')

    def click_action_auto(self):
        tkinter.messagebox.showinfo('消息', '进入自动操作模式')

    def click_action_erase(self):
        tkinter.messagebox.showinfo('消息', '擦除成功')

    def click_action_check_empty(self):
        tkinter.messagebox.showinfo('消息', '查空中：\n结果无异常')

    def click_action_help(self):
        tkinter.messagebox.showinfo('消息', '当前模式下无帮助指引')

    def click_action_save_project(self):
        tkinter.messagebox.showinfo('消息', '项目保存成功')

    def click_action_import_project(self):
        tkinter.messagebox.showinfo('消息', '项目载入中')

    def click_action_set(self):
        tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')

    def click_action_option(self):
        tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')

    def click_action_eeprom(self):
        tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')

    def click_action_option(self):
        tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')

    def click_action_option(self):
        tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')



    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        menuBar = Menu(self.top)

        filemenu = Menu(menuBar, tearoff=False)
        filemenu.add_command(label='载入')
        filemenu.add_command(label='保存')
        filemenu.add_command(label='另存为')
        filemenu.add_separator()
        filemenu.add_command(label='对比')
        filemenu.add_command(label='下载')
        filemenu.add_command(label='退出')
        menuBar.add_cascade(label='文件', menu=filemenu)

        operation_menu = Menu(menuBar, tearoff=False)
        operation_menu.add_command(label='查空')
        operation_menu.add_command(label='擦除')
        operation_menu.add_command(label='校验')
        operation_menu.add_command(label='编程')
        operation_menu.add_command(label='自动')
        menuBar.add_cascade(label='操作', menu=operation_menu)

        update_menu = Menu(menuBar, tearoff=False)
        update_menu.add_command(label='更新MCU库')
        update_menu.add_command(label='升级固件')
        update_menu.add_command(label='自动升级检测')
        menuBar.add_cascade(label='升级', menu=update_menu)

        language_menu = Menu(menuBar, tearoff=False)
        language_menu.add_command(label='简体中文')
        language_menu.add_command(label='English')
        language_menu.add_command(label='蘩体中文')
        menuBar.add_cascade(label='语言', menu=language_menu)

        help_menu = Menu(menuBar, tearoff=False)
        help_menu.add_command(label='帮助（CHM）')
        help_menu.add_command(label='关于')
        menuBar.add_cascade(label='帮助', menu=help_menu)

        CRC_menu = Menu(menuBar, tearoff=False)
        CRC_menu.add_command(label='CRC读取')
        menuBar.add_cascade(label='CRC', menu=CRC_menu)

        self.top.config(menu=menuBar)

        img = Image.open('./pic/open.png').resize((30, 45))
        global photo
        photo = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo, compound=LEFT,
                               command=self.click_action_open, style='Command6.TButton')
        self.Command6.place(relx=0.010, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/save.png').resize((30, 45))
        global photo1
        photo1 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo1, compound=LEFT,
                               command=self.click_action_save, style='Command6.TButton')
        self.Command6.place(relx=0.105, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/download.png').resize((30, 45))
        global photo2
        photo2 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo2, compound=LEFT,
                               command=self.click_action_download, style='Command6.TButton')
        self.Command6.place(relx=0.20, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/diff.png').resize((30, 45))
        global photo3
        photo3 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo3, compound=LEFT,
                               command=self.click_action_difference, style='Command6.TButton')
        self.Command6.place(relx=0.295, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/code.png').resize((30, 45))
        global photo4
        photo4 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo4, compound=LEFT,
                               command=self.click_action_coding, style='Command6.TButton')
        self.Command6.place(relx=0.390, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/checkout.png').resize((30, 45))
        global photo5
        photo5 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo5, compound=LEFT,
                               command=self.click_action_check, style='Command6.TButton')
        self.Command6.place(relx=0.485, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/auto.png').resize((30, 45))
        global photo6
        photo6 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo6, compound=LEFT,
                               command=self.click_action_auto, style='Command6.TButton')
        self.Command6.place(relx=0.580, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/erase.png').resize((30, 45))
        global photo7
        photo7 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo7, compound=LEFT,
                               command=self.click_action_erase, style='Command6.TButton')
        self.Command6.place(relx=0.675, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/check.png').resize((30, 45))
        global photo8
        photo8 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo8, compound=LEFT,
                               command=self.click_action_check_empty, style='Command6.TButton')
        self.Command6.place(relx=0.770, rely=0.067, relwidth=0.09, relheight=0.119)

        img = Image.open('./pic/help.png').resize((30, 45))
        global photo9
        photo9 = ImageTk.PhotoImage(img)
        self.style.configure('Command6.TButton', font=('宋体', 9))
        self.Command6 = Button(self.top, text='', image=photo9, compound=LEFT,
                               command=self.click_action_help, style='Command6.TButton')
        self.Command6.place(relx=0.865, rely=0.067, relwidth=0.09, relheight=0.119)

        # 芯片选择
        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='芯片选择', style='Label1.TLabel')
        self.Label1.place(relx=0.10, rely=0.2, relwidth=0.116, relheight=0.035)
        # 下拉框
        self.Combo1List = ['SC92F83A3', 'SC92F83A2', 'SC91F73', 'SC91F72B',
                           'SC91F729B', 'SC91F731', 'SC91F73A3', 'SC91F73A2']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体', 9))
        self.Combo1.place(relx=0.035, rely=0.233, relwidth=0.227, relheight=0.042)
        self.Combo1.set(self.Combo1List[0])
        # 上 左
        self.style.configure('Line4.TSeparator', background='#000000')
        self.Line4 = Separator(self.top, orient='horizontal', style='Line4.TSeparator')
        self.Line4.place(relx=0.017, rely=0.216, relwidth=0.087, relheight=0.0021)
        # 上 右
        self.style.configure('Line5.TSeparator', background='#000000')
        self.Line5 = Separator(self.top, orient='horizontal', style='Line5.TSeparator')
        self.Line5.place(relx=0.208, rely=0.216, relwidth=0.069, relheight=0.0021)
        # 左
        self.style.configure('Line2.TSeparator', background='#000000')
        self.Line2 = Separator(self.top, orient='vertical', style='Line2.TSeparator')
        self.Line2.place(relx=0.017, rely=0.216, relwidth=0.0022, relheight=0.067)
        # 右
        self.style.configure('Line3.TSeparator', background='#000000')
        self.Line3 = Separator(self.top, orient='vertical', style='Line3.TSeparator')
        self.Line3.place(relx=0.277, rely=0.216, relwidth=0.0022, relheight=0.067)
        # 下
        self.style.configure('Line1.TSeparator', background='#000000')
        self.Line1 = Separator(self.top, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0.017, rely=0.283, relwidth=0.26, relheight=0.0021)

        # 编程区域
        self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
        self.Label1 = Label(self.top, text='编程区域', style='Label1.TLabel')
        self.Label1.place(relx=0.381, rely=0.2, relwidth=0.116, relheight=0.035)
        # 下拉框
        self.Combo2List = ['Code', 'EEPROM', 'Code+EEPROM']
        self.Combo2 = Combobox(self.top, values=self.Combo2List, font=('宋体', 9))
        self.Combo2.place(relx=0.329, rely=0.233, relwidth=0.227, relheight=0.042)
        self.Combo2.set(self.Combo2List[0])
        # 上 左
        self.style.configure('Line8.TSeparator', background='#000000')
        self.Line8 = Separator(self.top, orient='horizontal', style='Line8.TSeparator')
        self.Line8.place(relx=0.312, rely=0.216, relwidth=0.069, relheight=0.0021)
        # 上 右
        self.style.configure('Line10.TSeparator', background='#000000')
        self.Line10 = Separator(self.top, orient='horizontal', style='Line10.TSeparator')
        self.Line10.place(relx=0.485, rely=0.216, relwidth=0.087, relheight=0.0021)
        # 左
        self.style.configure('Line7.TSeparator', background='#000000')
        self.Line7 = Separator(self.top, orient='vertical', style='Line7.TSeparator')
        self.Line7.place(relx=0.312, rely=0.216, relwidth=0.0022, relheight=0.067)
        # 右
        self.style.configure('Line9.TSeparator', background='#000000')
        self.Line9 = Separator(self.top, orient='vertical', style='Line9.TSeparator')
        self.Line9.place(relx=0.571, rely=0.216, relwidth=0.0022, relheight=0.067)
        # 下
        self.style.configure('Line6.TSeparator', background='#000000')
        self.Line6 = Separator(self.top, orient='horizontal', style='Line6.TSeparator')
        self.Line6.place(relx=0.312, rely=0.283, relwidth=0.26, relheight=0.0021)

        # 保存项目
        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.top, text='保存项目', command=self.click_action_save_project, style='Command2.TButton')
        self.Command2.place(relx=0.606, rely=0.2, relwidth=0.193, relheight=0.052)
        # 载入项目
        self.style.configure('Command2.TButton', font=('宋体', 9))
        self.Command2 = Button(self.top, text='载入项目', command=self.click_action_import_project, style='Command2.TButton')
        self.Command2.place(relx=0.606, rely=0.249, relwidth=0.193, relheight=0.052)
        # 当前：常规烧录
        self.style.configure('Command3.TButton', font=('宋体', 9))
        self.Command3 = Button(self.top, text='  当前：\n常规烧录', command=open_progress_window, style='Command3.TButton')
        self.Command3.place(relx=0.814, rely=0.2, relwidth=0.158, relheight=0.102)

        # 设置
        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='设置', command=self.click_action_set, style='Command4.TButton')
        self.Command4.place(relx=0.035, rely=0.333, relwidth=0.21, relheight=0.069)
        # Option
        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='Option', command=self.click_action_option, style='Command4.TButton')
        self.Command4.place(relx=0.26, rely=0.333, relwidth=0.21, relheight=0.069)
        # 代码
        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='代码', command=self.click_action_coding, style='Command4.TButton')
        self.Command4.place(relx=0.485, rely=0.333, relwidth=0.21, relheight=0.069)
        # EEPROM
        self.style.configure('Command4.TButton', font=('宋体', 9))
        self.Command4 = Button(self.top, text='EEPROM', command=self.click_action_eeprom, style='Command4.TButton')
        self.Command4.place(relx=0.71, rely=0.333, relwidth=0.21, relheight=0.069)

        # ******************************************************************************
        # ******************************************************************************
        # ******************************************************************************
        # ******************************************************************************
        # 中间的界面
        self.style.configure('Frame1.TLabelframe', font=('宋体', 9))
        self.Frame1 = LabelFrame(self.top, text='', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.017, rely=0.40, relwidth=0.972, relheight=0.451)
        # 序列号选项
        self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
        self.Label2 = Label(self.Frame1, text='序列号选项', style='Label2.TLabel')
        self.Label2.place(relx=0.225, rely=0.040, relwidth=0.145, relheight=0.078)
        # 左上
        self.style.configure('Line15.TSeparator', background='#000000')
        self.Line15 = Separator(self.Frame1, orient='horizontal', style='Line15.TSeparator')
        self.Line15.place(relx=0.018, rely=0.111, relwidth=0.196, relheight=0.0046)
        # 右上
        self.style.configure('Line18.TSeparator', background='#000000')
        self.Line18 = Separator(self.Frame1, orient='horizontal', style='Line18.TSeparator')
        self.Line18.place(relx=0.374, rely=0.111, relwidth=0.267, relheight=0.0046)
        # 左
        self.style.configure('Line11.TSeparator', background='#000000')
        self.Line11 = Separator(self.Frame1, orient='vertical', style='Line11.TSeparator')
        self.Line11.place(relx=0.018, rely=0.111, relwidth=0.0022, relheight=0.627)
        # 右
        self.style.configure('Line17.TSeparator', background='#000000')
        self.Line17 = Separator(self.Frame1, orient='vertical', style='Line17.TSeparator')
        self.Line17.place(relx=0.641, rely=0.111, relwidth=0.0022, relheight=0.627)
        # 下
        self.style.configure('Line16.TSeparator', background='#000000')
        self.Line16 = Separator(self.Frame1, orient='horizontal', style='Line16.TSeparator')
        self.Line16.place(relx=0.018, rely=0.737, relwidth=0.624, relheight=0.0046)

        # 使用序列号
        self.style.configure('Label5.TLabel', anchor='w', font=('宋体', 9))
        self.Label5 = Label(self.Frame1, text='使用序列号', style='Label5.TLabel')
        self.Label5.place(relx=0.089, rely=0.147, relwidth=0.163, relheight=0.078)
        # 进制
        self.style.configure('Label6.TLabel', anchor='w', font=('宋体', 9))
        self.Label6 = Label(self.Frame1, text='进制', style='Label6.TLabel')
        self.Label6.place(relx=0.107, rely=0.221, relwidth=0.109, relheight=0.115)
        # 左上
        self.style.configure('Line28.TSeparator', background='#000000')
        self.Line28 = Separator(self.Frame1, orient='horizontal', style='Line28.TSeparator')
        self.Line28.place(relx=0.036, rely=0.258, relwidth=0.071, relheight=0.0046)
        # 右上
        self.style.configure('Line29.TSeparator', background='#000000')
        self.Line29 = Separator(self.Frame1, orient='horizontal', style='Line29.TSeparator')
        self.Line29.place(relx=0.16, rely=0.258, relwidth=0.071, relheight=0.0046)
        # 左
        self.style.configure('Line25.TSeparator', background='#000000')
        self.Line25 = Separator(self.Frame1, orient='vertical', style='Line25.TSeparator')
        self.Line25.place(relx=0.036, rely=0.258, relwidth=0.0022, relheight=0.184)
        # 右
        self.style.configure('Line27.TSeparator', background='#000000')
        self.Line27 = Separator(self.Frame1, orient='vertical', style='Line27.TSeparator')
        self.Line27.place(relx=0.232, rely=0.258, relwidth=0.0022, relheight=0.184)
        # 下
        self.style.configure('Line26.TSeparator', background='#000000')
        self.Line26 = Separator(self.Frame1, orient='horizontal', style='Line26.TSeparator')
        self.Line26.place(relx=0.036, rely=0.442, relwidth=0.196, relheight=0.0046)
        # 10
        self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
        self.Option1 = Radiobutton(self.Frame1, text='10', value=1, style='Option1.TRadiobutton')
        self.Option1.place(relx=0.065, rely=0.300, relwidth=0.110, relheight=0.065)
        # 16
        self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
        self.Option2 = Radiobutton(self.Frame1, text='16', value=0, style='Option2.TRadiobutton')
        self.Option2.place(relx=0.065, rely=0.365, relwidth=0.110, relheight=0.067)

        # 计数方式
        self.style.configure('Label7.TLabel', anchor='w', font=('宋体', 9))
        self.Label7 = Label(self.Frame1, text='计数方式', style='Label7.TLabel')
        self.Label7.place(relx=0.089, rely=0.479, relwidth=0.119, relheight=0.078)
        # 左上
        self.style.configure('Line33.TSeparator', background='#000000')
        self.Line33 = Separator(self.Frame1, orient='horizontal', style='Line33.TSeparator')
        self.Line33.place(relx=0.036, rely=0.516, relwidth=0.053, relheight=0.0046)
        # 右上
        self.style.configure('Line34.TSeparator', background='#000000')
        self.Line34 = Separator(self.Frame1, orient='horizontal', style='Line34.TSeparator')
        self.Line34.place(relx=0.196, rely=0.516, relwidth=0.036, relheight=0.0046)
        # 左
        self.style.configure('Line30.TSeparator', background='#000000')
        self.Line30 = Separator(self.Frame1, orient='vertical', style='Line30.TSeparator')
        self.Line30.place(relx=0.036, rely=0.516, relwidth=0.0022, relheight=0.184)
        # 右
        self.style.configure('Line32.TSeparator', background='#000000')
        self.Line32 = Separator(self.Frame1, orient='vertical', style='Line32.TSeparator')
        self.Line32.place(relx=0.232, rely=0.514, relwidth=0.0022, relheight=0.184)
        # 下
        self.style.configure('Line31.TSeparator', background='#000000')
        self.Line31 = Separator(self.Frame1, orient='horizontal', style='Line31.TSeparator')
        self.Line31.place(relx=0.036, rely=0.7, relwidth=0.196, relheight=0.0046)
        # 递增
        self.style.configure('Option3.TRadiobutton', font=('宋体', 9))
        self.Option3 = Radiobutton(self.Frame1, text='递增', value=0, style='Option3.TRadiobutton')
        self.Option3.place(relx=0.065, rely=0.553, relwidth=0.127, relheight=0.072)
        # 递减
        self.style.configure('Option4.TRadiobutton', font=('宋体', 9))
        self.Option4 = Radiobutton(self.Frame1, text='递减', value=1, style='Option4.TRadiobutton')
        self.Option4.place(relx=0.065, rely=0.628, relwidth=0.127, relheight=0.072)



        # 长度
        self.style.configure('Label8.TLabel', anchor='w', font=('宋体', 9))
        self.Label8 = Label(self.Frame1, text='长度（位）', style='Label8.TLabel')
        self.Label8.place(relx=0.267, rely=0.221, relwidth=0.145, relheight=0.078)

        self.Combo3List = ['长度(位)', ]
        self.Combo3 = Combobox(self.Frame1, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.41, rely=0.221, relwidth=0.216, relheight=0.092)
        self.Combo3.set(self.Combo3List[0])
        # 步进
        self.style.configure('Label9.TLabel', anchor='w', font=('宋体', 9))
        self.Label9 = Label(self.Frame1, text='步进', style='Label9.TLabel')
        self.Label9.place(relx=0.267, rely=0.369, relwidth=0.127, relheight=0.078)

        self.Combo3List = ['步进', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.416, rely=0.582, relwidth=0.21, relheight=0.042)
        self.Combo3.set(self.Combo3List[0])
        # 起始值
        self.style.configure('Label10.TLabel', anchor='w', font=('宋体', 9))
        self.Label10 = Label(self.Frame1, text='起始值', style='Label10.TLabel')
        self.Label10.place(relx=0.267, rely=0.516, relwidth=0.127, relheight=0.078)

        self.Combo3List = ['起始值', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.416, rely=0.632, relwidth=0.21, relheight=0.042)
        self.Combo3.set(self.Combo3List[0])
        # 起始地址
        self.style.configure('Label11.TLabel', anchor='w', font=('宋体', 9))
        self.Label11 = Label(self.Frame1, text='起始地址', style='Label11.TLabel')
        self.Label11.place(relx=0.267, rely=0.627, relwidth=0.127, relheight=0.078)

        self.Combo3List = ['起始地址', ]
        self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
        self.Combo3.place(relx=0.416, rely=0.682, relwidth=0.21, relheight=0.042)
        self.Combo3.set(self.Combo3List[0])

        # 烧录次数
        self.style.configure('Label3.TLabel', anchor='w', font=('宋体', 9))
        self.Label3 = Label(self.Frame1, text='烧录次数', style='Label3.TLabel')
        self.Label3.place(relx=0.249, rely=0.737, relwidth=0.119, relheight=0.078)
        # 左上
        self.style.configure('Line19.TSeparator', background='#000000')
        self.Line19 = Separator(self.Frame1, orient='horizontal', style='Line19.TSeparator')
        self.Line19.place(relx=0.018, rely=0.774, relwidth=0.214, relheight=0.0046)
        # 右上
        self.style.configure('Line20.TSeparator', background='#000000')
        self.Line20 = Separator(self.Frame1, orient='horizontal', style='Line20.TSeparator')
        self.Line20.place(relx=0.374, rely=0.774, relwidth=0.267, relheight=0.0046)
        # 左
        self.style.configure('Line12.TSeparator', background='#000000')
        self.Line12 = Separator(self.Frame1, orient='vertical', style='Line12.TSeparator')
        self.Line12.place(relx=0.018, rely=0.774, relwidth=0.0022, relheight=0.184)
        # 右
        self.style.configure('Line14.TSeparator', background='#000000')
        self.Line14 = Separator(self.Frame1, orient='vertical', style='Line14.TSeparator')
        self.Line14.place(relx=0.641, rely=0.774, relwidth=0.0022, relheight=0.184)
        # 下
        self.style.configure('Line13.TSeparator', background='#000000')
        self.Line13 = Separator(self.Frame1, orient='horizontal', style='Line13.TSeparator')
        self.Line13.place(relx=0.018, rely=0.959, relwidth=0.624, relheight=0.0046)
        # 限制烧录次数
        self.Check3Var = StringVar(value='0')
        self.style.configure('Check3.TCheckbutton', font=('宋体', 9))
        self.Check3 = Checkbutton(self.Frame1, text='限制烧录次数', variable=self.Check3Var,
                                  style='Check3.TCheckbutton')
        self.Check3.place(relx=0.053, rely=0.848, relwidth=0.216, relheight=0.078)
        # 次数
        self.Combo4List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.Combo4 = Combobox(self.Frame1, values=self.Combo4List, font=('宋体', 9))
        self.Combo4.place(relx=0.41, rely=0.848, relwidth=0.198, relheight=0.092)
        self.Combo4.set(self.Combo4List[0])

        # 烧录选项
        self.style.configure('Label4.TLabel', anchor='w', font=('宋体', 9))
        self.Label4 = Label(self.Frame1, text='烧录选项', style='Label4.TLabel')
        self.Label4.place(relx=0.766, rely=0.074, relwidth=0.127, relheight=0.078)
        # 左上
        self.style.configure('Line22.TSeparator', background='#000000')
        self.Line22 = Separator(self.Frame1, orient='horizontal', style='Line22.TSeparator')
        self.Line22.place(relx=0.677, rely=0.111, relwidth=0.071, relheight=0.0046)
        # 右上
        self.style.configure('Line23.TSeparator', background='#000000')
        self.Line23 = Separator(self.Frame1, orient='horizontal', style='Line23.TSeparator')
        self.Line23.place(relx=0.891, rely=0.111, relwidth=0.089, relheight=0.0046)
        # 左
        self.style.configure('Line21.TSeparator', background='#000000')
        self.Line21 = Separator(self.Frame1, orient='vertical', style='Line21.TSeparator')
        self.Line21.place(relx=0.677, rely=0.111, relwidth=0.0022, relheight=0.221)
        # 右
        self.style.configure('Line24.TSeparator', background='#000000')
        self.Line24 = Separator(self.Frame1, orient='vertical', style='Line24.TSeparator')
        self.Line24.place(relx=0.98, rely=0.111, relwidth=0.0022, relheight=0.221)
        # 下
        self.style.configure('Line35.TSeparator', background='#000000')
        self.Line35 = Separator(self.Frame1, orient='horizontal', style='Line35.TSeparator')
        self.Line35.place(relx=0.677, rely=0.332, relwidth=0.303, relheight=0.0046)
        # 出厂设置
        self.Check1Var = StringVar(value='0')
        self.style.configure('Check1.TCheckbutton', font=('宋体', 9))
        self.Check1 = Checkbutton(self.Frame1, text='出厂设置', variable=self.Check1Var, style='Check1.TCheckbutton')
        self.Check1.place(relx=0.748, rely=0.147, relwidth=0.18, relheight=0.085)
        # 写入硬件CRC
        self.Check4Var = StringVar(value='0')
        self.style.configure('Check4.TCheckbutton', font=('宋体', 9))
        self.Check4 = Checkbutton(self.Frame1, text='写入硬件CRC', variable=self.Check4Var, style='Check4.TCheckbutton')
        self.Check4.place(relx=0.748, rely=0.221, relwidth=0.198, relheight=0.10)

        # 脱机烧录选项
        self.style.configure('Label12.TLabel', anchor='w', font=('宋体', 9))
        self.Label12 = Label(self.Frame1, text='脱机烧录选项', style='Label12.TLabel')
        self.Label12.place(relx=0.748, rely=0.369, relwidth=0.18, relheight=0.078)
        # 左上
        self.style.configure('Line36.TSeparator', background='#000000')
        self.Line36 = Separator(self.Frame1, orient='horizontal', style='Line36.TSeparator')
        self.Line36.place(relx=0.677, rely=0.406, relwidth=0.071, relheight=0.0046)
        # 右上
        self.style.configure('Line37.TSeparator', background='#000000')
        self.Line37 = Separator(self.Frame1, orient='horizontal', style='Line37.TSeparator')
        self.Line37.place(relx=0.909, rely=0.406, relwidth=0.071, relheight=0.0046)
        # 左
        self.style.configure('Line42.TSeparator', background='#000000')
        self.Line42 = Separator(self.Frame1, orient='vertical', style='Line42.TSeparator')
        self.Line42.place(relx=0.677, rely=0.406, relwidth=0.0022, relheight=0.332)
        # 右
        self.style.configure('Line43.TSeparator', background='#000000')
        self.Line43 = Separator(self.Frame1, orient='vertical', style='Line43.TSeparator')
        self.Line43.place(relx=0.98, rely=0.406, relwidth=0.0022, relheight=0.332)
        # 下
        self.style.configure('Line38.TSeparator', background='#000000')
        self.Line38 = Separator(self.Frame1, orient='horizontal', style='Line38.TSeparator')
        self.Line38.place(relx=0.677, rely=0.737, relwidth=0.303, relheight=0.0046)
        # 自动烧录
        self.Check5Var = StringVar(value='0')
        self.style.configure('Check5.TCheckbutton', font=('宋体', 9))
        self.Check5 = Checkbutton(self.Frame1, text='自动烧录', variable=self.Check5Var, style='Check5.TCheckbutton')
        self.Check5.place(relx=0.748, rely=0.450, relwidth=0.163, relheight=0.082)
        # 单通道
        self.Check6Var = StringVar(value='0')
        self.style.configure('Check6.TCheckbutton', font=('宋体', 9))
        self.Check6 = Checkbutton(self.Frame1, text='单通道', variable=self.Check6Var, style='Check6.TCheckbutton')
        self.Check6.place(relx=0.748, rely=0.540, relwidth=0.145, relheight=0.082)
        # CRC CheckSum
        self.Check7Var = StringVar(value='0')
        self.style.configure('Check7.TCheckbutton', font=('宋体', 9))
        self.Check7 = Checkbutton(self.Frame1, text='CRC CheckSum', variable=self.Check7Var,
                                  style='Check7.TCheckbutton')
        self.Check7.place(relx=0.748, rely=0.630, relwidth=0.216, relheight=0.082)
        # 加密选项
        self.style.configure('Label13.TLabel', anchor='w', font=('宋体', 9))
        self.Label13 = Label(self.Frame1, text='加密选项', style='Label13.TLabel')
        self.Label13.place(relx=0.766, rely=0.737, relwidth=0.127, relheight=0.078)
        # 左上
        self.style.configure('Line39.TSeparator', background='#000000')
        self.Line39 = Separator(self.Frame1, orient='horizontal', style='Line39.TSeparator')
        self.Line39.place(relx=0.677, rely=0.774, relwidth=0.089, relheight=0.0046)
        # 右上
        self.style.configure('Line40.TSeparator', background='#000000')
        self.Line40 = Separator(self.Frame1, orient='horizontal', style='Line40.TSeparator')
        self.Line40.place(relx=0.873, rely=0.774, relwidth=0.107, relheight=0.0046)
        # 左
        self.style.configure('Line44.TSeparator', background='#000000')
        self.Line44 = Separator(self.Frame1, orient='vertical', style='Line44.TSeparator')
        self.Line44.place(relx=0.677, rely=0.774, relwidth=0.0022, relheight=0.184)
        # 右
        self.style.configure('Line45.TSeparator', background='#000000')
        self.Line45 = Separator(self.Frame1, orient='vertical', style='Line45.TSeparator')
        self.Line45.place(relx=0.98, rely=0.774, relwidth=0.0022, relheight=0.184)
        # 下
        self.style.configure('Line41.TSeparator', background='#000000')
        self.Line41 = Separator(self.Frame1, orient='horizontal', style='Line41.TSeparator')
        self.Line41.place(relx=0.677, rely=0.959, relwidth=0.303, relheight=0.0046)
        # 加密
        self.Check8Var = StringVar(value='0')
        self.style.configure('Check8.TCheckbutton', font=('宋体', 9))
        self.Check8 = Checkbutton(self.Frame1, text='加密', variable=self.Check8Var, style='Check8.TCheckbutton')
        self.Check8.place(relx=0.748, rely=0.848, relwidth=0.163, relheight=0.078)

        # *************************************************************
        # *************************************************************
        # *************************************************************
        # 最下方
        # 自动烧录
        self.style.configure('Label14.TLabel', anchor='w', font=('宋体', 9))
        self.Label14 = Label(self.top, text='自动烧录', style='Label14.TLabel')
        self.Label14.place(relx=0.242, rely=0.865, relwidth=0.141, relheight=0.035)
        # 左上
        self.style.configure('Line49.TSeparator', background='#000000')
        self.Line49 = Separator(self.top, orient='horizontal', style='Line49.TSeparator')
        self.Line49.place(relx=0.035, rely=0.881, relwidth=0.19, relheight=0.0021)
        # 右上
        self.style.configure('Line50.TSeparator', background='#000000')
        self.Line50 = Separator(self.top, orient='horizontal', style='Line50.TSeparator')
        self.Line50.place(relx=0.364, rely=0.881, relwidth=0.277, relheight=0.0021)
        # 左
        self.style.configure('Line46.TSeparator', background='#000000')
        self.Line46 = Separator(self.top, orient='vertical', style='Line46.TSeparator')
        self.Line46.place(relx=0.035, rely=0.881, relwidth=0.0022, relheight=0.1)
        # 右
        self.style.configure('Line48.TSeparator', background='#000000')
        self.Line48 = Separator(self.top, orient='vertical', style='Line48.TSeparator')
        self.Line48.place(relx=0.641, rely=0.881, relwidth=0.0022, relheight=0.1)
        # 下
        self.style.configure('Line47.TSeparator', background='#000000')
        self.Line47 = Separator(self.top, orient='horizontal', style='Line47.TSeparator')
        self.Line47.place(relx=0.035, rely=0.981, relwidth=0.606, relheight=0.0021)
        # 编程
        self.Check9Var = StringVar(value='0')
        self.style.configure('Check9.TCheckbutton', font=('宋体', 9))
        self.Check9 = Checkbutton(self.top, text='编程', variable=self.Check9Var, style='Check9.TCheckbutton')
        self.Check9.place(relx=0.069, rely=0.938, relwidth=0.123, relheight=0.035)
        # 查空
        self.Check10Var = StringVar(value='0')
        self.style.configure('Check10.TCheckbutton', font=('宋体', 9))
        self.Check10 = Checkbutton(self.top, text='查空', variable=self.Check10Var, style='Check10.TCheckbutton')
        self.Check10.place(relx=0.069, rely=0.898, relwidth=0.141, relheight=0.035)
        # 擦除
        self.Check11Var = StringVar(value='0')
        self.style.configure('Check11.TCheckbutton', font=('宋体', 9))
        self.Check11 = Checkbutton(self.top, text='擦除', variable=self.Check11Var, style='Check11.TCheckbutton')
        self.Check11.place(relx=0.208, rely=0.898, relwidth=0.141, relheight=0.035)
        # 校验
        self.Check12Var = StringVar(value='0')
        self.style.configure('Check12.TCheckbutton', font=('宋体', 9))
        self.Check12 = Checkbutton(self.top, text='校验', variable=self.Check12Var, style='Check12.TCheckbutton')
        self.Check12.place(relx=0.208, rely=0.938, relwidth=0.141, relheight=0.035)
        # 自动烧录按钮
        self.style.configure('Command5.TButton', font=('宋体', 9))
        self.Command5 = Button(self.top, text='自动烧录', command=open_progress_window, style='Command5.TButton')
        self.Command5.place(relx=0.381, rely=0.898, relwidth=0.227, relheight=0.069)
        # 代码校验和
        self.style.configure('Label15.TLabel', anchor='w', font=('宋体', 9))
        self.Label15 = Label(self.top, text='代码校验和', style='Label15.TLabel')
        self.Label15.place(relx=0.749, rely=0.855, relwidth=0.141, relheight=0.052)
        # 左上
        self.style.configure('Line51.TSeparator', background='#000000')
        self.Line51 = Separator(self.top, orient='horizontal', style='Line51.TSeparator')
        self.Line51.place(relx=0.885, rely=0.881, relwidth=0.087, relheight=0.0021)
        # 右上
        self.style.configure('Line55.TSeparator', background='#000000')
        self.Line55 = Separator(self.top, orient='horizontal', style='Line55.TSeparator')
        self.Line55.place(relx=0.675, rely=0.881, relwidth=0.069, relheight=0.0021)
        # 左
        self.style.configure('Line53.TSeparator', background='#000000')
        self.Line53 = Separator(self.top, orient='vertical', style='Line53.TSeparator')
        self.Line53.place(relx=0.675, rely=0.881, relwidth=0.0022, relheight=0.1)
        # 右
        self.style.configure('Line54.TSeparator', background='#000000')
        self.Line54 = Separator(self.top, orient='vertical', style='Line54.TSeparator')
        self.Line54.place(relx=0.97, rely=0.881, relwidth=0.0022, relheight=0.1)
        # 下
        self.style.configure('Line52.TSeparator', background='#000000')
        self.Line52 = Separator(self.top, orient='horizontal', style='Line52.TSeparator')
        self.Line52.place(relx=0.675, rely=0.981, relwidth=0.294, relheight=0.0021)
        # 内容
        self.style.configure('Label16.TLabel', anchor='w', font=('宋体', 7))
        self.Label16 = Label(self.top, text='Option:0×005b-1e5f\nCodeSUM 0×0230\nCodeCRC 0×00133200\nEEPROM 0×00344340',
                             style='Label16.TLabel')
        self.Label16.place(relx=0.685, rely=0.898, relwidth=0.279, relheight=0.080)

        self.Check2Var = StringVar(value='0')
        self.style.configure('Check2.TCheckbutton', font=('宋体', 9))
        self.Check2 = Checkbutton(self.Frame1, text='Check2', variable=self.Check2Var, style='Check2.TCheckbutton')
        self.Check2.place(relx=0.036, rely=0.147, relwidth=0.038, relheight=0.078)

class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

class ProgressWindow(tkinter.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("烧录中")

        self.progress_var = tkinter.DoubleVar()
        self.progress_bar = tkinter.ttk.Progressbar(self, length=400, mode='determinate', variable=self.progress_var)
        self.progress_bar.pack(pady=20)

        self.current_progress = 0
        self.update_progress()

    def update_progress(self):
        self.current_progress += 10  # 每次更新增加10%
        self.progress_var.set(self.current_progress)

        if self.current_progress >= 100:
            self.destroy()  # 进度达到100%时关闭窗口
        else:
            # 在100毫秒后再次调用update_progress，创建循环更新效果
            self.after(700, self.update_progress)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass



# import tkinter.messagebox
# from tkinter import *
# from tkinter.ttk import *
# from PIL import Image, ImageTk
#
#
# class Application_ui(Frame):
#     # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         # self.Command1_Cmd = None
#         self.master.title('HX1 HXIIA2 V1.0')
#         self.master.geometry('462x481')
#         self.createWidgets()
#
#
#     def click_action(self):
#         tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')
#
#
#     def createWidgets(self):
#         self.top = self.winfo_toplevel()
#         self.style = Style()
#
#         menuBar = Menu(self.top)
#
#         filemenu = Menu(menuBar, tearoff=False)
#         filemenu.add_command(label='载入')
#         filemenu.add_command(label='保存')
#         filemenu.add_command(label='另存为')
#         filemenu.add_separator()
#         filemenu.add_command(label='对比')
#         filemenu.add_command(label='下载')
#         filemenu.add_command(label='退出')
#         menuBar.add_cascade(label='文件', menu=filemenu)
#
#         operation_menu = Menu(menuBar, tearoff=False)
#         operation_menu.add_command(label='查空')
#         operation_menu.add_command(label='擦除')
#         operation_menu.add_command(label='校验')
#         operation_menu.add_command(label='编程')
#         operation_menu.add_command(label='自动')
#         menuBar.add_cascade(label='操作', menu=operation_menu)
#
#         update_menu = Menu(menuBar, tearoff=False)
#         update_menu.add_command(label='更新MCU库')
#         update_menu.add_command(label='升级固件')
#         update_menu.add_command(label='自动升级检测')
#         menuBar.add_cascade(label='升级', menu=update_menu)
#
#         language_menu = Menu(menuBar, tearoff=False)
#         language_menu.add_command(label='简体中文')
#         language_menu.add_command(label='English')
#         language_menu.add_command(label='蘩体中文')
#         menuBar.add_cascade(label='语言', menu=language_menu)
#
#         help_menu = Menu(menuBar, tearoff=False)
#         help_menu.add_command(label='帮助（CHM）')
#         help_menu.add_command(label='关于')
#         menuBar.add_cascade(label='帮助', menu=help_menu)
#
#         CRC_menu = Menu(menuBar, tearoff=False)
#         CRC_menu.add_command(label='CRC读取')
#         menuBar.add_cascade(label='CRC', menu=CRC_menu)
#
#         self.top.config(menu=menuBar)
#
#
#         img = Image.open('./pic/open.png').resize((30, 45))
#         global photo
#         photo = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.010, rely=0.067, relwidth=0.09, relheight=0.119)
#
#         img = Image.open('./pic/save.png').resize((30, 45))
#         global photo1
#         photo1 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo1, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.105, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#
#         img = Image.open('./pic/download.png').resize((30, 45))
#         global photo2
#         photo2 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo2, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.20, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#         img = Image.open('./pic/diff.png').resize((30, 45))
#         global photo3
#         photo3 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo3, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.295, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#         img = Image.open('./pic/code.png').resize((30, 45))
#         global photo4
#         photo4 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo4, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.390, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#
#         img = Image.open('./pic/checkout.png').resize((30, 45))
#         global photo5
#         photo5 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo5, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.485, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#
#         img = Image.open('./pic/auto.png').resize((30, 45))
#         global photo6
#         photo6 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo6, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.580, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#
#         img = Image.open('./pic/erase.png').resize((30, 45))
#         global photo7
#         photo7 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo7, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.675, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#         img = Image.open('./pic/check.png').resize((30, 45))
#         global photo8
#         photo8 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo8, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.770, rely=0.067, relwidth=0.09, relheight=0.119)
#
#
#
#         img = Image.open('./pic/help.png').resize((30, 45))
#         global photo9
#         photo9 = ImageTk.PhotoImage(img)
#         self.style.configure('Command6.TButton', font=('宋体', 9))
#         self.Command6 = Button(self.top, text='', image=photo9, compound=LEFT,
#                                command=self.click_action, style='Command6.TButton')
#         self.Command6.place(relx=0.865, rely=0.067, relwidth=0.09, relheight=0.119)
#
#         # 芯片选择
#         self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
#         self.Label1 = Label(self.top, text='芯片选择', style='Label1.TLabel')
#         self.Label1.place(relx=0.10, rely=0.2, relwidth=0.116, relheight=0.035)
#         # 下拉框
#         self.Combo1List = ['SC92F83A3', 'SC92F83A2', 'SC91F73', 'SC91F72B',
#                            'SC91F729B', 'SC91F731', 'SC91F73A3', 'SC91F73A2']
#         self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体', 9))
#         self.Combo1.place(relx=0.035, rely=0.233, relwidth=0.227, relheight=0.042)
#         self.Combo1.set(self.Combo1List[0])
#         # 上 左
#         self.style.configure('Line4.TSeparator', background='#000000')
#         self.Line4 = Separator(self.top, orient='horizontal', style='Line4.TSeparator')
#         self.Line4.place(relx=0.017, rely=0.216, relwidth=0.087, relheight=0.0021)
#         # 上 右
#         self.style.configure('Line5.TSeparator', background='#000000')
#         self.Line5 = Separator(self.top, orient='horizontal', style='Line5.TSeparator')
#         self.Line5.place(relx=0.208, rely=0.216, relwidth=0.069, relheight=0.0021)
#         # 左
#         self.style.configure('Line2.TSeparator', background='#000000')
#         self.Line2 = Separator(self.top, orient='vertical', style='Line2.TSeparator')
#         self.Line2.place(relx=0.017, rely=0.216, relwidth=0.0022, relheight=0.067)
#         # 右
#         self.style.configure('Line3.TSeparator', background='#000000')
#         self.Line3 = Separator(self.top, orient='vertical', style='Line3.TSeparator')
#         self.Line3.place(relx=0.277, rely=0.216, relwidth=0.0022, relheight=0.067)
#         # 下
#         self.style.configure('Line1.TSeparator', background='#000000')
#         self.Line1 = Separator(self.top, orient='horizontal', style='Line1.TSeparator')
#         self.Line1.place(relx=0.017, rely=0.283, relwidth=0.26, relheight=0.0021)
#
#         # 编程区域
#         self.style.configure('Label1.TLabel', anchor='w', font=('宋体', 9))
#         self.Label1 = Label(self.top, text='编程区域', style='Label1.TLabel')
#         self.Label1.place(relx=0.381, rely=0.2, relwidth=0.116, relheight=0.035)
#         # 下拉框
#         self.Combo2List = ['Code', 'EEPROM', 'Code+EEPROM']
#         self.Combo2 = Combobox(self.top, values=self.Combo2List, font=('宋体', 9))
#         self.Combo2.place(relx=0.329, rely=0.233, relwidth=0.227, relheight=0.042)
#         self.Combo2.set(self.Combo2List[0])
#         # 上 左
#         self.style.configure('Line8.TSeparator', background='#000000')
#         self.Line8 = Separator(self.top, orient='horizontal', style='Line8.TSeparator')
#         self.Line8.place(relx=0.312, rely=0.216, relwidth=0.069, relheight=0.0021)
#         # 上 右
#         self.style.configure('Line10.TSeparator', background='#000000')
#         self.Line10 = Separator(self.top, orient='horizontal', style='Line10.TSeparator')
#         self.Line10.place(relx=0.485, rely=0.216, relwidth=0.087, relheight=0.0021)
#         # 左
#         self.style.configure('Line7.TSeparator', background='#000000')
#         self.Line7 = Separator(self.top, orient='vertical', style='Line7.TSeparator')
#         self.Line7.place(relx=0.312, rely=0.216, relwidth=0.0022, relheight=0.067)
#         # 右
#         self.style.configure('Line9.TSeparator', background='#000000')
#         self.Line9 = Separator(self.top, orient='vertical', style='Line9.TSeparator')
#         self.Line9.place(relx=0.571, rely=0.216, relwidth=0.0022, relheight=0.067)
#         # 下
#         self.style.configure('Line6.TSeparator', background='#000000')
#         self.Line6 = Separator(self.top, orient='horizontal', style='Line6.TSeparator')
#         self.Line6.place(relx=0.312, rely=0.283, relwidth=0.26, relheight=0.0021)
#
#         # 保存项目
#         self.style.configure('Command2.TButton', font=('宋体', 9))
#         self.Command2 = Button(self.top, text='保存项目', command=self.click_action, style='Command2.TButton')
#         self.Command2.place(relx=0.606, rely=0.2, relwidth=0.193, relheight=0.052)
#         # 载入项目
#         self.style.configure('Command2.TButton', font=('宋体', 9))
#         self.Command2 = Button(self.top, text='载入项目', command=self.click_action, style='Command2.TButton')
#         self.Command2.place(relx=0.606, rely=0.249, relwidth=0.193, relheight=0.052)
#         # 当前：常规烧录
#         self.style.configure('Command3.TButton', font=('宋体', 9))
#         self.Command3 = Button(self.top, text='  当前：\n常规烧录', command=self.click_action, style='Command3.TButton')
#         self.Command3.place(relx=0.814, rely=0.2, relwidth=0.158, relheight=0.102)
#
#         # 设置
#         self.style.configure('Command4.TButton', font=('宋体', 9))
#         self.Command4 = Button(self.top, text='设置', command=self.click_action, style='Command4.TButton')
#         self.Command4.place(relx=0.035, rely=0.333, relwidth=0.21, relheight=0.069)
#         # Option
#         self.style.configure('Command4.TButton', font=('宋体', 9))
#         self.Command4 = Button(self.top, text='Option', command=self.click_action, style='Command4.TButton')
#         self.Command4.place(relx=0.26, rely=0.333, relwidth=0.21, relheight=0.069)
#         # 代码
#         self.style.configure('Command4.TButton', font=('宋体', 9))
#         self.Command4 = Button(self.top, text='代码', command=self.click_action, style='Command4.TButton')
#         self.Command4.place(relx=0.485, rely=0.333, relwidth=0.21, relheight=0.069)
#         # EEPROM
#         self.style.configure('Command4.TButton', font=('宋体', 9))
#         self.Command4 = Button(self.top, text='EEPROM', command=self.click_action, style='Command4.TButton')
#         self.Command4.place(relx=0.71, rely=0.333, relwidth=0.21, relheight=0.069)
#
#         # ******************************************************************************
#         # ******************************************************************************
#         # ******************************************************************************
#         # ******************************************************************************
#         # 中间的界面
#         self.style.configure('Frame1.TLabelframe', font=('宋体', 9))
#         self.Frame1 = LabelFrame(self.top, text='', style='Frame1.TLabelframe')
#         self.Frame1.place(relx=0.017, rely=0.40, relwidth=0.972, relheight=0.451)
#         # 序列号选项
#         self.style.configure('Label2.TLabel', anchor='w', font=('宋体', 9))
#         self.Label2 = Label(self.Frame1, text='序列号选项', style='Label2.TLabel')
#         self.Label2.place(relx=0.225, rely=0.040, relwidth=0.145, relheight=0.078)
#         # 左上
#         self.style.configure('Line15.TSeparator', background='#000000')
#         self.Line15 = Separator(self.Frame1, orient='horizontal', style='Line15.TSeparator')
#         self.Line15.place(relx=0.018, rely=0.111, relwidth=0.196, relheight=0.0046)
#         # 右上
#         self.style.configure('Line18.TSeparator', background='#000000')
#         self.Line18 = Separator(self.Frame1, orient='horizontal', style='Line18.TSeparator')
#         self.Line18.place(relx=0.374, rely=0.111, relwidth=0.267, relheight=0.0046)
#         # 左
#         self.style.configure('Line11.TSeparator', background='#000000')
#         self.Line11 = Separator(self.Frame1, orient='vertical', style='Line11.TSeparator')
#         self.Line11.place(relx=0.018, rely=0.111, relwidth=0.0022, relheight=0.627)
#         # 右
#         self.style.configure('Line17.TSeparator', background='#000000')
#         self.Line17 = Separator(self.Frame1, orient='vertical', style='Line17.TSeparator')
#         self.Line17.place(relx=0.641, rely=0.111, relwidth=0.0022, relheight=0.627)
#         # 下
#         self.style.configure('Line16.TSeparator', background='#000000')
#         self.Line16 = Separator(self.Frame1, orient='horizontal', style='Line16.TSeparator')
#         self.Line16.place(relx=0.018, rely=0.737, relwidth=0.624, relheight=0.0046)
#
#         # 使用序列号
#         self.style.configure('Label5.TLabel', anchor='w', font=('宋体', 9))
#         self.Label5 = Label(self.Frame1, text='使用序列号', style='Label5.TLabel')
#         self.Label5.place(relx=0.089, rely=0.147, relwidth=0.163, relheight=0.078)
#         # 进制
#         self.style.configure('Label6.TLabel', anchor='w', font=('宋体', 9))
#         self.Label6 = Label(self.Frame1, text='进制', style='Label6.TLabel')
#         self.Label6.place(relx=0.107, rely=0.221, relwidth=0.109, relheight=0.115)
#         # 左上
#         self.style.configure('Line28.TSeparator', background='#000000')
#         self.Line28 = Separator(self.Frame1, orient='horizontal', style='Line28.TSeparator')
#         self.Line28.place(relx=0.036, rely=0.258, relwidth=0.071, relheight=0.0046)
#         # 右上
#         self.style.configure('Line29.TSeparator', background='#000000')
#         self.Line29 = Separator(self.Frame1, orient='horizontal', style='Line29.TSeparator')
#         self.Line29.place(relx=0.16, rely=0.258, relwidth=0.071, relheight=0.0046)
#         # 左
#         self.style.configure('Line25.TSeparator', background='#000000')
#         self.Line25 = Separator(self.Frame1, orient='vertical', style='Line25.TSeparator')
#         self.Line25.place(relx=0.036, rely=0.258, relwidth=0.0022, relheight=0.184)
#         # 右
#         self.style.configure('Line27.TSeparator', background='#000000')
#         self.Line27 = Separator(self.Frame1, orient='vertical', style='Line27.TSeparator')
#         self.Line27.place(relx=0.232, rely=0.258, relwidth=0.0022, relheight=0.184)
#         # 下
#         self.style.configure('Line26.TSeparator', background='#000000')
#         self.Line26 = Separator(self.Frame1, orient='horizontal', style='Line26.TSeparator')
#         self.Line26.place(relx=0.036, rely=0.442, relwidth=0.196, relheight=0.0046)
#         # 10
#         self.style.configure('Option1.TRadiobutton', font=('宋体', 9))
#         self.Option1 = Radiobutton(self.Frame1, text='10', value=1, style='Option1.TRadiobutton')
#         self.Option1.place(relx=0.065, rely=0.300, relwidth=0.110, relheight=0.065)
#         # 16
#         self.style.configure('Option2.TRadiobutton', font=('宋体', 9))
#         self.Option2 = Radiobutton(self.Frame1, text='16', value=0, style='Option2.TRadiobutton')
#         self.Option2.place(relx=0.065, rely=0.365, relwidth=0.110, relheight=0.067)
#
#
#
#         # 计数方式
#         self.style.configure('Label7.TLabel', anchor='w', font=('宋体', 9))
#         self.Label7 = Label(self.Frame1, text='计数方式', style='Label7.TLabel')
#         self.Label7.place(relx=0.089, rely=0.479, relwidth=0.119, relheight=0.078)
#         # 左上
#         self.style.configure('Line33.TSeparator', background='#000000')
#         self.Line33 = Separator(self.Frame1, orient='horizontal', style='Line33.TSeparator')
#         self.Line33.place(relx=0.036, rely=0.516, relwidth=0.053, relheight=0.0046)
#         # 右上
#         self.style.configure('Line34.TSeparator', background='#000000')
#         self.Line34 = Separator(self.Frame1, orient='horizontal', style='Line34.TSeparator')
#         self.Line34.place(relx=0.196, rely=0.516, relwidth=0.036, relheight=0.0046)
#         # 左
#         self.style.configure('Line30.TSeparator', background='#000000')
#         self.Line30 = Separator(self.Frame1, orient='vertical', style='Line30.TSeparator')
#         self.Line30.place(relx=0.036, rely=0.516, relwidth=0.0022, relheight=0.184)
#         # 右
#         self.style.configure('Line32.TSeparator', background='#000000')
#         self.Line32 = Separator(self.Frame1, orient='vertical', style='Line32.TSeparator')
#         self.Line32.place(relx=0.232, rely=0.514, relwidth=0.0022, relheight=0.184)
#         # 下
#         self.style.configure('Line31.TSeparator', background='#000000')
#         self.Line31 = Separator(self.Frame1, orient='horizontal', style='Line31.TSeparator')
#         self.Line31.place(relx=0.036, rely=0.7, relwidth=0.196, relheight=0.0046)
#         # 递增
#         self.style.configure('Option3.TRadiobutton', font=('宋体', 9))
#         self.Option3 = Radiobutton(self.Frame1, text='递增', value=0, style='Option3.TRadiobutton')
#         self.Option3.place(relx=0.065, rely=0.553, relwidth=0.127, relheight=0.072)
#         # 递减
#         self.style.configure('Option4.TRadiobutton', font=('宋体', 9))
#         self.Option4 = Radiobutton(self.Frame1, text='递减', value=1, style='Option4.TRadiobutton')
#         self.Option4.place(relx=0.065, rely=0.628, relwidth=0.127, relheight=0.072)
#
#
#
#
#
#         # 长度
#         self.style.configure('Label8.TLabel', anchor='w', font=('宋体', 9))
#         self.Label8 = Label(self.Frame1, text='长度（位）', style='Label8.TLabel')
#         self.Label8.place(relx=0.267, rely=0.221, relwidth=0.145, relheight=0.078)
#
#         self.Combo3List = ['长度(位)', ]
#         self.Combo3 = Combobox(self.Frame1, values=self.Combo3List, font=('宋体', 9))
#         self.Combo3.place(relx=0.41, rely=0.221, relwidth=0.216, relheight=0.092)
#         self.Combo3.set(self.Combo3List[0])
#         # 步进
#         self.style.configure('Label9.TLabel', anchor='w', font=('宋体', 9))
#         self.Label9 = Label(self.Frame1, text='步进', style='Label9.TLabel')
#         self.Label9.place(relx=0.267, rely=0.369, relwidth=0.127, relheight=0.078)
#
#         self.Combo3List = ['步进', ]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
#         self.Combo3.place(relx=0.416, rely=0.582, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#         # 起始值
#         self.style.configure('Label10.TLabel', anchor='w', font=('宋体', 9))
#         self.Label10 = Label(self.Frame1, text='起始值', style='Label10.TLabel')
#         self.Label10.place(relx=0.267, rely=0.516, relwidth=0.127, relheight=0.078)
#
#         self.Combo3List = ['起始值', ]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
#         self.Combo3.place(relx=0.416, rely=0.632, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#         # 起始地址
#         self.style.configure('Label11.TLabel', anchor='w', font=('宋体', 9))
#         self.Label11 = Label(self.Frame1, text='起始地址', style='Label11.TLabel')
#         self.Label11.place(relx=0.267, rely=0.627, relwidth=0.127, relheight=0.078)
#
#         self.Combo3List = ['起始地址', ]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体', 9))
#         self.Combo3.place(relx=0.416, rely=0.682, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#
#         # 烧录次数
#         self.style.configure('Label3.TLabel', anchor='w', font=('宋体', 9))
#         self.Label3 = Label(self.Frame1, text='烧录次数', style='Label3.TLabel')
#         self.Label3.place(relx=0.249, rely=0.737, relwidth=0.119, relheight=0.078)
#         # 左上
#         self.style.configure('Line19.TSeparator', background='#000000')
#         self.Line19 = Separator(self.Frame1, orient='horizontal', style='Line19.TSeparator')
#         self.Line19.place(relx=0.018, rely=0.774, relwidth=0.214, relheight=0.0046)
#         # 右上
#         self.style.configure('Line20.TSeparator', background='#000000')
#         self.Line20 = Separator(self.Frame1, orient='horizontal', style='Line20.TSeparator')
#         self.Line20.place(relx=0.374, rely=0.774, relwidth=0.267, relheight=0.0046)
#         # 左
#         self.style.configure('Line12.TSeparator', background='#000000')
#         self.Line12 = Separator(self.Frame1, orient='vertical', style='Line12.TSeparator')
#         self.Line12.place(relx=0.018, rely=0.774, relwidth=0.0022, relheight=0.184)
#         # 右
#         self.style.configure('Line14.TSeparator', background='#000000')
#         self.Line14 = Separator(self.Frame1, orient='vertical', style='Line14.TSeparator')
#         self.Line14.place(relx=0.641, rely=0.774, relwidth=0.0022, relheight=0.184)
#         # 下
#         self.style.configure('Line13.TSeparator', background='#000000')
#         self.Line13 = Separator(self.Frame1, orient='horizontal', style='Line13.TSeparator')
#         self.Line13.place(relx=0.018, rely=0.959, relwidth=0.624, relheight=0.0046)
#         # 限制烧录次数
#         self.Check3Var = StringVar(value='0')
#         self.style.configure('Check3.TCheckbutton', font=('宋体', 9))
#         self.Check3 = Checkbutton(self.Frame1, text='限制烧录次数', variable=self.Check3Var,
#                                   style='Check3.TCheckbutton')
#         self.Check3.place(relx=0.053, rely=0.848, relwidth=0.216, relheight=0.078)
#         # 次数
#         self.Combo4List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         self.Combo4 = Combobox(self.Frame1, values=self.Combo4List, font=('宋体', 9))
#         self.Combo4.place(relx=0.41, rely=0.848, relwidth=0.198, relheight=0.092)
#         self.Combo4.set(self.Combo4List[0])
#
#         # 烧录选项
#         self.style.configure('Label4.TLabel', anchor='w', font=('宋体', 9))
#         self.Label4 = Label(self.Frame1, text='烧录选项', style='Label4.TLabel')
#         self.Label4.place(relx=0.766, rely=0.074, relwidth=0.127, relheight=0.078)
#         # 左上
#         self.style.configure('Line22.TSeparator', background='#000000')
#         self.Line22 = Separator(self.Frame1, orient='horizontal', style='Line22.TSeparator')
#         self.Line22.place(relx=0.677, rely=0.111, relwidth=0.071, relheight=0.0046)
#         # 右上
#         self.style.configure('Line23.TSeparator', background='#000000')
#         self.Line23 = Separator(self.Frame1, orient='horizontal', style='Line23.TSeparator')
#         self.Line23.place(relx=0.891, rely=0.111, relwidth=0.089, relheight=0.0046)
#         # 左
#         self.style.configure('Line21.TSeparator', background='#000000')
#         self.Line21 = Separator(self.Frame1, orient='vertical', style='Line21.TSeparator')
#         self.Line21.place(relx=0.677, rely=0.111, relwidth=0.0022, relheight=0.221)
#         # 右
#         self.style.configure('Line24.TSeparator', background='#000000')
#         self.Line24 = Separator(self.Frame1, orient='vertical', style='Line24.TSeparator')
#         self.Line24.place(relx=0.98, rely=0.111, relwidth=0.0022, relheight=0.221)
#         # 下
#         self.style.configure('Line35.TSeparator', background='#000000')
#         self.Line35 = Separator(self.Frame1, orient='horizontal', style='Line35.TSeparator')
#         self.Line35.place(relx=0.677, rely=0.332, relwidth=0.303, relheight=0.0046)
#         # 出厂设置
#         self.Check1Var = StringVar(value='0')
#         self.style.configure('Check1.TCheckbutton', font=('宋体', 9))
#         self.Check1 = Checkbutton(self.Frame1, text='出厂设置', variable=self.Check1Var, style='Check1.TCheckbutton')
#         self.Check1.place(relx=0.748, rely=0.147, relwidth=0.18, relheight=0.085)
#         # 写入硬件CRC
#         self.Check4Var = StringVar(value='0')
#         self.style.configure('Check4.TCheckbutton', font=('宋体', 9))
#         self.Check4 = Checkbutton(self.Frame1, text='写入硬件CRC', variable=self.Check4Var, style='Check4.TCheckbutton')
#         self.Check4.place(relx=0.748, rely=0.221, relwidth=0.198, relheight=0.10)
#
#         # 脱机烧录选项
#         self.style.configure('Label12.TLabel', anchor='w', font=('宋体', 9))
#         self.Label12 = Label(self.Frame1, text='脱机烧录选项', style='Label12.TLabel')
#         self.Label12.place(relx=0.748, rely=0.369, relwidth=0.18, relheight=0.078)
#         # 左上
#         self.style.configure('Line36.TSeparator', background='#000000')
#         self.Line36 = Separator(self.Frame1, orient='horizontal', style='Line36.TSeparator')
#         self.Line36.place(relx=0.677, rely=0.406, relwidth=0.071, relheight=0.0046)
#         # 右上
#         self.style.configure('Line37.TSeparator', background='#000000')
#         self.Line37 = Separator(self.Frame1, orient='horizontal', style='Line37.TSeparator')
#         self.Line37.place(relx=0.909, rely=0.406, relwidth=0.071, relheight=0.0046)
#         # 左
#         self.style.configure('Line42.TSeparator', background='#000000')
#         self.Line42 = Separator(self.Frame1, orient='vertical', style='Line42.TSeparator')
#         self.Line42.place(relx=0.677, rely=0.406, relwidth=0.0022, relheight=0.332)
#         # 右
#         self.style.configure('Line43.TSeparator', background='#000000')
#         self.Line43 = Separator(self.Frame1, orient='vertical', style='Line43.TSeparator')
#         self.Line43.place(relx=0.98, rely=0.406, relwidth=0.0022, relheight=0.332)
#         # 下
#         self.style.configure('Line38.TSeparator', background='#000000')
#         self.Line38 = Separator(self.Frame1, orient='horizontal', style='Line38.TSeparator')
#         self.Line38.place(relx=0.677, rely=0.737, relwidth=0.303, relheight=0.0046)
#         # 自动烧录
#         self.Check5Var = StringVar(value='0')
#         self.style.configure('Check5.TCheckbutton', font=('宋体', 9))
#         self.Check5 = Checkbutton(self.Frame1, text='自动烧录', variable=self.Check5Var, style='Check5.TCheckbutton')
#         self.Check5.place(relx=0.748, rely=0.450, relwidth=0.163, relheight=0.082)
#         # 单通道
#         self.Check6Var = StringVar(value='0')
#         self.style.configure('Check6.TCheckbutton', font=('宋体', 9))
#         self.Check6 = Checkbutton(self.Frame1, text='单通道', variable=self.Check6Var, style='Check6.TCheckbutton')
#         self.Check6.place(relx=0.748, rely=0.540, relwidth=0.145, relheight=0.082)
#         # CRC CheckSum
#         self.Check7Var = StringVar(value='0')
#         self.style.configure('Check7.TCheckbutton', font=('宋体', 9))
#         self.Check7 = Checkbutton(self.Frame1, text='CRC CheckSum', variable=self.Check7Var,
#                                   style='Check7.TCheckbutton')
#         self.Check7.place(relx=0.748, rely=0.630, relwidth=0.216, relheight=0.082)
#         # 加密选项
#         self.style.configure('Label13.TLabel', anchor='w', font=('宋体', 9))
#         self.Label13 = Label(self.Frame1, text='加密选项', style='Label13.TLabel')
#         self.Label13.place(relx=0.766, rely=0.737, relwidth=0.127, relheight=0.078)
#         # 左上
#         self.style.configure('Line39.TSeparator', background='#000000')
#         self.Line39 = Separator(self.Frame1, orient='horizontal', style='Line39.TSeparator')
#         self.Line39.place(relx=0.677, rely=0.774, relwidth=0.089, relheight=0.0046)
#         # 右上
#         self.style.configure('Line40.TSeparator', background='#000000')
#         self.Line40 = Separator(self.Frame1, orient='horizontal', style='Line40.TSeparator')
#         self.Line40.place(relx=0.873, rely=0.774, relwidth=0.107, relheight=0.0046)
#         # 左
#         self.style.configure('Line44.TSeparator', background='#000000')
#         self.Line44 = Separator(self.Frame1, orient='vertical', style='Line44.TSeparator')
#         self.Line44.place(relx=0.677, rely=0.774, relwidth=0.0022, relheight=0.184)
#         # 右
#         self.style.configure('Line45.TSeparator', background='#000000')
#         self.Line45 = Separator(self.Frame1, orient='vertical', style='Line45.TSeparator')
#         self.Line45.place(relx=0.98, rely=0.774, relwidth=0.0022, relheight=0.184)
#         # 下
#         self.style.configure('Line41.TSeparator', background='#000000')
#         self.Line41 = Separator(self.Frame1, orient='horizontal', style='Line41.TSeparator')
#         self.Line41.place(relx=0.677, rely=0.959, relwidth=0.303, relheight=0.0046)
#         # 加密
#         self.Check8Var = StringVar(value='0')
#         self.style.configure('Check8.TCheckbutton', font=('宋体', 9))
#         self.Check8 = Checkbutton(self.Frame1, text='加密', variable=self.Check8Var, style='Check8.TCheckbutton')
#         self.Check8.place(relx=0.748, rely=0.848, relwidth=0.163, relheight=0.078)
#
#         # *************************************************************
#         # *************************************************************
#         # *************************************************************
#         # 最下方
#         # 自动烧录
#         self.style.configure('Label14.TLabel', anchor='w', font=('宋体', 9))
#         self.Label14 = Label(self.top, text='自动烧录', style='Label14.TLabel')
#         self.Label14.place(relx=0.242, rely=0.865, relwidth=0.141, relheight=0.035)
#         # 左上
#         self.style.configure('Line49.TSeparator', background='#000000')
#         self.Line49 = Separator(self.top, orient='horizontal', style='Line49.TSeparator')
#         self.Line49.place(relx=0.035, rely=0.881, relwidth=0.19, relheight=0.0021)
#         # 右上
#         self.style.configure('Line50.TSeparator', background='#000000')
#         self.Line50 = Separator(self.top, orient='horizontal', style='Line50.TSeparator')
#         self.Line50.place(relx=0.364, rely=0.881, relwidth=0.277, relheight=0.0021)
#         # 左
#         self.style.configure('Line46.TSeparator', background='#000000')
#         self.Line46 = Separator(self.top, orient='vertical', style='Line46.TSeparator')
#         self.Line46.place(relx=0.035, rely=0.881, relwidth=0.0022, relheight=0.1)
#         # 右
#         self.style.configure('Line48.TSeparator', background='#000000')
#         self.Line48 = Separator(self.top, orient='vertical', style='Line48.TSeparator')
#         self.Line48.place(relx=0.641, rely=0.881, relwidth=0.0022, relheight=0.1)
#         # 下
#         self.style.configure('Line47.TSeparator', background='#000000')
#         self.Line47 = Separator(self.top, orient='horizontal', style='Line47.TSeparator')
#         self.Line47.place(relx=0.035, rely=0.981, relwidth=0.606, relheight=0.0021)
#         # 编程
#         self.Check9Var = StringVar(value='0')
#         self.style.configure('Check9.TCheckbutton', font=('宋体', 9))
#         self.Check9 = Checkbutton(self.top, text='编程', variable=self.Check9Var, style='Check9.TCheckbutton')
#         self.Check9.place(relx=0.069, rely=0.938, relwidth=0.123, relheight=0.035)
#         # 查空
#         self.Check10Var = StringVar(value='0')
#         self.style.configure('Check10.TCheckbutton', font=('宋体', 9))
#         self.Check10 = Checkbutton(self.top, text='查空', variable=self.Check10Var, style='Check10.TCheckbutton')
#         self.Check10.place(relx=0.069, rely=0.898, relwidth=0.141, relheight=0.035)
#         # 擦除
#         self.Check11Var = StringVar(value='0')
#         self.style.configure('Check11.TCheckbutton', font=('宋体', 9))
#         self.Check11 = Checkbutton(self.top, text='擦除', variable=self.Check11Var, style='Check11.TCheckbutton')
#         self.Check11.place(relx=0.208, rely=0.898, relwidth=0.141, relheight=0.035)
#         # 校验
#         self.Check12Var = StringVar(value='0')
#         self.style.configure('Check12.TCheckbutton', font=('宋体', 9))
#         self.Check12 = Checkbutton(self.top, text='校验', variable=self.Check12Var, style='Check12.TCheckbutton')
#         self.Check12.place(relx=0.208, rely=0.938, relwidth=0.141, relheight=0.035)
#         # 自动烧录按钮
#         self.style.configure('Command5.TButton', font=('宋体', 9))
#         self.Command5 = Button(self.top, text='自动烧录', command=self.click_action, style='Command5.TButton')
#         self.Command5.place(relx=0.381, rely=0.898, relwidth=0.227, relheight=0.069)
#         # 代码校验和
#         self.style.configure('Label15.TLabel', anchor='w', font=('宋体', 9))
#         self.Label15 = Label(self.top, text='代码校验和', style='Label15.TLabel')
#         self.Label15.place(relx=0.749, rely=0.855, relwidth=0.141, relheight=0.052)
#         # 左上
#         self.style.configure('Line51.TSeparator', background='#000000')
#         self.Line51 = Separator(self.top, orient='horizontal', style='Line51.TSeparator')
#         self.Line51.place(relx=0.885, rely=0.881, relwidth=0.087, relheight=0.0021)
#         # 右上
#         self.style.configure('Line55.TSeparator', background='#000000')
#         self.Line55 = Separator(self.top, orient='horizontal', style='Line55.TSeparator')
#         self.Line55.place(relx=0.675, rely=0.881, relwidth=0.069, relheight=0.0021)
#         # 左
#         self.style.configure('Line53.TSeparator', background='#000000')
#         self.Line53 = Separator(self.top, orient='vertical', style='Line53.TSeparator')
#         self.Line53.place(relx=0.675, rely=0.881, relwidth=0.0022, relheight=0.1)
#         # 右
#         self.style.configure('Line54.TSeparator', background='#000000')
#         self.Line54 = Separator(self.top, orient='vertical', style='Line54.TSeparator')
#         self.Line54.place(relx=0.97, rely=0.881, relwidth=0.0022, relheight=0.1)
#         # 下
#         self.style.configure('Line52.TSeparator', background='#000000')
#         self.Line52 = Separator(self.top, orient='horizontal', style='Line52.TSeparator')
#         self.Line52.place(relx=0.675, rely=0.981, relwidth=0.294, relheight=0.0021)
#         # 内容
#         self.style.configure('Label16.TLabel', anchor='w', font=('宋体', 7))
#         self.Label16 = Label(self.top, text='Option:0×005b-1e5f\nCodeSUM 0×0230\nCodeCRC 0×00133200\nEEPROM 0×00344340',
#                              style='Label16.TLabel')
#         self.Label16.place(relx=0.685, rely=0.898, relwidth=0.279, relheight=0.080)
#
#
#
#         self.Check2Var = StringVar(value='0')
#         self.style.configure('Check2.TCheckbutton', font=('宋体', 9))
#         self.Check2 = Checkbutton(self.Frame1, text='Check2', variable=self.Check2Var, style='Check2.TCheckbutton')
#         self.Check2.place(relx=0.036, rely=0.147, relwidth=0.038, relheight=0.078)
#
#         # self.Picture2 = Canvas(self.top)
#         # self.Picture2.place(relx=0.883, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.779, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.675, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.571, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.468, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.364, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.26, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.173, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0.087, rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.Picture1 = Canvas(self.top)
#         # self.Picture1.place(relx=0., rely=0.05, relwidth=0.089, relheight=0.135)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='CRC', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0.485, rely=0., relwidth=0.123, relheight=0.052)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='帮助[H]', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0.606, rely=0., relwidth=0.123, relheight=0.052)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='语言[L]', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0.364, rely=0., relwidth=0.123, relheight=0.052)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='升级[U]', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0.242, rely=0., relwidth=0.123, relheight=0.052)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='操作[O]', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0.121, rely=0., relwidth=0.123, relheight=0.052)
#         #
#         # self.style.configure('Command1.TButton', background='#FFFFE1', font=('宋体', 9))
#         # self.Command1 = Button(self.top, text='文件[F]', command=self.Command1_Cmd, style='Command1.TButton')
#         # self.Command1.place(relx=0., rely=0., relwidth=0.123, relheight=0.052)
#
#
# class Application(Application_ui):
#     # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
#     def __init__(self, master=None):
#         Application_ui.__init__(self, master)
#
#     def Command4_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command3_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command2_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command2_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         tkinter.messagebox.showinfo('消息', '鼠标事件点击成功')
#
#
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#     def Command5_Cmd(self, event=None):
#         # TODO, Please finish the function here!
#         pass
#
#
# if __name__ == "__main__":
#     top = Tk()
#     Application(top).mainloop()
#     try:
#         top.destroy()
#     except:
#         pass
