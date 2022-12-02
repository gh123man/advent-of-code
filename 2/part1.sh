#!/bin/bash
cat 2.txt | tr '\n' '+' | sed 's/A X/4/g; s/A Y/8/g; s/A Z/3/g; s/B X/1/g; s/B Y/5/g; s/B Z/9/g; s/C X/7/g; s/C Y/2/g; s/C Z/6/g' | bc