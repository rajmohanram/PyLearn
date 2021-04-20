with open('testfile', 'r') as f:
    all_modules = f.read().splitlines()

with open('default_modules', 'r') as f:
    default_modules = f.read().splitlines()

modules_list = []

for item in all_modules:
    if item.startswith('mod_'):
        item = item.replace('mod_', '')
        item = item.replace('.c', '')
        item = item.replace('.h', '')
        item = item.replace('.dsp', '')
        item = item.replace('.exp', '')
        item = item.replace('.def', '')
        if item not in modules_list:
            if item not in default_modules:
                modules_list.append(item)

print(len(modules_list))
print(modules_list)

for item in modules_list:
    print(item)

print(" ".join(sorted(modules_list)))

