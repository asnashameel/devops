echo "enter the folder"
read -r f
zip -r {f.zip} . -i f
