import glob

files = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
substrings_file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\substrings.txt",'r+')

for file in files:
    f = open(file)
    for line in f:
        sub_str = line.find('ip address ')
        if sub_str != -1:
            substrings_file.write(line)
    f.close()

mylist = []
substrings_file.seek(0)

for i in substrings_file: mylist.append[i]
print(mylist)


#убрать лишние и повторяющиеся значения из собраных данных
#сортировать по ip и маске