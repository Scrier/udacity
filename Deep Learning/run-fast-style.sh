#/bin/sh

if [[ $# -eq 1 ]]; then
    INPUT="../${1}"
else
    echo "Missing input file: use $0 <input-file>"
    exit 1;
fi

prompt="Please select a file:"
options=( $(find fast-style/*.ckpt -maxdepth 1 -print0 | xargs -0) )

PS3="$prompt "
select opt in "${options[@]}" "Quit" ; do
    if (( REPLY == 1 + ${#options[@]} )) ; then
        exit

    elif (( REPLY > 0 && REPLY <= ${#options[@]} )) ; then
        echo  "You picked $opt which is file $REPLY"
        break

    else
        echo "Invalid option. Try another one."
    fi
done

CKPT="../$opt"

PWD=`pwd`

cd fast-style-transfer

~/anaconda2/bin/python evaluate.py --checkpoint $CKPT --in-path $INPUT --out-path ../output.jpg

cd "$PWD"
