#!/bin/bash

nArg=$#

if (( nArg < 2 )); then
	echo "Error: you need to enter at least 2 cml arguments!"; exit;
fi

option=$1;
shift;

case "$option" in
	S)
		declare -i Sum;
		Sum=0;

		for arg in "${@:1}"; do
			Sum=$(( Sum + arg));
		done
		echo "Sum = $Sum";;

	P)
		declare -i Product;
		Product=1;

		for arg in "${@:1}"; do
			Product=$(( Product * arg));
		done
		echo "Product = $Product";;

	M)
		declare -i Max;
		Max=$1
		for arg in "${@:1}"; do
			if (( arg > Max)); then
				Max=arg;
			fi
		done
		echo "Max = $Max";;

	m)
		declare -i Min;
		Min=$1
		for arg in "${@:1}"; do
			if (( arg < Min)); then
				Min=arg;
			fi
		done
		echo "Min = $Min";;

	*)
		echo "$0: invalid option \"$option\""; exit ;;
esac
