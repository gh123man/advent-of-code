#!/bin/bash 
# part 1
seq $(cat 6.txt | wc -c)  | xargs -n1 bash -c 'cat 6.txt | sed "s/\(.\)/\1\n/g" | head -n$(($0 + 3)) | tail -n4 | sort | uniq | wc -l' | nl | awk '{print $1 " " $2}' | sed -n 's/\([0-9]*\) 4/\1 + 3/p' | head -n1 | bc
# part 2
seq $(cat 6.txt | wc -c)  | xargs -n1 bash -c 'cat 6.txt | sed "s/\(.\)/\1\n/g" | head -n$(($0 + 13)) | tail -n14 | sort | uniq | wc -l' | nl | awk '{print $1 " " $2}' | sed -n 's/\([0-9]*\) 14/\1 + 13/p' | head -n1 | bc
