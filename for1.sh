#!/bin/bash
#author: Asna 
#Purpose: Learning variables
#Usage: ./for.sh




fruits=("apple" "orange" "banana")
for i in "${!fruits[@]}"; do
	if  ((i % 2 == 0 )); then 
	
		echo " i like to eat ${fruits[$i]}"
	else
		echo "i dont like to eat ${fruits[$i]}"
		
	fi
done


num=0
fruits=("apple" "orange" "banana")
for i in "${!fruits[@]}"; do
	if [ $(expr $num % 2) -eq 0 ]; then
    		echo "i like to eat ${fruits[$i]}"
	else
    		echo "i dont like to eat ${fruits[$i]}"
	fi
	((num++))
done