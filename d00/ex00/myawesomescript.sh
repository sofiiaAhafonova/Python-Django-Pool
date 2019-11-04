#!/bin/sh
if [ ! -z $1 ] ; then 
    curl -I -s  $1 | grep Location | cut -d " "  -f 2
fi
