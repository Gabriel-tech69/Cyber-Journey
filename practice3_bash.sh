#!/bin/bash

filename=$1
if [ -f "$filename" ] && [ -w "$filename" ]
then
        echo 'hello' > $filename
        echo 'Append' $filename 'with hello'
else
        touch "filename"
        echo "hello" > $filename
        echo 'created' $filename 'with content hello'
fi
