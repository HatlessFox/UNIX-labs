#!/bin/bash

if [[ $# < 1 ]];then
  echo No parameters - no numbers
  exit
fi

fibs() {
  if (( $1 <= 1 )); then
    echo 1
  else
    p1=$(( $1 - 1 ))
    p2=$(( $1 - 2 ))
    echo $(( $(fibs $p1) + $(fibs $p2) ))
  fi
}

echo $(fibs $1)