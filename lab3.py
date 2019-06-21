#!/usr/bin/env python
import psutil, os, json
from psutil._common import bytes2human


class Mypc:
    """Class for printing overall system info with psutil"""
    logtype = "plain"
    file_name = str("perf.log")

    def writetofile(self):
        """ writing info to file, depend on "logtype" """
        # TODO different log types to different files
        if os.path.isfile(self.file_name) is False:
            log = open("%s" % self.file_name, "w+")
        else:
            log = open("%s" % self.file_name, "a")
        if self.logtype is "plain":
            current = self.howareyou()
            for key, value in current.items():
                log.write(str(key) + ": " + str(value) + "  ")
                log.write('\n')
        elif self.logtype is "json":
            current = json.dumps(self.howareyou())
            log.write(current)
            log.write('\n')
        log.close()

    def howareyou(self):
        """ requesting sysinfo and return it as dictionary """
        #TODO change log format to "SNAPSHOT 1: TIMESTAMP : <columns for system wide data>"
        current = {}
        current["CPU"] = psutil.cpu_percent(interval=1)
        current["RAM total"] = bytes2human(psutil.virtual_memory()[0])
        current["RAM available"] = bytes2human(psutil.virtual_memory()[4])
        current["I/O read count "] = bytes2human(psutil.disk_io_counters()[0])
        current["I/O write count "] = bytes2human(psutil.disk_io_counters()[1])
        return(current)

    def plsremovelog(self):
        """ if you decide to delete log file """
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


if __name__ == "__main__":
    """main void"""
    #TODO open and read config file
    a1 = Mypc()
    a1.writetofile()
    print(a1.howareyou())
