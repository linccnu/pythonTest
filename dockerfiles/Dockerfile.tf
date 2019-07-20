From tensorflow/tensorflow:1.12.0-devel-gpu-py3
ENV LANG C UTF-8
ARG user=zhonglin
ARG passwd=xxxx

COPY sources.list /etc/apt/sources.list


# ==================================================================
# environment
# ------------------------------------------------------------------
RUN APT_INSTALL="apt-get install -y --no-install-recommends" && \
    PIP_INSTALL="python -m pip --no-cache-dir install --upgrade" && \
    GIT_CLONE="git clone --depth 10" && \

    apt-get update && \
    
    DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
        build-essential \
        ca-certificates \
        cmake \
        wget \
        git \
        vim \
        && \
    
    
# ==================================================================
# config & cleanup
# ------------------------------------------------------------------    
    ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

EXPOSE 6006