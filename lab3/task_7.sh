#!/bin/sh

if (( $# -lt 1 )); then
  echo "No achive - no content"
  exit 
fi

if [ ! -e $1 ]; then
  echo File $1 doesn\'t exist
  exit
fi

ext=${1#*\.}

case ${ext} in
  "tar")
    tar tf $1;;
  "gz")
    gzip -lv $1;;
  "bz2")
    tar -ztf $1;;
  "zip")
    unzip -l $1;;
esac 
