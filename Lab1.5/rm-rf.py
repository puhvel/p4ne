import glob

files = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
substr_f = list(open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", 'a'))

count=0

for file in files:
    f_open = open(file)
    for line in f_open:
        substr_s = str(line).find("ip address ")
        if substr_s            substr_f.write(substr_s)
    f_open.close()
    substr_f.write("")
    substr_f.write(count+1)

substr_f.close()
print(count)