#!/usr/bin/env python
import psutil
import os
import json
import configparser
import time
import datetime
from psutil._common import bytes2human


class Mypc:
    """Class for printing overall system info with psutil"""
    __file_name = str("sysf.log")
    __json_name = str("sysj.log")
    __snap_count = 1

    def writetojson(self):
        """ writing info to file, json format, create if not exist """

        if os.path.isfile(self.__json_name) is False:
            log = open("%s" % self.__json_name, "w+")
        else:
            log = open("%s" % self.__json_name, "a")
        current = json.dumps(self.howareyou())
        log.write(current)
        log.write('\n')
        log.close()

    def writetofile(self):
        """ writing info to file, plain info, create if not exist """

        if os.path.isfile(self.__file_name) is False:
            log = open("%s" % self.__file_name, "w+")
        else:
            log = open("%s" % self.__file_name, "a")
        current = self.howareyou()
        for key, value in current.items():
            log.write(str(key) + ": " + str(value) + "  ")
        log.write('\n')
        log.close()

    def howareyou(self):
        """ requesting sysinfo and return it as dictionary """
        time = str(datetime.datetime.now().isoformat())
        snapshot = "SNAPSHOT " + str(self.__snap_count)
        current = {snapshot: time}
        current["CPU"] = psutil.cpu_percent(interval=1)
        current["RAM total"] = bytes2human(psutil.virtual_memory()[0])
        current["RAM available"] = bytes2human(psutil.virtual_memory()[4])
        current["I/O read count "] = bytes2human(psutil.disk_io_counters()[0])
        current["I/O write count "] = bytes2human(psutil.disk_io_counters()[1])
        self.__snap_count += 1
        return current

    def plsremovelog(self):
        """ if you decide to delete log file """
        if os.path.isfile(self.__file_name):
            os.remove(self.__file_name)
        if os.path.isfile(self.__json_name):
            os.remove(self.__json_name)


if __name__ == "__main__":
    """main void"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    log_type = config.get("common", "output")
    log_interval = config.get("common", "interval")
    a1 = Mypc()
    if log_type == "plain":
        print(type(log_type))
        while True:
            a1.writetofile()
            time.sleep(int(log_interval))
    if log_type == "json":
        while True:
            a1.writetojson()
            time.sleep(int(log_interval))
