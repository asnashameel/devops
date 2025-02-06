#!/bin/bash
#purpose:write a shellscript to write fibonacci number

echo "enter a number"
read -r n
if [ "$n" -le 0 ];then
    echo "no not found"
    exit 0
fi

 a=0
 b=1
 for (( i=0;i<n;i++ )); do
    echo -n "$a "
    c=$((a + b))
    a=$b
    b=$c
done

echo
