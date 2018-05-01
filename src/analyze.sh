#!/bin/bash

if [ "$1" == "ldd" ]; then
    ldd $2
fi

if [ "$1" == "file-header" ]; then
    readelf --file-header $2
fi

if [ "$1" == "program-headers" ]; then
    readelf --program-headers $2
fi

if [ "$1" == "sha512" ]; then
    sha512sum $2 | cut -d" " -f1
fi
