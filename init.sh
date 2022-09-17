#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

# install byobu
echo "Installing Byobu"
sudo apt-get install byobu -y

# install git
echo "Installing git"
sudo apt-get install git -y

# install docker
echo "Install docker"
sudo apt-get remove docker docker-engine docker.io containerd runc -y
sudo apt-get update -y
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo groupadd docker 
sudo usermod -aG docker $USER
newgrp docker 

# install go
echo "Installing go"
sudo apt-get install wget
wget https://mirrors.ustc.edu.cn/golang/go1.19.1.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.19.1.linux-amd64.tar.gz

# install anaconda.sh
echo "Installing anaconda3"
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh && sh Anaconda3-5.3.1-Linux-x86_64.sh

# install zsh
sudo apt-get install zsh -y
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install BT panel
echo "Installing BT panel"
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh ed8484bec -y
