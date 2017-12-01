#!/bin/bash

filename="$HOME/.bookmarks"
option=$1
shift

# Crates variables of all existing bookmarks
while read -r line
do
    IFS='|' read -r -a array <<< "$line"
    export ${array[0]}=${array[1]}
done < "$filename"


case "$option" in
  -a)

    if [ "$1" = "" ]; then
      echo "Error: Missing bookmarkname (2nd argument)"; exit;
    fi

    # write bookmarkname entry to file
    echo "$1|$PWD" >> $filename
    export $1=$PWD;;

  -r)

    if [ "$1" = "" ]; then
      echo "Error: Missing bookmarkname (2nd argument)"; exit;
    fi

    # remove bookmarkname entry from file and unset variable bookmarkname
    sed -i "/^$1|/d" $filename
    unset $1;;

  "")
    : ;;     #Does nothing, continues the code

  *)
    echo "Error: First argument must be either -a or -r"; exit;;
esac
