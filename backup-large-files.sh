#/bin/sh

rsync -zarv --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" --exclude="*" . andreas@gpu02:./large-items

