mkdir newfolder

echo "enter the folder"
read -r f
zip_file="${f}.zip"
zip -r "zip_file" "$f"
# echo "folder '$f' has zipped succesfully as '{$f}.zip'."
if [ -f "$zip_file" ]; then
    echo "Folder '$folder' has been zipped successfully as '$zip_file'."
else
    echo "Error: Zipping failed!"
fi