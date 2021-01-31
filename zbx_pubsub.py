#!/usr/bin/python3

import os
from google.cloud import pubsub

import argparse
import time

#
# Settings
#
ENABLE_LOG = True
LOG_FILE = "/var/log/zabbix/zbx_pubsub.log"

project_id = "your_gcp_project_id"

def log(msg):
    """
    Send log line to stdout and to LOG_FILE if logging is enabled
    """
    msg = "[%s] %s" % (logTimeStamp(), msg)

    # Print to stdout
    print(msg)

    # Output to logfile
    if ENABLE_LOG:
        try:
            lf = open(LOG_FILE, 'a')
            lf.write("%s\n" % (msg))

        except (OSError) as exc:
            print("Error while trying to log event: %s" % rlb(str(exc)))
            return False
        
        lf.close()    

    return True

def rlb(thing):
    """
    Return thing with line breaks replaced by spaces
    """
    return thing.replace("\r", " ").replace("\n", " ")

def logTimeStamp():
    """
    Return current date/time formatted for log output
    """
    return  time.strftime('%a %b %d %H:%M:%S %Y')

# Arguments parser
parser = argparse.ArgumentParser(description='Send Zabbix notification to GCP Pub/Sub.')
parser.add_argument('pubsub_topic', metavar=('Topic'), type=str, help='PubSub topic.')
parser.add_argument('subject', metavar=('Subject'), type=str, help='Subject you want to push to the device(s).')
parser.add_argument('message', metavar=('Message'), type=str, help='Message you want to push to the device(s).')

# Argument processing
args = parser.parse_args()
subject = args.subject
message = args.message

log("Message: is  %s" % (message))

publisher = pubsub.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id,
    topic='zabbix',  # Set this to something appropriate.
)

publisher.publish(topic_name, b'Zabbix Alert!', subject=subject, message=message)
