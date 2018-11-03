#!/bin/bash

for i in {1..5};
do
    python ddos-proxy.py http:// &
    echo $i
done

sleep 30

pgrep python|xargs kill
