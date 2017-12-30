from pyecharts import Bar
# 参考文档http://mp.weixin.qq.com/s?__biz=MzAxMjM2MTY0OQ==&mid=2650473730&idx=1&sn=1367985a74df3c8634423be381ddc0a2&chksm=83bcafdcb4cb26ca7ca13ece0784e5fca114e2226c13672caad4a94c22c03900dadbb1e44494&mpshare=1&scene=1&srcid=07254l6Uyd7z0IveF9WvfzSG#rd

bar =   Bar("我的第一个图标","这是副标题")

# 添加图表的数据和设置各种配置项
bar.add("服装",["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],[5,20,36,10,75,90])

# 打印输出图表的所有配置项
bar.show_config()

# 生成 .html 文件
bar.render()