FILE_NAME="test5.txt"

author=$(sed -n '1p' $FILE_NAME)

let q_num=$(( $RANDOM % $(sed -n '2p' $FILE_NAME)))

exec <$FILE_NAME 

echo -en \\033[32m

st_line=-1
end_line=$
ln_num=1
while read line; do
  if $(echo "$line" | grep -q "^*");then
    curr_q_num="$(echo "$line" | sed 's/[^0-9]*\([0-9]*\)/\1/g')"
    if (( $curr_q_num == $q_num )); then
      st_line=$(( $ln_num + 1 ))
    else
      if (( $st_line != -1 ));then
        end_line=$(( $ln_num - 1 ))
        break
      fi
    fi
  fi

  let ln_num++
done

cat $FILE_NAME | sed -n "$st_line,$end_line p"
echo ""
echo -e \\t\\t\\033[33m$author\\033[00m
