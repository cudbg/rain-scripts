import numpy as np
import csv
from collections import *
from pygg import *
from wuutils import *
import pandas as pd

names = {"Loss": "Loss", "Complaint": "Holistic", "Tiresias": "TwoStep", "SelfLoss": "InfLoss"}


def load_rc_data(fpath):
  df = pd.read_csv(fpath)
  _data = df.to_dict(orient="records")
  replace_attr(_data, "name", names.get)

  # need to reshape into an actual table..
  data = []
  for _d in _data:
    recalls = list(map(float, _d['recall'][1:-1].split()))
    block = int(len(recalls) / 10)
    for k, recall in enumerate(recalls):
      if k == 1 or k % block == 0 or k == len(recalls)-1: 
        d = dict(_d)
        d['recall'] = recall
        d['k'] = k+1
        data.append(d)
  return data



