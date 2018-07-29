#!/usr/bin/python
import os
import sys
from bs4 import BeautifulSoup


# the directory argument should go to '/~panx2/tmp/typing/zh' or '/~panx2/tmp/typing/en'
# directory = '/Users/liangjianzhong/Desktop/internship/rpi_7k/~panx2/tmp/typing/zh'
if len(sys.argv) != 4:
	print('the arguments format is (src_directory, des_directory, lannguage)')
	print('for example: (../~panx2/tmp/typing/zh, ../ouput, zh)')
	exit()

src_directory = sys.argv[1]
des_directory = sys.argv[2]
lannguage = sys.argv[3]




def write_conll_zh(src_dirpath,filenames):
    file_name = src_dirpath + '/' + filenames
    type_name = src_dirpath.split('/')[-1][:-4]
    writed_file_name = des_directory + '/' + type_name + '.conll'
    with open(file_name,'r') as f_read, open(writed_file_name, 'w+') as f_write:
        content = f_read.read().splitlines()
        print(type_name)
        for line in content:
            if line:
                token,temp,entity_type = line.split()
                if entity_type != 'O':
                    entity_type = entity_type[:2] + type_name
                output_line = token + "    " + entity_type + '\n'
#                 output_line =line.split()[0]+ "    " +line.split()[2] + '\n'
    
                f_write.write(output_line)
            else:
                f_write.write('\n')


# directory = '/Users/liangjianzhong/Desktop/internship/rpi_7k/~panx2/tmp/typing/zh'
if lannguage == 'zh':
	for (dirpath, dirnames, filenames) in os.walk(src_directory):
	    if 'dev.bio' in filenames:
	        # write_conll_zh(dirpath, 'dev.bio')
	        print(dirpath)
	        writed_file_name = des_directory + '/' + type_name + '.conll'
	        with open(writed_file_name, 'w+') as f_write:
	        	f_write.write(dirpath)

elif lannguage == 'en':
	for (dirpath, dirnames, filenames) in os.walk(src_directory):
	    if 'dev.bio' in filenames:
	        # write_conll_en(dirpath, 'dev.bio')
	        print(dirpath)
