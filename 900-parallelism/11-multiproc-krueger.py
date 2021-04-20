from multiprocessing import Pool
import subprocess


def execute_cmds(cmd):
    process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode == 0:
        if "successfully unshut" in process.stdout:
            tmp = cmd.split()
            print(f'\n{tmp[2]} {tmp[3]}')


def pool_handler():
    p = Pool(4)
    p.map(execute_cmds, unshut_ports)


if __name__ == '__main__':
    unshut_ports = []
    row = '5'
    for device in range(1, 17):
        for port in range(1, 5):
            unshut_ports.append(f"krueger unshut nrt55-69-es-e1-s{row}-r{device} jrp30-{port} 0526726305 --no-narg")

    pool_handler()
