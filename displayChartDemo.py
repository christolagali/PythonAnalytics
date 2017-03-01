import pygal
import lxml

bar_chart = pygal.Bar()
bar_chart.add('Demo',[0,1,1,2,3,5,8,13,21,34,55])
#bar_chart.render_to_file('bar_chart.svg')
#bar_chart.render_in_browser()

line_chart = pygal.Line()
line_chart.title = 'Browser Usage'
line_chart.x_labels = map(str,range(2002,2103))
line_chart.add('Firefox',[None,None,0,16.6,25,0,31,36.4,45.5,46.3,42.8,37.1])
line_chart.add('Chrome',[None,None,None,None,None,None,0,3.9,10.8,23.8,35.3])
line_chart.add('IE',[85.8,84.6,84.7,74.5,66,58.6,54.7,44.8,36.2,26.6,20.1])
line_chart.render_in_browser()
#line_chart.render_table()