'''
To run:
CUDA_VISIBLE_DEVICES="" python3.5 main.py &
CUDA_VISIBLE_DEVICES=1 python3.5 main.py &
CUDA_VISIBLE_DEVICES=2 python3.5 main.py &
CUDA_VISIBLE_DEVICES=3 python3.5 main.py &
'''
from __future__ import print_function
import os
import argparse
from argparse import RawTextHelpFormatter
import sys
from neuroner_modified import NeuroNER
import shutil
import warnings
from distutils import util
warnings.filterwarnings('ignore')
import time
import pandas as pd
from subprocess import call
import json
import pickle



def main(argv=sys.argv):

    # setting your argument here
    arguments = {
              'pretrained_model_folder':None,
              'dataset_text_folder':None,
              'character_embedding_dimension':25,
              'character_lstm_hidden_state_dimension':25,
              'check_for_digits_replaced_with_zeros':True,
              'check_for_lowercase':True,
              'debug':False,
              'dropout_rate':0.5,
              'experiment_name':'experiment',
              'freeze_token_embeddings':True,
              'gradient_clipping_value':5.0,
              'learning_rate':0.005,
              'load_only_pretrained_token_embeddings':False,
              'main_evaluation_mode':'conll',
              'maximum_number_of_epochs':25,###############################
              'number_of_cpu_threads':8,
              'number_of_gpus':0,
              'optimizer':'sgd',
              'output_folder':None,
              'patience':4,#########################################3
              'plot_format':'pdf',
              'reload_character_embeddings':False,
              'reload_character_lstm':False,
              'reload_crf':False,
              'reload_feedforward':False,
              'reload_token_embeddings':False,
              'reload_token_lstm':False,
              'remap_unknown_tokens_to_unk':True,
              'spacylanguage':'en',
              'tagging_format':'bio',
              'token_embedding_dimension':100,
              'token_lstm_hidden_state_dimension':100,
              'token_pretrained_embedding_filepath':'../data/word_vectors/glove.6B.100d.txt',########################
              'tokenizer':'spacy',
              'train_model':True,
              'use_character_lstm':True,
              'use_crf':True,
              'use_pretrained_model':False,
              'verbose':False}

    root_data_path = '../data/RPI/fold0_large/'
    


    # loading the entities to be train.
    with open("large_entities_set.txt", "rb") as fp:   # Unpickling
        entities = pickle.load(fp)
    n_entity = len(entities)


    # main loop, go through all entities selected.
    for i, entity in enumerate(entities):

        new_data_folder = root_data_path + entity +'/'
        new_output_folder = new_data_folder + 'output/'
        arguments['dataset_text_folder'] = new_data_folder
        arguments['output_folder'] = new_output_folder

        nn = NeuroNER(**arguments)
        best_epoch = nn.fit()
        nn.close()

        # delete the needless files but keep the labeling files of the best epoch
        model_data_folder_name = os.listdir(new_output_folder)[0]
        model_data_path = new_output_folder + model_data_folder_name + '/'
        file1 = '{0:03d}_train.txt'.format(best_epoch)
        file2 = '{0:03d}_valid.txt'.format(best_epoch)
        file1_path = model_data_path + file1
        file2_path = model_data_path + file2
        new_file1_path = model_data_path + 'best_train.conll'
        new_file2_path = model_data_path + 'best_vaild.conll'
        os.rename(file1_path, new_file1_path)
        os.rename(file2_path, new_file2_path)
        call(["find", model_data_path, "-name", "*.txt", "-delete"])
        call(["find", new_data_folder, "-name", "*.txt", "-delete"])
        # show the progress
        print('{} / {} entities are done'.format(i,n_entity))



if __name__ == "__main__":
    main()


