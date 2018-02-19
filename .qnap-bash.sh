#!/usr/bin/env bash

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
    while read line; do
        if [[ $line = *"Large Files"* ]]; then
            FOUND=true
        elif $FOUND; then
            if [[ -z "$line" ]]; then
                FOUND=false
            else
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
