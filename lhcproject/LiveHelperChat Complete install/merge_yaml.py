import subprocess
import os,re
os.chdir(r"C:/Users/hung/Desktop/Devops/K8s/Live Helper Chat Project/lhcproject/LiveHelperChat Complete install/lhc/templates")
files = subprocess.call("ls")
list = []
for file in files:
    if re.match(r"dpl-*\.yaml", "rw"):
        list.append(file)
        with open(r"dpl-nginx-lhc.yaml") as filename:
        #x = "---".join(list)
        subprocess.run("cat" + list + ">>","deploymentall.yaml")
