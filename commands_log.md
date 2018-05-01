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
