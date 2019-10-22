from util import *
import pandas as pd

def f(_, items):
  d = dict(items[0])
  f1s = list(map(float, pluckone(items, "recall")))
  d['y'] = np.mean(f1s)
  d['ymax'] = d['y'] + np.std(f1s)
  d['ymin'] = d['y'] - np.std(f1s)
  return d



data = []
for name, rate in [("a", "overshoot"), ("b", "partial"), ("c", "wrong")]:
  _data = load_rc_data("../data/figure_11%s.csv" % name)
  for d in _data:
    d['Complaint'] = rate.capitalize()
  data.extend(_data)

data = split_and_run(data, ["Complaint", "proc", "name", "k"], f)
#func = "function(x) x / %s" % _d['ntruth']
p = ggplot(data, aes(x="k", y="y", ymax='ymax', ymin='ymin',
  color="name", fill="name", shape="name"))
#p += stat_function(fun=func, color=esc("grey"))
p += geom_line()
p += geom_linerange(size=0.25)
p += geom_point()
p += facet_grid(".~Complaint")
p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, .5, .75]))
p += legend_bottom
p += theme(**{"legend.position": [.885, .34]})
ggsave("../assets/[RC]MNISTCountWrongComplaint-1-7-LogReg-10000-0.3.png", p, postfix=postfix, width=6, height=2.5, scale=0.8)


