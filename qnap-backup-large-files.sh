#/bin/sh

source ./.qnap-bash.sh

GetLargeFileExtensions INCLUDE "--include=\"" "\""
GetGitModulePaths EXCLUDE "--exclude=\"" "\""

ARGS="-zarv --prune-empty-dirs --delete"
FIXED_EXCLUDES="--exclude=\".git/\" --exclude=\".idea/\""
SERVER="admin@scrier.myqnapcloud.com"
TARGET="/share/rsync/udacity"
SOURCE="."

COMMAND="rsync $ARGS $FIXED_EXCLUDES --include=\"*/\" $INCLUDE --exclude=\"*\" $SOURCE $SERVER:$TARGET"

echo $COMMAND

eval $COMMAND
