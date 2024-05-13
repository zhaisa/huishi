import tkinter as tk
import sqlite3



class AddFrame:
    # 初始化界面
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x300')
        self.master.title('添加职工信息')

        # 创建标签和输入框
        tk.Label(self.master, text='姓名：').place(x=50, y=50)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.place(x=100, y=50)

        tk.Label(self.master, text='性别：').place(x=50, y=80)
        self.gender_entry = tk.Entry(self.master)
        self.gender_entry.place(x=100, y=80)

        tk.Label(self.master, text='年龄：').place(x=50, y=110)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.place(x=100, y=110)

        tk.Label(self.master, text='职位：').place(x=50, y=140)
        self.job_entry = tk.Entry(self.master)
        self.job_entry.place(x=100, y=140)

        tk.Label(self.master, text='工资：').place(x=50, y=170)
        self.salary_entry = tk.Entry(self.master)
        self.salary_entry.place(x=100, y=170)
       # 创建确认和取消按钮
        tk.Button(self.master, text='确认', command=self.add_employee).place(x=120, y=220)
        tk.Button(self.master, text='取消', command=self.master.destroy).place(x=220, y=220)

    # 添加职工信息
    def add_employee(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        job = self.job_entry.get()
        salary = self.salary_entry.get()

        # 连接数据库
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        # 执行SQL语句
        cursor.execute('INSERT INTO employee (name, gender, age, job, salary) VALUES (?, ?, ?, ?, ?)',
                       (name, gender, age, job, salary))

        # 提交事务
        conn.commit()

        # 关闭数据库连接
        cursor.close()
        conn.close()

        # 提示用户添加成功
        tk.messagebox.showinfo(title='提示', message='添加职工信息成功！')
        # 清空输入框
        self.name_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.job_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)

if __name__ == '__main__':
    AddFrame(master=tk.Tk())