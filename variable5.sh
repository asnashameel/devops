#!/bin/bash
#author: Asna 
#Purpose: Learning variables
#Usage: ./variable.sh

file=$1
if [ -f "$file" ]; then

	echo "file exist $file"
else
	echo "file doesnot exist"
fi
if [ -f $file ]; then
	echo "file exist $file"
else
	echo "file doesnot exist"
 
fi
 file=$1
if [[ -f "$file" ]]; then

	echo "file exist $file"
else
	echo "file doesnot exist"
fi
if [ -f "$file" ]; then

	echo "file exist $file"
else
	echo "file doesnot exist"
fi
i
 

