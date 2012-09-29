#!/bin/bash

tput civis
tput clear

echo -en \\033[32m

#set up character time to LIVE
let TTL=3
let SPEED_LIMIT=2
let MAX_RUNNERS=30

COLS=$(tput cols)
ROWS=$(tput lines)

rand_char() {
  echo -n $( tr -dc '[:alpha:]#$?[:digit:]' </dev/urandom | head -c 1)
}

#runners info: (x,y,speed)
RUNNER_ARG_NUM=3
runners=()
#track info: (x,y,TTL)
TRACKS_ARG_NUM=4
tracks=()

while true
do
  sleep .001
  runners_cnt=$(( ${#runners[*]} / $RUNNER_ARG_NUM ))

  #add runner
  if (( $runners_cnt < $MAX_RUNNERS ));then
    #generate runner
    let y=$(( $RANDOM % $ROWS - 10))
    if (( $y < 0 )); then
      let y=0
    fi
    let x=$(( $RANDOM % $COLS ))
    let speed=$(( $RANDOM % $SPEED_LIMIT + 1 ))
    runners=(${runners[*]} $x $y $speed)
  fi

  #update runner
  let r_ind=0
  while (( $r_ind < ${#runners[*]} ))
  do

    let x=${runners[r_ind]}
    let y=${runners[r_ind+1]}
    let sp=${runners[r_ind+2]}

    tracks=(${tracks[*]} $x $y $TTL $sp)
    while (( $sp > 0 ))
    do
      let sp--
      let y++
      ch=$(rand_char)
      if (( $y == $ROWS ));then
        break
      else
        tput cup $y $x
        echo -n $ch
      fi
    done


    if (( $y == $ROWS || $RANDOM % 10 > 8))
    then
      #runner reached the bottom -> remove it
      runners=(${runners[*]:0:r_ind} ${runners[*]:r_ind+3})
    else
      runners=(${runners[*]:0:r_ind+1} $y ${runners[*]:r_ind+2})
      let r_ind+=$RUNNER_ARG_NUM
    fi
  done
  
  let tracks_ind=0
  while (( $tracks_ind < ${#tracks[*]} ))
  do
    tr_ttl=$(( ${tracks[tracks_ind+2]} - 1 ))

    if (( $tr_ttl == 0 ))
    then
      let x=${tracks[tracks_ind]}
      let y=${tracks[tracks_ind+1]}
      let sp=${tracks[tracks_ind+3]}

      while (( $sp > 0 ))
      do
        let sp--
        let y++
        if (( $y == $ROWS ));then
          break
        else
          tput cup $y $x
          echo -n " "
        fi
      done

      #track has been shown enough time -> remove it
      tracks=(${tracks[*]:0:tracks_ind} ${tracks[*]:tracks_ind+4})
    else
      tracks=(${tracks[*]:0:tracks_ind+2} $tr_ttl ${tracks[*]:tracks_ind+3})
    fi
    let tracks_ind+=$TRACKS_ARG_NUM
  done

done
