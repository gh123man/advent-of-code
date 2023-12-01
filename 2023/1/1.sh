#!/bin/bash
cat 1.txt | sed -e 's/[^0-9]//g' | awk '{print substr($0,1,1) substr($0,length,1)}' | tr '\n' '+' | sed 's/\(.*\)+/\1\n/' | bc