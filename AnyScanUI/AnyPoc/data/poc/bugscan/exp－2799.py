#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = 奶权
#_PlugName_ = 五车图书管系统WEB路径泄露
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-0128686
import re
def assign(service, arg):
    if service == '5clib':
        return True, arg
def audit(arg):
    payload = '5clib/property.action'
    target = arg + payload
    
    code, head, res, errcode, _ = curl.curl2(target);
    if code == 200 and 'DEFAULT_PDF_LIB_PATH' in res and 'DEFAULT_SQL_BACKUP_PATH' in res:
        security_warning(target)

        return arg
if __name__== '__main__':
    from dummy import *
