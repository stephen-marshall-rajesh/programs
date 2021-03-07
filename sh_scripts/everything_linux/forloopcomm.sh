#!/bin/bash

for x in `ls` # also  $(ls) can be used instead of back tick
do
   echo "I see in our current directory $x"
done
