## ini

```
virtualenv ENV --no-site-packages

# Linux
source ENV/bin/activate

# Windows
cd ENV/Scripts

activate

cd ../../app

deactivate

# In Evn
pip install Django
```

## Django

```
python manage.py runserver

# ini SQLite
python manage.py migrate

# 迁移 models
python manage.py makemigrations polls

# 查看迁移后将进行的 SQL 操作，非必要
python manage.py sqlmigrate polls 0001

# 数据库里创建新定义的模型的数据表——将对模型的更改同步到数据库结构上
python manage.py migrate
```

改变模型需要这三步：

- 编辑 models.py 文件，改变模型。
- 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
- 运行 python manage.py migrate 来应用数据库迁移。

```
# 命令行调试
python manage.py shell
```

创建管理员

```
python manage.py createsuperuser
```
