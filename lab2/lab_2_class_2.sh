sed 's@\([^/]*\)//\(.*\)@\1@' main.cpp | grep -oE '"(\\.|[^\\"])*"'
