#!/bin/bash

tput clear
tput reset
tput civis
tput cup 0 0

read DELIMS
N=$(echo $DELIMS | sed 's/\([0-9]*\) .*/\1/')
M=$(echo $DELIMS | sed 's/.* \([0-9]*\)/\1/')

data=""

for i in $(seq $N);do
  read ROW
  for j in $(seq $M); do
    data=$data${ROW:j-1:1}
  done
done

read POINT
s_y=$(echo $POINT | sed 's/\([0-9]*\) .*/\1/')
s_x=$(echo $POINT | sed 's/.* \([0-9]*\)/\1/')
read POINT
e_y=$(echo $POINT | sed 's/\([0-9]*\) .*/\1/')
e_x=$(echo $POINT | sed 's/.* \([0-9]*\)/\1/')
 
data=${data:0:M*s_y-M+s_x-1}2${data:M*s_y-M+s_x}
data=${data:0:M*e_y-M+e_x-1}3${data:M*e_y-M+e_x}

function df_print {
  data=$1
  for __i in $(seq 0 $((${N}-1)) );do
    for __j in $(seq 0 $((${M}-1)) );do
      value=${data:M*__i+__j:1} 
      msg=""	
      case $value in
      3)
        msg='\033[44m \033[49m';;
      0) 
	      msg='\033[47m \033[49m';;
     	1) 
	      msg='\033[41m \033[49m';;
	    2)
	      msg='\033[42m \033[49m';;
      esac
      echo -en $msg* 
    done
  done
}

function df_routine {
  local di
  local dj
  local res
  local data
  local ind
  
  data=$1
  ind=$(( $M * $2 + $3 ))
  if (( ${data:ind:1} == 3 ));then
    data=${data:0:$ind}2${data:$ind+1}
    echo -en $(df_print $data)'#'2
    exit
  fi

  data=${data:0:$ind}2${data:$ind+1}
  echo -en $(df_print $data)'#'
  res=1
  for di in $(seq -1 1);do
   for dj in $(seq -1 1);do
     if (( $di * $dj != 0)); then
       continue;
     fi
     if (( $2 + $di < 0 || $2+$di > $N-1 || $3 + $dj < 0 || $3+$dj>$M-1)); then 
       continue
     fi
		
     let ind=$M*$2+$M*$di+$dj+$3
     val=${data:$ind:1}
     if (( $val == '0' || $val == '3' )); then
       test_i=$(( $2 + $di ))
	     test_j=$(( $3 + $dj ))

       res=$(df_routine $data $test_i $test_j)
       status=$(echo $res | sed 's/.*#\([12]\)/\1/')
       history=$(echo $res | sed 's/\(.*\)#[12]/\1/')
       if (( $status == 2 ));then
	       echo -en $res
         exit;
       fi
	     echo -en $history'#'$(df_print $data)'#'
     fi
   done
 done
 echo 1
}

case $1 in
'-bf')

  stat=0
  while (:);do
    next_data=$data
    state=0
    for i in $(seq 0 $((${N}-1)) );do
      for j in $(seq 0 $((${M}-1)) );do
   	    tput cup ${i} ${j}
   	    value=${data:M*i+j:1} 
	
	      case $value in
	      0) 
	        echo -e '\033[47m \033[49m';;
	      1) 
	        echo -e '\033[41m \033[49m';;
	      3)
	        let state+=1     
	        echo -e '\033[44m \033[49m';;
        2)
	        for di in $(seq -1 1);do
	          for dj in $(seq -1 1);do
		          if (( $di * $dj != 0 )); then
                continue;
              fi
		          if (( $i + $di < 0 || $i+$di > $N-1 || $j + $dj < 0 || $j+$dj>$M-1)); then 
		            continue
		          fi
		
 		          let ind=$M*$i+$M*$di+$dj+$j
	            val=${data:$ind:1}
              case $val in
	 	          0)
		            let state+=2 
		            next_data=${next_data:0:$ind}2${next_data:$ind+1};;
	            3)
		            let state+=2
		            next_data=${next_data:0:$ind}2${next_data:$ind+1};;
              esac
            done
          done
	        echo -e '\033[42m \033[49m';;
	      esac
      done
    done

    if (( $state == 1 )); then
      tput cup $N $0
      echo NO SOLUTION
      break;
    fi
  
    if (( $state % 2 == 0 )); then
      tput cup $N $0    
      echo SOLVED
      break
    fi
    data=$next_data
    sleep .05
  done;;

'-df')
  let s_y-=1
  let s_x-=1
  
  tput cup 0 0
  echo In progress...
  val=$( df_routine $data $s_y $s_x)
  tmp_str=""
  curr_chars=0
  tput clear
  for i in $(seq 0 ${#val});do
    ch=${val:i:1}
    case $ch in
    '#')
      tmp_str=""
      curr_chars=0
      sleep .05
	    tput cup 0 0;;
    '*')
      let curr_chars++
      if (( $curr_chars % $M == 0 )); then
        #flush
        echo -e $tmp_str
        tmp_str=""
      fi;;
    *)
      tmp_str=$tmp_str$ch
    esac
  done
  last_ind=$(( ${#val} - 1 ))
  tput cup $N $0 
  if (( ${val:last_ind:1} == 1 )); then
    echo NO SOLUTION
  else   
    echo SOLVED
  fi
  ;;
*)
  echo 'Enter alg type (-df or -bf)'
esac

tput cnorm
