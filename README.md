# robosys2022_ROS2

[![test](https://github.com/kashwagi/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kashwagi/mypkg/actions/workflows/test.yml)


当レポジトリは2022年度ロボットシステム学の講義内においてGitHubやプログラムなどロボットシステムへの理解を深める学習目的で制作及び公開しています。

第二回課題提出用。

また、このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，教育目的で本人の許可を得て自身の著作としたものです．

ryuichiueda/my_slides robosys_2022

## 概要
ROS2環境下においてtalker及びlistenerを用いて通信処理を行い、ROS及びロボットシステムへの理解を深めることを目的としたパッケージです。
ROS2 Humbleでの使用を想定しています。

## 開発環境
ubunntu 22.04.1LTS

Python 3.10

ROS2 Humble

## ノード及びトピックの概要

### ノード

#### talker
実行後変数を1ずつ増やし続ける。

#### listener
受け取ったトピックの内容をを標準出力する。

### トピック

#### countup
talkerの変数をlistenerに送る。

# テスト
ubunntu 22.04.1LTS

Python 3.10

ROS2 Humble

また、当テストにはロボットシステム学授業内で提供していただいた上田隆一先生のコンテナを使用しています（以下URLを添付）。
https://hub.docker.com/layers/ryuichiueda/ubuntu22.04-ros2/latest/images/sha256-0e1773bc6f12b57172c8818aac36aeb97ca13269028028d49ad5f6f8cc0d6204?context=explore

# ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
© 2022 Yuki kashiwagi
