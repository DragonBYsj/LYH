# LYH

个人学习代码仓库：机器学习练习 + Python 小项目。代码均为学习过程中的练习，注释与命名保留原始写法。

## 目录结构

```
LYH/
├── 机器学习/
│   ├── 红酒品质分类案例.py          # XGBoost 多分类 + 网格搜索
│   ├── 红酒品质分类.csv            # 原始数据（; 分隔）
│   ├── 红酒品质分类_train.csv      # 划分后的训练集
│   ├── 红酒品质分类_test.csv       # 划分后的测试集
│   ├── 红酒品质分类.pkl            # 训练好的模型（joblib）
│   ├── 鸢尾花案例.py               # KNN 鸢尾花分类
│   ├── 泰坦尼克号案例CRT树分类.py   # CART 决策树分类 + 树可视化
│   ├── 随机森林泰坦尼克号.py        # 决策树 vs 随机森林 + 网格搜索
│   └── titanic_train.csv          # 泰坦尼克号数据（891 行）
└── 学生管理系统/
    ├── main.py                     # 程序入口
    ├── studentcms.py               # 学生管理业务逻辑
    ├── student.py                  # Student 实体类
    └── 拓展.py                     # 对象 <-> 字典 互转练习
```

## 机器学习

### 红酒品质分类案例.py

用 XGBoost 对红酒品质做多分类，并配合网格搜索调参。

- **数据**：`红酒品质分类.csv` 为分号 `;` 分隔，共 1600 行；11 个理化特征（fixed acidity、volatile acidity、citric acid、residual sugar、chlorides、free sulfur dioxide、total sulfur dioxide、density、pH、sulphates、alcohol）+ 1 个标签 `quality`
- **标签处理**：`quality` 取值 3–8，脚本整体减 3 映射为 0–5 共 6 类
- **dmo1_data_split()**：按标签分层抽样，8:2 划分训练集 / 测试集，并导出 `_train.csv`（1280 行）与 `_test.csv`（320 行），导出后为逗号分隔
- **dmo2_train_mode()**：训练 `XGBClassifier(max_depth=5, n_estimators=100, learning_rate=0.1, random_state=23)`，用 `joblib` 保存为 `红酒品质分类.pkl`
- **dmo3_use_mode()**：加载模型，结合 `GridSearchCV` 与 `StratifiedKFold(n_splits=5)` 搜索最优参数

运行（工作目录需在 `机器学习/` 下，脚本使用相对路径）：

```bash
cd 机器学习
python 红酒品质分类案例.py
```

> 注意：`__main__` 中默认调用 `dmo2_train_mode()`，每次运行都会重新训练并覆盖 `红酒品质分类.pkl`；`dmo1_data_split()` 已注释，如需重新划分数据集请手动取消注释。

依赖：`pandas`、`numpy`、`scikit-learn`、`xgboost`、`joblib`

### 鸢尾花案例.py

用 KNN 完成鸢尾花数据集的分类。

- 使用 `sklearn.datasets.load_iris()` 内置数据（150 样本 / 4 特征 / 3 类）
- `StandardScaler` 标准化后训练 `KNeighborsClassifier(n_neighbors=3)`
- 含 seaborn + matplotlib 散点图可视化函数
- 用 `accuracy_score` 与自造样本验证模型

运行：

```bash
cd 机器学习
python 鸢尾花案例.py
```

依赖：`scikit-learn`、`pandas`、`seaborn`、`matplotlib`

### 泰坦尼克号案例CRT树分类.py

用 CART 决策树预测泰坦尼克号乘客是否生还，并把树结构画出来。

- **数据**：`titanic_train.csv`，891 行 12 列，标签 `Survived`（0 未生还 / 1 生还）
- **特征**：`Pclass`（船舱等级）、`Sex`（性别）、`Age`（年龄）
- **预处理**：`Age` 列存在缺失，用该列均值填充；`Sex` 列做 one-hot 编码
- **划分**：8:2，`random_state=23`
- **模型**：`DecisionTreeClassifier(max_depth=10)`
- **评估**：`classification_report` 输出准确率 / 精确率 / 召回率 / F1
- **可视化**：`plot_tree(filled=True, max_depth=10)`，画布 30×20

运行（工作目录需在 `机器学习/` 下）：

```bash
cd 机器学习
python 泰坦尼克号案例CRT树分类.py
```

依赖：`pandas`、`scikit-learn`、`matplotlib`

### 随机森林泰坦尼克号.py

对比单棵决策树与随机森林（bagging），并对随机森林做网格搜索调参。

- **数据与特征**：同上，`titanic_train.csv` 的 `Pclass` / `Sex` / `Age`，`Age` 均值填充
- **三组实验**：默认参数决策树 → 默认参数随机森林 → `GridSearchCV` 调参后的随机森林
- **搜索空间**：`n_estimators` ∈ [30, 50, 60, 90, 110]，`max_depth` ∈ [2, 3, 5, 7]，交叉验证 `cv=2`
- 用 `score()` 打印三者测试集准确率做对比

运行：

```bash
cd 机器学习
python 随机森林泰坦尼克号.py
```

依赖：`pandas`、`scikit-learn`

## 学生管理系统

命令行版学生信息增删改查系统。

- `main.py`：程序入口，创建 `StudentManager` 并启动主循环
- `studentcms.py`：核心业务，菜单含 添加 / 删除 / 修改 / 查询单个 / 查询全部 / 保存 / 退出
- `student.py`：`Student` 实体类（姓名、年龄、性别、电话、描述）
- 数据持久化：保存到脚本同目录下的 `student_data.txt`

运行：

```bash
cd 学生管理系统
python main.py
```

> 注意：启动时会调用 `load_student()` 读取同目录的 `student_data.txt`，若该文件不存在会抛出 `FileNotFoundError`，先手动新建一个内容为 `[]` 的空文件即可。该数据文件未纳入版本管理。

## 环境

- Python 3.14
- 第三方库：`pandas`、`numpy`、`scikit-learn`、`xgboost`、`joblib`、`seaborn`、`matplotlib`

## 说明

- `__pycache__/`、`*.pyc` 等编译产物已通过 `.gitignore` 排除
- `红酒品质分类.pkl` 为二进制模型文件（约 1 MB），与源码版本相关，重新训练即可覆盖
- 数据集与源码放在同一目录，脚本均使用相对路径，**运行前先 `cd 机器学习` 或 `cd 学生管理系统`**
