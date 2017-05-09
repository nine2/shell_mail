#!/bin/bash
# ====================================================
#   Copyright (C)2016 All rights reserved.
#
#   Author        : bbxytl
#   Email         : bbxytl@gmail.com
#   File Name     : install.sh
#   Last Modified : 2016-08-31 22:59
#   Describe      :
#
#   Log           :
#
# ====================================================

ls template_*.py | while read fl;do
	out=${fl##template_}
	cp $fl $out
	chmod +x $out
	cp config.py $HOME/.mail_config.py
	touch $HOME/.mail_emails
done

cur_dir=`pwd`
BIN=$cur_dir/bin
mkdir -p $BIN
args='$@'
home='$HOME'
echo "python $cur_dir/send_define.py $args" > $BIN/mailsend.sh
echo "cp ./config.py  $home/.mail_config.py; touch $home/.mail_emails" > $BIN/mailconfig.sh
echo "cat $home/.mail_emails" > $BIN/catemail.sh
echo "echo $args >> $home/.mail_emails" > $BIN/addemail.sh
chmod +x $BIN/mailsend.sh $BIN/mailconfig.sh $BIN/catemail.sh $BIN/addemail.sh

localbin="$HOME/.local/bin"
# localbin=/usr/local/bin
if [ ! -d $localbin ];then
	mkdir -p $localbin
fi
mkdir -p $localbin/rm_bk
for i in $localbin/mailsend $localbin/mailconfig $localbin/catemail $localbin/addemail;
do
	[ -e $i ] && [ -L $i ] && unlink $i;
	[ -e $i ] && mv $i $localbin/rm_bk;
done
ln -s $BIN/mailsend.sh $localbin/mailsend
ln -s $BIN/mailconfig.sh $localbin/mailconfig
ln -s $BIN/catemail.sh $localbin/catemail
ln -s $BIN/addemail.sh $localbin/addemail

echo "PATH=$localbin/bin:$PATH"  >> $HOME/.bashrc
echo "export PATH"  >> $HOME/.bashrc
source "$HOME/.bashrc"
