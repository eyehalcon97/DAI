#!/bin/sh

link=http://localhost:5000/pokedexAPI/;
if [ $1 = "get"  ]; then
    curl $link$2;
fi
if [ $1 = "delete"  ]; then
    curl -X DELETE $link$2;
fi
var="unir"
if [ $1 = "add"  ]; then
    curl -X POST -H 'Content-Type: application/json' $link$var -d @$2
fi
var="mod"
if [ $1 = "put"  ]; then
    curl -X PUT -H 'Content-Type: application/json' $link$2 -d @$3
fi
