#!/bin/bash

if [ "$1" == "ldd" ]; then
    string=$(file -b $2)
    chmod +x $2

    if [[ $string =~ .*static* || $string =~ .*shared* || $string =~ .*symbolic.link* ]]
    then
        echo "GTFO with statically linked binaries/shared objects/symlinks."
    else
        if [[ $string =~ .*ELF* && $string =~ .*executable* ]]; then
            LD_TRACE_LOADED_OBJECTS=1 $2
        else
            echo "not an elf"
        fi
    fi
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
