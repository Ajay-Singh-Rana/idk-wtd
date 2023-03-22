# h3avren
import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    text = file.read()

text = text.strip()
text = text.split('\n')

new_text = []
wait_flag = False
held_items = []
ordered_flag = False
ordered_list_items = []
unordered_flag = False
unordered_list_items = []

for line in text:
    if(ordered_flag):
        if((line[0].isnumeric() == True) and line[1] == '.' and line[2] == ' '):
            ordered_list_items.append(line)
        else:
            markup = '<ol>'
            for li in ordered_list_items:
                markup += '<li>' + li + '</li>'
            markup += '</ol>'
            ordered_list_items = []
            ordered_flag = False
            new_text.append(markup)
            new_text.append('<p>' + line + '</p>')
    elif(unordered_flag):
        if((line[0] == '-' or line[0] == '*' or line[0] == '+') and line[1] == ' '):
            unordered_list_items.append(line)
        else:
            markup = '<ul>'
            for li in unordered_list_items:
                markup += '<li>' + li + '</li>'
            markup += '</ul>'
            unordered_list_items = []
            unordered_flag = False
            new_text.append(markup)
            new_text.append(line)
    elif(wait_flag):
        if(line == '```'):
            markup = '<code>'
            for code in held_items:
                markup += code + '<br/>'
            markup += '</code>'
            new_text.append(markup)
            wait_flag = False
            held_items = []
        else:
            held_items.append(line)
    elif(line[0] == '#'):
        count = 1
        flag = False
        for literal in line[1:]:
            if(literal == '#'):
                count += 1
            elif(literal == ' '):
                flag = True
                break
            else:
                break
        if(flag and count <= 6):
            new_text.append(f'<h{count}>' + line[(count + 1):]+ f'</h{count}>')
        else:
            new_text.append('<p>' + line + '</p>')
    elif(line[0] == '>' and line[1] == ' '):
        new_text.append('<blockquote style="border-left: 1vw Solid #2a8bdc;">' + line[2:] + '</blockquote>')
    elif(line == '***' or line == '___' or line == '---'):
        new_text.append('<hr/>')
    elif(line == '```'):
        wait_flag = True
    elif((line[0].isnumeric() == True) and line[1] == '.' and line[2] == ' '):
       ordered_flag = True
       ordered_list_items.append(line)
    elif((line[0] == '-' or line[0] == '+' or line[0] == '*') and line[1] == ' '):
        unordered_flag = True
        unordered_list_items.append(line)
    else:
        new_text.append('<p>' + line + '</p>')

for i in range(0,len(new_text)):
    if(new_text[i][:6] == '<code>'):
        continue
    count = 0
    while(new_text[i].find("**") != -1):
        index = new_text[i].find("**")
        if(count%2 == 0):
            new_text[i] = new_text[i][0 : index] + '<b>' + new_text[i][index + 2 : ]
        else:
            new_text[i] = new_text[i][0 : index] + '</b>' + new_text[i][index + 2 : ]
        count += 1
    if(count%2 != 0):
        index = new_text[i][::-1].find('>b<') + 1 + 2   # 2 is the length of the remaining string
        new_index = len(new_text[i]) - index
        new_text[i] = new_text[i][0: new_index] + "**" + new_text[i][new_index + 3 : ]
    count = 0
    while(new_text[i].find("==") != -1):
        index = new_text[i].find("==")
        if(count%2 == 0):
            new_text[i] = new_text[i][0 : index] + '<mark>' + new_text[i][index + 2 : ]
        else:
            new_text[i] = new_text[i][0 : index] + '</mark>' + new_text[i][index + 2 : ]
        count += 1
    if(count%2 != 0):
        index = new_text[i][::-1].find('>kram<') + 1 + 5   # 5 is the remaining length of the markup
        new_index = len(new_text[i]) - index
        new_text[i] = new_text[i][0: new_index] + "==" + new_text[i][new_index + 6 : ]
    count = 0

with open('xyz.html', 'w') as file:
    file.write('\n'.join(new_text))


print('\n'.join(new_text))
