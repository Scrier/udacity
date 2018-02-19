#/bin/sh


# rsync -zarv --delete-after --exclude="Deep.Learning/fast-style-transfer" --exclude="Deep.Learning/DeepLearningFlappyBird"
# --exclude="Deep.Learning/deep-learning" --exclude="Deep.Learning/aind2-cnn"
# --exclude="Deep.Learning/3.Convulutional-Networks/6.Transfer-Learning-in-Tensorflow/tensorflow_vgg"
# --exclude="Deep.Learning/3.Convulutional-Networks/7.Dog-Breed-Classifier/dog-project"
# --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" --include="*.tar.gz" --include="*.bin"
# --include="*.npz" --include="*.zip" --exclude="*" andreas@gpu02:./large-items/ .


source ./qnap-shared.sh

GetLargeFileExtensions INCLUDE "--include=\"" "\""
GetGitModulePaths EXCLUDE "--exclude=\"" "\""

ARGS="-zarv -e ssh --delete-after"
SERVER="admin@scrier.myqnapcloud.com"
SOURCE="/share/rsync/udacity/"
TARGET="."

COMMAND="rsync $ARGS $EXCLUDE --include=\"*/\" $INCLUDE --exclude=\"*\" $SERVER:$SOURCE $TARGET"

echo $COMMAND
echo "rsync -zarv --delete-after --exclude=\"Deep.Learning/fast-style-transfer\" --exclude=\"Deep.Learning/DeepLearningFlappyBird\" --exclude=\"Deep.Learning/deep-learning\" --exclude=\"Deep.Learning/aind2-cnn\" --exclude=\"Deep.Learning/3.Convulutional-Networks/6.Transfer-Learning-in-Tensorflow/tensorflow_vgg\" --exclude=\"Deep.Learning/3.Convulutional-Networks/7.Dog-Breed-Classifier/dog-project\" --include=\"*/\" --include=\"*.csv\" --include=\"*.hdf5\" --include=\"*.pickle\" --include=\"*.tar.gz\" --include=\"*.bin\" --include=\"*.npz\" --include=\"*.zip\" --exclude=\"*\" andreas@gpu02:./large-items/ ."

