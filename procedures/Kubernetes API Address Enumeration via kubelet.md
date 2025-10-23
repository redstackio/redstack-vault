---
id: 061199cf-7813-4b7a-9ffa-c32673ba0bab
name: Kubernetes API Address Enumeration via kubelet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.549081+00:00'
updated_at: '2023-04-10T20:34:00.965468+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Service Discovery|T1007 - System Service Discovery]]'
tags:
- '[[API addresses that you should know]]'
- '[[kubelet (Read only)]]'
- '[[Kubernetes]]'
commands:
- '[[Retrieve Pod Information]]'
---

# Kubernetes API Address Enumeration via kubelet

## Summary

This procedure involves enumerating the API addresses of a Kubernetes cluster via the kubelet API. The kubelet API provides read-only access to the state of the Kubernetes node, including information about running pods, containers, and their associated metadata. By accessing this API, an attacker c

## Description

# Description

This procedure involves enumerating the API addresses of a Kubernetes cluster via the kubelet API. The kubelet API provides read-only access to the state of the Kubernetes node, including information about running pods, containers, and their associated metadata. By accessing this API, an attacker can gain valuable information about the cluster's configuration and the applications running on it. This information can then be used to plan further attacks on the cluster. Business value of this attack is that an attacker can gain access to sensitive information about the Kubernetes cluster which can lead to data theft, data tampering, and other malicious activities.

 

## Requirements

1. Access to the kubelet API

1. Curl or similar tool to send HTTP requests

 

## Defense

1. Disable the kubelet API if it is not required for the cluster's operation

1. Restrict access to the kubelet API to trusted sources only

1. Monitor the kubelet API for suspicious activity

 

## Objectives

1. Enumerate the API addresses of a Kubernetes cluster via the kubelet API

1. Gather information about the cluster's configuration and the applications running on it

 

# Instructions

1. Replace <IP Address> with the IP address of the Kubernetes node and <external-IP> with the external IP address of the node. Run the command in a terminal or command prompt.

 



**Code**: [[curl -k https://<IP Address>:10255
http://<externa]]



> This command sends HTTP requests to the kubelet API endpoints to obtain information about the running pods and containers on the Kubernetes node. The -k option is used to bypass SSL certificate verification.



**Command** ([[Retrieve Pod Information]]):

```bash
curl -k https://<IP Address>:10255
http://<external-IP>:10255/pods
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[Retrieve Pod Information]]

## Tags

- [[API addresses that you should know]]
- [[kubelet (Read only)]]
- [[Kubernetes]]


