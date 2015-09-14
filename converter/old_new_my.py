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
        input_file = "/home/cube26/Desktop/logstash.stdout"
        with open(input_file, 'r') as f:
            content = f.readline()
            while True:
                content = f.readline()
                logger.info("Content of file for processing {0}".format(content))
                logger.info("Going for processing")
                logger.info("Position of file {0}".format(f.tell()))
                if content:
                    json_data = content
                    logger.info("Loading Json")
                    s = json.loads(json_data)
                    logger.info("method")
                    method = s['method']
                    logger.info("Method for processing {0} ".format(method))
                    if "GET" == method:
                        logger.info("With in Method {0} ".format(method))
                        andId = s['android_id']
                        model = s['model']
                        eve_action = s['eA']
                        eve_name = s['eL']
                        eve_category = s['eC']
                        eve_value = s['eV']
                        devId = s['user_id']
                        ip = s['geoip']['ip']
                        country = s['country_code']
                        epochC = s['eT']
                        tzC = s['eTz']
                        timestamp = s['timestamp']
                        epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                        ti = time.mktime(epochR.timetuple())
                        package_name = s['package_name']
                        if "app_version" in s:
                            app_version = s['app_version'].split(" ")[0]
                        else:
                            app_version = ""
                        if "com.cube26.cube26libraries" in package_name:
                            product = "lib"
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
                        message = s['message'].split("&")
                        epochS = message[5].split("=")[1]
                        tzS = message[6].split("=")[1]
                        andId = s['android_id']
                        model = s['model']
                        eve_action = s['eA']
                        eve_name = s['eL']
                        eve_category = s['eC']
                        eve_value = s['eV']
                        devId = s['user_id']
                        ip = s['geoip']['ip']
                        country = s['country_code']
                        epochC = s['eT']
                        tzC = s['eTz']
                        timestamp = s['timestamp']
                        epochR = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S +0000")
                        ti = time.mktime(epochR.timetuple())
                        package_name = s['package_name']
                        if "app_version" in s:
                            app_version = s['app_version'].split(" ")[0]
                        else:
                            app_version = ""
                        if "com.cube26.cube26libraries" in package_name:
                            product = "lib"
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
                        filename = "/tmp/raw" + str(datetime.now()).replace("_", "") + ".json"
                        fe = open(filename, 'w')
                        json.dump(json_file, fe, indent=4)
                        fe.flush()
                        json_file = []
                    logger.info("Its time to sleep")
                    f.next()
                    time.sleep(5)
                    continue


class MyDaemon(Daemon):
    def run(self):
        code = json_converter()
        code.run()


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
