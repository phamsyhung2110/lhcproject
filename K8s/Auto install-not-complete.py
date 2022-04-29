from doctest import NORMALIZE_WHITESPACE
from hashlib import new
from importlib.resources import path
from logging import root
from msilib.schema import File
import os,shutil,glob,sys,re
from pydoc import describe
import subprocess
import fnmatch,yaml,jinja2
from unicodedata import name
from jinja2 import Template

# action = sys.argv[1] 
# app_name = sys.argv[2]
# env = sys.argv[3]  
# mode_nginx = sys.argv[4]
app_name = "Helm app"
# new_name = str(app_name + "-values-" + env + ".yaml")  
# find_j2_value = glob.glob("*%s*.j2"%env)
# find_j2_nginx = glob.glob("*.conf.j2")
#### Find the app directory and move to it ###
# def get_root_app():
pattern = app_name
def get_root_app():
    for root, dirs, files in os.walk(r"././"):
        for dirname in fnmatch.filter(dirs, pattern):
            path_app = os.path.join(root,dirname) # Path from specified directory
            root_app = os.path.abspath(path_app)  # Path from root directory
            parent = os.path.abspath(os.curdir)
            print("App directory: " + root_app)
            print("Parent directory: " + parent)
            return root_app
get_root_app()
def get_input_file():
    pattern = "input.yaml"
    for root,dir,file in os.walk(r"C:/Users/hung/Desktop/Devops/K8s/"):
        for file_name in fnmatch.filter(file,pattern):
            # global file_locate 
            path_input_file = os.path.join(root,file_name)
            file_locate = os.path.abspath(path_input_file)
            return file_locate
app_folder = str(get_root_app())
input_file = str(get_input_file())
## Get input from input file
def get_input_sample():
    global input_file
    with open(input_file, 'r', encoding='UTF-8') as file:
        return file.read()

def change_nginx(name_template):
    global app_folder
    os.chdir(app_folder)
    ## Split j2 tail ##
    name_split = name_template.split(".j2")[0]
    def save_nginx(out_put):                                  ## Save output rendered
        with open(name_split , 'w', encoding='UTF-8') as file:
            return file.write(out_put)                        ## Get template
    def get_template_nginx(name_template):
        with open(name_template , 'r', encoding='UTF-8') as file:
            return file.read()
    input = yaml.safe_load(get_input_sample())
    nginx_template = get_template_nginx(name_template)
    template = Template(nginx_template)
    out_put = template.render(**input)
    save_nginx(out_put)
    

def change_values_file(name_template):
    global app_folder
    os.walk(app_folder)
    name_split = name_template.split(".j2")[0]
    def save_values(out_put):
        with open(name_split, 'w', encoding='UTF-8') as file:
            file.write(out_put)    
    def get_template_values(name_template):
        with open(name_template , 'r', encoding='UTF-8') as file:
            return file.read()    
    input = yaml.safe_load(get_input_sample())
    template_input = get_template_values(name_template)
    template_values = Template(template_input)
    out_put = template_values.render(**input)
    save_values(out_put)
    return name_split
# def change_run(name_template):
#     for dir in os.listdir(app_folder):
#         if dir=="run" :
#             os.chdir(dir)

### Install ###
def install():  
    global env, action, app_name, new_name, app_folder
    os.chdir(app_folder)  
    for dir in os.listdir(app_folder):
        if dir=="run" :
            print("Found run folder")
            print("Executing command: kubectl apply -f %s"%dir) 
            subprocess.call("kubectl apply -f ./%s/"%dir)
    ## Action
    print("Executing command: helm " + action + " " + app_name + " .  -f " + "%s-values-%s.yaml"%(app_name,env) )
    subprocess.call("helm " + action + " " + app_name + " .  -f " + "%s-values-%s.yaml"%(app_name,env)) 
print("App directory: " + app_folder)

os.chdir(app_folder)
find_j2_value = glob.glob("*%s*.j2"%env)
find_j2_nginx = glob.glob("*.conf.j2")
if mode_nginx=="--mod-nginx": 
    for conf_file in find_j2_nginx:
        print("Nginx config file: %s"%conf_file)
        change_nginx(conf_file)
elif mode_nginx=="--no-mod-nginx":
        print("No modify nginx config")
for name_tempate in find_j2_value:
    print(*input_file.split(" "))
    print("Value file template: %s"%name_tempate)
    change_values_file(name_tempate)
    install() 
           
         
                    
                    
                    



















