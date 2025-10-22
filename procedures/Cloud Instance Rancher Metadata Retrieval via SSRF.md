---
id: 69c95c3f-3c4f-4db2-b1a2-0824b42afb59
name: Cloud Instance Rancher Metadata Retrieval via SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.800958+00:00'
updated_at: '2023-04-10T20:24:14.009532+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Rancher]]'
commands:
- '[[Curl rancher-metadata]]'
---

# Cloud Instance Rancher Metadata Retrieval via SSRF

## Summary

Cloud instances often have access to metadata APIs that provide information about the instance itself, including sensitive data such as access keys. Server-Side Request Forgery (SSRF) can be used to retrieve this data by sending a request to the metadata API URL. This specific procedure focuses on 

## Description

# Description

Cloud instances often have access to metadata APIs that provide information about the instance itself, including sensitive data such as access keys. Server-Side Request Forgery (SSRF) can be used to retrieve this data by sending a request to the metadata API URL. This specific procedure focuses on retrieving Rancher metadata via SSRF. 

Technical Explanation: This procedure involves sending a crafted request to the metadata API URL using a vulnerable server as a proxy. The request will be redirected to the Rancher metadata API, which will return sensitive data about the instance. 

Business Value: This technique can be used to gain access to sensitive data such as access keys, which can lead to further compromise of the cloud environment.

## Requirements

1. Access to a vulnerable server that can be used as a proxy

1. Knowledge of the metadata API URL for the cloud instance

1. Ability to send crafted requests to the vulnerable server

## Defense

1. Restrict access to the metadata API URL to trusted sources only

1. Implement input validation to prevent SSRF attacks

1. Monitor network traffic for suspicious activity

## Objectives

1. Retrieve sensitive data such as access keys from cloud instances

1. Gain access to the cloud environment

# Instructions

1. Use this command to retrieve metadata from the Rancher server.

**Code**: [[curl http://rancher-metadata/<version>/<path>]]

> The 'version' parameter in the URL should be replaced with the version of the Rancher metadata API you want to use (e.g. '2015-12-19'). The 'path' parameter should be replaced with the path to the metadata you want to retrieve (e.g. 'self/container/name'). This command can be used to retrieve information about the current container, such as its name, IP address, and more.

**Command** ([[Curl rancher-metadata]]):

```bash
curl http://rancher-metadata/<version>/<path>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Curl rancher-metadata]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Rancher]]
