from datetime import datetime

#
# def massageData(myline):
#     my_line = myline.replace('"', "")
#     mylist = my_line.split('\t')
#     print(mylist)
#     # print(len(mylist))
#     print(','.join(mylist))
#
# myline = '"US-EAST"	"IAD085CONP05"	"2020-11-09 12:00:00"	""	""	""	"PENDING_PIRP"	"IAD"	"IAD7"	"IAD85"	"CON"	"IAD085CONP05.001"	"2019-09-01 12:00:00"	"2020-08-16"	"Conversion Build"	"2020-11-09"	"2020-08-17 09:04:34.903581"'
# massageData(myline)

with open('myfile.txt', 'r') as f:
    content = f.readlines()


def convert_date_obj(d):
    d_obj = datetime.strptime(d, '%m/%d/%Y')
    return d_obj.strftime("%Y-%m-%d")

def get_date(item, nho, offset):
    i = item
    if not i:
        nho_obj = datetime.strptime(nho, '%Y-%m-%d')
        d_obj = nho_obj
    else:
        d = i.split()[0]
        result = convert_date_obj(d)



def format_csv(line):
    tmp = list()
    myline = line.split(',')
    tmp.extend((myline[9], myline[1]))
    nho = myline[2].split()[0]
    pfho = myline[3]
    freeze = myline[4]
    nea = myline[5]
    tmp.append(convert_date_obj(nho))
    print(myline)
    print(tmp)

# site  fbn nho pfho    change_freeze   nea
i = 0
for line in content:
    if i == 0:
        i = i + 1
        continue
    format_csv(line)
    i = i + 1
    break
