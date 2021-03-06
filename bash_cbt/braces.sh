#!/bin/bash

echo "# echo test='hello'(initiates  variable)"
test="hello"

echo $test123

echo "#echo ${test}123"

echo ${test}


echo " # echo ${test/ll/ff} (substitutes ll with ff) "

echo ${test/ll/ff}

echo " # echo  f{oo,ee,a}t"

echo f{oo,ee,a}t
