#!/bin/bash
cat 2.txt | tr '\n' '+' | sed 's/A X/3/g; s/A Y/4/g; s/A Z/8/g; s/B X/1/g; s/B Y/5/g; s/B Z/9/g; s/C X/2/g; s/C Y/6/g; s/C Z/7/g' | bc