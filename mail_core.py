#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2015 All rights reserved.
#
#   Author        : bbxytl
#   Email         : bbxytl@gmail.com
#   File Name     : mail_core.py
#   Last Modified : 2016-08-10 11:26
#   Describe      : 发送邮件核心
#
#   Log           :
#
# ====================================================
#==========================================
# 导入smtplib和MIMEText
#==========================================
# import codecs
#  import json
import time
import os
import sys
import getopt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def encode(str):
    return str.encode("utf-8")

#==========================================
# 设置服务器，用户名、口令以及邮箱的后缀
#==========================================
mail_host="smtp.exmail.qq.com"
# 企业邮箱,需要全称
mail_user="xxx@yy.com"
mail_pwd=""
mail_postfix="eim"
# 非QQ企业邮箱,只需要用户名
# mail_user="xxx"
# mail_pwd="pppppp"
# mail_postfix="yy"
#==========================================
# 发送邮件
#==========================================
# 全局变量
g_sender = ""  # 寄件人
g_sender_email = "" # 寄件人的email地址
g_show_user_name = g_sender_email
g_receivers = []  # 收件人
g_sub = ""   # 主题
g_content = ""  # 内容
g_attachments = []  # 附件列表

g_log_path = "./send_mail.log"  # 记录发件log
g_server_type = ""  # 寄件服务器类型
g_have_fix_server = ['eim']   # 使用后缀的用户名

def set_sender(host, user, pwd, postfix, show_user_name, server_type):
	global mail_host
	global mail_user
	global mail_pwd
	global mail_postfix
	global g_sender
	global g_server_type
	global g_sender_email
	global g_show_user_name
	global g_have_fix_server

	mail_host = host
	mail_user = user
	mail_pwd = pwd
	mail_postfix = postfix
	g_show_user_name = show_user_name
	server_type = server_type.lower()
	g_server_type = server_type
	if server_type in g_have_fix_server:
		g_sender_email = mail_user
	else:
		g_sender_email = mail_user + "@" + mail_postfix
	# 非QQ企业邮箱：
	g_sender = g_show_user_name+"<"+g_sender_email+">"
	if server_type.lower == "eim":
		# QQ企业邮箱
		g_sender = g_show_user_name+"<"+g_sender_email+">"

def get_user_info():
	info = [
			mail_host,
			mail_user,
			mail_pwd,
			mail_postfix,
			g_show_user_name,
			g_sender_email,
			g_server_type
			]
	return info

def get_sender():
	return g_sender

def get_sender_email():
	return g_sender_email

def set_receivers(receivers):
	global g_receivers
	g_receivers = receivers

def get_receivers():
	return g_receivers

def set_sub(sub):
	global g_sub
	g_sub = sub

def get_sub():
	return g_sub

def set_content(content):
	global g_content
	g_content = content

def get_content():
	return g_content

def set_attachments(attachments):
	global g_attachments
	g_attachments = attachments

def get_attachments():
	return g_attachments

def set_log_path(log_path):
	global g_log_path
	g_log_path = log_path

def get_log_path():
	return g_log_path

