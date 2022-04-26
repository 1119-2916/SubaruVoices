#!/bin/bash

# 音声データのバックアップ
cp ./voices/raw/*.wav ./voices/backup/.

cp ./script/volume_barancer.py ./voices/raw/.
cd ./voices/raw/.
python3 ./volume_barancer.py

