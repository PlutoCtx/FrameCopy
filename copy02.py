# @Version: python3.10
# @Time: 2024/1/29 22:00
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: copy02.py
# @Software: PyCharm
# @User: chent
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#
# import os, sys
# from tkinter import *
# from tkinter.ttk import *
# from tkinter.messagebox import *
#
#
#
# class Application_ui(Frame):
#     #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master.title('Form1')
#         self.master.geometry('462x481')
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.top = self.winfo_toplevel()
#
#         self.style = Style()
#
#         self.Combo3List = ['Add items in design or code!',]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体',9))
#         self.Combo3.place(relx=0.416, rely=0.682, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#
#         self.Combo3List = ['Add items in design or code!',]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体',9))
#         self.Combo3.place(relx=0.416, rely=0.632, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#
#         self.Combo3List = ['Add items in design or code!',]
#         self.Combo3 = Combobox(self.top, values=self.Combo3List, font=('宋体',9))
#         self.Combo3.place(relx=0.416, rely=0.582, relwidth=0.21, relheight=0.042)
#         self.Combo3.set(self.Combo3List[0])
#
#         self.style.configure('Option2.TRadiobutton',font=('宋体',9))
#         self.Option2 = Radiobutton(self.top, text='递减', value=0, style='Option2.TRadiobutton')
#         self.Option2.place(relx=0.087, rely=0.699, relwidth=0.123, relheight=0.025)
#
#         self.style.configure('Option1.TRadiobutton',font=('宋体',9))
#         self.Option1 = Radiobutton(self.top, text='16', value=0, style='Option1.TRadiobutton')
#         self.Option1.place(relx=0.087, rely=0.582, relwidth=0.089, relheight=0.025)
#
#         self.style.configure('Frame1.TLabelframe',font=('宋体',9))
#         self.Frame1 = LabelFrame(self.top, text='Frame1', style='Frame1.TLabelframe')
#         self.Frame1.place(relx=0.017, rely=0.416, relwidth=0.972, relheight=0.451)
#
#
#
#
#
#
#
#         self.Combo2List = ['Add items in design or code!',]
#         self.Combo2 = Combobox(self.top, values=self.Combo2List, font=('宋体',9))
#         self.Combo2.place(relx=0.329, rely=0.233, relwidth=0.227, relheight=0.042)
#         self.Combo2.set(self.Combo2List[0])
#
#         self.Combo1List = ['Add items in design or code!',]
#         self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
#         self.Combo1.place(relx=0.035, rely=0.233, relwidth=0.227, relheight=0.042)
#         self.Combo1.set(self.Combo1List[0])
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='CRC', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0.485, rely=0., relwidth=0.123, relheight=0.052)
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='帮助[H]', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0.606, rely=0., relwidth=0.123, relheight=0.052)
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='语言[L]', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0.364, rely=0., relwidth=0.123, relheight=0.052)
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='升级[U]', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0.242, rely=0., relwidth=0.123, relheight=0.052)
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='操作[O]', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0.121, rely=0., relwidth=0.123, relheight=0.052)
#
#         self.style.configure('Command1.TButton',background='#FFFFE1', font=('宋体',9))
#         self.Command1 = Button(self.top, text='文件[F]', command=self.Command1_Cmd, style='Command1.TButton')
#         self.Command1.place(relx=0., rely=0., relwidth=0.123, relheight=0.052)
#
#
#         self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
#         self.Label1 = Label(self.top, text='编程区域', style='Label1.TLabel')
#         self.Label1.place(relx=0.381, rely=0.2, relwidth=0.106, relheight=0.035)
#
#
#         self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
#         self.Label1 = Label(self.top, text='芯片选择', style='Label1.TLabel')
#         self.Label1.place(relx=0.104, rely=0.2, relwidth=0.106, relheight=0.035)
#
#
#
#         self.Check9Var = StringVar(value='0')
#         self.style.configure('Check9.TCheckbutton',font=('宋体',9))
#         self.Check9 = Checkbutton(self.top, text='编程', variable=self.Check9Var, style='Check9.TCheckbutton')
#         self.Check9.place(relx=0.069, rely=0.948, relwidth=0.123, relheight=0.025)
#
#         self.Check10Var = StringVar(value='0')
#         self.style.configure('Check10.TCheckbutton',font=('宋体',9))
#         self.Check10 = Checkbutton(self.top, text='查空', variable=self.Check10Var, style='Check10.TCheckbutton')
#         self.Check10.place(relx=0.069, rely=0.898, relwidth=0.141, relheight=0.035)
#
#         self.Check11Var = StringVar(value='0')
#         self.style.configure('Check11.TCheckbutton',font=('宋体',9))
#         self.Check11 = Checkbutton(self.top, text='擦除', variable=self.Check11Var, style='Check11.TCheckbutton')
#         self.Check11.place(relx=0.208, rely=0.909, relwidth=0.141, relheight=0.025)
#
#         self.Check12Var = StringVar(value='0')
#         self.style.configure('Check12.TCheckbutton',font=('宋体',9))
#         self.Check12 = Checkbutton(self.top, text='校验', variable=self.Check12Var, style='Check12.TCheckbutton')
#         self.Check12.place(relx=0.208, rely=0.948, relwidth=0.141, relheight=0.025)
#
#         self.style.configure('Command5.TButton',font=('宋体',9))
#         self.Command5 = Button(self.top, text='自动烧录', command=self.Command5_Cmd, style='Command5.TButton')
#         self.Command5.place(relx=0.381, rely=0.898, relwidth=0.227, relheight=0.069)
#
#
#         self.style.configure('Label14.TLabel',anchor='w', font=('宋体',9))
#         self.Label14 = Label(self.top, text='自动烧录', style='Label14.TLabel')
#         self.Label14.place(relx=0.242, rely=0.865, relwidth=0.141, relheight=0.035)
#
#
#         self.style.configure('Label15.TLabel',anchor='w', font=('宋体',9))
#         self.Label15 = Label(self.top, text='代码校验和', style='Label15.TLabel')
#         self.Label15.place(relx=0.762, rely=0.865, relwidth=0.141, relheight=0.052)
#
#         self.style.configure('Label16.TLabel',anchor='w', font=('宋体',9))
#         self.Label16 = Label(self.top, text='Option:0×005b-1e5f', style='Label16.TLabel')
#         self.Label16.place(relx=0.693, rely=0.898, relwidth=0.279, relheight=0.085)
#
#
#         self.style.configure('Command6.TButton',font=('宋体',9))
#         self.Command6 = Button(self.top, text='Command6', command=self.Command6_Cmd, style='Command6.TButton')
#         self.Command6.place(relx=0.017, rely=0.067, relwidth=0.955, relheight=0.119)
#
#         self.Combo3List = ['Add items in design or code!',]
#         self.Combo3 = Combobox(self.Frame1, values=self.Combo3List, font=('宋体',9))
#         self.Combo3.place(relx=0.41, rely=0.221, relwidth=0.216, relheight=0.092)
#         self.Combo3.set(self.Combo3List[0])
#
#         self.style.configure('Option2.TRadiobutton',font=('宋体',9))
#         self.Option2 = Radiobutton(self.Frame1, text='递增', value=0, style='Option2.TRadiobutton')
#         self.Option2.place(relx=0.071, rely=0.553, relwidth=0.127, relheight=0.055)
#
#         self.style.configure('Option1.TRadiobutton',font=('宋体',9))
#         self.Option1 = Radiobutton(self.Frame1, text='10', value=0, style='Option1.TRadiobutton')
#         self.Option1.place(relx=0.071, rely=0.295, relwidth=0.091, relheight=0.055)
#
#         self.Check2Var = StringVar(value='0')
#         self.style.configure('Check2.TCheckbutton',font=('宋体',9))
#         self.Check2 = Checkbutton(self.Frame1, text='Check2', variable=self.Check2Var, style='Check2.TCheckbutton')
#         self.Check2.place(relx=0.036, rely=0.147, relwidth=0.038, relheight=0.078)
#
#         self.style.configure('Label11.TLabel',anchor='w', font=('宋体',9))
#         self.Label11 = Label(self.Frame1, text='起始地址', style='Label11.TLabel')
#         self.Label11.place(relx=0.267, rely=0.627, relwidth=0.109, relheight=0.078)
#
#         self.style.configure('Label10.TLabel',anchor='w', font=('宋体',9))
#         self.Label10 = Label(self.Frame1, text='起始值', style='Label10.TLabel')
#         self.Label10.place(relx=0.267, rely=0.516, relwidth=0.127, relheight=0.078)
#
#         self.style.configure('Label9.TLabel',anchor='w', font=('宋体',9))
#         self.Label9 = Label(self.Frame1, text='步进', style='Label9.TLabel')
#         self.Label9.place(relx=0.267, rely=0.369, relwidth=0.127, relheight=0.078)
#
#         self.style.configure('Label8.TLabel',anchor='w', font=('宋体',9))
#         self.Label8 = Label(self.Frame1, text='长度（位）', style='Label8.TLabel')
#         self.Label8.place(relx=0.267, rely=0.221, relwidth=0.145, relheight=0.078)
#
#
#         self.style.configure('Label7.TLabel',anchor='w', font=('宋体',9))
#         self.Label7 = Label(self.Frame1, text='计数方式', style='Label7.TLabel')
#         self.Label7.place(relx=0.089, rely=0.479, relwidth=0.109, relheight=0.078)
#
#
#         self.style.configure('Label6.TLabel',anchor='w', font=('宋体',9))
#         self.Label6 = Label(self.Frame1, text='进制', style='Label6.TLabel')
#         self.Label6.place(relx=0.107, rely=0.221, relwidth=0.109, relheight=0.115)
#
#
#         self.style.configure('Label5.TLabel',anchor='w', font=('宋体',9))
#         self.Label5 = Label(self.Frame1, text='使用序列号', style='Label5.TLabel')
#         self.Label5.place(relx=0.089, rely=0.147, relwidth=0.163, relheight=0.078)
#
#
#         self.style.configure('Label4.TLabel',anchor='w', font=('宋体',9))
#         self.Label4 = Label(self.Frame1, text='烧录选项', style='Label4.TLabel')
#         self.Label4.place(relx=0.766, rely=0.074, relwidth=0.127, relheight=0.078)
#
#
#         self.style.configure('Label3.TLabel',anchor='w', font=('宋体',9))
#         self.Label3 = Label(self.Frame1, text='烧录次数', style='Label3.TLabel')
#         self.Label3.place(relx=0.249, rely=0.737, relwidth=0.109, relheight=0.078)
#
#
#         self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
#         self.Label2 = Label(self.Frame1, text='序列号选项', style='Label2.TLabel')
#         self.Label2.place(relx=0.232, rely=0.074, relwidth=0.145, relheight=0.078)
#
#
#         self.Check3Var = StringVar(value='0')
#         self.style.configure('Check3.TCheckbutton',font=('宋体',9))
#         self.Check3 = Checkbutton(self.Frame1, text='限制烧录次数', variable=self.Check3Var, style='Check3.TCheckbutton')
#         self.Check3.place(relx=0.053, rely=0.848, relwidth=0.216, relheight=0.078)
#
#         self.Combo4List = ['Add items in design or code!',]
#         self.Combo4 = Combobox(self.Frame1, values=self.Combo4List, font=('宋体',9))
#         self.Combo4.place(relx=0.41, rely=0.848, relwidth=0.198, relheight=0.092)
#         self.Combo4.set(self.Combo4List[0])
#
#         self.Check1Var = StringVar(value='0')
#         self.style.configure('Check1.TCheckbutton',font=('宋体',9))
#         self.Check1 = Checkbutton(self.Frame1, text='出厂设置', variable=self.Check1Var, style='Check1.TCheckbutton')
#         self.Check1.place(relx=0.748, rely=0.147, relwidth=0.18, relheight=0.078)
#
#         self.Check4Var = StringVar(value='0')
#         self.style.configure('Check4.TCheckbutton',font=('宋体',9))
#         self.Check4 = Checkbutton(self.Frame1, text='写入硬件CRC', variable=self.Check4Var, style='Check4.TCheckbutton')
#         self.Check4.place(relx=0.748, rely=0.221, relwidth=0.198, relheight=0.078)
#
#         self.style.configure('Label12.TLabel',anchor='w', font=('宋体',9))
#         self.Label12 = Label(self.Frame1, text='脱机烧录选项', style='Label12.TLabel')
#         self.Label12.place(relx=0.748, rely=0.369, relwidth=0.18, relheight=0.078)
#
#         self.Check5Var = StringVar(value='0')
#         self.style.configure('Check5.TCheckbutton',font=('宋体',9))
#         self.Check5 = Checkbutton(self.Frame1, text='自动烧录', variable=self.Check5Var, style='Check5.TCheckbutton')
#         self.Check5.place(relx=0.748, rely=0.442, relwidth=0.163, relheight=0.078)
#
#         self.Check6Var = StringVar(value='0')
#         self.style.configure('Check6.TCheckbutton',font=('宋体',9))
#         self.Check6 = Checkbutton(self.Frame1, text='单通道', variable=self.Check6Var, style='Check6.TCheckbutton')
#         self.Check6.place(relx=0.748, rely=0.516, relwidth=0.145, relheight=0.078)
#
#         self.Check7Var = StringVar(value='0')
#         self.style.configure('Check7.TCheckbutton',font=('宋体',9))
#         self.Check7 = Checkbutton(self.Frame1, text='CRC CheckSum', variable=self.Check7Var, style='Check7.TCheckbutton')
#         self.Check7.place(relx=0.748, rely=0.59, relwidth=0.216, relheight=0.055)
#
#         self.style.configure('Label13.TLabel',anchor='w', font=('宋体',9))
#         self.Label13 = Label(self.Frame1, text='加密选项', style='Label13.TLabel')
#         self.Label13.place(relx=0.766, rely=0.737, relwidth=0.127, relheight=0.078)
#
#         self.Check8Var = StringVar(value='0')
#         self.style.configure('Check8.TCheckbutton',font=('宋体',9))
#         self.Check8 = Checkbutton(self.Frame1, text='加密', variable=self.Check8Var, style='Check8.TCheckbutton')
#         self.Check8.place(relx=0.748, rely=0.848, relwidth=0.163, relheight=0.078)
#
#
#
# class Application(Application_ui):
#     #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
#     def __init__(self, master=None):
#         Application_ui.__init__(self, master)
#
#     def Command4_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command4_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command3_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command2_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command2_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command1_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command5_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
#     def Command6_Cmd(self, event=None):
#         #TODO, Please finish the function here!
#         pass
#
# if __name__ == "__main__":
#     top = Tk()
#     Application(top).mainloop()
#     try: top.destroy()
#     except: pass


# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Creating a photoimage object to use image
photo = PhotoImage(file=r"./pic.png")

# 调整图片尺寸适应按钮大小
photoimage = photo.subsample(3, 3)

# 图片在button的左边
Button(root, text='点我 !', image=photoimage,
       compound=LEFT).pack(side=TOP)

mainloop()