import pandas as pd
import joblib
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split,GridSearchCV
from collections import Counter #统计数据的
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold#分层K折交叉验证,类似于网格搜索时cv折数
from sklearn.utils import class_weight#平衡权重
#定义函数对红酒品质分类数据:拆分成训练集和测试集 并保存到csv文件中
def dmo1_data_split():
    df=pd.read_csv('./红酒品质分类.csv',sep=';')
    #抽取特征数据和标签数据
    x=df.iloc[:,:-1]
    y=df.iloc[:,-1] - 3  #最后一列是标签 默认值是:[3,8]->[0,5]
    #stratify 参考数据集的标签分布
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=23,stratify=y)
    #把上述的训练集特征和标签数据拼到一起,测试集特征和标签数据拼接到一起 最后写到文件中
    pd.concat([x_train,y_train],axis=1).to_csv('./红酒品质分类_train.csv',index=False)#axis=1表示横向拼接
    pd.concat([x_test,y_test],axis=1).to_csv('./红酒品质分类_test.csv',index=False)
#定义函数训练模型并保存
def dmo2_train_mode():
    train_data=pd.read_csv('./红酒品质分类_train.csv')
    test_data=pd.read_csv('./红酒品质分类_test.csv')
    x_train=train_data.iloc[:,:-1]
    y_train=train_data.iloc[:,-1]
    x_test=test_data.iloc[:,:-1]
    y_test=test_data.iloc[:,-1]
    estimator=xgb.XGBClassifier(max_depth=5,n_estimators=100,learning_rate=0.1,random_state=23,objective='multi:softmax')
    #加入权重 因为数据集是样本不均衡的
    class_weight.compute_sample_weight('balanced',y_train)#参1 平衡权重 
    estimator.fit(x_train,y_train)
    joblib.dump(estimator,'./红酒品质分类.pkl')
#定义函数测试模型
def dmo3_use_mode():
    train_data=pd.read_csv('./红酒品质分类_train.csv')
    test_data=pd.read_csv('./红酒品质分类_test.csv')
    x_train=train_data.iloc[:,:-1]
    y_train=train_data.iloc[:,-1]
    x_test=test_data.iloc[:,:-1]
    y_test=test_data.iloc[:,-1]
    estimator=joblib.load('./红酒品质分类.pkl')
    #创建网格搜索+交叉验证(结合分层采样数据),找模型最优参数组合
    param_dict={'max_depth':[2,3,5,6],'n_estimator':[30,50,100,150],'learning_rate':[0.2,0.3,1,1.3]}
    #创建分层采样对象
    #参1是折数 参2 是否打乱数据
    skf=StratifiedKFold(n_splits=5,shuffle=True,random_state=23)
    gs_estimator=GridSearchCV(estimator,param_dict,cv=skf)
    gs_estimator.fit(x_train,y_train)
    y_pre=gs_estimator.predict(x_test)
    print(f'预测值{y_pre}')
    print(f'最优估计器对象组合{gs_estimator.best_estimator_}')
    print(f'最优评分{gs_estimator.best_score_}')
if __name__=='__main__':
    #dmo1_data_split()
    dmo2_train_mode()
    dmo3_use_mode 