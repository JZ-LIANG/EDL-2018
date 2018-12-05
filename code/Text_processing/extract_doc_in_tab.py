
# coding: utf-8

# In[2]:


import os
from shutil import copyfile


# In[8]:


# find the doc in tab
def etract_tab_filenames(dirpath):
    set_file = set()
    with open(dirpath, 'r') as f_read:
        content =f_read.read().splitlines()
        for line in content:
            token = line.split('\t')
            set_file.add(token[3].split(':')[0])
    return(set_file)
        
path_root = '/home/liang/internship/golden2conll/'
path_doc = path_root + 'LDC2017E25_TAC_KBP_2017_Evaluation_Source_Corpus_V1.1/data/'    
path_tab = path_root + 'LDC2017E52_TAC_KBP_2017_Entity_Discovery_and_Linking_Evaluation_Gold_Standard_Entity_Mentions_and_Knowledge_Base_Links/data/tac_kbp_2017_edl_evaluation_gold_standard_entity_mentions.tab'    
path_en_df = path_root +'doc_in_tab/2017_eval/EN_DF/'
path_zh_df = path_root +'doc_in_tab/2017_eval/ZH_DF/'
path_es_df = path_root +'doc_in_tab/2017_eval/ES_DF/'
path_en_nw = path_root +'doc_in_tab/2017_eval/EN_NW/'
path_zh_nw = path_root +'doc_in_tab/2017_eval/ZH_NW/'
path_es_nw = path_root +'doc_in_tab/2017_eval/ES_NW/'



ls_tab = etract_tab_filenames(path_tab)


for (dirpath, dirnames, filenames) in os.walk(path_doc):
        if filenames:
            if filenames[0][-3:] == 'xml':
                for filename in filenames:
                    doc_name = filename[:-4]
                    if doc_name in ls_tab:
                        doc_category = doc_name[:6]
                        src_filepath = dirpath + '/'+ filename
                        if doc_category == 'CMN_DF':
                            dst_filepath = path_zh_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'CMN_NW':
                            dst_filepath = path_zh_nw + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'SPA_DF':
                            dst_filepath = path_es_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'SPA_NW':
                            dst_filepath = path_es_nw + filename
                            copyfile(src_filepath, dst_filepath)                    
                        elif doc_category == 'ENG_DF':
                            dst_filepath = path_en_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'ENG_NW' or doc_category == 'NYT_EN':
                            dst_filepath = path_en_nw + filename
                            copyfile(src_filepath, dst_filepath)
                        else:
                            print('error: encounter unkonw doc category:', doc_name)
                            exit()

    
    
    
    


# In[9]:


# find the doc in tab
def etract_tab_filenames(dirpath):
    set_file = set()
    with open(dirpath, 'r') as f_read:
        content =f_read.read().splitlines()
        for line in content:
            token = line.split('\t')
            set_file.add(token[3].split(':')[0])
    return(set_file)
        
path_root = '/home/liang/internship/golden2conll/'
path_doc = path_root + 'LDC2017E03_TAC_KBP_Entity_Discovery_and_Linking_Comprehensive_Training_and_Evaluation_Data_2014-2016_V1.1/data/2016/eval/source_documents/' 
path_tab = path_root + 'LDC2017E03_TAC_KBP_Entity_Discovery_and_Linking_Comprehensive_Training_and_Evaluation_Data_2014-2016_V1.1/data/2016/eval/tac_kbp_2016_edl_evaluation_gold_standard_entity_mentions.tab'    
path_en_df = path_root +'doc_in_tab/2016_eval/EN_DF/'
path_zh_df = path_root +'doc_in_tab/2016_eval/ZH_DF/'
path_es_df = path_root +'doc_in_tab/2016_eval/ES_DF/'
path_en_nw = path_root +'doc_in_tab/2016_eval/EN_NW/'
path_zh_nw = path_root +'doc_in_tab/2016_eval/ZH_NW/'
path_es_nw = path_root +'doc_in_tab/2016_eval/ES_NW/'



ls_tab = etract_tab_filenames(path_tab)


for (dirpath, dirnames, filenames) in os.walk(path_doc):
        if filenames:
            if filenames[0][-3:] == 'xml':
                for filename in filenames:
                    doc_name = filename[:-4]
                    if doc_name in ls_tab:
                        doc_category = doc_name[:6]
                        src_filepath = dirpath + '/'+ filename
                        if doc_category == 'CMN_DF':
                            dst_filepath = path_zh_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'CMN_NW':
                            dst_filepath = path_zh_nw + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'SPA_DF':
                            dst_filepath = path_es_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'SPA_NW':
                            dst_filepath = path_es_nw + filename
                            copyfile(src_filepath, dst_filepath)                    
                        elif doc_category == 'ENG_DF':
                            dst_filepath = path_en_df + filename
                            copyfile(src_filepath, dst_filepath)
                        elif doc_category == 'ENG_NW' or doc_category == 'NYT_EN':
                            dst_filepath = path_en_nw + filename
                            copyfile(src_filepath, dst_filepath)
                        else:
                            print('error: encounter unkonw doc category:', doc_name)
                            exit()

