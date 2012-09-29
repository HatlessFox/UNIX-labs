#!/bin/bash


wget -O- -q 'cnn.com' | sed -n -e '{ 
  /.*<body.*/ {
    s|.*<body[^>]*>\(.*\)|\1|
    h
  }
  /.*<\/body>.*/ {
    s|\(.*\)<\/body>.*|\1|
    H;
    x;
    p
  }
  /.*<.*/ {
    s|<[^>]*>||g
    s|</[^>]*>||g
    H;
  } 
  /.*/ {
    H;
  }
}' | grep  -v '^[[:space:]]*$'
