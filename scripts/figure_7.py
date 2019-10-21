from util import *
import pandas as pd

#6a
data = load_rc_data("../data/figure_7a.csv")

# func = "function(x) x / %s" % _d['ntruth']

p = ggplot(data, aes(x="k", y="recall", color="name", fill="name", shape="name"))
#p += stat_function(fun=func, color=esc("grey"))
p += geom_line()
p += geom_point()
p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, .5, .75]))
p += legend_bottom
p += theme(**{"legend.position": [.35, .4]})
ggsave("../assets/[RC]MNISTJoinRow-1-7-LogReg-10000-0.5.png", p, postfix=postfix, width=4, height=2.5, scale=0.8)



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

data = load_csv("../data/figure_7b.csv")
replace_attr(data, "name", names.get)
replace_attr(data, "AUC", float)
# group by aggregation to average the AUCs
data = split_and_run(data, ["proc", "name", "Corruption"], f)
p = ggplot(data, aes(x="Corruption", y="y", ymax='ymax', ymin='ymin', group="name", color="name", shape="name"))
p += geom_line(size=1)
p += geom_linerange(size=.5)
p += geom_point(size=3)
p += legend_bottom
ggsave("../assets/[AUCCR]MNISTJoinRow-1-7-LogReg-10000.png",
    p, postfix=postfix, width=4, height=2.5, scale=0.8)


