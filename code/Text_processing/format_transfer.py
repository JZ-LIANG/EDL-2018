# the origin file separate 4 whitespace, new with tab
# the origin file one empty line between two sentence, new remove those empty line

src_directory = '/home/liang/internship/stanford_NER/data/rpi_5_folds'
dst_directory = '/home/liang/internship/stanford_NER/data/rpi_5_fold_NER'

def tranfer_format(input_file, output_file):
    with open(input_file,'r') as r_file, open(output_file,'w+') as w_file:
        lines = r_file.readlines()
        for line in lines:
            if line == '\n':
                pass
            else:
                token, label = line.split('    ')
                new_line = token + '\t' +label
                w_file.write(new_line)
        new_line = '\n'
        w_file.write(new_line)
#     print('document: ', document)


for (dirpath, dirnames, filenames) in os.walk(src_directory):
    if filenames[0][-5:] == 'conll':
        # make new directory
        entity_name = filenames[0][:-12]
        new_directory = dst_directory + '/' + entity_name
        os.makedirs(new_directory)
        for filename in filenames:
            foldname = filename[:-6]
            input_file_path = dirpath + '/' + filename
            output_file_path = new_directory + '/' + foldname + '.tsv'
            tranfer_format(input_file_path, output_file_path)
            
