# Flask-SaeStorage
[新浪SAE Storage](http://sae.sina.com.cn/doc/python/storage.html) Flask扩展，新浪SAE Storage for Flask

## 安装
```python
pip install Flask-SaeStorage
```
本扩展仅能在SAE环境中使用，但可跨SAE应用而使用其它应用的Storage。

## 配置
| 配置项 | 说明 |
|:--------------------:|:---------------------------:|
| SAE_ACCESS_KEY | SAE Access Key（可选，默认为当前应用） |
| SAE_SECRET_KEY | SAE Secret Key（可选，默认为当前应用） |
| SAE_APP_NAME | Storage归属应用名（可选，默认为当前应用） |
| SAE_BUCKET_NAME | SAE 空间名称 |

## 使用
```python
from flask import Flask
from flask_saestorage import SaeStorage

SAE_ACCESS_KEY = 'SAE Access Key'
SAE_SECRET_KEY = 'SAE Secret Key'
SAE_APP_NAME = 'SAE App Name'
SAE_BUCKET_NAME = 'SAE Bucket Name'

app = Flask(__name__)
app.config.from_object(__name__)
sae_storage = SaeStorage(app)
# 或者
# sae_storage = SaeStorage()
# sae_storage.init_app(app)

# 保存文件到SAE Storage
@app.route('/save')
def save():
    data = 'data to save'
    filename = 'filename'
    ret = sae_storage.save(data, filename)
    return str(ret)

# 删除SAE Storage中的文件
@app.route('/delete')
def delete():
    filename = 'filename'
    ret = sae_storage.delete(filename)
    return str(ret)

# 根据文件名获取对应的公开URL
@app.route('/url')
def url():
    filename = 'filename'
    return sae_storage.url(filename)
```

## 返回值
`save`与`delete`返回值为[SAE Storage Python API](http://sae.sina.com.cn/doc/python/storage.html#module-sae.storage)中对应API的返回值。

## 测试
需在SAE环境中进行。

## 许可
The MIT License (MIT). 详情见 __License文件__