import csv

with open('cb_sn_id.csv', 'rb') as f:
    reader = csv.reader(f)
    my_dict = {rows[0]:rows[1] for rows in reader}

with open('serial_room_jx.csv', 'rb') as g:
    reader2 = csv.reader(g)
    my_list = map(tuple, reader2)
 
new_list = []

for i,e in enumerate(my_list):
    serial_number = my_list[i][0]
    this_id = my_dict[serial_number]
    this_tuple = my_list[i]
    this_tuple = list(this_tuple)
    this_tuple.insert(3,this_id)
    this_tuple = tuple(this_tuple)
    new_list.append(this_tuple)
    print this_tuple

with open('new_csv.csv', 'wb') as out:
    csv_out = csv.writer(out)
    csv_out.writerow([])
    for row in new_list:
        csv_out.writerow(row)