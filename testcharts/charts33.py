from pyecharts import Scatter

scatter = Scatter("散点图示例", width=800, height=480)
v1 ,v2 = scatter.draw("../images/love.png")
scatter.add("Love", v1, v2)
scatter.render()