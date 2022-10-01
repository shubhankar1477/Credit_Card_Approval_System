#!/bin/sh

cd src
python -W ignore train.py --model Logsitic
python -W ignore train.py --model GB