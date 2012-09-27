#!/bin/sh

for i in $(seq $1)
do
  echo $(tr -dc A-Za-z0-9 < /dev/urandom | head -c $2)
done
