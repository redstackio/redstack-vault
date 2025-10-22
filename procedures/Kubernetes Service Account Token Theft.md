---
id: db9d9ef7-e9a5-4262-bd32-4f35b0e5f1df
name: Kubernetes Service Account Token Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.381970+00:00'
updated_at: '2023-04-06T03:56:17.398594+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Code Signing|T1553.002 - Code Signing]]'
tags:
- '[[Container - Kubernetes Pentest]]'
- '[[Obtaining Service Account Token]]'
commands:
- '[[Retrieve Kubernetes Service Account Token]]'
---

# Kubernetes Service Account Token Theft

## Summary

Kubernetes service account tokens are used to authenticate between Kubernetes components and the Kubernetes API server. These tokens can be used to obtain sensitive information and perform unauthorized actions within the cluster. An attacker can obtain these tokens by exploiting vulnerabilities in 

## Description

# Description

Kubernetes service account tokens are used to authenticate between Kubernetes components and the Kubernetes API server. These tokens can be used to obtain sensitive information and perform unauthorized actions within the cluster. An attacker can obtain these tokens by exploiting vulnerabilities in Kubernetes components or by compromising a pod that has access to the token. Once the token is obtained, an attacker can use it to execute commands and access resources within the cluster.

Technical Explanation: Kubernetes service account tokens are stored in the file system of the pod at the path '/var/run/secrets/kubernetes.io/serviceaccount/token'. An attacker can obtain the token by accessing the file system of the pod or by running commands within the pod. The token can then be used to authenticate with the Kubernetes API server and perform unauthorized actions.

Business Value: An attacker who gains access to a Kubernetes service account token can compromise the entire cluster and steal sensitive data. This can lead to significant financial and reputational damage for the organization.

## Requirements

1. Access to the Kubernetes cluster

1. Knowledge of Kubernetes components and pods

1. Ability to execute commands within a pod

## Defense

1. Limit access to the Kubernetes cluster to authorized personnel only

1. Implement RBAC policies to restrict access to sensitive resources

1. Monitor the Kubernetes API server for unauthorized access and actions

## Objectives

1. Steal Kubernetes service account tokens

1. Gain access to sensitive data within the cluster

1. Perform unauthorized actions within the cluster

# Instructions

1. Use this token to authenticate with the Kubernetes API server

**Code**: [[/var/run/secrets/kubernetes.io/serviceaccount/toke]]

> This token is used to authenticate requests to the Kubernetes API server. It is automatically mounted into pods that are created with a service account. The token can be used to authenticate requests to the API server from within the pod or from outside the cluster (if the API server is exposed externally).

**Command** ([[Retrieve Kubernetes Service Account Token]]):

```bash
/var/run/secrets/kubernetes.io/serviceaccount/token
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Code Signing|T1553.002 - Code Signing]]

## Commands Used

- [[Retrieve Kubernetes Service Account Token]]

## Tags

- [[Container - Kubernetes Pentest]]
- [[Obtaining Service Account Token]]
