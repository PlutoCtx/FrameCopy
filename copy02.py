# @Version: python3.10
# @Time: 2024/1/29 22:00
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: copy02.py
# @Software: PyCharm
# @User: chent

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