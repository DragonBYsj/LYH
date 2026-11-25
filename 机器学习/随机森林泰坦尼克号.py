import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier#随机森林
from sklearn.model_selection import GridSearchCV
df=pd.read_csv('./titanic_train.csv')
x=df[['Pclass','Sex','Age']].copy()#Pclass是船舱等级,copy是为了防止报错复制自己一遍
y=df['Survived']
#空值处理 用Age列的平均值填充列的空值
x['Age']=x['Age'].fillna(x['Age'].mean())
x=pd.get_dummies(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=23)

#创建决策树对象演示单一的决策树效果 默认参数
estimator1=DecisionTreeClassifier()
estimator1.fit(x_train,y_train)
y_pre1=estimator1.predict(x_test)
print(f'决策树模型的准确率{estimator1.score(x_test,y_test)}')
print('-'*23)

#创建随机森林对象 演示多个决策树(bagging)效果 默认参数
estimator2=RandomForestClassifier()
estimator2.fit(x_train,y_train)
y_pre2=estimator2.predict(x_test)
print(f'随机森林模型准确率{estimator2.score(x_test,y_test)}')

#随机森林 网格搜索
estimator3=RandomForestClassifier()
estimator3.fit(x_train,y_train)
params={'n_estimators':[30,50,60,90,110],'max_depth':[2,3,5,7]}
gs_estimator=GridSearchCV(estimator3,param_grid=params,cv=2)
gs_estimator.fit(x_train,y_train)
y_pre3=gs_estimator.predict(x_test)
print(f'随机森林模型准确率{estimator3.score(x_test,y_test)}')
