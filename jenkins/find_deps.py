with open('META-INF', 'r') as f:
    content = f.read()

content_list = content.split()
start = content_list.index('Plugin-Dependencies:') + 1
end = content_list.index('Plugin-Developers:')
dep_string = "".join(content_list[start:end])
print(dep_string.split(','))