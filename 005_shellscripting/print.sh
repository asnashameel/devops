#!/bin/bash
#purpose:write a shellscript to print the fun
print() {
    local message="$1"
    echo "message passed: $message"
}

# print_new{
#     args: string message

# }{
#     echo "$new_message"
# }

echo "enter the message you want to print:"
read -r message
print "$message"