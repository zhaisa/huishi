import tkinter as tk
import sqlite3

class ModifyFrame:
    # 初始化界面
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x300')
        self.master.title('修改职工信息')

        # 创建标签和输入框
        tk.Label(self.master, text='职工ID：').place(x=50, y=50)
        self.emp_id_entry = tk.Entry(self.master)
        self.emp_id_entry.place(x=120, y=50)

        tk.Label(self.master, text='姓名：').place(x=50, y=80)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.place(x=100, y=80)

        tk.Label(self.master, text='性别：').place(x=50, y=110)
        self.gender_entry = tk.Entry(self.master)
        self.gender_entry.place(x=100, y=110)

        tk.Label(self.master, text='年龄：').place(x=50, y=140)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.place(x=100, y=140)

        tk.Label(self.master, text='职位：').place(x=50, y=170)
        self.job_entry = tk.Entry(self.master)
        self.job_entry.place(x=100, y=170)

        tk.Label(self.master, text='工资：').place(x=50, y=200)
        self.salary_entry = tk.Entry(self.master)
        self.salary_entry.place(x=100, y=200)

        # 创建确认和取消按钮
        tk.Button(self.master, text='确认', command=self.modify_employee).place(x=120, y=250)
        tk.Button(self.master, text='取消', command=self.master.destroy).place(x=220, y=250)

    # 修改职工信息
    def modify_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        job = self.job_entry.get()
        salary = self.salary_entry.get()

        # 连接数据库
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        # 执行SQL语句
        cursor.execute('UPDATE employee SET name=?, gender=?, age=?, job=?, salary=? WHERE id=?',
                       (name, gender, age, job, salary, emp_id))

        # 提交事务
        conn.commit()

        # 关闭数据库连接
        cursor.close()
        conn.close()

        # 提示用户修改成功
        tk.messagebox.showinfo(title='提示', message='修改职工信息成功！')

        # 清空输入框
        self.emp_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.job_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)