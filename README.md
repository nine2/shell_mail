# shell_mail
直接使用命令发送邮件内容，包括附件

提供了一个配置模板用来发送附件

## 文件说明：
- `mail_core.py`: 发送邮件核心代码，所有模板最终调用到这里，也可以直接使用此文件进行发送邮件，查看帮助可运行 `python mail_core.py`
- `template_config.py`: 配置基本的邮件服务器设置
- `template_send_define.py`: 使用 `template_config.py` 中的配置，其他参数由此文件传入，如：邮件名，邮件内容，接收人，邮件附件。其他参数参考`python mail_core.py`
- `template_send.py`: 将接收人、邮件名、邮件内容先写入此文件中，查看文件中的TODO。帮助：`python template_send.py`
- `template_send_by_pwd`: 在 `template_send.py` 的基础上自己传入密码，这样不会明文显示出密码。帮助：`python  template_send_by_pwd.py`

## 其他

建议使用时 `cp` 一份模板为 自己使用，尽量不要更改模板文件！
