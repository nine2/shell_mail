#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import config

file_abs = os.path.abspath(__file__)
file_dir = os.path.dirname(file_abs)
g_mail_core_path = "TODO: 给出mail_core.py 文件位置, 最好是绝对位置"
g_mail_core_path = file_dir + "/mail_core.py"  # 默认


def get_help_info():
	file_name = os.path.basename(__file__)
	print "python ",file_name, "-p pwd -r 'receiver1' -r 'receiver2' -s 'subject' -c 'content' -a att1(附件) -a att2"
	print "-s, -c, -a 可省略"
	print "-r 如果未设置，则只给自己发邮件"
	print "!!! 注意："
	print "\t所有传入的单个参数，中间不能有空格!"


def main(argv):
	if len(argv) < 1 :
		print get_help_info()
		sys.exit(0)
	#=======================================================
	# 设置服务器，用户名、口令以及邮箱的后缀, 【可修改部分】
	#=======================================================
	config_data = config.get_config()

	host=config_data["host"]
	# 企业邮箱,需要全称
	# 非QQ企业邮箱,只需要用户名
	user=config_data["user"]
	show_user_name = config_data["show_user_name"]
	postfix=config_data["postfix"]
	server_type=config_data["server_type"]

	pwd=config_data["pwd"]

	# 是否备份邮件(发给自己一份)
	backup = config_data["backup"]
	# 邮件log
	log_path = config_data["log_path"]
	# 收件人
	receivers = config_data["receivers"]

	# 默认主题、内容
	subject = "from " + show_user_name + "(" + user + ")"
	content = "默认内容\n"

	subject = config_data["subject"]
	content = config_data["content"]

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
