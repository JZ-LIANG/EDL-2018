import os

directory = '/Users/liangjianzhong/Desktop/internship/rpi_7k/~panx2/tmp/typing/zh'
for (dirpath, dirnames, filenames) in os.walk(directory):
    if 'dev.bio' in filenames:
        write_conll_zh(dirpath, 'dev.bio')