RELEASE=$1
LINUXFAMILY=$2
BOARD=$3
BUILD_DESKTOP=$4

Main() {
     echo "Installing XKRig"
        apt update -y
        apt install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
        git clone https://github.com/kryptokrona/xkrig.git
        mkdir xkrig/build && cd xkrig/build
        cmake ..
        make -j$(nproc)
        mv xkrig /usr/bin

}
Main "$@"