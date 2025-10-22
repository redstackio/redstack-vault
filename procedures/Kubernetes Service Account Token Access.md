---
id: 11e6166b-19f4-4806-b4d6-f5ab9c57767f
name: Kubernetes Service Account Token Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.003683+00:00'
updated_at: '2023-04-10T20:34:02.439779+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tags:
- '[[Container Environment]]'
- '[[Kubernetes]]'
- '[[Service Account]]'
---

# Kubernetes Service Account Token Access

## Summary

Kubernetes provides a default service account for each namespace that is automatically mounted into pods running in the namespace. The service account is used to authenticate and authorize API requests made from within the pod. The service account token is mounted into the pod at /var/run/secrets/k

## Description

# Description

Kubernetes provides a default service account for each namespace that is automatically mounted into pods running in the namespace. The service account is used to authenticate and authorize API requests made from within the pod. The service account token is mounted into the pod at /var/run/secrets/kubernetes.io/serviceaccount/token. An attacker who gains access to the token can use it to authenticate as the service account and make requests to the Kubernetes API server, potentially allowing for further lateral movement within the cluster.

## Requirements

1. Access to a container running within a Kubernetes cluster

## Defense

1. Limit access to the Kubernetes API server to only trusted sources

1. Monitor for unauthorized access to the Kubernetes service account token

1. Rotate service account tokens regularly

## Objectives

1. Gain access to the Kubernetes service account token

1. Authenticate as the service account and make requests to the Kubernetes API server

# Instructions

1. 

2. service account token can be used to authenticate and make requests to the Kubernetes API server using the Kubernetes API directly.

**Code**: [[kubectl]]

> 

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]

## Tags

- [[Container Environment]]
- [[Kubernetes]]
- [[Service Account]]
