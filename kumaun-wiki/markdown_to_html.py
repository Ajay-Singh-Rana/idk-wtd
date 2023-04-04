# h3avren
import sys

filename = sys.argv[1]
with open(filename, 'r') as file:
    text = file.read()

text = text.strip()
text = text.split('\n')

"""emoji_dict = {':smile:': , ':heart_eyes:' : , ':wink:' : , ':expressionless:' : ,
              ':scream:' : , ':rage:' : , ':pensive:' : , ':sob:' : , ':joy:' : , ':mask:' : ,
              ':heart:' : , ':fire:' : , ':poop:' : ,
              ':+1:' : , ':-1:' : , ':raised_hands:' : , ':point_up:' : 
            }"""

no_flag = True
new_text = []
checkbox_flag = False
checkbox_list_items = {}
wait_flag = False
held_items = []
ordered_flag = False
ordered_list_items = []
unordered_flag = False
unordered_list_items = []
table_flag = False
table_details = {"columns" : [],"alignment":[]}

for line in text:
    if(table_flag):
        if(line == "endtable%"):
            alignment = table_details['alignment']
            header = table_details.get('header')
            columns = table_details.get('columns')
            if(alignment == []):
                alignment = ['center' for i in range(len(max(columns)))]
            if(header):
                markup = "<table><tr>"
                for (data,align) in zip(header,alignment):
                    markup += f"<th style='text-align : {align}'>{data}</th>"
                markup += "</tr>"
            else:
                markup = "<table>"
            for col in columns:
                markup += "<tr>"
                for (data,align) in zip(col,alignment):
                    markup += f"<td style='text-align: {align}'>{data}</td>"
                markup+= "</tr>"
            markup += "</table>"
            new_text.append(markup)
            table_flag = False
            no_flag = True
            table_details = {"columns" : [], "alignment" : []}
            continue
        else:
            if(line[0] == "!"):
                line = line[1:].split("|")
                alignment = []
                headers = []
                for col in line:
                    col = col.strip()
                    if(col[0] == ":" and col[-1] == ":"):
                        alignment.append("center")
                        headers.append(col[1:-1])
                    elif(col[0] == ":"):
                        alignment.append("left")
                        headers.append(col[1:])
                    elif(col[-1] == ":"):
                        alignment.append("right")
                        headers.append(col[:-1])
                    else:
                        alignment.append("center")
                        headers.append(col[1 : -1])

                table_details["header"] = headers
                table_details["alignment"] = alignment
            else:
                columns_data = line.split("|")
                columns = table_details['columns']
                columns.append(columns_data)
                table_details["columns"] = columns
    elif(checkbox_flag):
        if(line[0:6] in ["- [ ] ", "- [x] ", "- [X] "]):
            if(line[3] == " "):
                checkbox_list_items[line[6 : ]] = False
            else:
                checkbox_list_items[line[6 : ]] = True
        else:
            markup = "<ul style='list-style-type : none;'>"
            for (text,checked) in checkbox_list_items.items():
                if(checked):
                    markup += f'<li><input type="checkbox" checked="{checked}"/>{text}</li>'
                else:
                    markup += f'<li><input type="checkbox"/>{text}</li>'
            markup += "</ul>"
            checkbox_list_items = {}
            checkbox_flag = False
            no_flag = True
            new_text.append(markup)
    elif(ordered_flag):
        if((line[0].isnumeric() == True) and line[1] == '.' and line[2] == ' '):
            ordered_list_items.append(line[3:])
        else:
            markup = '<ol>'
            for li in ordered_list_items:
                markup += '<li>' + li + '</li>'
            markup += '</ol>'
            ordered_list_items = []
            ordered_flag = False
            no_flag = True
            new_text.append(markup)
    elif(unordered_flag):
        if((line[0] == '-' or line[0] == '*' or line[0] == '+') and line[1] == ' '):
            unordered_list_items.append(line[2 : ])
        else:
            markup = '<ul>'
            for li in unordered_list_items:
                markup += '<li>' + li + '</li>'
            markup += '</ul>'
            unordered_list_items = []
            unordered_flag = False
            no_flag = True
            new_text.append(markup)
    elif(wait_flag):
        if(line == '```'):
            markup = '<code style="display: block">'
            for code in held_items:
                markup += code + '<br/>'
            markup += '</code>'
            new_text.append(markup)
            wait_flag = False
            no_flag = True
            held_items = []
        else:
            held_items.append(line)
    
    if(no_flag):
        if(line[0] == '#'):
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
            no_flg = False
        elif((line[0].isnumeric() == True) and line[1] == '.' and line[2] == ' '):
            ordered_flag = True
            no_flag = False
            ordered_list_items.append(line[3 :])
        elif(line[0 : 6] in ["- [ ] ", "- [x] ", "- [X] "]):
            checkbox_flag = True
            no_flag = False
            if(line[3] == " "):
                checkbox_list_items[line[6 : ]] = False
            else:
                checkbox_list_items[line[6 : ]] = True
        elif((line[0] == '-' or line[0] == '+' or line[0] == '*') and line[1] == ' '):
            unordered_flag = True
            no_flag = False
            unordered_list_items.append(line[2 : ])
        elif(line == "%starttable"):
            table_flag = True
            no_flag = False
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
    while(new_text[i].find("~~") != -1):
        index = new_text[i].find("~~")
        if(count%2 == 0):
            new_text[i] = new_text[i][0: index] + '<del>' + new_text[i][index + 2 : ]
        else:
            new_text[i] = new_text[i][0 : index] + '</del>' + new_text[i][index + 2 : ]
        count += 1
    if(count%2 != 0):
        index = new_text[i][::-1].find('>led<') + 1 + 4 # 4 is the remaining length of the markup
        new_index = len(new_text[i]) - index
        new_text[i] = new_text[i][0: new_index] + "~~" + new_text[i][new_index + 5 : ]
    temp_text = new_text[i].split(' ')
    for word_num in range(len(temp_text)):
        count = 0
        while(temp_text[word_num].find('^') != -1):
            index = temp_text[word_num].find('^')
            if(count%2 == 0):
                temp_text[word_num] = temp_text[word_num][0:index] + '<sup>' + temp_text[word_num][index + 1:]
            else:
                temp_text[word_num] = temp_text[word_num][0 :index] + '</sup>' + temp_text[word_num][index + 1 :]
            count += 1
        if(count%2 != 0):
            index = temp_text[word_num][::-1].find('>pus<') + 1 + 4 # 4 is the length of the remaining string 1 is for adjustment
            new_index = len(temp_text[word_num]) - index
            temp_text[word_num] = temp_text[word_num][0: new_index] + '^' + temp_text[word_num][new_index + 5 :]    # 5 is the length of the markup
    new_text[i] = ' '.join(temp_text)
    temp_text = new_text[i].split(' ')
    for word_num in range(len(temp_text)):
        count = 0
        while(temp_text[word_num].find('~') != -1):
            index = temp_text[word_num].find('~')
            if(count%2 == 0):
                temp_text[word_num] = temp_text[word_num][0 : index] + '<sub>' + temp_text[word_num][index + 1 :]
            else:
                temp_text[word_num] = temp_text[word_num][0 : index] + '</sub>' + temp_text[word_num][index + 1 :]
            count += 1
        if(count%2 != 0):
            index = temp_text[word_num][::-1].find('>bus<') + 1 + 4 # 4 is the remaining words in the markup
            new_index = len(temp_text[word_num]) - index
            temp_text[word_num] = temp_text[word_num][0 : new_index] + '~' + temp_text[word_num][new_index + 5 : ]  #5 is the length of the markup
    new_text[i] = ' '.join(temp_text)
    count = 0
    while(new_text[i].find('`') != -1):
        index = new_text[i].find('`')
        if(count%2 == 0):
            new_text[i] = new_text[i][0 : index] + '<code>' + new_text[i][index + 1 : ]
        else:
            new_text[i] = new_text[i][0 : index] + '</code>' + new_text[i][index + 1 : ]
        count += 1
    if(count%2 != 0):
        index = new_text[i][::-1].find('>edoc<') + 1 + 5    # 5 is the remaining length of the markup
        new_index = len(new_text[i]) - index
        new_text[i] = new_text[i][0 : new_index] + '`' + new_text[i][new_index + 6 : ]
    count = 0
    while(new_text[i].find('*') != -1):
        index = new_text[i].find('*')
        if(count%2 == 0):
            new_text[i] = new_text[i][0 : index] + '<em>' + new_text[i][index + 1 :]
        else:
            new_text[i] = new_text[i][0 : index] + '</em>' + new_text[i][index + 1 : ]
        count += 1
    if(count%2 != 0):
        index = new_text[i][::-1].find('>me<') + 1 + 3   # add 1 as index starts at 0 and add 2 as it is the remaining length of the string
        new_index = len(new_text[i]) - index
        new_text[i] = new_text[i][0 : new_index] + '*' + new_text[i][new_index + 4 : ]
    # count = 0     # need not reset as it is not required to do so for spoilers
    while(new_text[i].find('>!') != -1):
        start_index = new_text[i].find('>!')
        end_index = new_text[i].find('!<')
        if(end_index == -1):
            break
        else:
            new_text[i] = new_text[i][: start_index] + "<span class='spoiler'>" \
                          + new_text[i][start_index + 2 : end_index] + "</span>" \
                          + new_text[i][end_index + 2 : ]
            count += 1
    # finding and replacing images
    while(new_text[i].find('![') != -1):
        image_index = new_text[i].find('![')
        alt_text_end = new_text[i][image_index : ].find('](')
        if(alt_text_end != -1):
            alt_text = new_text[i][image_index + 2 : image_index + alt_text_end]
            image_end_index = new_text[i][image_index + alt_text_end + 1 : ].find(')')
            if(image_end_index != -1):
                image_end_index += image_index + alt_text_end + 1
                link = new_text[i][image_index + alt_text_end + 2 : image_end_index]
            sub_string = new_text[i][image_index : image_end_index + 1]
            image_markup = f'<img src="{link}" alt="{alt_text}" />'
            new_text[i] = new_text[i].replace(sub_string, image_markup)
        else:
            break
    # finding and replacing links
    while(new_text[i].find('[') != -1):
        link_index = new_text[i].find('[')
        link_text_end = new_text[i][link_index : ].find('](')
        if(link_text_end != -1):
            link_text = new_text[i][link_index + 1 : link_index + link_text_end]
            link_end_index = new_text[i][link_index + link_text_end + 1 : ].find(')')
            if(link_end_index != -1):
                link_end_index += link_index + link_text_end + 1
                link = new_text[i][link_index + link_text_end + 2 : link_end_index]
            sub_string = new_text[i][link_index : link_end_index + 1]
            link_markup = f"<a href='{link}'>{link_text}</a>"
            new_text[i] = new_text[i].replace(sub_string, link_markup)
        else:
            break

with open('xyz.html', 'w') as file:
    initials = """<!DOCTYPE html>
                  <html>
                  <head>
                    <link href='md.css' rel='stylesheet' type='text/css' />
                  </head>
                  <body>
               """
    final = "</body></html>"
    file.write(initials)
    file.write('\n'.join(new_text))
    file.write(final)
#print('\n'.join(new_text))
