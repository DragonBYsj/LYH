#通过KNN算法实现鸢尾花的分类操作
from sklearn.datasets import load_iris #加载鸢尾花测试集
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split #分割训练集和测试集
from sklearn.preprocessing import StandardScaler #数据标准化
from sklearn.neighbors import KNeighborsClassifier #KNN算法 分类对象
from sklearn.metrics import accuracy_score #模型评估,计算模型预测的准确率

#定义函数加载鸢尾花数据集并查看数据集
def dmo1_loadiris():
    #加载数据集
    iris_data=load_iris()
    #查看数据集
    print(f'数据集{iris_data}')#字典形态 

#定义函数绘制数据集的散点图
def dmo2_showiris():
    iris_data=load_iris()
    #把数据封装为DataFrame对象,seaborn可视化需要DataFrame对象
    iris_df=pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
    #给df对象新增一列充当标签列
    iris_df['label']=iris_data.target
    #通过seaborn绘制散点图
    sns.lmplot(data=iris_df,x='sepal length (cm)',y='sepal width (cm)',hue='label',fit_reg=False)#hue是分组操作,让散点有颜色区分,fit_reg如果等于True的话会有拟合线回归线
    #设置标题
    plt.title('iris data')
    plt.tight_layout()#自动调整子图参数,以使整个图像的边界与子图匹配
    plt.show()

#定义函数切分训练集和测试集
def dmo3_split_train_test():
    iris_data=load_iris()
    #数据的预处理,从150个特征和标签中,按照8:2切分训练集和测试集
    """参1是特征数据,参2是标签数据,参3是测试集的比例,参4是随机种子(种子一致,每次生成的随机数据集是固定的)
       返回值是训练集的特征数据,测试集的特征数据,训练集的标签数据,测试集的标签数据"""
    x_train,x_test,y_train,y_test=train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=23)#返回元组

#定义函数实现鸢尾花完整案例
def dmo4_iris_evalue_test():
    iris_data=load_iris()
    x_train,x_test,y_train,y_test=train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=23)
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.fit_transform(x_test)
    #创建模型对象
    estimator=KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)
    #对切分的测试集进行测试
    y_pre=estimator.predict(x_test)
    print(f'预测值{y_pre}')
    #自定义测试集
    my_data=[[7.8,2.1,3.9,1.6]]
    my_data=transfer.transform(my_data)
    y_pre_new=estimator.predict(my_data)
    print(y_pre_new)
    #查看上述数据集,每种分类的预测概率
    y_pre_proba=estimator.predict_proba(my_data)
    print(f'各分类预测概率{y_pre_proba}')
    #模型评估
    #方式1  基于训练集的特征和训练集的标签
    print(f'正确率{estimator.score(x_train,y_train)}')
    #方式2  基于测试集标签和预测结果进行评分
    print(f'正确率{accuracy_score(y_test,y_pre)}')
if __name__=='__main__':
    dmo4_iris_evalue_test()