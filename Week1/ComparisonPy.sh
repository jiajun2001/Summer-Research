for file in *; do
    if [ "${file: -3}" == ".py" ]
    then
        (echo "********** ${file}" >> outputPy.txt)
        (Python $file < input.txt 2>> outputPy.txt)
    else
        echo "Condition not met"
    fi
done