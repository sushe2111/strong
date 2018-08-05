#from .test1 import ceshi
import tornado.web

#print(ceshi)

import os

import tornado.options
from tornado.options import define, options
'''
print("__file__",__file__)
print("dirname", os.path.dirname(__file__))
print("asdf",os.path.join(os.path.dirname(__file__),"asdf" ) )

print("__abspath__",os.path.abspath(".") )

print("split",os.path.split(os.path.realpath(__file__)) )
print("realpath",os.path.realpath(__file__) )
'''
#tornado.options.parse_config_file( os.path.abspath(".") + "/ttt.conf")
#print( os.path.abspath(".") + "/ttt.conf")

#print(options.port)

#print(options._options)

import hashlib
md5 = hashlib.md5()
md5.update('1'.encode(encoding='UTF-8')  )
print(md5.hexdigest())
