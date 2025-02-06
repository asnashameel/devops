#!/bin/bash
#purpose:to write the directory size
# print_size(){
#     local_directory="$1"
#     local_size=0
    size=du -h "$directory"
    echo "size of directory: $size"
# }

echo "please enter directory path"
read -r directory
du -h "$directory"
# echo "size of directory: $s"
# print_size $directory