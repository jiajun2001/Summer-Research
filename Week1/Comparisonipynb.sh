for file in *; do
    if [ "${file: -6}" == ".ipynb" ]
    then
        (echo "********** ${file}" >> outputipynb.txt)
        (ipython -c "%run ${file}" < input.txt | sed 's/\x1B\[[0-9;]\{1,\}[A-Za-z]//g' >> outputipynb.txt)
    else
        echo "Condition not met"
    fi
done
