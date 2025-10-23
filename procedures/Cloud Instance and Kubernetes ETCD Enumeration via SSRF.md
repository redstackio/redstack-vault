---
id: cf447f25-cfed-4c27-9979-0204675a275a
name: Cloud Instance and Kubernetes ETCD Enumeration via SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.734002+00:00'
updated_at: '2023-04-10T20:24:00.903364+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Kubernetes ETCD]]'
commands:
- '[[Get etcd Keys recursively]]'
- '[[Get etcd Version]]'
---

# Cloud Instance and Kubernetes ETCD Enumeration via SSRF

## Summary

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to enumerate cloud instances and Kubernetes ETCD information. An attacker can use this technique to discover information about the target environment, such as the number of cloud instances and version information,

## Description

# Description

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to enumerate cloud instances and Kubernetes ETCD information. An attacker can use this technique to discover information about the target environment, such as the number of cloud instances and version information, which can be used for further attacks. SSRF is a vulnerability that allows an attacker to send crafted requests from a vulnerable web application, bypassing access controls and potentially accessing internal resources. In this case, the attacker sends requests to cloud instance metadata endpoints and Kubernetes ETCD endpoints to retrieve information.

 

## Requirements

1. Access to a vulnerable web application with SSRF vulnerability.

 

## Defense

1. Implement input validation for user-supplied URLs to prevent SSRF vulnerabilities.

1. Use network segmentation to restrict access to cloud instance metadata endpoints and Kubernetes ETCD endpoints.

1. Monitor network traffic for suspicious requests to cloud instance metadata endpoints and Kubernetes ETCD endpoints.

 

## Objectives

1. Enumerate cloud instances and Kubernetes ETCD information.

1. Gather version information for cloud instances and Kubernetes ETCD.

 

# Instructions

1. To retrieve the version and list of keys in ETCD, execute the following commands:

 



**Code**: [[curl -L http://127.0.0.1:2379/version
curl http://]]



> The first command retrieves the version of ETCD running on the specified IP address and port. The second command retrieves the list of keys stored in ETCD, including all sub-keys and their values. The 'recursive=true' argument ensures that all sub-keys are included in the response. Note that this command can potentially expose sensitive information such as API keys and internal IP addresses and ports, so it should be used with caution and only in secure environments.



**Command** ([[Get etcd Version]]):

```bash
curl -L http://127.0.0.1:2379/version
```





**Command** ([[Get etcd Keys recursively]]):

```bash
curl http://127.0.0.1:2379/v2/keys/?recursive=true
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get etcd Keys recursively]]
- [[Get etcd Version]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Kubernetes ETCD]]


