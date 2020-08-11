with open('myfile.txt', 'r') as f:
    content = f.readlines()

print(content)
print(len(content))

new_content = []
i = 0
for item in content:
    if i % 2 == 0:
        tmp = item.rstrip('\n')
    if i % 2 != 0:
        tmp = item.lstrip('\t')
        tmp = item.replace('\t\t', '\t')
    new_content.append(tmp)
    i = i + 1

print(new_content)
print(len(new_content))

final_content = []
while len(new_content) != 0:
    tmp_list = [new_content[0], new_content[1]]
    final_content.append(''.join(tmp_list))
    new_content.pop(0)
    new_content.pop(0)

for item in final_content:
    line = item.rstrip('\n')
    print(line)