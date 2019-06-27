import glob

files = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
substrings_file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", 'a')
c=0
for file in files:
    f = open(file)
    c=c+1
    for line in f:
        sub_str = line.find('ip address ')
        if sub_str:
            substrings_file.write(line)
    f.close()

print(c)
#substrings.write(sub_str)
