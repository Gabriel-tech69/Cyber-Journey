#!/bin/bash

transport=('car' 'train' 'bike' 'bus')
echo "${transport[@]}"
echo "${transport[1]}"
unset transport[1]
echo "${transport[@]}"
transport[1]='ride'
echo "${transport[@]}"
cars=('honda' 'audi' 'bmw' 'tesla')
echo "${cars[1]}"
unset cars[3]
cars[3]='toyota'
echo "${cars[@]}"

count=10
if [ $count -eq 10 ]
then
    echo "True"
else
    echo "False"
fi

value="guessme"
guess=$1
if [ '$value' = $guess ]
then
    echo "they are equal"
 else:
    echo "they are not equal"
fi




name=1
echo "$name"

