#!/bin/sh
sudo hbsd-update &&
    sudo pkg update &&
    sudo pkg install -y ca_root_nss &&
    sudo pkg clean -y
