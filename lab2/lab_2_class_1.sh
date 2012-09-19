#!/bin/sh
grep -oE '"(\\.|[^\\"])*"' main.cpp
