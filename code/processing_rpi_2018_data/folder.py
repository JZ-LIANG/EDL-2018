
def five_folds(dirpath, filename):
    file_path = dirpath + '/' + filename
    type_name = filename.split('.')[0]
    with open(file_path,"rb") as f_read:
        lt_doc = f_read.readlines()
    line_indeice = [i for i,x in enumerate(lt_doc) if x == b'\n']
    n_line = len(line_indeice) - 1
    index_location = cut_location(n_line)
    ls_files_path = create_directory(type_name)
    
    with open(ls_files_path[0], "wb+") as f_write:
        f_write.write(b''.join(lt_doc[0:line_indeice[index_location[1]]]))
        f_write.write(b'\n')
    with open(ls_files_path[1], "wb+") as f_write:
        f_write.write(b''.join(lt_doc[line_indeice[index_location[1]]+1:line_indeice[index_location[2]]]))
        f_write.write(b'\n')    
    with open(ls_files_path[2], "wb+") as f_write:
        f_write.write(b''.join(lt_doc[line_indeice[index_location[2]]+1:line_indeice[index_location[3]]]))
        f_write.write(b'\n')    
    with open(ls_files_path[3], "wb+") as f_write:
        f_write.write(b''.join(lt_doc[line_indeice[index_location[3]]+1:line_indeice[index_location[4]]]))
        f_write.write(b'\n')
    with open(ls_files_path[4], "wb+") as f_write:
        f_write.write(b''.join(lt_doc[line_indeice[index_location[4]]+1:line_indeice[index_location[5]]]))
        f_write.write(b'\n')    





def create_directory (type_name):
    
    # create folder
    root_path = '/Users/liangjianzhong/Desktop/internship/folded_rpi/'
    directory = root_path + type_name + '/'
    try:
        os.makedirs(directory)
    except:
        print("error in create directory, program exit")
        exit()
   
    # create fold file name
    ls_files_path = []
    for i in range(5):
        ls_files_path.append(directory + type_name +'_' + 'fold{}'.format(i) + '.conll')
        
    return ls_files_path


def cut_location(n_line):
    cut_location = [int(n_line*(i+1)/5) for i in range(4)]
    cut_location.append(-1)
    cut_location = [-1] + cut_location
    return cut_location

