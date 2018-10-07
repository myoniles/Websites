#! /usr/bin/python3

import datetime
import sys
import os.path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("htmlFile", help="The html file being posted to")
parser.add_argument("postFile", help="The post file")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False)
parser.add_argument("-f", "--formatted", action="store_true", dest="formated", default=False, help="The postFile is already formatted html")
parser.add_argument("-n", "--newFile", action="store", dest="newFileName", help="Specifies a filename to dump a new standalone html file")
parser.add_argument("-t", "--title", action="store", dest="title", help="Specify the title of the post")
parser.add_argument("--template", action="store", dest="template", default="template.html", help="If, \"-n\" option is selected, chooses the new template the html doc will be based on")
args=parser.parse_args()

htmlFile = open(args.htmlFile)
postFile = open(args.postFile)

lines = htmlFile.readlines()
post_text = postFile.read()
index = [ i for i in range(len(lines)) if ("Content Begins" in lines[i])]
index = index[0]

if (args.title != None):
	title = sys.argv[2].split(".")
	# make an assumption that if the filetype is html that the input is formated
	if title[1] == "html":
		args.formated = True
	title = title[0]
else:
	title = args.title

lines.insert(index+1, "<div class=\"content\" id=\""+ title +"\">\n")
lines.insert(index+2, "<h2>"+ title + "</h2>\n")
if args.formated:
	lines.insert(index+3, post_text + "\n")
else:
	# is it Jank?
	# yes
	lines.insert(index+3, "<p>" + post_text + "</p>\n")
lines.insert(index+4, "<h6>" + str(datetime.datetime.today())[:10] + "</h6>\n")
lines.insert(index+5, "</div>\n")

htmlFile.close()

htmlFile = open(sys.argv[1], 'w')

if args.verbose:
	print(lines)

for l in lines:
	htmlFile.write(l)

htmlFile.close()
postFile.close()

if args.newFileName != None:
	with open(args.template) as fileTemplate:
		with open(args.newFileName, "w+") as newFile:
			lines = fileTemplate.readlines()
			index = [ i for i in range(len(lines)) if ("Content Begins" in lines[i])]
			index = index[0]
			lines.insert(index+1, "<div class=\"content\" id=\""+ title +"\">\n")
			lines.insert(index+2, "<h2>"+ title + "</h2>\n")
			if args.formated:
				lines.insert(index+3, post_text + "\n")
			else:
				# is it Jank?
				# yes
				lines.insert(index+3, "<p>" + post_text + "</p>\n")
			lines.insert(index+4, "<h6>" + str(datetime.datetime.today())[:10] + "</h6>\n")
			lines.insert(index+5, "</div>\n")
			for l in lines:
				newFile.write(l)
