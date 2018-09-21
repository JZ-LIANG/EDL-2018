#!/bin/bash

# To install TensorFlow: (!! if there is not tensorflow)
sudo pip3 install tensorflow

# To install a few more packages which NeuroNER depends on:
sudo pip3 install -U networkx matplotlib scikit-learn scipy pycorenlp pickle

# Installing spaCy
sudo apt-get install -y build-essential python3 -dev
sudo pip3 install -U spacy
sudo python3 -m spacy download en





# NeuroNER is now ready to run! By default it is configured to train and test on CoNLL-2003. To start the training:
# To use the CPU if you have installed tensorflow, or use the GPU if you have installed tensorflow-gpu:
cd ../../src
python3.5 main.py
