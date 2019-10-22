from util import *

def f(_, items):
  d = dict(items[0])
  vals = list(map(float, pluckone(items, "val")))

  d['y'] = np.mean(vals)
  return d


data = load_csv("../data/figure_5.csv")

data = fold(data, ["Train", "Encode", "Rank"])
replace_attr(data, "name", names.get)
data = split_and_run(data, ["key", "name"], f)


#replace_attr(data, "val", lambda v: np.log10(float(v)))
p = ggplot(data, aes(x="name", y="y", color="key", fill="key"))
p += geom_bar(stat=esc('identity'), position=esc("stack"))
p += geom_text(aes(label=esc("46.1s"), y=4, x=esc("InfLoss")), color=esc("black"), fill=esc("black"))
p += axis_labels("", "Runtime (s)", "discrete", "continuous")
p += legend_bottom
p += coord_flip(ylim=[0,5])
ggsave("../assets/[Time]DBL-positive-0.5-3-LogReg-0.5.png", p, width=4, height=2.5, scale=0.8)

