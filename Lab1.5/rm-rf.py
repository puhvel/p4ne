import glob

files = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
strings_file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", 'a')

# for i in file_dir:
#   print(i)

count=0

for file in files:
    f_open = open(file)
    for line in f_open:
        for str_find in line:
            str(line).find("ip address ")==True:
                strings_file.write(str_find)
    f_open.close()
    strings_file.write("")
    count=count+1

strings_file.close()
print(count)
