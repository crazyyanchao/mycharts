from pyecharts import WordCloud

name = ['Sam S Club', 'Macys', '曹宇飞', '孙颖', '汪州','尹若辰', '高煜东', 'Express', 'Home', 'Johnny Depp',        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham','Serena Williams','Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,         550, 462, 366, 360, 282, 273, 265]

wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render()