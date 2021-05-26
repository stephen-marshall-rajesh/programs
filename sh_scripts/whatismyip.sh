#!/bin/bash

ifconfig | grep broadcast | awk '{print $2}'

# Below can be used set it up as alias 
#alias whatismyipaddress = "echo $(above command)"
# $whatismyipaddress


