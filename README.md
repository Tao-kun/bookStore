# 小型网上书店系统

## 部署运行环境

### 安装python3.6

安装完成后，windows用户可以使用以下命令使用python3.6：

```bat
py -3.6
```

当然，你可能需要把pip切换到国内源

### 创建venv环境

#### Windows：

```bat
py -3.6 -m venv your_venv_path\your_venv_name
```

#### *unix

```bash
python36 -m venv your_venv_path/your_venv_name
```

### 激活venv环境

#### Windows

如果使用cmd.exe，那么：

```bat
your_venv_path\your_venv_name\Scripts\activate.bat
```

如果使用powershell.exe，那么首先使用管理员身份运行powershell，运行

```powershell
Set-ExecutionPolicy Unrestricted
```

输入`Y`或`A`允许后，运行

```powershell
your_venv_path\your_venv_name\Scripts\Activate.ps1
```

#### *unix

```bash
source your_venv_path/your_venv_name/bin/activate
```

### 安装依赖包

```bash
pip install django==1.11.20
```

### 拉取远程代码

```bash
git clone https://github.com/ndlteam/bookStore.git
```

### 运行项目

```bash
manage.py runserver
```
