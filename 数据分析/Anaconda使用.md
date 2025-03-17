

### 虚拟环境管理

#### 创建虚拟环境

```python
# conda create -n 虚拟环境名称 python=解释器版本 要安装的包名，可省略

conda create --name python36 python=3.6 requests

```



#### 查看虚拟环境

```python
conda env list

# conda environments:
#
demo311                  C:\Users\BSI\.conda\envs\demo311
djangoProject            C:\Users\BSI\.conda\envs\djangoProject
base                     D:\anaconda3
```



#### 激活虚拟环境

```python
conda activate 虚拟环境名称

conda activate demo311
```



#### 退出虚拟环境

```python
conda deactivate
```



#### 共享虚拟环境

```python
# 类似于pip导出环境包

# 导出虚拟环境包
conda env export --file python36_env.yml
conda env export > python36_env.yaml

# 根据导出的虚拟环境创建新环境
conda env create -f /home/user1/python36_env.yml


# 直接打包现有环境
# 安装conda-pack
pip install conda-pack

# 打包指定环境 该命令会在你当前所在的目录产生一个环境包的压缩文件 env_name.tar.gz
conda pack -n env_name

# 将打包好的包直接复制到新的环境中解压即可使用
```



#### 删除虚拟环境

```python
conda remove -n python36 --all
```



### 包管理

#### 安装包

```python
conda install package_name
pip install package_name
```



#### 列出包

```python
conda list
```



#### 更新包

```python
conda update package_name

# 一次更新所有包
conda update --all
```



#### 查找包

```PYTHON
conda search keyword

# 例如：我们要安装pandas，但是忘了准确名称，可以这样查找：
conda search pan

```



#### 删除包

```python
conda remove package_name
```









