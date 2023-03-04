## How To Remove Single Line Comments..?

I was recently working on a college project ([pyamaid]()) of mine which was similar to markup and wanted to add comment support to it. As comments are very useful for documentation and I find these a blessing, I wanted to ensure my project had this feature too. So, I set out to write code for parsing these. I failed in quite a few approaches of mine but then I succeeded and wanted to share the joy of having successfully coded a comment remover.

I wanted to implement comments starting with “#”. After failing multiple times I set two basic rules for myself:

- If the first character of the line is ‘#’ remove the whole line.

- If the number of apostrophes or quotes before the “#” symbol are even then remove everything from the “#” symbol to the end of the line.

Having set these two rules, I now had a direction for myself to move in. I was testing my code against the following text:

`test.txt`
```python
#this is a comment
this is not a "#comment"
this is a # comment and #this follows in
"#this is not a comment" but #this is
"# not a comment"
```
#### Implementing the first rule is as easy as:

```python
with open("test.txt","r") as file:
	text = file.read()

lines = text.strip().split('\n')	# splitting lines 
comments = []	# to store commented lines for removal
for line in lines:
	if(line[0] == "#"):
		comments.append(line)

for line in comments:
	lines.remove(line)
```

Doing this removes all the lines that start with a “#”. Now, we head on to the second rule which was quite interesting to implement. Here is how it goes:

- Maintain a list with indexes of apostrophes, quotes and hash symbols for each line. And a separate list of indexes of comments for each line

- Count the number of apostrophes and quotes for each hash whose index is less than that of the hash itself. Two cases arise here:

	- If the count of apostrophes as well as quotes is even then add the index of the hash symbol to the comment list and do not check for the remaining hash symbols.

	- If the count of apostrophes or the quotes is not even then check for the next hash in the line, if there are no more hashes in the line add 0 as an index to the comments list.

- Now we have the indexes of the start of comments in each line and lines which do not have a comment have an index of 0 for them.Therefore, we’ll now move ahead to remove text starting at the index of the hash to the end of the line in order to remove the comment. And would do nothing in case the index is 0 as the line doesn’t have any comment.

#### Here’s the full Implementation of the rule appended to the above code:

```python
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
new_text = \n'.join(new_text)
```

Though not the best solution, this worked for me. I hope I was able to write a tidy article on my experience. I am a happy man after having implemented this tiny feature. I am well aware of popular tools such as regex and wouldn’t  wonder if someone came with some regex expression to remove comments (It would be tough though).
