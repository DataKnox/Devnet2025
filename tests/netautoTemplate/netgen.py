# netgen.py
from jinja2 import Template

def generate_interface_config(interface_data):
    template_str = """
interface {{ name }}
 description {{ description }}
 ip address {{ ip_address }} {{ subnet_mask }}
 no shutdown
"""
    template = Template(template_str.strip())
    return template.render(interface_data)
