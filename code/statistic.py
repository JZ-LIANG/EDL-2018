import os
import pickle
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


ls_entity_type = []
ls_n_document = []
ls_n_sentence = []
ls_n_token = []
ls_n_MISC = []
ls_n_ALL = []


#version
if lannguage == 'en':
    def extract_name(dirpath):
        return dirpath.split('/')[-1]
elif lannguage == 'zh':
        def extract_name(dirpath):
            return dirpath.split('/')[-1][:-4]



for (dirpath, dirnames, filenames) in os.walk(src_directory):
    if dirpath != src_directory:
        type_name = extract_name(dirpath)
        ls_entity_type.append(type_name)
        n_document = 0
        n_sentence = 0
        n_token = 0
        n_MISC = 0
        n_ALL = 0

        for filename in filenames:
            if filename.startswith("_",0,1) and filename.endswith(".html"):
                n_document += 1
                filepath = dirpath +'/'+ filename
                #scrapy the tag
                # soup = BeautifulSoup(open(filepath), "html.parser")
                # lxml is faster
                with open(file_name,'r') as f_read:
                    soup = BeautifulSoup(f_read, "lxml")
                    tag = soup.find_all('p')
                    n_sentence += int(re.findall(r'\d+',tag[0].text)[0])
                    # print(int(re.findall(r'\d+',tag[0].text)[0]))
                    n_token += int(re.findall(r'\d+',tag[1].text)[0])
                    tag = soup.find_all('th',align="left" )[0].find_all('th')
                    n_MISC += int(tag[7].text)
                    n_ALL += int(tag[8].text)

        ls_n_document.append(n_document)
        ls_n_sentence.append(n_sentence)
        ls_n_token.append(n_token)
        ls_n_MISC.append(n_MISC)
        ls_n_ALL.append(n_ALL)


if lannguage == 'en':    
    output_path = des_directory + '/' + 'en_result.txt'
elif lannguage == 'zh':
    output_path = des_directory + '/' + 'zh_result.txt'

with open (output_path, "wb") as fp:
    pickle.dump((ls_entity_type,ls_n_document,ls_n_sentence,ls_n_token,ls_n_MISC,ls_n_ALL), fp)

# print(ls_entity_type)
# print(ls_n_document)
# print(ls_n_sentence)
# print(ls_n_token)
# print(ls_n_MISC)
# print(ls_n_ALL)
# print(len(ls_entity_type),len(ls_n_document),len(ls_n_sentence),len(ls_n_token),len(ls_n_MISC),len(ls_n_ALL))