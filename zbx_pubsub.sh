#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/root/.ssh/gcp-project-id.json"
PROJECT="gcp-project-id"
TOPIC="zabbix"

gcloud auth activate-service-account --key-file=[path to gcp project key] 

ACCESS_TOKEN=$(gcloud auth print-access-token)

curl -H 'content-type: application/json' -H "Authorization: Bearer $ACCESS_TOKEN" -X POST --data $'{ "messages": [{"data": "abcd"}]}' https://pubsub.googleapis.com/v1/projects/$PROJECT/topics/$TOPIC:publish
