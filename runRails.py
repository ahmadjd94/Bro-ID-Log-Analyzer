#!/usr/bin/python3
import os
os.chdir(os.getcwd()+"/front/BILA/")
print (os.getcwd())
os.system('ruby -v')
os.system('rails s -p 9497')