---
id: 8889cf25-f63e-4dc3-87f4-15f5df18a723
name: Kubernetes etcd API Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.488408+00:00'
updated_at: '2023-04-10T20:34:02.099446+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Data Compressed|T1002 - Data Compressed]]'
tags:
- '[[API addresses that you should know]]'
- '[[etcd API]]'
- '[[Kubernetes]]'
commands:
- '[[Get etcd keys]]'
- '[[Get etcd version]]'
---

# Kubernetes etcd API Enumeration

## Summary

Kubernetes etcd API Enumeration is a technique used to discover the etcd API endpoints of a Kubernetes cluster. etcd is a distributed key-value store that stores the configuration data of a Kubernetes cluster. This technique can be used by an attacker to gather information about the cluster's confi

## Description

# Description

Kubernetes etcd API Enumeration is a technique used to discover the etcd API endpoints of a Kubernetes cluster. etcd is a distributed key-value store that stores the configuration data of a Kubernetes cluster. This technique can be used by an attacker to gather information about the cluster's configuration and architecture, which can be used to plan further attacks. By enumerating the etcd API endpoints, an attacker can determine the keys and values stored in the etcd database, which can contain sensitive information such as secrets, certificates, and passwords.

Technical Explanation: etcd is a distributed key-value store that stores the configuration data of a Kubernetes cluster. The etcd API endpoints can be accessed using the curl command or the etcdctl command-line tool. The etcdctl command-line tool can be used to read, write, and delete keys and values from the etcd database. The curl command can be used to retrieve the version of the etcd API and to enumerate the keys and values stored in the etcd database.

Business Value: An attacker can use this technique to gather information about the target Kubernetes cluster, such as the configuration data, architecture, and sensitive information. This information can be used to plan further attacks and to gain unauthorized access to the cluster.

 

## Requirements

1. Access to the Kubernetes cluster

1. Authentication credentials

 

## Defense

1. Ensure that the etcd API endpoints are not exposed to the internet

1. Implement access controls to restrict access to the etcd API endpoints

1. Encrypt sensitive data stored in the etcd database

 

## Objectives

1. Discover the etcd API endpoints of a Kubernetes cluster

1. Enumerate the keys and values stored in the etcd database

 

# Instructions

1. Run the following commands in a terminal:

 



**Code**: [[curl -k https://<IP address>:2379
curl -k https://]]



> The first command retrieves the version of the etcd API. The second command retrieves the keys and values stored in the etcd database. The --prefix and --keys-only flags are used to retrieve only the keys and not the values.



**Command** ([[Get etcd version]]):

```bash
curl -k https://<IP address>:2379/version
```





**Command** ([[Get etcd keys]]):

```bash
etcdctl --endpoints=http://<MASTER-IP>:2379 get / --prefix --keys-only
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Data Compressed|T1002 - Data Compressed]]

## Commands Used

- [[Get etcd keys]]
- [[Get etcd version]]

## Tags

- [[API addresses that you should know]]
- [[etcd API]]
- [[Kubernetes]]


