from pyecharts import Line

line = Line("折线图-阶梯图示例")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
line.show_config()
line.render()