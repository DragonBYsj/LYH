class Student:
    def __init__(self,name,age,gender,phone,desc):
        """学生类,包含姓名,年龄,性别,电话,描述等属性"""
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone
        self.desc=desc
    def __str__(self):
        return f'学生的姓名是{self.name},学生的年龄是{self.age},学生的性别是{self.gender},学生的电话是{self.phone},学生的描述是{self.desc}'
#测试运行
if __name__=='__main__':
    s1=Student('张三',18,'男','12345678901','学习努力')
    print(s1)