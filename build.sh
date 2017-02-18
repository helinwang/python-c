#!/bin/bash

g++ -c -fPIC foo.cpp -o foo.o && g++ -shared -Wl -o libfoo.so foo.o
