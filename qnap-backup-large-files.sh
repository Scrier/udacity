#/bin/sh

#if [ "$HOSTNAME" = gpu02 ]; then
#  rsync -zarv --prune-empty-dirs --delete --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" \
#    --include="*.tar.gz" --include="*.bin" --include="*.tar.gz" --include="*.npz" --include="*.zip" --exclude="*" . \
#    ../large-items/
#else
#  rsync -zarv --prune-empty-dirs --delete --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" \
#    --include="*.tar.gz" --include="*.bin" --include="*.npz" --include="*.zip" --exclude="*" . \
#    andreas@gpu02:./large-items/
#fi

#rsync -zarv -e ssh --prune-empty-dirs --delete --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle"
# --include="*.tar.gz" --include="*.bin" --include="*.npz" --include="*.zip" --exclude="*" .
# admin@scrier.myqnapcloud.com:/share/rsync/udacity

source ./qnap-shared.sh

GetLargeFileExtensions INCLUDE "--include=\"" "\""

ARGS="-zarv -e ssh --prune-empty-dirs"
SERVER="admin@scrier.myqnapcloud.com"
TARGET="/share/rsync/udacity"
SOURCE="."

COMMAND="rsync $ARGS --include=\"*/\" $INCLUDE --exclude=\"*\" $SOURCE $SERVER:$TARGET"

echo $COMMAND
echo "rsync -zarv -e ssh --prune-empty-dirs --delete --include=\"*/\" --include=\"*.csv\" --include=\"*.hdf5\" --include=\"*.pickle\" --include=\"*.tar.gz\" --include=\"*.bin\" --include=\"*.npz\" --include=\"*.zip\" --exclude=\"*\" . admin@scrier.myqnapcloud.com:/share/rsync/udacity"
