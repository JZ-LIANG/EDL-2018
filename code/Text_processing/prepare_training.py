# this file use to convert thte 5 fold conll RPI_blender 2018 data to the format need by NeuroNER

import os

def space2tab (data_path, tab_path,entity_name):
    files = os.listdir(data_path)
    new_tab_path = tab_path + entity_name + '/'
    if not os.path.exists(new_tab_path):
        os.makedirs(new_tab_path)    
    if len(files) == 5:
        for file in files:
            r_file_path = data_path + '/' + file
            w_file_path = new_tab_path + file[-11:]
            with open(r_file_path, 'r') as r_file, open(w_file_path, 'w+') as w_file:
                lines = r_file.readlines()
                for line in lines:
                    if line in ['\n', '\r\n']:
                        w_file.write('\n')
                    else:
                        token,_,_,_, label = line.split(' ')
                        new_line = token + ' ' + label
                        w_file.write(new_line)
    return new_tab_path

def convert2NeuroNER_format(src_path, dst_path, entity_name):
    train_conll = ['fold1.conll','fold2.conll','fold0.conll','fold4.conll']
    valid_conll = 'fold3.conll'
    new_NeuroNER_path = dst_path + entity_name + '/'
    if not os.path.exists(new_NeuroNER_path):
        os.makedirs(new_NeuroNER_path)
    train_file = new_NeuroNER_path + 'train.txt'
    valid_file = new_NeuroNER_path + 'valid.txt'
    with open (train_file, 'w+') as w_file:
        for file in train_conll:
            r_file_path = src_path + '/' + file
            with open(r_file_path, 'r') as r_file:
                w_file.write("-DOCSTART- -X- -X- O\n\n")
                w_file.write(r_file.read())
    r_file_path = src_path + '/' + valid_conll
    with open (valid_file, 'w+') as w_file, open(r_file_path, 'r') as r_file:
        w_file.write("-DOCSTART- -X- -X- O\n\n")
        w_file.write(r_file.read())


data_path = 'data/'
result_path_NeuroNER = 'result/NeuroNER/'
result_path_tab = 'result/tab/'

for (dirpath, dirnames, filenames) in os.walk(data_path):
    if len(filenames) == 5:
        entity_name = dirpath.split('/')[1]
        tab_path = space2tab(dirpath, result_path_tab, entity_name)
        convert2NeuroNER_format(tab_path, result_path_NeuroNER, entity_name)
