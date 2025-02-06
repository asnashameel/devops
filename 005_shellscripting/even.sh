#!/bin/bash
#purpose:write a shellscript to check  number

echo "enter a number"
read -r no

if ((no % 2 == 0)); then
    echo "no is even"
else
    echo "no is odd"
fi