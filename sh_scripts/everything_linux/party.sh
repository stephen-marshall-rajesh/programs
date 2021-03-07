#!/bin/bash
echo " what is your name "
read NAME
if [ $NAME = "bob" ] || [ $NAME = "tom" ] || [ $NAME = "Martha" ]
then
 echo "You might have been at the party  $NAME"
else
 echo "You were probably not at the party, $NAME"
fi

