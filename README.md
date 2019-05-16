# 小型网上书店系统

## 部署运行环境

### 安装python3.6

安装完成后，windows用户可以使用以下命令使用python3.6：

```bat
py -3.6
```

当然，你可能需要把pip[切换到国内源](https://blog.csdn.net/lambert310/article/details/52412059)。

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

### 拉取远程代码

```bash
git clone https://github.com/ndlteam/bookStore.git
```

### 安装依赖包

请确保位于已激活虚拟环境的shell环境，并位于项目的根目录。

```bash
pip install -r requirements.txt
```

如果你添加了安装了新的python包，请使用以下命令更新requirements文件：

```bash
pip freeze > requirements.txt
```

### 运行项目

请确保位于已激活虚拟环境的shell环境，并位于项目的根目录。

```powershell
py -3.6 manage.py runserver
```