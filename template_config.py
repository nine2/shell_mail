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
	# 如果只使用一个邮箱，可以将其他的邮箱类型注释掉，也可以在后面添加除这四种以外的其他邮箱
	"host":{
		1: {"server_type":"eim", "postfix": "175game.com", "host": "smtp.exmail.qq.com"},
		2: {"server_type":"163", "postfix": "163.com", "host": "smtp.163.com" },
		3: {"server_type":"126", "postfix": "126.com", "host": "smtp.126.com" },
		4: {"server_type":"qq",  "postfix": "qq.com", "host": "smtp.qq.com" },
	},
	# user="TODO: 改成自己的邮箱, @前面的部分 ,eg: 完整邮箱为:xyz@gmail.com，user 填写 xyz"，
	# 在 host 开启了 2，3，4 时，这里最好不填
    # 如："user":"tl0485"
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
# 个人目录下可修改此 log 目录
	"log_path" : os.environ["HOME"] + '/.mail_send.log'
}

def get_config():
	# 默认内容
	# config_data["subject"] = "subject:_from:" + config_data["show_user_name"] + "(" + config_data["user"] + ")"
	# config_data["content"] = "Content____"
	return config_data
