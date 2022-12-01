#!/bin/bash
cat 1.txt | tr '\n' '+' | sed 's/++/\n/g; s/\(.*\)/\1\n/g' | bc | sort -n -r | head -n 1