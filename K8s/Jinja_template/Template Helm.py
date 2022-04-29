import yaml,json
import yaml
import jinja2
from jinja2 import Template,loaders,FileSystemLoader,Environment

def get_input_sample():
        with open("input.yaml", 'r', encoding='UTF-8') as file:
            return file.read()

def change_nginx():
    def save_nginx(out_put):
        with open("nginx-jinja.conf", 'w', encoding='UTF-8') as file:
            return file.write(out_put)
    def get_template_nginx():
        with open("site-nodejs-template.j2", 'r', encoding='UTF-8') as file:
            return file.read()
    # yaml1 = yaml.dump(get_input_sample(),ff, allow_unicode=True)
    input = yaml.safe_load(get_input_sample())
    nginx_template = get_template_nginx()
    template = Template(nginx_template)
    out_put = template.render(**input)
    save_nginx(out_put)

def change_values_file():
    def save_values(out_put):
        with open("values-lhc-prod.yaml", 'w', encoding='UTF-8') as file:
            file.write(out_put)
    def get_template_values():
        with open("values-lhc-prod.j2", 'r', encoding='UTF-8') as file:
            return file.read()    
    input = yaml.safe_load(get_input_sample())
    template_input = get_template_values()
    template_values = Template(template_input)
    out_put = template_values.render(**input)
    save_values(out_put)
change_nginx()
change_values_file()

# file_loader = FileSystemLoader("k8s")
# env = Environment(loader=file_loader)
# template = env.get_template("template.txt")