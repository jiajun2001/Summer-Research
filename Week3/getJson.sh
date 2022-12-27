for file in *; do
    cd /Users/apple/Desktop/hyperstyle/hyperstyle/src/python/review
    echo "Script executed from: ${PWD}"
    echo "${file}"
    if [ "${file: -3}" == ".py" ]
    then    
        echo "Processing: ${file}"
        (Python run_tool.py /Users/apple/Desktop/SummerResearch/Week3/Dataset2/"${file}" --format=json >> /Users/apple/Desktop/SummerResearch/Week3/JSON_output2/${file%.*}.json)
    else
        echo "Condition not met"
    fi
done