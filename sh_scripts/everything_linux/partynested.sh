#!/bin/bash

echo "What is your name "
read name

if [ $name = 'bob' ]
  then
 	echo "You might have been at the party $name "
elif [ $name = 'tom' ]
  then
 	echo "You might have been at the parth Tom"
elif [ $name = 'Martha' ]
  then
	echo "You might have been at the party M...."
else
    echo "Did not see you there "
fi
