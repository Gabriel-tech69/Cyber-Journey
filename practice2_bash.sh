#!/bin/bash
value="guessme"
guess=$1
if [ "$value" != "$guess" ]
 then
     echo "They are equal"
 else
     echo "they are not equal"
 fi

