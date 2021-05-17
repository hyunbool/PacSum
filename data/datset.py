"""
문자열로 만드는 코드
"""
import h5py
import os
import pandas as pd
import json
from collections import OrderedDict
import numpy as np

books_path = "./books/"
new_path = "../"
books_list = sorted(os.listdir(books_path))
dtype = h5py.special_dtype(vlen=str)
documents = list()

for i in books_list:
    title = i[:-4]

    with open(books_path + i, encoding='utf-8') as f:
        doc = [sent.strip() for sent in f]

    doc_json = dict()
    doc_json["title"] = i[:-4]
    doc_json["article"] = doc

    documents.append(doc_json)


    f.close()

documents = np.array(documents, dtype=dtype)

f = h5py.File(new_path + 'seg_train.h5df','w')  # 'a'
f.create_dataset('dataset', data=documents)
f.close()
