library(ggplot2)
library(grid)

data = read.csv("figure_3.csv")
basedata = read.csv("figure_3_base.csv")
data$name  = factor(data$name, levels=c('TwoStep', 'Holistic', 'Loss', 'InfLoss'))



p = ggplot(data, aes(x=k, y=y, ymax=ymax, ymin=ymin, color=name, fill=name, shape=name))
p = p + layer(geom="line", inherit.aes=F, data=basedata, mapping=aes(x=k, y=y), position="identity", stat="identity", params=list(color="gray"))#, color="black") #, show.legend=F)
p = p + geom_line()
p = p + geom_point()
p = p + geom_linerange(size=.25)
p = p + facet_grid(.~rate, scale="free_x")
p = p + scale_x_continuous(name="K")
p = p + scale_y_continuous(name="Recall", breaks=c(0.25, .5, .75))
p = p + coord_cartesian(ylim=c(0,1))
p = p + theme_bw() 
p = p + theme(
  legend.background= element_blank(),
  legend.justification=c(1,0),
  legend.position=c(.84,.36),
  legend.key = element_blank(),
  legend.title=element_blank(),
  text= element_text(colour = '#333333', size=11),
  axis.text= element_text(colour = '#333333', size=11),  
  plot.background= element_blank(),
  panel.border= element_rect(color="#e0e0e0"),
  strip.background= element_rect(fill="#efefef", color="#e0e0e0"),
  strip.text= element_text(color="#333333")
)



#p += legend_bottom
#p += theme(**{"legend.position": [0.84, 0.39]})
ggsave(
    "../assets/[RC]DBL-positive-0.5-3-LogReg.png", p, width=7, height=3, scale=0.8
)

