from util import *

def f(_, items):
  d = dict(items[0])
  print pluckone(items, "AUC")
  d['AUC'] = np.mean(pluckone(items, "AUC"))
  return [d]

data = load_csv("fig6b.csv")
replace_attr(data, "name", names.get)
replace_attr(data, "AUC", float)
data = split_and_run(data, ["proc", "name", "Corruption"], f)
p = ggplot(data, aes(x="Corruption", y="AUC", group="name", color="name", shape="name"))
p += geom_line(size=1)
p += geom_point(size=3)
p += legend_bottom
ggsave("[AUCCR]MNISTJoinAggregation-1-7-((1, 2, 3, 4, 5), (6, 7, 8, 9, 0))-LogReg-10000.png",
    p, width=6, height=3, scale=0.8)



_data = load_csv("fig3.csv")
replace_attr(_data, "name", names.get)

# need to reshape into an actual table..
data = []
for _d in _data:
  recalls = list(map(float, _d['recall'][1:-1].split()))
  for k, recall in enumerate(recalls):
    if k == 1 or k % 5 == 0 or k == len(recalls)-1: 
      d = dict(_d)
      d['recall'] = recall
      d['k'] = k+1
      data.append(d)

func = "function(x) x / %s" % _d['ntruth']

p = ggplot(data, aes(x="k", y="recall", color="name", fill="name", shape="name"))
p += stat_function(fun=func, color=esc("grey"))
p += geom_line()
p += geom_point()
p += axis_labels("K", "Recall")
p += legend_bottom
ggsave("[RC]DBL-positive-0.5-3-LogReg-0.3.png", p, width=4, height=3, scale=0.8)




data = load_csv("runtimes.csv")

data = fold(data, ["Train", "Encode", "Rank"])
#replace_attr(data, "val", lambda v: np.log10(float(v)))
p = ggplot(data, aes(x="name", y="val", color="key", fill="key"))
p += geom_bar(stat=esc('identity'), position=esc("stack"))
p += geom_text(aes(label="46.1", y=.95, x=esc("InfLoss")), color=esc("black"), fill=esc("black"))
p += axis_labels("", "Runtime (s)", "discrete", "continuous")
p += legend_bottom
p += coord_flip(ylim=[0,1])
ggsave("[Time]DBL-positive-0.5-3-LogReg-0.5.png", p, width=6, height=2.5, scale=0.8)







