RELEASE=$1
LINUXFAMILY=$2
BOARD=$3
BUILD_DESKTOP=$4

Main() {
     echo "Installing XKRig"
        apt update -y
        apt install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev python3 python3-pip
        git clone https://github.com/kryptokrona/xkrig.git
        mkdir xkrig/build && cd xkrig/build
        cmake ..
        make -j$(nproc)
        mv xkrig /usr/bin

        git clone https://github.com/TechyGuy17/kryptokrona-mini-miner
        mkdir /miner
        mv kryptokrona-mini-miner/Software/Dashboard /miner
        mv kryptokrona-mini-miner/Software/miner* /etc/systemd/system
        mv kryptokrona-mini-miner/Software/config.json /miner
        apt install python3-requests python3-flask
        systemctl enable miner
        systemctl enable minerBackend
}
Main "$@"