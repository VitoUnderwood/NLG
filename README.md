# MyLog

## 准备

### 虚拟环境
创建虚拟环境，隔离版本，稳定开发。
1. 使用python自带的venv, python -m venv path
2. source venv/bin/activate(deactivate)
3. pip freeze > requirements.txt (pip install -r requirements.txt)
如果要是对特定版本对python版本有要求，可以使用anaconda进行python版本控制和包管理

### 依赖
python3.8.2 
numpy pandas pytorch transformers
详细版本见requirement.txt

### 类图

使用plantUML绘制类图，见nlg.puml

### 基本框架

构建Args Dictionary BaseModel Utils基本框架，使用常见的工厂模式便于拓展使用

