# @Version: python3.10
# @Time: 2024/2/19 21:35
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: progressbar.py
# @Software: PyCharm
# @User: chent

# import tkinter as tk
# from tkinter import ttk
# from threading import Thread
# import time
#
# class ProgressWindow(tk.Toplevel):
#     def __init__(self, master):
#         super().__init__(master)
#         self.title("进度条")
#
#         # 设置下载初值
#         self.byte = 0
#         # 设置下载最大值
#         self.maxbyte = 10000
#
#         self.progressbarOne = tk.ttk.Progressbar(root)
#         self.progressbarOne.pack(pady=20)
#
#
#         self.progress_var = tk.DoubleVar()
#         self.progress_var.set(0)
#
#         self.progress_bar = ttk.Progressbar(self, length=200, mode='determinate', variable=self.progress_var)
#         self.progress_bar.pack(pady=20)
#
#         # self.update_progress()
#         self.show()
#
#     # def update_progress(self):
#     #     for i in range(101):
#     #         self.progress_var.set(i / 100)
#     #         self.update_idletasks()
#     #         time.sleep(0.1)  # 模拟进度更新
#     #     self.destroy()  # 进度达到100%时自动关闭窗口
#
#     def show(self):
#         # 设置进度条的目前值
#         self.progressbarOne['value'] = 0
#         # 设置进度条的最大值
#         self.progressbarOne['maximum'] = self.maxbyte
#         # 调用loading方法
#         self.loading()
#
#     def loading(self):
#         # 改变变量属性
#         global byte
#         # 每次运行500B
#         byte += 500
#         # 设置指针
#         self.progressbarOne['value'] = byte
#         if byte < self.maxbyte:
#             # 经过100ms后再次调用loading方法
#             self.progressbarOne.after(100, self.loading)
#         self.destroy()
#
# def open_progress_window():
#     progress_window = ProgressWindow(root)
#
#
# def main():
#     global root
#     root = tk.Tk()
#     root.title("主界面")
#     button = tk.Button(root, text="打开进度条", command=open_progress_window)
#     button.pack(pady=20)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()


import tkinter as tk
from tkinter import ttk


class ProgressWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("进度条")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, length=400, mode='determinate', variable=self.progress_var)
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
            self.after(300, self.update_progress)


def open_progress_window():
    progress_window = ProgressWindow(root)


root = tk.Tk()
root.title("主界面")

button = tk.Button(root, text="打开进度条", command=open_progress_window)
button.pack(pady=20)

root.mainloop()