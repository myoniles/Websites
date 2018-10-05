#! /usr/bin/python3

import datetime
import sys
import os.path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("htmlFile", help="The html file being posted to")
parser.add_argument("postFile", help="The post file")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False)
parser.add_argument("-f", "--formatted", action="store_true", dest="formatted", default=False, help="The postFile is already formatted html")
args=parser.parse_args()

htmlFile = open(args.htmlFile)
postFile = open(args.postFile)

lines = htmlFile.readlines()
post_text = postFile.read()
index = [ i for i in range(len(lines)) if ("Content Begins" in lines[i])]
index = index[0]
title = sys.argv[2].split(".")
title = title[0]

lines.insert(index+1, "<div class=\"content\" id=\""+ title +"\">\n")
lines.insert(index+2, "<h2>"+ title + "</h2>\n")
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
