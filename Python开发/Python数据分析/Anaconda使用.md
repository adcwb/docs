
### 一、Anaconda简介

```python
Anaconda：是一个基于数据分析+机器学习的集成环境。
anadonda安装注意事项:
    > 安装路径中不可以出现中文和特殊符号
    > 安装时要勾选环境变量
jupyter：Anaconda提供的一个基于浏览器可视化的编码工具。
	安装了anaconda后，需要在终端中录入jupyter notebook指令。
	注意：jupyter notebook指令对应的终端目录就是jupyter启动后的根目录

jupyter的基本操作：
	.ipynb：jupyter中的一个源文件，代码的编写就要基于该源文件。该源文件是由cell组成的
    
cell的使用
	cell是分成了两种不同的模式：
	code：用来编写程序的
    	注意：代码编写不分上下，代码的执行分先后
	markdown：用来编写笔记
快捷键：
	添加cell：a上插入cell，b下插入cell
	删除cell：x
    撤销：z
	执行cell：shift+enter
	切换cell的模式：
		code-》markdown：m
		反之：y
	查看帮助文档：shift+tab
```



### 二、环境变量配置

注意是系统变量，而不是用户变量。我这里anaconda安装在`C:\ProgramData`中

| 系统变量 | 路径                                           | 说明                    |
| :------- | :--------------------------------------------- | :---------------------- |
| Path     | C:\ProgramData\Anaconda3                       | Python需要              |
| Path     | C:\ProgramData\Anaconda3\Scripts               | conda自带脚本           |
| Path     | C:\ProgramData\Anaconda3\Library\bin           | jupyter notebook动态库  |
| Path     | C:\ProgramData\Anaconda3\Library\mingw-w64\bin | 使用C with python的时候 |
| Path     | C:\ProgramData\Anaconda3\Library\usr\bin       | 没有该目录就算了        |

由于版本不一致，可能有些目录不存在，没有就算了。

**测试是否安装成功**

终端中输入如下几个命令，正常返回说明安装成功，否则检查添加path是否成功，或者重启系统后尝试：

```
python -V
conda info
conda --version
```

### 三、配置国内镜像源

一些第三方的包的官网都在国外，导致下载太慢或者无法下载。这里提供配置国内的镜像源：

```bash
# 添加清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

# 阿里家的
conda config --add channels http://mirrors.aliyun.com/pypi/simple/


# 设置搜索时显示通道地址
conda config --set show_channel_urls yes

# 查看是否修改好通道
conda config --show channels
```





### 三、虚拟环境管理

```bash
# 查看conda的配置
conda config --show

# 修改配置
conda config --add key value
conda config --remove key value

# 检查更新当前的conda管理工具
conda update -n base -c defaults conda -y

# 查看当前环境已安装的包
conda list
pip list
pip freeze

# 创建虚拟环境，指定虚拟环境的Python版本，不指定的话，默认跟anaconda的默认Python解释器版本
# 注意，使用conda config --show查看envs_dirs指向的路径，该路径是虚拟环境的默认安装位置，你也可以修改这个值
conda create -n 虚拟环境名称 python=3.6 -y

# 修改虚拟环境的保存位置，默认是保存到了用户家目录下
conda config --add envs_dirs C:\ProgramData\Anaconda3\envs

# 激活/退出虚拟环境
conda activate 虚拟环境名称
conda deactivate

# 为指定虚拟环境安装指定包，删除指定包；当然，也可以在激活虚拟环境后，使用pip下载，他俩的区别：conda可以不激活虚拟环境，就可以为指定虚拟环境安装包，而pip需要激活对应的虚拟环境才能安装包
conda install -n 虚拟环境名称 包名 -y
conda remove -n 虚拟环境名称 包名 -y

# 查看所有虚拟环境
conda info --envs
conda info -e
conda env list

# 删除指定虚拟环境
conda remove -n 虚拟环境名称 --all -y
```



### 四、Jupyter notebook

#### 1、内核操作

```bash
# 查看内核
jupyter kernelspec list

# 删除内核
jupyter kernelspec remove 需要删除的kernel 名称

# 创建内核，env_name为内核名称
conda create -n env_name python=3.9
conda activate env_name
conda install ipykernel -y
conda list
conda deactivate
python -m ipykernel install --name env_name
jupyter kernelspec list
```

