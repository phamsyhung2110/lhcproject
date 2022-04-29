from distutils.command.config import config
from multiprocessing.sharedctypes import Value
import os,fnmatch,shutil,re,argparse
from traceback import format_list
import yaml
import yaml.reader

# src_file = "C:/Users/hung/Desktop/Devops/k8s/lhc-template/conf/nginx/site-nodejs-template.conf"
# des_file = "site-nodejs-template.conf"
# shutil.copy2(src_file, des_file)
def get_value():
    with open('value.yaml', "r+") as file:
        conf = yaml.safe_load(file)   
        data = conf.get("config")
        print(data)
    #     for key in data:
    #         value = data.get(key)
    # with open("value2.yaml", "r+") as file2:
    #     conf2 = yaml.safe_load(file2)   
    #     data2 = conf2.get("config")
    #     for key2 in data2:
    #         value2 = data2.get(key2)
    # with open("value.yaml", "r+") as file:
    #     file_contents = file.read()
    #     file_contents = re.sub(str(value), str(value2)  , file_contents )
    #     file.seek(0)
    #     file.truncate()
    #     file.write(file_contents)    
    # print(value,value2)
        
                     
get_value() 
