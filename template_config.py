#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2016 All rights reserved.
#
#   Author        : bbxytl
#   Email         : bbxytl@gmail.com
#   File Name     : config.py
#   Last Modified : 2016-08-31 19:40
#   Describe      :
#
#   Log           :
#
# ====================================================

#  import sys
import os

config_data = {
# host="TODO: 填写SMTP, eg:smtp.xxx.com"
	# "host":"smtp.exmail.qq.com"
	# 编号从 1 开始
	# postfix="TODO:改成邮箱后缀,eg: gamil.com"
	# "postfix":"175game.com" ,
	# server_type='TODO: 如果是user中需要带@的全称的，此处为 eim， 否则，为邮箱后缀'
	# "server_type" : "eim" ,
	"host":{
		1: {"server_type":"eim", "postfix": "175game.com", "host": "smtp.exmail.qq.com"},
		2: {"server_type":"163", "postfix": "163.com", "host": "smtp.163.com" },
		3: {"server_type":"126", "postfix": "126.com", "host": "smtp.126.com" },
		4: {"server_type":"qq",  "postfix": "qq.com", "host": "smtp.qq.com" },
	},
# user="TODO: 改成自己的邮箱,eg: xyz@gmail.com"
	"user":""
	,
# show_user_name = "TODO: 改成自己的名字"
	"show_user_name" : ""
	,
# pwd="TODO:改成自己的密码"
	"pwd":""
	,
# 是否备份邮件(发给自己一份)
	"backup" : 0
	,
# 默认的收件人列表
	"receivers" : [
			# TODO:添加收件人 eg: "xxxx@gmail.com",
			]
	,
# 邮件log
	"log_path" : os.path.dirname(os.path.abspath(__file__)) + '/send_mail.log'
}

def get_config():
	# 默认内容
	# config_data["subject"] = "subject:_from:" + config_data["show_user_name"] + "(" + config_data["user"] + ")"
	# config_data["content"] = "Content____"
	return config_data
