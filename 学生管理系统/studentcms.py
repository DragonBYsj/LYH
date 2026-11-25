#该文件用于增删改查学生信息
#导包
from student import Student#student是文件名,Student是类名
import time
class StudentManager:
    def __init__(self):
        """存储学生信息的列表"""
        self.student_list=[Student('张三',18,'男','12345678901','学习努力'),Student('李四',19,'女','12345678902','学习认真')]
    def show_mean(self):
        """显示学生管理系统菜单"""
        print("\t学生管理系统")
        print("\t1.添加学生")
        print("\t2.删除学生")
        print("\t3.修改学生")
        print("\t4.查询单个学生信息")
        print("\t5.查询所有学生信息")
        print("\t6.保存学生信息")
        print("\t7.退出学生管理系统")
    #添加学生信息
    def add_student(self):
        name=input("请输入学生姓名:")
        age=int(input("请输入学生年龄:"))
        gender=input("请输入学生性别:")
        phone=input("请输入学生电话:")
        desc=input("请输入学生描述:")
        #创建学生对象
        stu=Student(name,age,gender,phone,desc)
        #把学生对象添加到列表中
        self.student_list.append(stu)
        print(f'添加{name}学生信息成功\n')
    #删除学生信息
    def del_student(self):
        del_name=input("请输入要删除的学生姓名:")
        for stu in self.student_list:
            if stu.name==del_name:
                self.student_list.remove(stu)
                print(f'删除{del_name}学生信息成功\n')
                break
        else:
            print(f'没有找到{del_name}学生信息\n')

    #修改学生信息
    def update_student(self):
        update_name=input("请输入要修改的学生姓名:")
        for stu in self.student_list:
            if stu.name==update_name:
                stu.age=int(input("请输入学生年龄:"))
                stu.gender=input("请输入学生性别:")
                stu.phone=input("请输入学生电话:")
                stu.desc=input("请输入学生描述:")
                print(f'修改{update_name}学生信息成功\n')
                break
        else:
            print(f'没有找到{update_name}学生信息\n')
    #查询单个学生信息
    def search_student(self):
        search_name=input("请输入要查询的学生姓名:")
        for stu in self.student_list:
            if stu.name==search_name:
                print(stu)
                break
        else:
            print(f'没有找到{search_name}学生信息\n')
    #查询所有学生信息
    def show_all_student(self):
        if len(self.student_list)==0:
            print("没有学生信息\n")
        else:
            for stu in self.student_list:
                print(stu)
    #保存学生信息
    def save_student(self):
        with open("./student_data.txt","w",encoding="utf-8") as f:
            stu_dict=[stu.__dict__ for stu in self.student_list]
            f.write(str(stu_dict))
    #加载学生信息
    def load_student(self):
        with open("./student_data.txt","r",encoding="utf-8") as f:
            stu_data=f.read()
            #上述字符串转为列表
            stu_list=eval(stu_data)
            if len(stu_list)==0:
                stu_list=[]
            #把列表套字典转换为学生对象并赋值给self.stu_list
            self.stu_list=[Student(**stu) for stu in stu_list]
             
    #把上述业务跑通
    def start(self):
        self.load_student()  # 加载学生信息
        while True:
            time.sleep(1)#添加延迟,效果更好
            self.show_mean()
            num = input("请输入功能序号:")
            if num == "1":
                self.add_student()
            elif num == "2":
                self.del_student()
            elif num == "3":
                self.update_student()
            elif num == "4":
                self.search_student()
            elif num == "5":
                self.show_all_student()
            elif num == "6":
                self.save_student()
            elif num == "7":
                result = input("您确定要退出吗？(yes/no): ")
                if result == "yes":
                    self.save_student()  # 保存学生信息
                    print("退出学生管理系统")
                    break
                else:
                    print("取消退出")
            else:
                print("输入有误,请重新输入")

    def __str__(self):
        return f'当前学生总数:{len(self.student_list)}'
