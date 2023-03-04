# h3avren

def parse_comments(text):
    lines = text.strip().split('\n')
    literals_indexes = []
    comments = []
    for line in lines:
        if(line[0] == '#'):
            comments.append(line)
        else:
            index_apos = []
            index_quote = []
            index = []
            for (i,char) in enumerate(line):
                if(char == "'"):
                    index_apos.append(i)
                if(char == '"'):
                    index_quote.append(i)
                if(char == '#'):
                    index.append(i)
            literals_indexes.append([index_apos,index_quote,index])

    for comment in comments:
        lines.remove(comment)
    comments = []
    for indexes in literals_indexes:
        if(indexes[2] != []):
            for hashes in indexes[2]:
                count_apos = 0
                count_quotes = 0
                append_flag = False
                if(indexes[0] != []):
                    for apos in indexes[0]:
                        if(apos < hashes):
                            count_apos += 1
                        else:
                            break
                if(indexes[1] != []):
                    for quotes in indexes[1]:
                        if(quotes < hashes):
                            count_quotes += 1
                        else:
                            break
                if(((count_apos % 2) == 0) and ((count_quotes % 2) == 0)):
                    append_flag = True
                    comments.append(hashes)
                    break
            if(not append_flag):
                comments.append(0)
        else:
            comments.append(0)

    new_text = []
    for (line,index) in zip(lines,comments):
        if(index != 0):
            line = line.replace(line[index:],"")
        new_text.append(line)

    return '\n'.join(new_text)

if __name__ == "__main__":
    import sys
    file_name = sys.argv[1] 
    with open(file_name,'r') as file:
        text = file.read()
    print(parse_comments(text))
