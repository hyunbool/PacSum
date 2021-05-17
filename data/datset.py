"""
문자열로 만드는 코드
"""
import h5py
import os
import pandas as pd
import json
from collections import OrderedDict
import numpy as np

path = "./extracted/"
new_path = "./extracted_h5df/"
file_list = os.listdir(path)
dtype = h5py.special_dtype(vlen=str)


documents = list()
for i in file_list:
    print(i)
    f = open(path + i, 'r')
    doc = list(map(lambda x: x.replace("\n", ""), f.readlines()))

    doc_json = OrderedDict()
    doc_json['title'] = i[:-4]
    doc_json['article'] = doc

    documents.append(str(doc_json))

    f.close()

documents = np.array(documents, dtype=dtype)

f = h5py.File(path + 'novel_data.hdf5','w')  # 'a'
f.create_dataset('dataset', data=documents)
f.close()
