from util import *
import pandas as pd

data = []
_data = load_csv("../data/figure_10_1.csv")
y = np.mean(map(float, pluckone(_data, "AUCCR")))
ymax = y + np.std(map(float, pluckone(_data, "AUCCR")))
ymin = y - np.std(map(float, pluckone(_data, "AUCCR")))

_data = load_csv("../data/figure_10_2.csv")

for d in _data:
  d['name'] = "Point\nComplaint"
  d['x'] = d['number_of_complaints']
  d['y'] = d['AUCCR']
  d['ymax'] = d['AUCCR']
  d['ymin'] = d['AUCCR']
  data.append(dict(
    name="Agg\nComplaint"
    x=d['x'],
    y=y,
    ymax=ymax,
    ymin=ymin
  ))
data.extend(_data)

p = ggplot(data, aes(x='x', y='y', ymax='ymax', ymin='ymin', color='name', shape='name'))
p += geom_line()
p += geom_point()
p += axis_labels("Number of Complaints", "AUC")
p += legend_bottom
ggsave("[PointVSAgg]MNISTCountPointComplaint-1-7-from-LogReg-10000-0.1.png", p, width=4, height=2.5, scale=0.8)


