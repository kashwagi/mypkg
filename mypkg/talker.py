#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023  Yuki Kashiwagi

import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
n = 0 #カウント用変数

def cb():          #17行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = n   #msgオブジェクトの持つdataにnを結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1

node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）
