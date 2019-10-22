from util import *
import pandas as pd


def f(_, items):
  d = dict(items[0])
  f1s = list(map(float, pluckone(items, "recall")))
  d['y'] = np.mean(f1s)
  d['ymax'] = d['y'] + np.std(f1s)
  d['ymin'] = d['y'] - np.std(f1s)
  return d



#6a
data = load_rc_data("../data/figure_6a.csv")
func = "function(x) x / %s" % pluckone(data, "ntruth")[0]
data = split_and_run(data, ["proc", "name", "k"], f)

p = ggplot(data, aes(x="k", y="y", ymax='ymax', ymin='ymin',
  color="name", fill="name", shape="name"))
p += stat_function(fun=func, color=esc("grey"))
p += geom_line()
p += geom_linerange(size=0.25)
p += geom_point()
p += axis_labels("K", "Recall@k", ykwargs=dict(breaks=[0.25, .5, .75]))
p += legend_bottom
p += theme(**{"legend.position": [.35, .4]})
ggsave("../assets/[RC]MNISTJoinAggregation-1-7-((1, 2, 3, 4, 5), (6, 7, 8, 9, 0))-LogReg-10000-0.5.png", p, 
    postfix=postfix, width=4, height=2.5, scale=0.8)



# 6b
def f(_, items):
  """
  aggregation function
  """
  d = dict(items[0])
  aucs = pluckone(items, "AUC")
  d['y'] = np.mean(aucs)
  d['ymax'] = np.mean(aucs) + np.std(aucs)
  d['ymin'] = np.mean(aucs) - np.std(aucs)
  return [d]

data = load_csv("../data/figure_6b.csv")
replace_attr(data, "name", names.get)
replace_attr(data, "AUC", float)
# group by aggregation to average the AUCs
data = split_and_run(data, ["proc", "name", "Corruption"], f)
p = ggplot(data, aes(x="Corruption", y="y", ymax='ymax', ymin='ymin', group="name", color="name", shape="name"))
p += geom_line(size=1)
p += geom_linerange(size=.5)
p += geom_point(size=3)
p += axis_labels("Corruption", "AUC(CR)", ykwargs=dict(lim=[0,1], breaks=[0.2, .5, .75]))
p += legend_bottom
p += theme(**{"legend.position": esc("bottom")})
ggsave("../assets/[AUCCR]MNISTJoinAggregation-1-7-((1, 2, 3, 4, 5), (6, 7, 8, 9, 0))-LogReg-10000.png",
    p, postfix=postfix, width=4, height=2.5, scale=0.8)


