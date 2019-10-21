from util import *
import pandas as pd

data = []
_data = load_csv("../data/figure_10_1.csv")
y = np.mean(map(float, pluckone(_data, "AUC")))
ymax = y + np.std(map(float, pluckone(_data, "AUC")))
ymin = y - np.std(map(float, pluckone(_data, "AUC")))

_data = load_csv("../data/figure_10_2.csv")

for d in _data:
  d['name'] = "Point\nComplaint"
  d['x'] = d['number_of_complaints']
  d['y'] = d['AUC']
  d['ymax'] = d['AUC']
  d['ymin'] = d['AUC']
  data.append(dict(
    name="Agg\nComplaint",
    x=d['x'],
    y=y,
    ymax=ymax,
    ymin=ymin
  ))
data.extend(_data)
data = _data

p = ggplot(data, aes(x='x', y='y', ymax='ymax', ymin='ymin', color='name', shape='name'))
p += geom_hline(yintercept=y)
p += geom_text(aes(y=1.05, x=550, label=esc("Agg Complaint") ), size=3.5, color=esc('black'))
p += geom_text(aes(y=.7, x=550, label=esc("Point Complaint"), color='name' ), size=3.5)
p += geom_line()
p += geom_linerange()
p += geom_point()
p += axis_labels("Number of Complaints", "AUC", ykwargs=dict(lim=[.25,1.1], breaks=[.25, .5, .75, 1]))
p += legend_none
ggsave("../assets/[PointVSAgg]MNISTCountPointComplaint-1-7-from-LogReg-10000-0.1.png", p, width=4, height=2.25, scale=0.8)


