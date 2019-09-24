#!/bin/bash

find data -type f \( -name '*mkv' -o  -name '*webm' \) \
     -exec scenedetect --input {} --output data/taylor --stats {}.stats.csv detect-content list-scenes \; 
