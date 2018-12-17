#!/bin/sh
sudo pkg update &&
    sudo pkg install -y libssl-devel &&
    sudo pkg clean -y
