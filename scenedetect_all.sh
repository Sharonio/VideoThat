#!/bin/bash

for f in data/**/*mkv data/**/*webm; do 
    scenedetect --input "${f}" --stats "${f}.stats.csv" detect-content list-scenes; 
done