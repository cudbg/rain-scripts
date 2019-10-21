from util import *

data = load_csv("../data/figure_5.csv")

data = fold(data, ["Train", "Encode", "Rank"])
replace_attr(data, "name", names.get)
#replace_attr(data, "val", lambda v: np.log10(float(v)))
p = ggplot(data, aes(x="name", y="val", color="key", fill="key"))
p += geom_bar(stat=esc('identity'), position=esc("stack"))
p += geom_text(aes(label=esc("46.1s"), y=.95, x=esc("InfLoss")), color=esc("black"), fill=esc("black"))
p += axis_labels("", "Runtime (s)", "discrete", "continuous")
p += legend_bottom
p += coord_flip(ylim=[0,1])
ggsave("../assets/[Time]DBL-positive-0.5-3-LogReg-0.5.png", p, width=4, height=2.5, scale=0.8)

