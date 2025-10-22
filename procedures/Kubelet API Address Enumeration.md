---
id: b1e526ca-9d9c-4521-857c-76df4681381c
name: Kubelet API Address Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.520451+00:00'
updated_at: '2023-04-10T20:34:01.297998+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[API addresses that you should know]]'
- '[[Kubelet API]]'
- '[[Kubernetes]]'
commands:
- '[[Curl Kubernetes API server]]'
- '[[Curl Kubernetes metrics endpoint]]'
- '[[Curl Kubernetes pods endpoint]]'
---

# Kubelet API Address Enumeration

## Summary

The Kubelet is the primary node agent that runs on each worker node in a Kubernetes cluster. It is responsible for managing the state of individual nodes, including starting and stopping pods. The Kubelet API is used by the Kubernetes control plane to communicate with the Kubelet on each node. An a

## Description

# Description

The Kubelet is the primary node agent that runs on each worker node in a Kubernetes cluster. It is responsible for managing the state of individual nodes, including starting and stopping pods. The Kubelet API is used by the Kubernetes control plane to communicate with the Kubelet on each node. An attacker can use the Kubelet API to enumerate information about the Kubernetes cluster, including the pods running on each node. This information can be used to identify potential targets for further exploitation.

## Requirements

1. Access to the Kubernetes cluster network

## Defense

1. Disable the Kubelet API if it is not needed for cluster operations

1. Use RBAC to limit access to the Kubelet API

1. Monitor the Kubelet API for unauthorized access or unusual activity

## Objectives

1. Enumerate information about the Kubernetes cluster

1. Identify potential targets for further exploitation

# Instructions

1. Replace <IP address> with the IP address of a worker node in the Kubernetes cluster.

**Code**: [[curl -k https://<IP address>:10250
curl -k https:/]]

> The first command retrieves the Kubelet API root endpoint. The second command retrieves metrics about the Kubelet. The third command retrieves information about the pods running on the node.

**Command** ([[Curl Kubernetes API server]]):

```bash
curl -k https://<IP address>:10250
```

**Command** ([[Curl Kubernetes metrics endpoint]]):

```bash
curl -k https://<IP address>:10250/metrics
```

**Command** ([[Curl Kubernetes pods endpoint]]):

```bash
curl -k https://<IP address>:10250/pods
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Curl Kubernetes API server]]
- [[Curl Kubernetes metrics endpoint]]
- [[Curl Kubernetes pods endpoint]]

## Tags

- [[API addresses that you should know]]
- [[Kubelet API]]
- [[Kubernetes]]
