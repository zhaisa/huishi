
import tkinter as tk
import sqlite3
from tkinter import ttk
class QueryFrame:
    # 初始化界面
    def __init__(self, master):
        self.master = master
        self.master.geometry('600x400')
        self.master.title('查询职工信息')

        # 创建标签和输入框
        tk.Label(self.master, text='职工ID：').place(x=50, y=50)
        self.emp_id_entry = tk.Entry(self.master)
        self.emp_id_entry.place(x=120, y=50)

        tk.Label(self.master, text='职工姓名：').place(x=250, y=50)
        self.emp_name_entry = tk.Entry(self.master)
        self.emp_name_entry.place(x=340, y=50)

        # 创建查询按钮
        tk.Button(self.master, text='查询', command=self.query_employee).place(x=500, y=45)

        # 创建表格
        self.tree = ttk.Treeview(self.master, columns=('ID', '姓名', '性别', '年龄', '职位', '工资'), show='headings')
        self.tree.column('ID', width=80)
        self.tree.column('姓名', width=100)
        self.tree.column('性别', width=80)
        self.tree.column('年龄', width=80)
        self.tree.column('职位', width=100)
        self.tree.column('工资', width=80)
        self.tree.heading('ID', text='ID')
        self.tree.heading('姓名', text='姓名')
        self.tree.heading('性别', text='性别')
        self.tree.heading('年龄', text='年龄')
        self.tree.heading('职位', text='职位')
        self.tree.heading('工资', text='工资')

        self.tree.place(x=50, y=100)

    # 查询职工信息
    def query_employee(self):
        emp_id = self.emp_id_entry.get()
        emp_name = self.emp_name_entry.get()

        # 连接数据库
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        # 执行SQL语句
        if emp_id:
            cursor.execute('SELECT * FROM employee WHERE id=?', (emp_id,))
        elif emp_name:
            cursor.execute('SELECT * FROM employee WHERE name=?', (emp_name,))
        else:
            cursor.execute('SELECT * FROM employee')

        # 获取查询结果
        results = cursor.fetchall()

        # 清空表格
        for item in self.tree.get_children():
            self.tree.delete(item)
        # 填充表格
        if results:
            for row in results:
                self.tree.insert('', tk.END, values=row)

        # 关闭数据库连接
        cursor.close()
        conn.close()