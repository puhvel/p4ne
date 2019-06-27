import glob

file_dir = (glob.glob("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\*.txt"))
strings_file = open("C:\\Users\\Dre\\Seafile\\p4ne_training\\config_files\\substrings.txt", 'a')

#for i in file_dir: print(i)

for i_file in file_dir:
    for i_str in i_file:
        j = str(i_file(i_str))
        if j in i_str:
            j = i_str.find("ip address ")

    i_file.close()

# strings.close()
print(strings_file)

# l = [i_string.strip() for line in f]