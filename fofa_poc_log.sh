#!/bin/sh
cd /root/py/test
pwd

nohup python fofa_poc_log.py>fofa_poc_log.out 2>/dev/null&

