#!/bin/sh

bash_path=$(which bash)

exec < '/etc/passwd'
while read line
do
  used_shell=${line##*:}
  user=$(echo $line | sed 's/\([^:]*\):.*/\1/g')
  if [[ $1 != "-b" || $used_shell == $bash_path ]]; then
    echo $user
  fi
done