from util import *
import pandas as pd

def f(_, items):
  d = dict(items[0])
  d['y'] = np.mean(list(map(float, pluckone(items, "AUC"))))
  d['ymax'] = np.mean(list(map(float, pluckone(items, "AUC"))))
  return d

models = dict(LogReg="LogReg", SimpleCNN="CNN")

data = load_csv("../data/figure_12.csv")
replace_attr(data, "name", names.get)
replace_attr(data, "model", models.get)
data = split_and_run(data, ["proc", "name", "model"], f)
print data

p = ggplot(data, aes(x="name", y="y", ymax='y', ymin=0,
  color="model", fill="model", shape="model"))
#p += stat_function(fun=func, color=esc("grey"))
p += geom_linerange(position=position_dodge(width=0.7))
p += geom_point(size=2, position=position_dodge(width=0.7))
p += axis_labels("", "AUC", "discrete",
    ykwargs=dict(breaks=[0.25, 0.5, 0.75]))
p += legend_bottom
p += coord_flip()
p += theme(**{"legend.position": [1, .37]})
ggsave("../assets/[LogRegVSCNN]MNISTCountAggregationComplaint-1-7-10000-0.5.png", p, postfix=postfix, width=4, height=2.0, scale=0.8)
