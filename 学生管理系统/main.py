#程序入口文件
from studentcms import StudentManager
#程序主入口 
if __name__=="__main__":
    #创建学生管理系统对象
    stu_cms=StudentManager()
    #启动学生管理系统
    stu_cms.start()