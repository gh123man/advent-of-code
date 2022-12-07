#!/bin/bash
# part 1
cat 7.txt | sed 's/dir/mkdir/g; s/\$//g; s/cd \//mkdir work \&\& cd work/g; s/\([0-9][0-9]*\) \([a-z\.]*\)/touch \1/g' | bash && echo "$(find work | sed 's/[0-9]//g' | sed 's/\(.*\)\/$/\1/g' )" | xargs -n1 bash -c 'echo "$0" $(find work | grep -o "$0.*" --color=never | grep -o "\d.*" --color=never  | paste -sd+ - | bc)' | sort -n | uniq | awk '{if ($2 <= 100000) print $2}' | paste -sd+ - | bc

# cleanup
rm -rf work

# part 2
cat 7.txt | sed 's/dir/mkdir/g; s/\$//g; s/cd \//mkdir work \&\& cd work/g; s/\([0-9][0-9]*\) \([a-z\.]*\)/touch \1/g' | bash  && echo "$(find work | sed 's/[0-9]//g' | sed 's/\(.*\)\/$/\1/g' )" | xargs -n1 bash -c 'echo "$0" $(find work | grep -o "$0.*" --color=never | grep -o "\d.*" --color=never  | paste -sd+ - | bc)' | sort -n | uniq | awk -v var=$(echo "30000000 - (70000000 - $(find work | grep -o '\d*' | paste -sd+ - | bc))" | bc) '{if ($2 > var) print $2}' | sort -n | head -n1

# cleanup
rm -rf work
