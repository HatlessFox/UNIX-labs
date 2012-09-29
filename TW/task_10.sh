#!/bin/bash

if [[ $1 == $(echo $1 | rev) ]]; then
  echo Yapp!
else
  echo NO
fi
	
