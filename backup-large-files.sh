#/bin/sh

if [ "$HOSTNAME" = gpu02 ]; then
  rsync -zarv --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" --exclude="*" . ../large-items/
else
  rsync -zarv --include="*/" --include="*.csv" --include="*.hdf5" --include="*.pickle" --exclude="*" . andreas@gpu02:./large-items/
fi

