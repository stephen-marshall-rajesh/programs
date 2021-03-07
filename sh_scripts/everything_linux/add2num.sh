#!/bin/bash

echo "Give me First number"
read num1
echo "Give me second number"
read num2

echo " The Total of the 2 numbers is:"

SUM=`expr $num1 + $num2`

echo $SUM  is the answer
