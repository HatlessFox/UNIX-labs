#!/bin/bash

file_content=$(cat $1)
echo $file_content | while read -r -n1 char; do
  code=$(( $(printf "%x" $(echo "0x"$(echo $char | xxd -l 1 -plain))) + 1 ))
  echo -en \\x$code
done >$1