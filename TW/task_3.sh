#!/bin/bash

if [[ $# < 2 ]];then
 echo Not enough args \(2 required\)
 exit
fi

find $1 -user $USER -ctime +$2
