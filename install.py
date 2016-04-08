#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-04 23:48
# @Author  : Alexa (AlexaZhou@163.com)
# @Link    : https://github.com/alexazhou/VeryNginx
# @Disc    : install VeryNginx

import os
import sys
import getopt

openresty_pkg_url = 'https://openresty.org/download/openresty-1.9.7.3.tar.gz'
openresty_pkg = 'openresty-1.9.7.3.tar.gz'

def main():

    work_path = os.curdir

    #check if the old version of VeryNginx installed
    if os.path.exists('/opt/VeryNginx/VeryNginx') == True:
        print("Seems that a old version of VeryNginx was installed in /opt/VeryNginx/...\nBefore install, please delete it and backup the configs if you need.")
        return
    
    #makesure the dir is clean
    print('### makesure the work directory is clean')
    os.system('rm ' + openresty_pkg)
    os.system('rm -rf ' + openresty_pkg.replace('.tar.gz',''))
    
    #download openresty
    print('### start download openresty package...')
    os.system( 'wget ' + openresty_pkg_url )
    
    print('### release the package ...')
    os.system( 'tar -xzf ' + openresty_pkg )

    #configure && compile && install openresty
    print('### configure openrestry ...')
    os.chdir( openresty_pkg.replace('.tar.gz','') )
    os.system( './configure --prefix=/opt/verynginx/openrestry --user=nginx --group=nginx --with-http_stub_status_module --with-luajit' )
    
    print('### compile openrestry ...')
    os.system( 'make' )
    
    print('### install openrestry ...')
    os.system( 'make install' )

    #install VeryNginx file
    print('### copy VeryNginx files ...')
    os.chdir( work_path )
    os.system( 'cp ./verynginx /opt/verynginx/verynginx' )


if __name__ == '__main__':
    help_doc = 'usage: install.py <cmd> ... \n\
    install\n\
        all        :  install verynginx and openresty\n\
        openresty  :  install openresty\n\
        verynginx  :  install verynginx\n\
    update\n\
        verynginx  :  update the installed verynginx\n\
    '

    opts, args = getopt.getopt(sys.argv[1:], '', []) 
    
    print( help_doc )
    
    main()

else:
    print ('install.py had been imported as a module')
