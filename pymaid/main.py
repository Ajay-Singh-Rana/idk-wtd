import sys
# import numpy as np
from matplotlib import pyplot as plt
from random import choice


# colors
colors = ['Black', 'Red', 'Magenta', 'Yellow', 'Blue']
# functions
def draw_pie(chart_header, commands, width):
    chart_title = chart_header[1] if (len(chart_header) > 1) else "pie_chart.png"
    legend_title = chart_header[2] if(len(chart_header) > 2) else ""
    labels_ = []
    pct_ = []
    colors_ = []
    explode_ = []
    for line in commands[1:]:
        line = line.strip().split(' ')
        labels_.append(line[0])
        pct_.append(int(line[1]))
        if(len(line) > 2):
            colors_.append(line[2])
        else:
            colors_.append(choice(colors)) 
        explode_.append(float(line[3])) if(len(line) > 3) else explode_.append(0)
    
    plt.pie(x = pct_, labels = labels_, colors = colors_, explode = explode_,
                autopct = lambda pct : f'{pct:.1f}%',
                wedgeprops = {"width" : width})
    plt.title(chart_title, loc = "left")    
    plt.legend(loc = [1, 0.85], title = legend_title)
    plt.savefig(chart_title + '.png')

# main program
file_name = sys.argv[1]

with open(file_name,'r') as file:
    commands = file.read()

commands = commands.strip().split('\n')
chart_header = commands[0].split(' ')

if(chart_header[0].lower() == "pie"):
    draw_pie(chart_header, commands, width = 1)
elif(chart_header[0].lower() == 'donut'):
    draw_pie(chart_header, commands, width = 0.35)
elif(chart_header[0].lower() == 'line'):
    chart_title = chart_header[1] if (len(chart_header) > 1) else "line_plot.png"
    legend_title = chart_header[2] if(len(chart_header) > 2) else ""
    for line in commands[1:]:
        line = line.strip().split(" ")
        label_ = line[0]
        points = [i for i in map(int, line[1].split(','))]
        marker_ = 'o' if (len(line) < 3) else line[2]
        linestyle_ = '-' if(len(line) < 4) else line[3]
        color_ = choice(colors) if(len(line) < 5 or line[4] == "") else line[4]
        plt.plot(points, label = label_, marker = marker_, linestyle = linestyle_, color = color_)
    plt.title(chart_title, loc = "left")
    plt.legend(loc = [1, 0.8], title = legend_title)
    plt.savefig(chart_title + '.png')
elif(chart_header[0].lower() == 'bar'):
    chart_title = chart_header[1] if (len(chart_header) > 1) else "bar_plot.png"
    legend_title = chart_header[2] if(len(chart_header) > 2) else ""
    for line in commands[1:]:
        line = line.strip().split(' ')
        label_ = line[0]
        x_points = [i for i in map(int,line[1].split(','))]
        y_points = [j for j in map(int,line[2].split(','))]
        color_ = choice(colors) if(len(line) < 4) else line[3]
        width_ = 0.8 if(len(line) < 5) else float(line[4])
        edgecolor_ = "Black" if(len(line) < 6) else line[5]
        plt.bar(x_points, y_points, label = label_, color = color_,
                width = width_, edgecolor = edgecolor_)
    plt.title(chart_title, loc = 'left')
    plt.legend(loc = [0.9, 0.85], title = legend_title)
    plt.savefig(chart_title + '.png')