# Zabbix Custom AlertScripts - GCP Pub/Sub 

Two example scripts for sending [custom alerts][zbx_customalerts] to a [GCP Pub/Sub Topic][pub/sub]. 

This code is intended to be an _example_. You will likely need to change or
update values to match your setup.

* [zbx_pubsub.py][py] - a python script to publish alert to Pub/Sub
* [zbx__pubsub.sh][sh] - a shell script to publish alert to Pub/Sub

# Reference

[Zabbix alertscripts][sriccio] provides good details of deploying the customer scripts and configuring a new Zabbix media type. 

[pub/sub]: https://cloud.google.com/pubsub/docs/publisher
[zbx_customalerts]: https://www.zabbix.com/documentation/current/manual/config/notifications/media/script
[sriccio]: https://github.com/sriccio/zabbix-alertscripts
[py]: https://github.com/highway7/zabbix_pubsub/blob/main/zbx_pubsub.py
[sh]: https://github.com/highway7/zabbix_pubsub/blob/main/zbx_pubsub.sh