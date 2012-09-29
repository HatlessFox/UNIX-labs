#!/bin/bash

#tput cnorm to show cursor
tput civis
while true
do
  echo -ne $(date +"%T")\\r
  sleep 1
done
