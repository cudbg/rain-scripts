import os
import numpy as np
import csv
from collections import *
from pygg import *
from wuutils import *
import pandas as pd

names = {"Loss": "Loss", "Complaint": "Holistic", "Tiresias": "TwoStep", "SelfLoss": "InfLoss"}
postfix = """
  data$name  = factor(data$name, levels=c('TwoStep', 'Holistic', 'Loss', 'InfLoss'))
"""

def write_csv(data, fname):
  keys = data[0].keys()

  with open(fname, 'wb') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(data)


def load_rc_data(fpath):
  df = pd.read_csv(fpath)
  _data = df.to_dict(orient="records")
  replace_attr(_data, "name", names.get)

  # need to reshape into an actual table..
  data = []
  for _d in _data:
    recalls = [float(digit) for digit in _d['recall'][1:-1].split()]
    block = int(len(recalls) / 10)
    for k, recall in enumerate(recalls):
      if k == 1 or k % block == 0 or k == len(recalls)-1: 
        d = dict(_d)
        d['recall'] = recall
        d['k'] = k+1
        data.append(d)
  return data



