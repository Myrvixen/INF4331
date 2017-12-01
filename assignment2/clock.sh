#!/bin/bash

option=$1
shift

while true;
do
	clear ;

	case "$option" in
		no)
			echo "Norwegian time (Oslo):"
			TZ=Europe/Oslo date +"%T";;

		sk)
			echo "Korean time (Seoul):"
			TZ=Asia/Seoul date +"%T";;

		us)
			echo "US time (New York):"
			TZ=America/New_York date +"%T";;

		"")
			echo "Local time:"
			date +"%T";;

		*)
			echo "$0: invalid option \"$option\""; exit ;;
	esac
	sleep  1 ;
done
