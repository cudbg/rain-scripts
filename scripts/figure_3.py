from util import *


data = []
for name, rate in [("a", 0.3), ("b", 0.5), ("c", 0.7)]:
  _data = load_rc_data("../data/figure_3%s.csv" % name)
  for d in _data:
    d['rate'] = "Corruption: %d%%" % (rate*100)
  data.extend(_data)


p = ggplot(data, aes(x="k", y="recall", color="name", fill="name", shape="name"))
p += geom_line()
p += geom_point()
p += facet_grid(".~rate", scale=esc("free_x"))
p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, 0.5, 0.75]))
p += legend_bottom
p += theme(**{"legend.position": [.84, .39]})
ggsave("../assets/[RC]DBL-positive-0.5-3-LogReg.png", p, postfix=postfix, width=7, height=3, scale=0.8)

exit()



# for name, rate in [("a", 0.3), ("b", 0.5), ("c", 0.7)]:
#     data = load_rc_data("../data/figure_3%s.csv" % name)
#     maxk = max(pluckone(data, "k"))
#     func = "function(x)  (1+x) / %s" % maxk
#     p = ggplot(data, aes(x="k", y="recall", color="name", fill="name", shape="name"))
#     p += stat_function(fun=func, color=esc("grey"))
#     p += geom_line()
#     p += geom_point()
#     p += axis_labels("K", "Recall", ykwargs=dict(breaks=[0.25, 0.5, 0.75]))
#     p += legend_bottom
#     p += theme(**{"legend.position": [.35, .31]})
#     ggsave("../assets/[RC]DBL-positive-0.5-3-LogReg-%s.png" % rate, p, width=4, height=2.5, scale=0.8)


