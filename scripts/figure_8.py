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
  
data = []
for name, rate in [("a", 0.1), ("b", 0.4), ("c", 0.8)]:
  _data = load_rc_data("../data/figure_8%s.csv" % name)
  for d in _data:
    d['rate'] = "%d%% Complaints" % (rate * 100)
  _data = split_and_run(_data, ["proc", "name", "k"], f)
  data.extend(_data)


#func = "function(x) x / %s" % _d['ntruth']

p = ggplot(data, aes(x="k", y="y", ymin="ymin", ymax="ymax", color="name", fill="name", shape="name"))
#p += stat_function(fun=func, color=esc("grey"))
p += geom_line()
p += geom_point()
p += geom_linerange()
p += facet_grid(".~rate")
p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, 0.5, 0.75], lim=[0,.8]))
p += legend_bottom
p += theme(**{"legend.position": [.84, .37]})
ggsave("../assets/[Ambiguity]MNISTJoinAmbiguity-LogReg-10000-1-7-0.3.png", p, postfix=postfix, width=7, height=2.5, scale=0.8)


