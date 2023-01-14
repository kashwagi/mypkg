#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log


cat /tmp/mypkg.log |
grep 'Listen: 10'
