import glob

files = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
strings_file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", 'a')

# for i in file_dir:
#   print(i)

for file in files:
    f_open = open(file)
    for line in f_open:
        if str(line).find("ip address "):
            strings_file.write()
    f_open.close()
    strings_file.write("")
    count = count + 1

print(count)
