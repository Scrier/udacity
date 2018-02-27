#/bin/sh


POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -dr|--dry-run)
    DRY_RUN="--dry-run "
    shift # past argument
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done


source ./.qnap-bash.sh

GetLargeFileExtensions INCLUDE "--include=\"" "\""
GetGitModulePaths EXCLUDE "--exclude=\"" "\""

ARGS="$DRY_RUN-zarv --delete-after"
FIXED_EXCLUDES="--exclude=\".git/\" --exclude=\".idea/\""
SERVER="admin@scrier.myqnapcloud.com"
SOURCE="/share/rsync/udacity/"
TARGET="."

COMMAND="rsync $ARGS $FIXED_EXCLUDES $EXCLUDE --include=\"*/\" $INCLUDE --exclude=\"*\" $SERVER:$SOURCE $TARGET"

echo $COMMAND

eval $COMMAND
