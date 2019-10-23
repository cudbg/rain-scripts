from util import *

def f(_, items):
  d = dict(items[0])
  f1s = list(map(float, pluckone(items, "F1")))
  d['y'] = np.mean(f1s)
  d['ymax'] = d['y'] + np.std(f1s)
  d['ymin'] = d['y'] - np.std(f1s)
  return d

data = load_csv("../data/figure_4.csv")
data = split_and_run(data, ["proc", "Corruption"], f)

p = ggplot(data, aes(x="Corruption", y="y", ymax='ymax', ymin='ymin'))
p += geom_line()
p += geom_linerange()
p = p + geom_point(color=esc("white"), size=2.5)
p = p + geom_point(size=1.5)
p += axis_labels("Corruption Rate", "F1 on Training Set", 
    ykwargs=dict(breaks=[0.25, 0.5, 0.75, 1]))
p += legend_none
ggsave("../assets/F1-DBLP-positive-3.png", p, width=4, height=2.5, scale=0.8)


