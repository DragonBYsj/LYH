import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.tree import plot_tree
#加载数据
data=pd.read_csv("./titanic_train.csv")
data.info()

#数据预处理
#提取特征和标签
x=data[['Pclass','Sex','Age']]
y=data['Survived']
#Age列有缺失  我们用该列的平均值做填充
x=x.copy()
x['Age']=x['Age'].fillna(x['Age'].mean())
#针对于Sex列进行one-hot编码
x=pd.get_dummies(x,columns=['Sex'])
#划分测试集和训练集
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=23)
#模型训练
#max——depth是绘制的决策树结构最多十层
estimator=DecisionTreeClassifier(max_depth=10)
estimator.fit(x_train,y_train)
#模型预测
y_pre=estimator.predict(x_test)
print(f'预测值为{y_pre}')
#模型评估
print(f'分类评估报告:\n{classification_report(y_test,y_pre)}')
#绘制
plt.figure(figsize=(30,20))#设置图片大小
#参1是模型对象 参2是是否颜色填充  参3是决策树结构 最多十层
plot_tree(estimator,filled=True,max_depth=10)
plt.show()