#!/bin/bash

res=0
fact=1
limit=10
ind=1
let x=1

while true; do
  fact=$(echo "$fact*$ind" | bc)
  rem=$(( $ind % 4 ))
  x=$(echo "scale=8;$x*$1" | bc)

  case $rem in
    1)
      pr_res=$res   
      res=$(echo "scale=8;$res+$x/$fact" | bc );;
    3)
      pr_res=$res
      res=$(echo "scale=8;$res-$x/$fact" | bc);;
  esac
  if [[ $res == $pr_res ]];then
    break
  fi
  let ind++;
done
echo $res
