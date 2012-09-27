#!/bin/sh

if (( $# -lt 1 )); then
  echo "No achive - no content"
  exit 
fi

name=${1%\.*}
ext=${1##*\.}

new_ext=""
for i in $(seq ${#ext}) 
do
  new_ext=${ext:i-1:1}$new_ext
done

mv $1 $name.$new_ext
