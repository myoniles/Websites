import datetime
import sys
import os.path

if(len(sys.argv) == 3 and os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2])):
	home = open(sys.argv[1], 'r')
	to_post =  open(sys.argv[2])
else:
	print("Usage: python3 htmlEdit.py <fileName>")
	quit();


lines = home.readlines()
post_text = to_post.read()
index = [ i for i in range(len(lines)) if ("Content Begins" in lines[i])]
index = index[0]
title = sys.argv[2].split(".")
title = title[0]

lines.insert(index+1, "<div class=\"content\">\n")
lines.insert(index+2, "<h2>"+ title + "</h2>\n")
lines.insert(index+3, "<p>" + post_text + "</p>\n")
lines.insert(index+4, "<h6>" + str(datetime.datetime.today())[:10] + "</h6>\n")
lines.insert(index+5, "</div>\n")

home.close()

home = open(sys.argv[1], 'w')

print(lines)
for l in lines:
	home.write(l)

home.close()
to_post.close()
