#! /bin/bash
if (($# == 0));
then  
  echo "No numbers - No sorting"
  exit 0
fi

lim=$(expr $# - 1)
for i in $(seq $lim)
do
  for j in $(seq $(expr $i + 1) $#)
  do
    if ((${!i} > ${!j})); then
      set ${@:1:i-1} ${!j} ${@:i+1:j-1-i} ${!i} ${@:j+1}
    fi
  done
done

echo $@