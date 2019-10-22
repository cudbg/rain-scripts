from util import *
import pandas as pd

def f(_, items):
  d = dict(items[0])
  f1s = list(map(float, pluckone(items, "recall")))
  d['y'] = np.mean(f1s)
  d['ymax'] = d['y'] + np.std(f1s)
  d['ymin'] = d['y'] - np.std(f1s)
  return d



basedata = []
data = []
for name, rate in [("a", "overshoot"), ("b", "partial"), ("c", "wrong")]:
  _data = load_rc_data("../data/figure_11%s.csv" % name)
  for d in _data:
    d['Complaint'] = rate.capitalize()
  data.extend(_data)

  ntruth = _data[0]['ntruth']
  for d in _data:
    basedata.append(dict(
      y = float(d['k']) / ntruth,
      k = d['k'],
      name = "Perfect",
      Complaint = d['Complaint']
    ))

data = split_and_run(data, ["Complaint", "proc", "name", "k"], f)
write_csv(data, "figure_11.csv")
write_csv(basedata, "figure_11_base.csv")

os.system("R --no-save < figure_11.R")
exit()
