#!/bin/bash

number=0
prefix=""
suffix=""

let params_cnt=0
for i in $@
do
  case "$i" in 
    '--number')
      param=1
      let params_cnt++;;
    '--prefix')
      param=2
      let params_cnt++;;
    '--suffix')
      param=3
      let params_cnt++;;
    *)
      case "$param" in
        1)
          number=$i;;
        2)
          prefix=$i;;
        3)
          suffix=$i;;
      esac
      #reset option
      param=-1;;
  esac
done

params_cnt=$(( $params_cnt * 2 + 1))
let number++;

for file_ind in $(seq $params_cnt $#)
do
  file_name=${!file_ind}
  ext=${file_name##*.}
  new_name=$(echo $prefix$number$suffix.$ext)
  mv $file_name $new_name
  let number++;
done

