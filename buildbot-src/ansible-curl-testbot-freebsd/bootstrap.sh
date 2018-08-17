#!/bin/sh
sudo pkg update &&
    sudo pkg install -y \
        python \
        ca_root_nss &&
    sudo pkg clean -y &&
    sudo python -m ensurepip
