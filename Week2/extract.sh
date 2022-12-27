index=0

for dir in */; do 
    echo $dir
    cd "$dir"
    for file in *
    do
        if [ "${file: -6}" == ".ipynb" ]
        then
            $(ipynb-py-convert "$file" "solution${index}.py")
            let "index=index+1"
        else 
            mv "$file" "${file/*/solution${index}.py}"
            let "index=index+1"
        fi
    done
    $(mv *.py ../)
    cd "../"
done




