#!/bin/zsh

# This file takes a html filename as argument $1
# and a txt or md filename as argument $2
# it then will change file $2 into a prepared html doc using pandoc
# pandoc code will be inserted into $1
# $2 will move to the posts directory

# Get the files names
# This code will be run if no user input is specified
if [ -z "$1" ]; then
	echo "What file are you posting to?"
	read html
	if [ ! -f "./$html" ]; then
		echo "Html filename not found"
		return
	fi
	echo "Post filename:"
	read post
	if [ ! -w "./$post" ]; then
		echo $post
		echo "Post filename not found"
		return
	fi
else
	# For readability sake we rename the variables
	html="$1"
	post="$2"
fi

html=${html/%"\ "/"_"}
post=${post/%"\ "/"_"}

# File type checking
# Just check html type
if [ ! "${html: -5}" '==' ".html" ]; then
	echo "Not posting to an html file"
	return
fi

# if text or md file, first we must pandoc it
if [ "${post: -4}" '==' ".txt" ]; then
	pandoc "./$post" -o "${post/%"txt"/"html"}"
	post=${post/%"txt"/"html"}
elif [ "${post: -3}" '==' ".md" ]; then
	pandoc "./$post" -o "${post: -3}.html"
	post="${post: -3}.html"
elif [ ! "${post: -5}" '==' ".html" ]; then
	echo "incorrect post filetype"
	return
fi

"./htmlAdd.py ./$html ./$post -f -t template.html -n posts/$post"
rm "$post"

echo "$html"
echo "$post"
