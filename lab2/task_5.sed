s/^$/--------------------------/

/addr:\(\([^.]*\)\.\([^.]*\)\.\([^.]*\).\([^.]*\)\b\)/{
  #store entire string
  h;
  #copy part of string with IP adress only
  s/\(.*addr:\(\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}\)\)\(.*\)/\1/
  #replace digits with 'x'es
  s/[0-9]/x/g
  #addend inital string to the modified one
  G;
  s/\n//
  #cut intial address from concatenated string
  s/[[:space:]]*inet addr:\(\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}\)//
}
 
