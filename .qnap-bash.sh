#!/usr/bin/env bash

SKIP_SYNC=.skipsync

function GetGitModulePaths() {
    local __resultback=$1
    local prefix=$2
    local postfix=$3
    PATHS=""
    while read line; do
        if [[ $line =~ path ]]; then
            value=$(echo $(cut -d "=" -f 2 <<< "$line") | xargs)
            if [[ -z "$PATHS" ]]; then
                PATHS+="$prefix$value$postfix"
            else
                PATHS+=" $prefix$value$postfix"
            fi
        fi
    done < .gitmodules
    eval $__resultback="'$PATHS'"
}

function GetLargeFileExtensions() {
    local __resultback=$1
    local prefix=$2
    local postfix=$3
    EXTENSIONS=""
    FOUND=false
    GetFilteredItems FILTER
    echo $FILTER
    while read line; do
        if [[ $line = *"Large Files"* ]]; then
            FOUND=true
        elif $FOUND; then
            if [[ -z "$line" ]]; then
                FOUND=false
            elif [[ $FILTER = *"$line"* ]]; then
                echo "Skipping $line as it is filtered in $SKIP_SYNC!"
            else
                # echo "$FILTER doesn't contain $line"
                if [[ -z "$EXTENSIONS" ]]; then
                    EXTENSIONS+="$prefix$line$postfix"
                else
                    EXTENSIONS+=" $prefix$line$postfix"
                fi
            fi
        fi
    done < .gitignore
    eval $__resultback="'$EXTENSIONS'"
}

function GetFilteredItems() {
    local __resultback=$1
    RESULT=()
    if [ ! -f $SKIP_SYNC ]; then
        touch $SKIP_SYNC
        echo "# Add file extensions that should not be synced in this file. One for each row." >> $SKIP_SYNC
        echo "# You will find the files being synced in .gitignore under Large Files category." >> $SKIP_SYNC
        echo "" >> $SKIP_SYNC
        echo "Missing file $SKIP_SYNC, I have created it and let you add the extension you wan't skipped. Pass if you
        are happy with syncing all"
        exit 1
    else
        while read line; do
            if [[ ! $line =~ '#' ]] && [[ ! -z "$line" ]]; then
                RESULT+=$line
            fi
        done < .skipsync
    fi
    eval $__resultback="'$RESULT'"
}
