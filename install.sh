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
done
