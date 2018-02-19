#/bin/sh

source ./.qnap-bash.sh

GetLargeFileExtensions INCLUDE "--include=\"" "\""
GetGitModulePaths EXCLUDE "--exclude=\"" "\""

ARGS="-zarv --delete-after"
FIXED_EXCLUDES="--exclude=\".git/\" --exclude=\".idea/\""
SERVER="admin@scrier.myqnapcloud.com"
SOURCE="/share/rsync/udacity/"
TARGET="."

COMMAND="rsync $ARGS $FIXED_EXCLUDES $EXCLUDE --include=\"*/\" $INCLUDE --exclude=\"*\" $SERVER:$SOURCE $TARGET"

echo $COMMAND

eval $COMMAND
