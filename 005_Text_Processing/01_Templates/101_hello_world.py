# Jinja2 Hello World example
# create and render the template

from jinja2 import Template

# create a template
t = Template("Hello {{ something }}!")

# render the template
result = t.render(something="World")
print(result)