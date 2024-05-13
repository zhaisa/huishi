import tkinter as tk
import sqlite3

class DeleteFrame:
    # 初始化界面
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x150')
        self.master.title('删除职工信息')

        # 创建标签和输入框
        tk.Label(self.master, text='职工ID：').place(x=50, y=50)
        self.emp_id_entry = tk.Entry(self.master)
        self.emp_id_entry.place(x=120, y=50)

        # 创建确认和取消按钮
        tk.Button(self.master, text='确认', command=self.delete_employee).place(x=120, y=90)
        tk.Button(self.master, text='取消', command=self.master.destroy).place(x=220, y=90)

    # 删除职工信息
    def delete_employee(self):
        emp_id = self.emp_id_entry.get()

        # 连接数据库
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        # 执行SQL语句
        cursor.execute('DELETE FROM employee WHERE id=?', (emp_id,))

        # 提交事务
        conn.commit()

        # 关闭数据库连接
        cursor.close()
        conn.close()

        # 提示用户删除成功
        tk.messagebox.showinfo(title='提示', message='删除职工信息成功！')

        # 清空输入框
        self.emp_id_entry.delete(0, tk.END)