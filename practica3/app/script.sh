#!/bin/sh

link=http://localhost:5000/pokedexAPI/;
if [ $1 = "get"  ]; then
    curl $link$2;
fi
if [ $1 = "delete"  ]; then
    curl $link$2 -X DELETE -v;
fi

if [ $1 = "add"  ]; then
    curl $link -X POST -v
fi
