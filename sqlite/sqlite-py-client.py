import sqlite3
from pprint import pprint

con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()

cursor.execute("select sqlite_version();")
record = cursor.fetchall()
print(record)

cursor.execute("PRAGMA database_list;")
record = cursor.fetchall()
print(record)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
record = cursor.fetchall()
print(record)

# dcb_project
table_name = 'dcb_project'
cursor.execute(f"PRAGMA table_info({table_name})")
record = cursor.fetchall()
print(record)

# id, fbn, scaling_fbn, tpm, svcRack_ChangeFreeze, nea, nho, site, pfho
cursor.execute(f"SELECT * from {table_name}")
record = cursor.fetchall()
pprint(record)

# site  fbn scaling_fbn tpm  change_freeze nea  pfho    nho
with open('input.csv', 'r') as f:
    content = f.readlines()

for line in content:
    my_str = line
    lst = my_str.split(',')
    query = f"INSERT into {table_name} (site, fbn, scaling_fbn, tpm, svcRack_ChangeFreeze, nea, pfho, nho) " \
            f"VALUES ('{lst[0]}', '{lst[1]}', '{lst[2]}', '{lst[3]}', '{lst[4]}', '{lst[5]}', '{lst[6]}', '{lst[7]}')"
    # print(query)
    try:
        cursor.execute(query)
    except sqlite3.IntegrityError:
        continue
    con.commit()
    record = cursor.fetchall()
    print(record)

if con:
    con.close()