def _send_mail(sender, receivers, sub, content, attachments):
	'''''
	receivers:发给谁
	sub:主题
	content:内容
	attachments:附件列表
	send_mail(sender, ["aaa@qq.com",],"sub","content", ["file_path",])
	'''

	msg = MIMEMultipart()
	msg['Subject'] = Header(sub, 'utf-8')
	msg['From'] = Header(sender, 'utf-8')
	msg['To'] = Header(";".join(receivers), 'utf-8')
	msg.attach(MIMEText(content, 'plain', 'utf-8'))

	# 构造附件
	for fl_path in attachments:
		att = MIMEText(open(fl_path, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		att["Content-Disposition"] = 'attachment; filename=' + os.path.basename(fl_path)
		msg.attach(att)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user,mail_pwd)
		s.sendmail(sender, receivers, msg.as_string())
		s.close()
		return True
	except Exception, e:
		print str(e)
		return False

def send_mail2():
	sender = get_sender()
	receivers = get_receivers()
	sub = get_sub()
	content = get_content()
	attachments = get_attachments()
	result = 0
	if _send_mail(sender, receivers, sub, content, attachments):
		result = 1
		ret = "发送成功"
	else:
		result = 0
		ret = "发送失败"
	print ret
	# 记录log
	fl = open(get_log_path(),'a')
	line_ats = 'attachments: '
	if len(get_attachments()):
		line_ats = line_ats + " ; ".join(get_attachments())
	lines = [
		"sender: " + get_sender(),
		"receivers: " + ";".join(get_receivers()),
		"subject: " + get_sub(),
		"len(content): " + str(len(get_content())),
		line_ats,
		"result: " + str(result),
		]
	print_line = "\n".join(lines)
	print print_line
	fl.write(print_line + "\n")
	fl.close()

def send_mail(receivers, sub, content, attachments, backup, log_path):
	if backup:
		receivers.append(get_sender_email())
	set_receivers(receivers)
	set_sub(sub)
	set_content(content)
	set_attachments(attachments)
	set_log_path(log_path)
	send_mail2()

def get_help_info():
	file_name = os.path.basename(__file__)
	help_str = '''
		--help
		-h/--host		<eg: -h smtp.exmail.qq.com>
		-u/--user		<eg: -u xxxx/xxxx@xx.com>
		-p/--pwd		<eg: -p xxxxxxxx>
		-f/--postfix		<eg: -f xx.com>
		-r/--receiver		<eg: -r 12345.xx.com>
		-s/--subject		<eg: -s "Test Email" . Default = Null>
		-c/--content		<eg: -c "This is a test email!" . Default = Null>
		-a/--attachment_file_path	<eg: -a "/home/xx/xxx.txt" . Default = Null>
		-t/--server_type	<eg: -t "EIM". Default = Null>
		-b/--backup		<eg: -b . Default No This Arg! >
		-l/--log_path		<eg: -l "/home/xx/xxx.log" . Default = "./send_mail.log">

		agrv_eg:
			python mail_core.py -h "smtp.qq.com" -u "xyz" -p "qwertyuiop" -f "qq.com" -n "XYZ"
				-s "Test Mail" -c "This is mail content!"
				-a "mail_core.py" -a "send_mail.py" -a "mine_send.py"
				-t "qq" -b -l "./send_mail.log"
	'''
	help_str = "python " + file_name + "\n" + help_str
	return help_str


def main(argv):
	argv_format_short = "h:u:p:f:n:r:s:c:a:t:bl:"
	argv_format_long  = ["host=","user=","pwd=","postfix=",
						"show_user_name=",
						"receiver=","subject=","content=",
						"attachment_file_path=",
						"server_type=","backup",
						"log_path=",
						"help="]
	# 记录log
	now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	now_time = "===========  " + str(now_time)
	argv_str = ''
	for a in argv:
		if len(a):
			if a[0] != '-':
				argv_str = argv_str + '"' + a + '" '
			else:
				argv_str = argv_str + a + ' '
	argv_str_arr = argv_str.split()
	idx = argv_str_arr.index("-p") + 1
	if idx < len(argv_str_arr):
		argv_str_arr[idx] = "******"
	argv_str = " ".join(argv_str_arr)
	lines = [
		now_time,
		argv_str,
		]
	line = '\n'.join(lines)
	print line
	try:
		if not len(argv):
			print get_help_info()
			sys.exit(2)
		opts, args = getopt.getopt(argv,argv_format_short,argv_format_long)
		if(len(args)):
			print "Error: Option not has ", args
			print get_help_info()
			sys.exit(2)
	except getopt.GetoptError:
		print get_help_info()
		sys.exit(2)

	host = ''
	user = ''
	pwd = ''
	postfix = ''
	show_user_name = user
	receivers = []
	subject = ''
	content = ''
	attachments = []
	server_type = ''
	backup = True
	log_path = get_log_path()

	for opt, arg in opts:
		if opt == '--help':
			print get_help_info()
			sys.exit(0)
		elif opt in ("-h", "--host"):
			host = arg
		elif opt in ("-u", "--user"):
			user = arg
		elif opt in ("-p", "--pwd"):
			pwd = arg
		elif opt in ("-f", "--postfix"):
			postfix = arg
		elif opt in ("-n", "--show_user_name"):
			show_user_name = arg
		elif opt in ("-r", "--receiver"):
			receivers.append(arg)
		elif opt in ("-s", "--subject"):
			subject = arg
		elif opt in ("-c", "--content"):
			content = arg
		elif opt in ("-a", "--attachment_file_path"):
			attachments.append(arg)
		elif opt in ("-t", "--server_type"):
			server_type = arg
		elif opt in ("-b", "--backup"):
			backup = True
		elif opt in ("-l", "--log_path"):
			log_path = arg

	#  print host, user, pwd, postfix, show_user_name, server_type
	#  print "receivers=",receivers
	#  print 'subject=', subject
	#  print 'content=', content
	#  print 'attachments=',attachments
	#  print 'backup=',backup
	set_log_path(log_path)
	fl = open(get_log_path(),'a')
	fl.write(line + "\n")
	fl.close()
	print "=========================== "
	set_sender(host, user, pwd, postfix, show_user_name, server_type)
	send_mail(receivers, subject, content, attachments, backup, log_path)

if __name__ == "__main__":
	main(sys.argv[1:])

