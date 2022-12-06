#!/bin/bash
# part 1
echo $(seq $(cat 5.txt | grep "^\s\d" | rev | awk '{print $1}') | xargs -n1 bash -c 'cat 5.txt | grep ".*\[.*"  --color=never | sed '\''1!G;h;$!d'\'' | sed "s/\[\([a-zA-Z]\)]/ \1 /g; s/\(....\)/\1,/g; s/ //g" | sed '\''1!G;h;$!d'\'' | awk -F, -v var=$0 '\''{print $var}'\'' | awk '\''NF'\'' > /tmp/AOC$0') $(cat 5.txt | grep "^move.*" --color=never | sed 's/move \([0-9][0-9]*\) from \([0-9][0-9]*\) to \([0-9][0-9]*\)/\1 \2 \3/g' | xargs -n3 bash -c 'seq $0 | xargs -n1 -I {} echo "$1 $2"' | xargs -n2 bash -c 'echo "$(cat <(head -n1 /tmp/AOC$0 ) /tmp/AOC$1)" > /tmp/AOC$1 && echo "$(tail -n$(($(wc -l < /tmp/AOC$0) - 1)) /tmp/AOC$0)" > /tmp/AOC$0')  "$(ls /tmp/AOC* | xargs -n1 head -n1 | tr -d '\n')"
# part 2
echo $(seq $(cat 5.txt | grep "^\s\d" | rev | awk '{print $1}') | xargs -n1 bash -c 'cat 5.txt | grep ".*\[.*"  --color=never | sed '\''1!G;h;$!d'\'' | sed "s/\[\([a-zA-Z]\)]/ \1 /g; s/\(....\)/\1,/g; s/ //g" | sed '\''1!G;h;$!d'\'' | awk -F, -v var=$0 '\''{print $var}'\'' | awk '\''NF'\'' > /tmp/AOC$0') $(cat 5.txt | grep "^move.*" --color=never | sed 's/move \([0-9][0-9]*\) from \([0-9][0-9]*\) to \([0-9][0-9]*\)/\1 \2 \3/g' | xargs -n3 bash -c 'echo "$(cat <(head -n$0 /tmp/AOC$1 ) /tmp/AOC$2)" > /tmp/AOC$2 && echo "$(tail -n$(($(wc -l < /tmp/AOC$1) - $0)) /tmp/AOC$1)" > /tmp/AOC$1') "$(ls /tmp/AOC* | xargs -n1 head -n1 | tr -d '\n')"