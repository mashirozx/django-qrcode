Django 入门~~
===

## 思路

- 通过 GitHub OAuth 获取用户用户信息

- 在 ~~MongoDB~~ SQLite 中将用户`邮箱`和`邮箱 md5 值`作为主键

- 以邮箱作为用户标识，暂不考虑折腾 cookie

- 将用户提供的微信和支付宝二维码字符串存入数据库

- 扫码时通过 url 参数查询 邮箱 md5 值并返回 HTML inline data

- 前端通过 JavaScript 为 inline data 生成二维码

## 组件

1. 数据库

2. Dashboard 模块

3. md5 查询模块

## Other

基于 Windows 开发，待后端完成后再考虑部署 Linux 测试

## Permission

禁止用于提供商业性质二维码接口服务（特指向别人收取费用以提供此接口的服务，但使用二维码收款本身不在限制范围内）。
