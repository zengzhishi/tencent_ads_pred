#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
########################################################################

"""
File: data_prepare.py
Author: lug(lug@baidu.com)
Date: 2017/05/11 22:37:16
"""
class DataPrepare(mp.Process):
    """
    多进程处理的模板类，内部的工作则采用多线程处理
    """
    def __init__(self, cf, logger, jobs=None):
        mp.Process.__init__(self)

        self._cf = cf
        self._logging = logger
        self._job_list = jobs

    def _multi_worker(self, lock):
        """多线程处理的主要逻辑"""
        self._logging.info("process " + str(os.getpid()) + " missions start")
        while self.start != self.amount:
            lock.acquire()
            end = self.start + self.request_size
            if end < self.amount:
                start = self.start
                self.start = end
            else:
                start = self.start
                end = self.amount
                self.start = self.amount
            self._logging.info("process %s start doing tasks %d - %d" % (str(os.getpid()), start, end))
            lock.release()
            for bid in self._bid_list[start:end]:
                status, saving_data, msg = self._request(bid)
                if status:
                    self._saving(saving_data)
                else:
                    self._error_saving(bid, msg)
            self._logging.info("process %s complete tasks %d - %d" % (str(os.getpid()), start, end))
        self._logging.info("process " + str(os.getpid()) + " missions complete")


    def run(self):
        self.amount = len(self._job_list)
        self.start = 0

        threads = []
        lock = threading.Lock()
        self._logging.info("initialize threads...")
        # 创建多线程
        for _ in xrange(self.thread_num):
            t = threading.Thread(target=self._multi_worker, args=(lock,))
            threads.append(t)
            t.start()
        self._logging.info("threads initialize complete")

        self._logging.info("waiting for worker done...")
        for t in threads:
            t.join()
        self._logging.info("worker complete")
