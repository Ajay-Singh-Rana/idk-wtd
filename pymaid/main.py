import sys
# import numpy as np
from matplotlib import pyplot as plt
from random import choice
from parse_comments import parse_comments


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
        pct_.append(float(line[1]))
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

commands = parse_comments(commands) # parse (remove) comments
commands = commands.strip().split('\n')
chart_header = commands[0].strip().split(' ')

if(chart_header[0].lower() == "pie"):
    draw_pie(chart_header, commands, width = 1)
elif(chart_header[0].lower() == 'donut'):
    draw_pie(chart_header, commands, width = 0.35)
elif(chart_header[0].lower() == 'line'):
    chart_title = chart_header[1] if (len(chart_header) > 1) else "line_plot.png"
    sep = int(chart_header[2]) if (len(chart_header) > 2) else 0
    legend_title = chart_header[3] if(len(chart_header) > 3) else ""
    if(sep):
        axes = len(commands[1:])
        axes = (axes//2,2) if (axes % 2 == 0) else ((axes//2 + 1),2)
        fig, ax = plt.subplots(axes[0], axes[1])
        for (i,line) in enumerate(commands[1:]):
            line = line.strip().split(" ")
            x_label_ = line[0]
            x_points = [i for i in map(float, line[1].split(','))]
            y_label_ = line[2]
            y_points = [i for i in map(float, line[3].split(','))]
            marker_ = 'o' if (len(line) < 5) else line[4]
            linestyle_ = '-' if(len(line) < 6) else line[5]
            color_ = choice(colors) if(len(line) < 7) else line[6]
            ax[i].set_xlabel(x_label_)
            ax[i].set_ylabel(y_label_)
            ax[i].plot(x_points,y_points, marker = marker_, linestyle = linestyle_, color = color_)
            # ax[i].legend(loc = [1, 0.8], title = legend_title)
        ax[i].set_title(chart_title, loc = "left")
        fig.tight_layout(h_pad = 2)
        fig.savefig(chart_title + '.png')
    else:
        for line in commands[1:]:
            line = line.strip().split(" ")
            x_label_ = line[0]
            x_points = [i for i in map(float, line[1].split(','))]
            y_label_ = line[2]
            y_points = [i for i in map(float, line[3].split(','))]
            group_label = "" if (len(line) < 5) else line[4]
            marker_ = 'o' if (len(line) < 6) else line[5]
            linestyle_ = '-' if(len(line) < 7) else line[6]
            color_ = choice(colors) if(len(line) < 8) else line[7]
            plt.xlabel(x_label_)
            plt.ylabel(y_label_)
            plt.plot(x_points, y_points, label = group_label, marker = marker_, linestyle = linestyle_, color = color_)
            plt.legend(loc = [1, 0.8], title = legend_title)
        plt.title(chart_title, loc = "left")
        plt.tight_layout()
        plt.savefig(chart_title + '.png')
elif(chart_header[0].lower() == 'bar'):
    chart_title = chart_header[1] if (len(chart_header) > 1) else "bar_plot.png"
    legend_title = chart_header[2] if(len(chart_header) > 2) else ""
    for line in commands[1:]:
        line = line.strip().split(' ')
        label_ = line[0]
        x_points = [i for i in map(float,line[1].split(','))]
        y_points = [j for j in map(float,line[2].split(','))]
        color_ = choice(colors) if(len(line) < 4) else line[3]
        width_ = 0.8 if(len(line) < 5) else float(line[4])
        edgecolor_ = "Black" if(len(line) < 6) else line[5]
        plt.bar(x_points, y_points, label = label_, color = color_,
                width = width_, edgecolor = edgecolor_)
    plt.title(chart_title, loc = 'left')
    plt.legend(loc = [0.9, 0.85], title = legend_title)
    plt.savefig(chart_title + '.png')

elif(chart_header[0].lower() == 'scatter'):
    chart_title = chart_header[1] if(len(chart_header) > 1) else "satter_plot.png"
    legend_title = chart_header[2] if(len(chart_header) > 2) else ""
    for line in commands[1:]:
        line = line.strip().split(' ')
        label_ = line[0]
        x_points = [i for i in map(float,line[1].split(','))]
        y_points = [j for j in map(float,line[2].split(','))]
        color_ = choice(colors) if(len(line) < 4) else [j for j in map(str,line[3].split(','))]
        edge_colors_ = choice(colors) if(len(line) < 5) else [j for j in map(str,line[4].split(','))]
        plt.bar(x_points, y_points, label = label_, c = color_, edgecolors = edge_colors_)
    plt.title(chart_title, loc = 'left')
    plt.legend(loc = [0.9, 0.85], title = legend_title)
    plt.savefig(chart_title + '.png')
