from pyecharts import Scatter

scatter = Scatter("散点图示例", width=1000, height=480)
v1 ,v2 = scatter.draw("../images/cup.png")
scatter.add("Cup", v1, v2)
scatter.render()