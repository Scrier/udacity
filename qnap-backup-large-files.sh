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

ARGS="$DRY_RUN-zarv --prune-empty-dirs --delete"
FIXED_EXCLUDES="--exclude=\".git/\" --exclude=\".idea/\""
SERVER="admin@scrier.myqnapcloud.com"
TARGET="/share/rsync/udacity"
SOURCE="."

COMMAND="rsync $ARGS $FIXED_EXCLUDES --include=\"*/\" $INCLUDE --exclude=\"*\" $SOURCE $SERVER:$TARGET"

echo $COMMAND

eval $COMMAND
