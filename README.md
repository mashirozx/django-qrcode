Django + MongoDB: Adaptive QR Code System
===

## 思路

- 通过 GitHub OAuth 获取用户用户信息

- 在 MongoDB 中将用户`邮箱`和`邮箱 md5 值`作为主键

- 以邮箱作为用户标识，暂不考虑折腾 cookie

- 将用户提供的微信和支付宝二维码字符串存入数据库

- 扫码时通过 url 参数查询 邮箱 md5 值并返回 HTML inline data

- 前端通过 JavaScript 为 inline data 生成二维码

## 组件

1. 数据库

2. Dashboard 模块

3. md5 查询模块

## Other

基于 Windows 开发，后期再后端完成后再考虑部署 Linux 测试

## Permission

商业使用禁止