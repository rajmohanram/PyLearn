from pprint import pprint
import subprocess

# https://queirozf.com/entries/python-3-subprocess-examples

cmd = '/apollo/env/HerculesConfigDownloader/bin/hercules-config get --hostname nrt55-69-np-cor-r101 released@latest --file all.live --save nrt55-69-np-cor-r101.txt'

devices_list = [
    'nrt55-69-es-c1-b1-t2-r1',
    'nrt55-69-es-c1-b1-t2-r2',
    'nrt55-69-es-c1-b1-t2-r3',
    'nrt55-69-es-c1-b1-t2-r4',
    'nrt55-69-es-c1-b1-t2-r5',
    'nrt55-69-es-c1-b1-t2-r6',
    'nrt55-69-es-c1-b1-t2-r7',
    'nrt55-69-es-c1-b1-t2-r8',
    'nrt55-69-es-c1-b1-t2-r9',
    'nrt55-69-es-c1-b1-t2-r10',
    'nrt55-69-es-c1-b1-t2-r11',
    'nrt55-69-es-c1-b1-t2-r12',
    'nrt55-69-es-c1-b1-t2-r13',
    'nrt55-69-es-c1-b1-t2-r14',
    'nrt55-69-es-c1-b1-t2-r15',
    'nrt55-69-es-c1-b1-t2-r16'
]

for device in devices_list:
    cmd = f'echo {device}'
    process = subprocess.run('pwd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # print(process)
    # CompletedProcess(args='echo nrt55-69-es-c1-b1-t2-r1', returncode=0, stdout=b'nrt55-69-es-c1-b1-t2-r1\n', stderr=b'')
    # CompletedProcess(args='echho nrt55-69-es-c1-b1-t2-r1', returncode=127, stdout=b'', stderr=b'/bin/sh: echho: command not found\n')

    if process.returncode == 0:
        print(process.stdout)
    else:
        print(process.stderr)