from student import Student
#学生转字典
s1=Student('张三',18,'男','12345678901','学习努力')
my_dict=s1.__dict__
#字典转学生对象
s2=Student(**my_dict)