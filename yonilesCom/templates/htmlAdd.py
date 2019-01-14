#! /usr/bin/python3

import datetime
import sys
from subprocess import call
import os.path
from argparse import ArgumentParser

# Handles the arguments passed.
# notes are self explanatory
def getArgs():
	parser = ArgumentParser()
	parser.add_argument("htmlFile", help="The html file being posted to")
	parser.add_argument("postFile", help="The post file")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False)
	parser.add_argument("-f", "--formatted", action="store_true", dest="formatted", default=False, help="The postFile is already formatted html")
	parser.add_argument("p", "--pandoc", "-f", "--Format", dest="callPandoc", action = "store_true", default=False, help="Specify that the arg is not html but You would like it to be")
	parser.add_argument("-n", "--newFile", action="store", dest="newFileName", help="Specifies a filename to dump a new standalone html file")
	parser.add_argument("-s", "--standalone", action="store_true", dest="standalone", default=False, help="creates a standalone file in \"./post/\"")
	parser.add_argument("-t", "--title", action="store", dest="title", help="Specify the title of the post")
	parser.add_argument("--template", action="store", dest="template", default="templates/post_template.html", help="If, \"-n\" option is selected, chooses the new template the html doc will be based on")
	return parser.parse_args()

# takes a post
# if formatted, it will shove the text in between some paragraph markers call it a day
# Else it will treat it as is.
def get_post_text( to_post_file, formatted=False, title=None, standalone=None):
	with open(to_post_file) as postFile:
		lines = postFile.readlines()
		if standalone != None:
			lines.insert(0,"<h2> <a href=\"" + standalone + "\">"+ title + "</a></h2>\n")
		else:
			lines.insert(0,"<h2>"+ title + "</h2>\n")
		lines.insert(0,"<div class=\"content\" id=\""+ title +"\">\n")
		lines.append("<h6>" + str(datetime.datetime.today())[:10] + "</h6>\n")
		lines.append("</div>\n")
	return lines

def get_new_text(post_text, newFileName):
	with open(newFileName) as newFile:
		lines = newFile.readlines()
		index = [i for i in range(len(lines)) if ("Content Begins" in lines[i])]
		index = index[0] +1
		for line in post_text:
			lines.insert(index, line)
			index = index +1
		return lines

def paste_to(postText, htmlFileName):
	with open(htmlFileName, "w") as htmlFile:
		for line in postText:
			htmlFile.write(line)

def main():
	args = getArgs()
	title = args.title
	if title == None:
		title=args.postFile.split(".")[0]

	if args.standalone and args.newFileName == None:
		cmdLineTitle = "posts/"+title.replace(" ", "_") + ".html"
	else:
		cmdLineTitle = args.newFileName

	postText = get_post_text(args.postFile, formatted = args.formatted, title=title, standalone=cmdLineTitle)
	new_text = get_new_text(postText, args.htmlFile)
	paste_to(new_text, args.htmlFile)

	if args.verbose:
		print(new_text)

	if args.standalone:
		postText = get_post_text(args.postFile, formatted = args.formatted, title=title)
		new_text= get_new_text(postText, args.template)
		if args.newFileName != None:
			paste_to(new_text, args.newFileName)
		else:
			paste_to(new_text, cmdLineTitle)
	return

if __name__ == "__main__":
	main()
