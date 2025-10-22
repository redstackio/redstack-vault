---
id: 119b7472-713c-4b1c-bdd7-54dd5d705ad0
name: Kubernetes Privileged Service Account Token Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.363869+00:00'
updated_at: '2023-04-10T20:33:59.606906+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
tags:
- '[[Kubernetes]]'
- '[[Privileged Service Account Token]]'
commands:
- '[[Retrieve Default Namespace Secrets]]'
- '[[Retrieve Kubernetes Service Account Token]]'
---

# Kubernetes Privileged Service Account Token Retrieval

## Summary

Kubernetes Service Accounts are used to provide a secure way to authenticate pods running within a Kubernetes cluster. A Service Account Token is issued to each pod and can be used to authenticate with the Kubernetes API. A Privileged Service Account Token is a Service Account Token that has been g

## Description

# Description

Kubernetes Service Accounts are used to provide a secure way to authenticate pods running within a Kubernetes cluster. A Service Account Token is issued to each pod and can be used to authenticate with the Kubernetes API. A Privileged Service Account Token is a Service Account Token that has been granted elevated privileges. An attacker who gains access to a Privileged Service Account Token can perform actions within the Kubernetes cluster that they would not normally be authorized to do. 

To retrieve a Privileged Service Account Token, the attacker can simply access the token file located at /run/secrets/kubernetes.io/serviceaccount/token within the pod's file system. The attacker can then use this token to authenticate with the Kubernetes API and gain access to the Kubernetes cluster.

This attack can be carried out by an attacker who has already gained access to a pod within the Kubernetes cluster.

## Requirements

1. Access to a pod within the Kubernetes cluster

## Defense

1. Limit access to pods within the Kubernetes cluster to trusted users and services.

1. Use RBAC to restrict access to Service Accounts and their associated tokens.

1. Monitor the Kubernetes API for unusual activity, such as requests from unknown IP addresses.

## Objectives

1. Retrieve a Privileged Service Account Token

# Instructions

1. Run the following commands:

**Code**: [[$ cat /run/secrets/kubernetes.io/serviceaccount/to]]

> The first command retrieves the token from the pod's file system. The second command uses the token to authenticate with the Kubernetes API and retrieve the secrets from the default namespace.

**Command** ([[Retrieve Kubernetes Service Account Token]]):

```bash
$ cat /run/secrets/kubernetes.io/serviceaccount/token

```

**Command** ([[Retrieve Default Namespace Secrets]]):

```bash
$ curl -k -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]

## Commands Used

- [[Retrieve Default Namespace Secrets]]
- [[Retrieve Kubernetes Service Account Token]]

## Tags

- [[Kubernetes]]
- [[Privileged Service Account Token]]
