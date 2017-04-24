#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import getpass
import config
# import mail_core
import imp

config_data = config.get_config()

home = os.environ["HOME"]
home_config_path = home + "/.mail_config.py"
config_home = {}
if os.path.isfile(home_config_path):
	home_config = imp.load_source('module.name', home_config_path)
	config_home = home_config.get_config();

file_abs = os.path.abspath(__file__)
file_dir = os.path.dirname(file_abs)
g_mail_core_path = "TODO: 给出mail_core.py 文件位置, 最好是绝对位置"
g_mail_core_path = file_dir + "/mail_core.py"  # 默认


def get_help_info():
	# file_name = os.path.basename(__file__)
	print "config file: ~/.mail_config.py"
	print "use: `mailconfig` to get config file"
	print ""
	# print "python ",file_name, "-r 'receiver1' -r 'receiver2' -s 'subject' -c 'content' -a att1(附件) -a att2"
	print "mailsend -r 'receiver1' -r 'receiver2' -s 'subject' -c 'content' -a att1(附件) -a att2"
	print "-s, -c, -a 可省略"
	print "-r 如果未设置，则只给自己发邮件"
	print "!!! 注意：所有传入的单个参数，中间不能有空格! 可使用双引号引起来!"
	# print "支持的所有参数如下："
	# print mail_core.get_help_info()


def main(argv):
	if len(argv) < 1 :
		print get_help_info()
		sys.exit(0)
	#=======================================================
	# 设置服务器，用户名、口令以及邮箱的后缀, 【可修改部分】
	#=======================================================

	for k, v in config_home.items():
		config_data[k] = v

	for i, v in config_data["host"].items():
		print i,": ", str(v)
	idx = 0
	if len(config_data["host"]) != 1:
		while not config_data["host"].has_key(idx):
			idx = int(raw_input("please chose a Email: "))
	else:
		for i, cf in config_data["host"].items():
			if len(cf):
				idx = i
				break
	if not config_data["host"].has_key(idx):
		return
	host_data = config_data["host"][idx]
	host=host_data["host"]
	postfix=host_data["postfix"]
	server_type=host_data["server_type"]

	if not len(config_data["user"]):
		user = raw_input("please input your user: ")
		config_data["user"] = user
	else:
		print "user: ", config_data["user"]

	if not len(config_data["pwd"]):
		pwd = getpass.getpass("please input your pwd: ")
		config_data["pwd"] = pwd

	# 企业邮箱,需要全称
	# 非QQ企业邮箱,只需要用户名
	user=config_data["user"]
	if server_type == "eim" and "@" not in user:
		user = user.strip() + "@" + postfix.strip()

	pwd=config_data["pwd"]

	show_user_name = config_data["show_user_name"]

	# 是否备份邮件(发给自己一份)
	backup = config_data["backup"]
	# 邮件log
	log_path = config_data["log_path"]
	# 收件人
	receivers = config_data["receivers"]

	# 默认主题、内容
	subject = "Subject:From:" + show_user_name + "(" + user + ")"
	content = "Content____ "

	#=========================================
	# 处理命令，勿改动
	#=========================================
	# 生成命令
	receivers_str = ''
	for rc in receivers:
		receivers_str = receivers_str + ' -r "' + rc + '"'
	if len(show_user_name):
		show_user_name = '-n "' + show_user_name +'"'
	if len(log_path):
		log_path = '-l "' + log_path + '"'
	if len(server_type):
		server_type = '-t ' + server_type
	if backup > 0:
		backup = '-b '
	else:
		backup = '--no-backup '

	cmd = "python {mail_core} -h {h} -u {u} -f {f} {sname} {t} {b} {l} -s '{s}' -c {c} {rs} ".format(
			mail_core=g_mail_core_path,
			h=host, u=user, f=postfix, sname=show_user_name,
			t=server_type, b=backup, l=log_path,
			s=subject, c=content,rs=receivers_str,
			input_argv=argv)
	if len(pwd) > 4 and pwd[0:4] != 'TODO':
		cmd = cmd + "-p {p} ".format(p=pwd)
	for a in argv:
		cmd = cmd + "\"{av}\"".format(av=a) + " "
	# 执行命令
	os.system(cmd)
	#=========================================

if __name__ == "__main__":
	# 这里如果传入了参数，只能是用做附件发送的文件。
	main(sys.argv[1:])
