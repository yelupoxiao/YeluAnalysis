import json
import re
import os
import requests

# 创建图片存储文档
query = '周星驰'
path = os.getcwd()
picpath = path + '/' + query
print(picpath)
if not os.path.isdir(picpath):
    os.mkdir(picpath)
