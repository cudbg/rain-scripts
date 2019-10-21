from __future__ import print_function
from util import *
import pandas as pd

# 9a 9b
def f(_, items):
  """
  aggregation function
  """
  d = dict(items[0])
  print(pluckone(items, "AUC"))
  d['AUC'] = np.mean(pluckone(items, "AUC"))
  return [d]

data = []
for name,rate in [("a", 0.3), ("b", 0.5)]:
  _data = load_csv("../data/figure_9%s.csv" % name)
  for d in _data:
    d['Setting'] = d['Corruption']
    d['Corruption'] = "Corruption: %d%%" % (rate * 100)
  data.extend(_data)

replace_attr(data, "name", names.get)
replace_attr(data, "AUC", float)
replace_attr(data, "Setting", lambda v: v.capitalize())


# group by aggregation to average the AUCs
data = split_and_run(data, ["proc", "name", "Setting", "Corruption"], f)
p = ggplot(data, aes(x="name", y="AUC", ymin=0, ymax='AUC',
  color="Setting", fill="Setting", shape="Setting"))
#p += geom_bar(stat=esc("identity"), position=esc("dodge"))
p += geom_linerange(position=position_dodge(width=.75))
p += geom_point(size=2, position=position_dodge(width=.75))
p += facet_grid(".~Corruption")
p += axis_labels("", "AUC", "discrete", ykwargs=dict(breaks=[.1,.2,.3,.4]))
p += legend_bottom
p += coord_flip()
p += theme(**{"legend.position": [.48, .31]})
ggsave("../assets/[AUCCR]Adult-LogReg.png", p, width=6, height=2.5, scale=0.8)


