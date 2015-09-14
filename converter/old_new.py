import json
import time
import sys
from datetime import datetime
import logging
from daemon import Daemon

logger = logging.getLogger('old_new')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('/tmp/logFile.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
json_file = []


class json_converter():
    def run(self):
        global json_file
        input_file = "/tmp/test.txt"
        with open(input_file, 'r') as f:
            content = f.readline()
            while True:
                content = f.readline()
                if "_grokparsefailure" in content:
                    continue
                logger.info("Content of file for processing {0}".format(content))
                logger.info("Going for processing")
                logger.info("Position of file {0}".format(f.tell()))
                if content:
                    json_data = content
                    logger.info("Loading Json")
                    s = json.loads(json_data)
                    logger.info("method")
                    method = s['method']
                    ip_check=s['clientip']
                    if ip_check == "127.0.0.1":
                        continue
                    logger.info("Method for processing {0} ".format(method))
                    if "GET" == method:
                        logger.info("With in Method {0} ".format(method))
                        if "android_id" in s:
                            logger.info("AndroidId {0} ".format(s['android_id']))
                            andId = s['android_id']
                        else:
                            andId = ""

                        if "model" in s:
                            logger.info("Model {0} ".format(s['model']))
                            model = s['model']
                        else:
                            model = ""

                        if 'eA' in s:
                            logger.info("Action {0} ".format(s['eA']))
                            eve_action = s['eA']
                        else:
                            eve_action = ""

                        if 'eL' in s:
                            logger.info("Label ".format(s['eL']))
                            eve_name = s['eL']
                        else:
                            eve_name = ""

                        if 'eC' in s:
                            logger.info("Category {0} ".format(s['eC']))
                            eve_category = s['eC']
                        else:
                            eve_category = ""

                        if 'eV' in s:
                            logger.info("Value ".format(s['eV']))
                            eve_value = s['eV']
                        else:
                            eve_value = ""

                        if 'user_id' in s:
                            logger.info("user_id {0} ".format(s['user_id']))
                            devId = s['user_id']
                        else:
                            devId = ""

                        if 'clientip' in s:
                            logger.info("Ip {0} ".format(s['clientip']))
                            ip = s['clientip']
                        else:
                            ip = ""

                        if 'country_code' in s:
                            logger.info("Country Code {0} ".format(s['country_code']))
                            country = s['country_code']
                        else:
                            country = ""

                        if 'eT' in s:
                            logger.info("eT {0} ".format(s['eT']))
                            epochC = s['eT']
                        else:
                            epochC = 0

                        if 'eTz' in s:
                            logger.info("eTz {0} ".format(s['eTz']))
                            tzC = s['eTz']
                        else:
                            tzC = ""

                        if 'timestamp' in s:
                            logger.info("Timestamp {0} ".format(s['timestamp']))
                            timestamp = s['timestamp']
                            epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                            ti = time.mktime(epochR.timetuple())
                        else:
                            ti = 0

                        if 'package_name' in s:
                            logger.info("Product {0} ".format(s['package_name']))
                            package_name = s['package_name']
                        else:
                            package_name = ""
                        if "app_version" in s:
                            app_version = s['app_version'].split(" ")[0]
                        else:
                            app_version = ""
                        if "com.cube26.cube26libraries" in package_name:
                            product = "lib"
                        else:
                            product = ""
                        l = {"andId": andId,
                             "model": model,
                             "devId": devId,
                             "eve_category": eve_category,
                             "eve_action": eve_action,
                             "eve_name": eve_name,
                             "eve_val": eve_value,
                             "product": product,
                             "meta3": ip,
                             "meta2": country,
                             "meta1": "manual",
                             "epochC": epochC,
                             "tzC": tzC,
                             "version": app_version,
                             "epochS": epochC,
                             "tzS": tzC,
                             "epochR": ti,
                             "tzR": tzC
                             }

                        json_file.append(l)
                        logger.info("Appeneded in Json file {0}".format(l))
                    if "POST" == method:
                        logger.info("With in Method {0}".format(method))
                        if "android_id" in s:
                            logger.info("Android {0} ".format(s['android_id']))
                            andId = s['android_id']
                        else:
                            andId = ""
                        if "model" in s:
                            logger.info("Model {0} ".format(s['model']))
                            model = s['model']
                        else:
                            model = ""
                        if 'eA' in s:
                            logger.info("Action {0} ".format(s['eA']))
                            eve_action = s['eA']
                        else:
                            eve_action = ""
                        if 'eL' in s:
                            logger.info("Label ".format(s['eL']))
                            eve_name = s['eL']
                        else:
                            eve_name = ""
                        if 'eC' in s:
                            logger.info("Category {0} ".format(s['eC']))
                            eve_category = s['eC']
                        else:
                            eve_category = ""
                        if 'eV' in s:
                            logger.info("Value ".format(s['eV']))
                            eve_value = s['eV']
                        else:
                            eve_value = ""
                        if 'user_id' in s:
                            logger.info("user_id {0} ".format(s['user_id']))
                            devId = s['user_id']
                        else:
                            devId = ""
                        if 'clientip' in s:
                            logger.info("Ip {0} ".format(s['clientip']))
                            ip = s['clientip']
                        else:
                            ip = ""
                        if 'country_code' in s:
                            logger.info("Country Code {0} ".format(s['country_code']))
                            country = s['country_code']
                        else:
                            country = ""
                        if 'eT' in s:
                            logger.info("eT {0} ".format(s['eT']))
                            epochC = s['eT']
                        else:
                            epochC = 0
                        if 'eTz' in s:
                            logger.info("eTz {0} ".format(s['eTz']))
                            tzC = s['eTz']
                        else:
                            tzC = ""
                        if 'timestamp' in s:
                            logger.info("Timestamp {0} ".format(s['timestamp']))
                            timestamp = s['timestamp']
                            epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                            ti = time.mktime(epochR.timetuple())
                        else:
                            ti = 0

                        if 'package_name' in s:
                            logger.info("Product {0} ".format(s['package_name']))
                            package_name = s['package_name']
                        else:
                            package_name = ""
                        if "app_version" in s:
                            app_version = s['app_version'].split(" ")[0]
                        else:
                            app_version = ""
                        if "com.cube26.cube26libraries" in package_name:
                            product = "lib"
                        else:
                            product = ""
                        message = s['message'].split("&")
                        if 'eT' in message and 'eTz' in message:
                            epochS = message[5].split("=")[1]
                            tzS = message[6].split("=")[1]
                        else:
                            epochS = 0
                            tzS = ""

                        l = {"andId": andId,
                             "model": model,
                             "devId": devId,
                             "eve_category": eve_category,
                             "eve_action": eve_action,
                             "eve_name": eve_name,
                             "eve_val": eve_value,
                             "product": product,
                             "meta3": ip,
                             "meta2": country,
                             "meta1": "manual",
                             "epochC": epochC,
                             "tzC": tzC,
                             "version": app_version,
                             "epochS": epochS,
                             "tzS": tzS,
                             "epochR": ti,
                             "tzR": tzC
                             }

                        json_file.append(l)
                        logger.info("Appeneded in Json file {0}".format(l))
                    logger.info("Value {0}".format(json_file))
                else:
                    if json_file:
                        logger.info("Processing File for storage {0}")
                        filename = "/var/karbonn_converter/raw" + str(datetime.now()).replace("_", "").replace(" ","") + ".json"
                        fe = open(filename, 'w')
                        json.dump(json_file, fe, indent=4)
                        fe.flush()
                        json_file = []
                    logger.info("Its time to sleep")
                    break
            f.close()


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


class MyDaemon(Daemon):
    def run(self):
        code = json_converter()
        code.run()
        filename="/tmp/test.txt"
        logfile = open(filename, "r")
        loglines = follow(logfile)
        global json_file
        json_file = []
        for line in loglines:
            if line and line.strip():
                logger.info("Tail line {0}".format(line))
                json_line = json_converter_tail(line)
                if json_line:
                    json_file.append(json_line)
                if json_file:
                    logger.info("Processing File for storage {0}")
                    filename = "/var/karbonn_converter/raw" + str(datetime.now()).replace("_", "").replace(" ","") + ".json"
                    fe = open(filename, 'w')
                    json.dump(json_file, fe, indent=4)
                    fe.flush()
                    json_file = []


def json_converter_tail(content):
    if content:
        if "_grokparsefailure" in content:
            return
        json_data = content
        logger.info("Loading Json")
        s = json.loads(json_data)
        logger.info("method")
        method = s['method']
        ip_check=s['clientip']
        if ip_check == "127.0.0.1":
            return
        logger.info("Method for processing {0} ".format(method))
        if "GET" == method:
            logger.info("With in Method {0} ".format(method))
            if "android_id" in s:
                logger.info("AndroidId {0} ".format(s['android_id']))
                andId = s['android_id']
            else:
                andId = ""

            if "model" in s:
                logger.info("Model {0} ".format(s['model']))
                model = s['model']
            else:
                model = ""

            if 'eA' in s:
                logger.info("Action {0} ".format(s['eA']))
                eve_action = s['eA']
            else:
                eve_action = ""

            if 'eL' in s:
                logger.info("Label ".format(s['eL']))
                eve_name = s['eL']
            else:
                eve_name = ""

            if 'eC' in s:
                logger.info("Category {0} ".format(s['eC']))
                eve_category = s['eC']
            else:
                eve_category = ""

            if 'eV' in s:
                logger.info("Value ".format(s['eV']))
                eve_value = s['eV']
            else:
                eve_value = ""

            if 'user_id' in s:
                logger.info("user_id {0} ".format(s['user_id']))
                devId = s['user_id']
            else:
                devId = ""

            if 'clientip' in s:
                logger.info("Ip {0} ".format(s['clientip']))
                ip = s['clientip']
            else:
                ip = ""

            if 'country_code' in s:
                logger.info("Country Code {0} ".format(s['country_code']))
                country = s['country_code']
            else:
                country = ""

            if 'eT' in s:
                logger.info("eT {0} ".format(s['eT']))
                epochC = s['eT']
            else:
                epochC = 0

            if 'eTz' in s:
                logger.info("eTz {0} ".format(s['eTz']))
                tzC = s['eTz']
            else:
                tzC = ""

            if 'timestamp' in s:
                logger.info("Timestamp {0} ".format(s['timestamp']))
                timestamp = s['timestamp']
                epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                ti = time.mktime(epochR.timetuple())
            else:
                ti = 0

            if 'package_name' in s:
                logger.info("Product {0} ".format(s['package_name']))
                package_name = s['package_name']
            else:
                package_name = ""
            if "app_version" in s:
                app_version = s['app_version'].split(" ")[0]
            else:
                app_version = ""
            if "com.cube26.cube26libraries" in package_name:
                product = "lib"
            else:
                product = ""
            l = {"andId": andId,
                 "model": model,
                 "devId": devId,
                 "eve_category": eve_category,
                 "eve_action": eve_action,
                 "eve_name": eve_name,
                 "eve_val": eve_value,
                 "product": product,
                 "meta3": ip,
                 "meta2": country,
                 "meta1": "manual",
                 "epochC": epochC,
                 "tzC": tzC,
                 "version": app_version,
                 "epochS": epochC,
                 "tzS": tzC,
                 "epochR": ti,
                 "tzR": tzC
                 }

            logger.info("Appeneded in Json file {0}".format(l))
            return l

        if "POST" == method:
            logger.info("With in Method {0}".format(method))
            if "android_id" in s:
                logger.info("Android {0} ".format(s['android_id']))
                andId = s['android_id']
            else:
                andId = ""
            if "model" in s:
                logger.info("Model {0} ".format(s['model']))
                model = s['model']
            else:
                model = ""
            if 'eA' in s:
                logger.info("Action {0} ".format(s['eA']))
                eve_action = s['eA']
            else:
                eve_action = ""
            if 'eL' in s:
                logger.info("Label ".format(s['eL']))
                eve_name = s['eL']
            else:
                eve_name = ""
            if 'eC' in s:
                logger.info("Category {0} ".format(s['eC']))
                eve_category = s['eC']
            else:
                eve_category = ""
            if 'eV' in s:
                logger.info("Value ".format(s['eV']))
                eve_value = s['eV']
            else:
                eve_value = ""
            if 'user_id' in s:
                logger.info("user_id {0} ".format(s['user_id']))
                devId = s['user_id']
            else:
                devId = ""
            if 'clientip' in s:
                logger.info("Ip {0} ".format(s['clientip']))
                ip = s['clientip']
            else:
                ip = ""
            if 'country_code' in s:
                logger.info("Country Code {0} ".format(s['country_code']))
                country = s['country_code']
            else:
                country = ""
            if 'eT' in s:
                logger.info("eT {0} ".format(s['eT']))
                epochC = s['eT']
            else:
                epochC = 0
            if 'eTz' in s:
                logger.info("eTz {0} ".format(s['eTz']))
                tzC = s['eTz']
            else:
                tzC = ""
            if 'timestamp' in s:
                logger.info("Timestamp {0} ".format(s['timestamp']))
                timestamp = s['timestamp']
                epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                ti = time.mktime(epochR.timetuple())
            else:
                ti = 0

            if 'package_name' in s:
                logger.info("Product {0} ".format(s['package_name']))
                package_name = s['package_name']
            else:
                package_name = ""
            if "app_version" in s:
                app_version = s['app_version'].split(" ")[0]
            else:
                app_version = ""
            if "com.cube26.cube26libraries" in package_name:
                product = "lib"
            else:
                product = ""
            message = s['message'].split("&")
            if 'eT' in message and 'eTz' in message:
                epochS = message[5].split("=")[1]
                tzS = message[6].split("=")[1]
            else:
                epochS = 0
                tzS = ""
            l = {"andId": andId,
                 "model": model,
                 "devId": devId,
                 "eve_category": eve_category,
                 "eve_action": eve_action,
                 "eve_name": eve_name,
                 "eve_val": eve_value,
                 "product": product,
                 "meta3": ip,
                 "meta2": country,
                 "meta1": "manual",
                 "epochC": epochC,
                 "tzC": tzC,
                 "version": app_version,
                 "epochS": epochS,
                 "tzS": tzS,
                 "epochR": ti,
                 "tzR": tzC
                 }

            logger.info("Appeneded in Json file {0}".format(l))
            return l


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
