#!/bin/bash

if (( ${#date} == 1 ));then
  date=$(echo " "$date)
fi

#not 1 since cal adds extra blank line
cal_out=$(cal $2 $3 | sed -n '3p')

let fw_days=0
for i in $cal_out
do
  let fw_days++
done

days=('Su' 'Mo' 'Tu' 'We' 'Th' 'Fr' 'Sa')
day_ind=$(( ($1 - 1 + 7 - fw_days) % 7 ))

echo ${days[day_ind]}

