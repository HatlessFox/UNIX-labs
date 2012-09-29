#!/bin/bash

exec <$1

for mail in $(grep -oE '[[:alpha:][:digit:].+_-]+@[[:alpha:][:digit:].+_-]*' $1);do
  echo $(grep -wc $mail $1) $mail
done | sort -rnk1 | uniq | sed 's/[[:digit:]]* \(.*\)/\1/g'
