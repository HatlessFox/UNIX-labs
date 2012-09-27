#!/bin/sh

page_src=$(wget -O- -q 'http://mit.spbau.ru/sewiki/index.php/Unix_и_Скриптовые_языки_2012' | tr '\n' ' ')
echo $page_src | grep -oE '<tr>.*</tr>' | grep -oE '([0-2][1-9]|30|31)\.(0[1-9]|1[0-2])\.20[0-9][0-9]'