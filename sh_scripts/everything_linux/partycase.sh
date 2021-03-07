#!/bin/bash

echo "What is your name"
read name

case $name in 

"tom")
   echo "Hi Tom you might have been at party"
   echo "$name"
;;

"bob")
   echo "Hi bob you might have been at party"
;;

"Martha")
   echo "Hi Martha you might have been at party"
;;

*)
   echo "You missed the party"
;;
esac

