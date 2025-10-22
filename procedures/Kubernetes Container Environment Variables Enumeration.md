---
id: f1cd363b-1843-4c0f-b05a-bbfe41c807c0
name: Kubernetes Container Environment Variables Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.061770+00:00'
updated_at: '2023-04-10T20:34:02.771958+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Container Environment]]'
- '[[Environment Variables]]'
- '[[Kubernetes]]'
commands:
- '[[Extract Redis Master Port]]'
- '[[Extract Redis Master Service Host]]'
- '[[Extract Redis Master Service Port]]'
- '[[Extract Redis Master TCP]]'
---

# Kubernetes Container Environment Variables Enumeration

## Summary

Kubernetes allows for the configuration of environment variables within containers. These environment variables can be used to store sensitive information such as passwords, keys, and tokens. An attacker can use this procedure to enumerate all environment variables within a container, potentially r

## Description

# Description

Kubernetes allows for the configuration of environment variables within containers. These environment variables can be used to store sensitive information such as passwords, keys, and tokens. An attacker can use this procedure to enumerate all environment variables within a container, potentially revealing sensitive information. By using this technique, an attacker can gain a better understanding of the target environment and move laterally within the cluster.

## Requirements

1. Access to the Kubernetes cluster

## Defense

1. Ensure sensitive information is not stored within environment variables

1. Limit access to the Kubernetes cluster to authorized personnel only

1. Monitor the Kubernetes environment for suspicious activity

## Objectives

1. Enumerate all environment variables within a container

1. Identify sensitive information within the environment variables

# Instructions

1. kubectl exec <pod-name> env

**Code**: [[redis-master]]

> This command will list all environment variables within the specified container.

2. 

This is an example output of the environment variables within a container.

**Command** ([[Extract Redis Master Service Host]]):

```bash
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

**Command** ([[Extract Redis Master Service Port]]):

```bash
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

**Command** ([[Extract Redis Master Port]]):

```bash
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

**Command** ([[Extract Redis Master TCP]]):

```bash
REDIS_MASTER_SERVICE_HOST=10.0.0.11
REDIS_MASTER_SERVICE_PORT=6379
REDIS_MASTER_PORT=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP=tcp://10.0.0.11:6379
REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
REDIS_MASTER_PORT_6379_TCP_PORT=6379
REDIS_MASTER_PORT_6379_TCP_ADDR=10.0.0.11
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Extract Redis Master Port]]
- [[Extract Redis Master Service Host]]
- [[Extract Redis Master Service Port]]
- [[Extract Redis Master TCP]]

## Tags

- [[Container Environment]]
- [[Environment Variables]]
- [[Kubernetes]]
