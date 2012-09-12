find . -maxdepth 1 -type f | sed "s@\./\(.\{1,\}\)\(\..*\)@'\1\2' '\1z\2'@" | sed "s@\./\(.*\)@'\1' '\1z'@" | xargs -L 1 mv
