#!/bin/bash

# 音声データのバックアップ
cp ./voices/raw/*.wav ./voices/backup/.

cp ./script/volume_barancer.py ./voices/raw/.
python3 ./voices/raw/volume_barancer.py
mv ./voices/*.wav ./voices/normalized/.

