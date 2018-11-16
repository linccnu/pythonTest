#!/bin/bash
apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev

echo "[zhonglin]git clone nccl..."
git clone https://github.com/NVIDIA/nccl.git && cd nccl && make -j install && cd .. && rm -rf nccl
echo "[zhonglin]installed nccl successfully."

CAFFE_DIR=/workspace/caffe/build
mkdir -p $CAFFE_DIR && cd $CAFFE_DIR && cmake -DUSE_CUDNN=1 -DUSE_NCCL=1 ..
echo $(nproc)
make -j"$(nproc)" && make install
echo "[zhonglin]installed caffe successfully."