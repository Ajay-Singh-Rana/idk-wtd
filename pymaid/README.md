# `pymaid` : A `mermaid` inspired charting tool

`pymaid` is a simple charting tool which uses `matplotlib` to
plot charts. It enlace the user with a markdown like format
for creating quick plots. 

### Code Snippet
```Python
Pie fruit_share.png
Apple 35
Banana 46
Grape 15
Mango 4
```
### Output:
![chart](https://i.imgur.com/ouWZf3J.png)

### To Do
- [x] Line Plots
- [x] Pie Charts
- [ ] Scatter Plots
- [ ] Flowcharts
- [ ] Documentation (underway)
- [ ] GUI Application
- [ ] Comment Support

### Documentation
To use `pymaid` clone the repo and then create a `.pmd' file with the 
figure rules/syntax.
To get the figure run:
```Python
python3 main.py file.pmd
```

Some basic plot syntaxes:

#### Pie Chart
Syntax:
```Syntax
Pie Figure_Title(without spaces) Legend_Title(without spaces)
Label1 Percentage Color(optional) Explode
Label2 Percentage Color(optional) Explode
Label4 Percentage Color(optional) Explode
Label5 Percentage Color(optional) Explode
```

Example:
```pmd
Pie Fruit_Share Fruit
Apple 35 Red 0.1
Banana 25 Yellow
Grape 40 Green
```
Output:
![Pie_Chart_Example](https://i.imgur.com/BdwR6QE.png)

#### Donut
Syntax:
```Syntax
Donut Figure_Title(without spaces) Legend_Title(without spaces)
Label1 Percentage Color(optional) Explode
Label2 Percentage Color(optional) Explode
Label4 Percentage Color(optional) Explode
Label5 Percentage Color(optional) Explode
```

Example:
```pmd
Donut Fruit_Share Fruit
Apple 35 Red 0.1
Banana 25
Grape 40 Green
```
Output:
![Donut_Example]()

#### Line Plot
Syntax:
```Syntax
Line Figure_Title(without spaces) Legend_Title(without spaces)
Label1 Points(comma separated, without space) Marker(optional) Linestyle(optional) Color(optional)

```

Example:
```pmd
x 4,6,7,9 o - Blue 
y 1,5,3,6 x -- Lightblue
z 4,9,8,1,6 * : Grey
```

Output:
![Line_Plot_Example]()
