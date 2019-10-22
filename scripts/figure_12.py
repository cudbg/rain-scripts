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
data = split_and_run(data, ["Corruption", "proc", "name", "model"], f)

p = ggplot(data, aes(x="Corruption", y="y", ymax='y', ymin=0,
  color="name", fill="name", shape="name"))
p += geom_point() + geom_line()
#p += geom_linerange(position=position_dodge(width=0.7))
#p += geom_point(size=2, position=position_dodge(width=0.7))
p += facet_grid(".~model")
p += axis_labels("Corruption Rate", "AUC(CR)",
    ykwargs=dict(breaks=[0.25, 0.5, 0.75, 1]))
p += legend_bottom
#p += coord_flip()
#p += theme(**{"legend.position": [1, .37]})
ggsave("../assets/[LogRegVSCNN]MNISTCountAggregationComplaint-1-7-10000-0.5.png", p, 
    postfix=postfix, width=4, height=2.5, scale=0.8)



data = load_csv("../data/figure_NN_time.csv")
data = fold(data, ["Train", "Encode", "Rank"])
data = [d for d in data if d['Corruption'] != '0.3']
replace_attr(data, "name", names.get)
replace_attr(data, "model", models.get)
p = ggplot(data, aes(x="factor(Corruption)", y="val", color="key", fill="key"))
p += geom_bar(stat=esc('identity'), position=esc("stack"), width=0.7)
#p += geom_line(position=position_stack()) + geom_point(position=position_stack())
p += facet_grid("model~name")
p += axis_labels("", "Runtime (s)", "discrete", "continuous")
p += legend_bottom
p += coord_flip()
#p += theme(**{"legend.position": [1, .0]})
ggsave("../assets/[LogRegVSCNN-Time]MNISTCountAggregationComplaint-10000-1-7-0.3.png", p, width=6, height=2.5, scale=1)

