#!/bin/bash

for i in $(seq 7); do
  for j in $(seq 7); do
    if (( (${i} + ${j}) % 2 != 0)); then
      echo -en "\033[47m  "
    else
      echo -en "\033[40m  "
    fi
    echo -en "\033[0m"
  done
  echo ""
done
