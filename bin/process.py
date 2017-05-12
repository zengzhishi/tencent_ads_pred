# !/bin/env python
# -*- coding: utf-8 -*_
########################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: process.py
Author: zengzhishi(zengzhishi@baidu.com)
Date: 2017/05/08 11:59:10
Brief: The main process of dataprepare.
"""
import sys
import os
import ConfigParser
import logging
import logging.config

import data_prepare

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: python process.py env.conf"
        sys.exit(-1)

    file_env = sys.argv[1]
    cf = ConfigParser.ConfigParser()
    cf.read(file_env)

    logging.config.fileConfig(cf.get("path", "conf_logging"))
    logger = logging.getLogger("process")

    logger.info("---------------- Processing started ---------------")

    jobs = []
    worker = data_prepare.DataPrepare(cf, logger, jobs)
    woker.start()
    del woker

    logger.info("---------------- Processing finished ---------------")

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
