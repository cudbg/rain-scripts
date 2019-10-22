from util import *
import pandas as pd


# 6b
def f(_, items):
  """
  aggregation function
  """
  d = dict(items[0])
  recalls = pluckone(items, "recall")
  
  d['y'] = np.mean(recalls)
  d['ymax'] = np.mean(recalls) + np.std(recalls)
  d['ymin'] = np.mean(recalls) - np.std(recalls)
  return [d]
  
basedata = []
data = []
for name, rate in [("a", 0.1), ("b", 0.4), ("c", 0.8)]:
  _data = load_rc_data("../data/figure_8%s.csv" % name)
  for d in _data:
    d['rate'] = "%d%% Complaints" % (rate * 100)
  _data = split_and_run(_data, ["proc", "name", "k"], f)
  data.extend(_data)

  ntruth = _data[0]['ntruth']
  for d in _data:
    basedata.append(dict(
      y = float(d['k']) / ntruth,
      k = d['k'],
      name = "Perfect",
      rate = d['rate']
    ))

write_csv(data, "figure_8.csv")
write_csv(basedata, "figure_8_base.csv")

os.system("R --no-save < figure_8.R")
exit()


