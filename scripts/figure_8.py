from util import *
import pandas as pd

for name, rate in [("a", 0.1), ("b", 0.4), ("c", 0.8)]:
  data = load_rc_data("../data/figure_8%s.csv" % name)
  #func = "function(x) x / %s" % _d['ntruth']

  p = ggplot(data, aes(x="k", y="recall", color="name", fill="name", shape="name"))
  #p += stat_function(fun=func, color=esc("grey"))
  p += geom_line()
  p += geom_point()
  p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, 0.5, 0.75], lim=[0,.8]))
  p += legend_bottom
  p += theme(**{"legend.position": [.35, .37]})
  ggsave("../assets/[Ambiguity]MNISTJoinAmbiguity-LogReg-10000-1-7-0.3-%s.png" % rate, p, width=4, height=2.5, scale=0.8)


