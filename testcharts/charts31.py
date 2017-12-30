import math
from pyecharts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
polar.show_config()
polar.render()