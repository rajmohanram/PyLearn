from datetime import datetime


with open('prizm_dates.txt', 'r') as f:
    content = f.readlines()

def convert_date_obj(d):
    d_obj = datetime.strptime(d, '%m/%d/%y')
    return d_obj.strftime("%Y-%m-%d")

def format_csv(line):
    tmp = list()
    myline = line.split(',')
    tmp.extend((myline[6], myline[2], myline[3], myline[1]))
    freeze = convert_date_obj(myline[17])
    nea = convert_date_obj(myline[14])
    pfho = convert_date_obj(myline[13])
    nho = convert_date_obj(myline[12])
    tmp.extend((freeze, nea, pfho, nho))

    print(','.join(tmp))

# site  fbn scaling_fbn tpm  change_freeze nea  pfho    nho
i = 0
for line in content:
    # print(i)
    if i == 0:
        i = i + 1
        continue
    tmp = line.split(',')
    # print(tmp)
    if not tmp[12] or not tmp[13] or not tmp[14] or not tmp[17]:
        continue
    else:
        format_csv(line)
    i = i + 1

