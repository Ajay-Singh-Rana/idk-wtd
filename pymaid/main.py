import sys
# import numpy as np
from matplotlib import pyplot as plt


file_name = sys.argv[1]

with open(file_name,'r') as file:
    commands = file.read()

commands = commands.split('\n')

chart_header = commands[0].split(' ')
if(chart_header[0].lower() == "pie"):
    fig_name = commands[1] if (len(chart_header) > 1) else "pie_chart.png"
    labels_ = []
    pct_ = []
    colors_ = []
    explode_ = []
    for line in commands[1:]:
        line = line.split(' ')
        labels_.append(line[0])
        pct_.append(line[1])
        if(len(line) > 2):
            colors_.append(line[2]) 
        explode_.append(line[3]) if(len(line) > 3) else explode_.append(0)
    if(colors_ == []):
        plt.pie(x = pct_, labels = labels_, explode = explode_)
    else:
        plt.pie(x = pct_, labels = labels_, colors = colors_)    
    plt.savefig(fig_name)