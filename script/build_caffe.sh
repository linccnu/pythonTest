#!/usr/bin/env bash
CAFFE_ROOT=/host/workspace/github/caffe
cd $CAFFE_ROOT

cd python && for req in $(cat requirements.txt) pydot; do pip install $req; done && cd .. && \
git clone https://github.com/NVIDIA/nccl.git && cd nccl && make -j install && cd .. && rm -rf nccl && \
mkdir build && cd build && \
cmake -DUSE_CUDNN=1 -DUSE_NCCL=1 .. && \
make -j"$(nproc)"
make -j pycaffe


# vim ~/.bashrc
# export CAFFE_ROOT=/host/workspace/github/caffe
# export PYCAFFE_ROOT=${CAFFE_ROOT}/python
# export PYTHONPATH=${PYCAFFE_ROOT}:${PYTHONPATH}
# export PATH=${CAFFE_ROOT}/build/tools:${PYCAFFE_ROOT}:${PATH}
# export LD_LIBRARY_PATH=${CAFFE_ROOT}/build/lib:${LD_LIBRARY_PATH}
#
# ldconfig