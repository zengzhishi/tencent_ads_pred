#!/bin/bash

#step1. load env
. ./env.sh

if [ ! -d "${DATA_PATH}" ];then
    mkdir -p "${DATA_PATH}"
fi
if [ ! -d "${LOG_PATH}" ];then
    mkdir -p "${LOG_PATH}"
fi
if [ ! -d "${OUTPUT_PATH}" ];then
    mkdir -p "${OUTPUT_PATH}"
fi
if [ ! -d "${TMP_PATH}" ];then
    mkdir -p "${TMP_PATH}"
fi
if [ ! -d "${BAKUP_PATH}" ];then
    mkdir -p "${BAKUP_PATH}"
fi
if [ ! -d "${LIB_PATH}" ];then
    mkdir -p "${LIB_PATH}"
fi

#step2. 主要的处理过程，包括了数据的预处理，特征提取以及模型的训练产出
python ./process.py ${CONF_PATH}/env.conf


# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
