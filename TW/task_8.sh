#!/bin/bash

if [[ $# < 1 ]];then
  echo No parameters - no numbers
  exit
fi

fibs=(1 1)

for i in $(seq 1 $(($1-2)) )
do
  next=$(( ${fibs[i]} + ${fibs[i-1]} ))
  fibs=(${fibs[*]} $next)

done

echo ${fibs[*]}