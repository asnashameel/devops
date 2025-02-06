echo "enter the file name"
read -r file

if [ -f $file ]; then
    echo "file exist"
else
    echo "file doesnt exist"
fi
