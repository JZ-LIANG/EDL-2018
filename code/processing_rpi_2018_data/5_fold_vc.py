import os
from subprocess import call
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##############################################################################
# this file is used to have a quick look how an un-tuned general CRFs 
# performance on the RPI_2018 data 
##############################################################################

##############################################################################
# refine the data format
##############################################################################
src_directory = '/Users/liangjianzhong/Desktop/rpi_5_fold_NER/'
dst_directory = '/Users/liangjianzhong/Desktop/test/result'
prop_directory = '/Users/liangjianzhong/Desktop/test/prop'
for (dirpath, dirnames, filenames) in os.walk(src_directory):
    if filenames and (filenames[0][-4:] == '.tsv'):
        # copy .prop
        prop_files = os.listdir(prop_directory)
        for file_name in prop_files:
            src_prop = prop_directory +'/' + file_name
            shutil.copy(src_prop, dirpath)
        # rename
        for filename in filenames:
            origin_file_name = dirpath + '/' + filename
            new_file_name = dirpath + '/' + filename[-9:]
            os.rename(origin_file_name, new_file_name)

path_jar = '/Users/liangjianzhong/Desktop/internship/stanford_tool/stanford-ner-2018-02-27/stanford-ner.jar'
classifier ='edu.stanford.nlp.ie.crf.CRFClassifier'
ls_test = ['fold0.tsv','fold1.tsv','fold2.tsv','fold3.tsv','fold4.tsv']
ls_prop = ['fold0.prop','fold1.prop','fold2.prop','fold3.prop','fold4.prop']
ls_stdout = ['stdout0.txt','stdout1.txt','stdout2.txt','stdout3.txt','stdout4.txt']
ls_stderr = ['stderr0.txt','stderr1.txt','stderr2.txt','stderr3.txt','stderr4.txt']


##############################################################################
# train 5-folds CV
##############################################################################

import gc
import os
from subprocess import call
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

src_directory = '/home/liang/internship/stanford_NER/data/rpi_5_fold_NER/'
#dst_directory = '/Users/liangjianzhong/Desktop/test/result'
#prop_directory = '/Users/liangjianzhong/Desktop/test/prop'

path_jar = '/home/liang/internship/stanford_NER/stanford-ner-2018-02-27/stanford-ner.jar'
classifier ='edu.stanford.nlp.ie.crf.CRFClassifier'
ls_test = ['fold0.tsv','fold1.tsv','fold2.tsv','fold3.tsv','fold4.tsv']
ls_prop = ['fold0.prop','fold1.prop','fold2.prop','fold3.prop','fold4.prop']
ls_stdout = ['stdout0.txt','stdout1.txt','stdout2.txt','stdout3.txt','stdout4.txt']
ls_stderr = ['stderr0.txt','stderr1.txt','stderr2.txt','stderr3.txt','stderr4.txt']



for (dirpath, dirnames, filenames) in os.walk(src_directory):
    if filenames and (filenames[0][-4:] == '.tsv'):
        print(dirpath)
        os.chdir(dirpath)
        for i in range(5):
            prop_file = dirpath + '/' + ls_prop[i]
            os.chdir(dirpath)
            call(["java", "-mx4g","-cp", path_jar, classifier, '-prop', prop_file])
            with open(ls_stdout[i], 'w+') as stdout_file,open(ls_stderr[i], 'w+') as stderr_file:
                call(["java", "-cp", path_jar, classifier,'-loadClassifier', 
                      'ner-model.ser.gz', '-testFile',ls_test[i]], stdout =stdout_file, stderr = stderr_file)
            os.remove("ner-model.ser.gz")
            del stdout_file, stderr_file
        gc.collect()    


        

##############################################################################
# collect the result
##############################################################################

src_directory = '/Users/liangjianzhong/Desktop/test/data'
dst_directory = '/Users/liangjianzhong/Desktop/test/result'
ls_test = ['fold0.tsv','fold1.tsv','fold2.tsv','fold3.tsv','fold4.tsv']
ls_prop = ['fold0.prop','fold1.prop','fold2.prop','fold3.prop','fold4.prop']
ls_stdout = ['stdout0.txt','stdout1.txt','stdout2.txt','stdout3.txt','stdout4.txt']
ls_stderr = ['stderr0.txt','stderr1.txt','stderr2.txt','stderr3.txt','stderr4.txt']

ls_entity = []
ls_P = []
ls_R = []
ls_F1 = []
ls_TP = []
ls_FP = []
ls_FN = []

for (dirpath, dirnames, filenames) in os.walk(src_directory):
    if len(filenames) > 5:
        os.chdir(dirpath)
        print(dirpath.split('/')[-1])
        ls_entity.append(dirpath.split('/')[-1])
        for i in range(5):
            stderr_file = dirpath + '/' + ls_stderr[i]
            os.chdir(dirpath)
            with open(stderr_file, 'r') as r_file:
                lines = r_file.readlines()
                print(lines[-2][:-1].split('\t'))
                _, P, R, F1, TP, FP, FN= lines[-2][:-1].split('\t')
                ls_P.append(float(P))
                ls_R.append(float(R))
                ls_F1.append(float(F1))
                ls_TP.append(float(TP))
                ls_FP.append(float(FP))
                ls_FN.append(float(FN))
length = len(ls_P)
ls_P = [ls_P[i:i+5] for i in range(0,length, 5)]
ls_R = [ls_R[i:i+5] for i in range(0,length, 5)]
ls_F1 = [ls_F1[i:i+5] for i in range(0,length, 5)]
ls_TP = [ls_TP[i:i+5] for i in range(0,length, 5)]
ls_FP = [ls_FP[i:i+5] for i in range(0,length, 5)]
ls_FN = [ls_FN[i:i+5] for i in range(0,length, 5)]
                
ls_P_cv = [sum(i)/5 for i in ls_P ]
ls_R_cv = [sum(i)/5 for i in ls_R ]
ls_F1_cv = [sum(i)/5 for i in ls_F1 ]
ls_TP_cv = [sum(i)/5 for i in ls_TP ]
ls_FP_cv = [sum(i)/5 for i in ls_FP ]
ls_FN_cv = [sum(i)/5 for i in ls_FN ]


##############################################################################
# plot the statistic
##############################################################################
# Setting the positions and width for the bars
pos = list(range(5)) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(25,10))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        ls_P_cv, 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label='P') 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        ls_R_cv,
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label='R') 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        ls_F1_cv, 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        label='F1') 

# Set the y axis label
ax.set_ylabel('Percentage')

# Set the chart's title
ax.set_title('5-fold CV performance')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(ls)

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
# plt.ylim([0, max(df['pre_score'] + df['mid_score'] + df['post_score'])] )

#Adding the legend and showing the plot
plt.legend( loc='upper right')
plt.grid()
plt.show()

