#!/bin/bash

links=$(ls -AFl -C1 | grep @ | sed 's/\(.*\)@/\1/')

for link in $links
do
  if [[ -f $(readlink $link) ]]; then echo $link; fi
done