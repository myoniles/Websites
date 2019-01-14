#! /usr/bin/python3

import datetime
import sys
import subprocess
import os.path
import os
from argparse import ArgumentParser

# Handles the arguments passed.
# notes are self explanatory
def getArgs():
	parser = ArgumentParser()
	parser.add_argument("postFile", help="The post file")
	parser.add_argument("-t", "--title", action="store", dest="title", help="Specify the title of the post")
	parser.add_argument("--template", action="store", dest="template", default="templates/post_template.html", help="If, \"-n\" option is selected, chooses the new template the html doc will be based on")
	return parser.parse_args()

def getContent(filename):
	debug = subprocess.check_output(['pandoc' ,filename]).decode('utf-8')
	print(debug)
	return debug

def update_file(filename, new_post, title):
	with open(filename, "r+") as f:
		fileTest = f.read() # this will be fine because the blog file only grows by one line
		to_rp= fileTest.replace("<!-- Last Post Link -->","<a href =\""+new_post+ "\">"+ title+ "</a>\n\t<!-- Last Post Link -->" )
		f.seek(0)
		f.write(to_rp)

def main():
	args = getArgs()
	title = args.title
	if title == None:
		title=args.postFile.split(".")[0]

	cmdLineTitle = title.replace(" ", "_") + ".html"
	with open('posts/'+ cmdLineTitle, "w+") as newFile:
		with open('templates/post_template.html', 'r') as t:
			for line in t:
				line = line.replace('<!-- Post Name -->', title)
				line = line.replace('<!-- Last Post Link -->', "<a href ="+cmdLineTitle+ ">"+ title+ "</a>\n\t<!-- Last Post Link -->")
				line = line.replace('<!-- Content -->', getContent( args.postFile ) )
				newFile.write(line)

	# add to posts block on blog page
	update_file("blog.html", "posts/"+cmdLineTitle, title)
	for post in os.listdir("posts/"):
		if post != cmdLineTitle:
			update_file("posts/"+post, cmdLineTitle, title)


if __name__ == "__main__":
	main()
