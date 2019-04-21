## 部署运行环境

### 拉取远程代码

```
git clone https://github.com/ndlteam/bookStore.git
```

### 创建venv环境

```
python36 -m venv ./venv
```

### 激活venv环境

```
.\venv\Scripts\activate.bat
or
source ./venv/bin/activate
```

### 安装依赖包

```
pip install django==1.11.20
```

### 运行项目

```
manage.py runserver
```
