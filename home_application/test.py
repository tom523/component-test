from mako.template import Template
from mako.lookup import TemplateLookup


mytemplate = Template(filename="tpl.txt")

print mytemplate.render(name="jack", x=5)



