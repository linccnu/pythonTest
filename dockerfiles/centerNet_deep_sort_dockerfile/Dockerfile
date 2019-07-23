From tensorflow/tensorflow:1.12.0-devel-gpu-py3
MAINTAINER lin_nudt0625@163.com
ENV LANG C UTF-8
ARG user=zhonglin

COPY sources.list /etc/apt/sources.list
COPY pip.conf     /root/.pip/pip.conf

# ==================================================================
# environment
# ------------------------------------------------------------------
RUN APT_INSTALL="apt-get install -y --no-install-recommends" && \
    PIP_INSTALL="python -m pip --no-cache-dir install --upgrade" && \
    GIT_CLONE="git clone --depth 10" && \

    apt-get update && \
	
	DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
		software-properties-common \
        build-essential \
		apt-utils \
        ca-certificates \
        cmake \
        wget \
        git \
        vim \
		curl \
		openjdk-8-jdk \
		python3-tk \
        && \
    
	pip install --upgrade pip && \
	
	$PIP_INSTALL setuptools && \
	
	$PIP_INSTALL \
		certifi==2019.3.9 \
		cffi==1.12.3 \
		cycler==0.10.0 \ 
		Cython==0.29.9 \
		joblib==0.13.2 \
		kiwisolver==1.1.0 \
		llvmlite==0.28.0 \
		matplotlib==3.0.3 \
		mkl-random \
		numba==0.43.1 \
		numpy==1.16.3 \
		olefile==0.46 \
		opencv-python==4.1.0.25 \
		Pillow==6.0.0 \
		progress==1.5 \
		pycparser==2.19 \
		pyparsing==2.4.0 \
		python-dateutil==2.8.0 \
		scikit-learn==0.21.2 \
		scipy==1.3.0 \
		six==1.12.0 \
		sklearn==0.0 \
		torch==0.4.1 \
		torchvision==0.2.1 \
		&& \
	
    
# ==================================================================
# config & cleanup
# ------------------------------------------------------------------    
    ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

EXPOSE 6006
