from util import *


def f(_, items):
    d = dict(items[0])
    f1s = list(map(float, pluckone(items, "recall")))
    
    d["y"] = np.mean(f1s)
    d["ymax"] = d['y'] + np.std(f1s)
    d["ymin"] = d['y'] - np.std(f1s)
    return d


basedata = []
data = []
for name, rate in [("a", 0.3), ("b", 0.5), ("c", 0.7)]:
  _data = load_rc_data("../data/figure_3%s.csv" % name)
  for d in _data:
      d["rate"] = "Corruption: %d%%" % (rate * 100)
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

write_csv(data, "figure_3.csv")
write_csv(basedata, "figure_3_base.csv")

os.system("R --no-save < figure_3.R")
