---
id: c1208877-1b69-4dbb-bd23-3541be592851
name: Kubernetes Endpoint Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.397235+00:00'
updated_at: '2023-04-10T20:34:01.643819+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Interesting endpoints to reach]]'
- '[[Kubernetes]]'
commands:
- '[[List default namespace daemonsets]]'
- '[[List Deployments]]'
- '[[List Pods]]'
- '[[List secrets using curl command]]'
---

# Kubernetes Endpoint Enumeration

## Summary

Kubernetes is a popular container orchestration system that is widely used in cloud environments. This procedure focuses on enumerating interesting endpoints in a Kubernetes cluster that can be accessed by an attacker with valid credentials. By listing pods, secrets, deployments, and daemonsets, an

## Description

# Description

Kubernetes is a popular container orchestration system that is widely used in cloud environments. This procedure focuses on enumerating interesting endpoints in a Kubernetes cluster that can be accessed by an attacker with valid credentials. By listing pods, secrets, deployments, and daemonsets, an attacker can gain valuable information about the target environment, such as the running services, credentials, and configurations. This information can be used to launch further attacks, such as lateral movement or privilege escalation.

## Requirements

1. Valid JWT token for authentication

1. Access to the Kubernetes API server

1. Curl or similar tool for sending HTTP requests

## Defense

1. Use RBAC to limit the access of Kubernetes API server to only authorized users and services

1. Use network policies to restrict the traffic between pods and nodes

1. Use encryption to protect the communication between the Kubernetes API server and the clients

## Objectives

1. Enumerate interesting endpoints in a Kubernetes cluster

1. Gather information about the running services, credentials, and configurations

1. Identify potential attack vectors for further exploitation

# Instructions

1. To list pods in the default namespace, run the following command:

**Code**: [[# List Pods
curl -v -H "Authorization: Bearer <jwt]]

> This command sends an HTTP GET request to the Kubernetes API server to list all the pods in the default namespace. The -H option is used to set the Authorization header with the JWT token. The <jwt_token>, <master_ip>, and <port> placeholders should be replaced with the actual values for the target environment.

**Command** ([[List Pods]]):

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/pods/
```

2. To list secrets in the default namespace, run the following command:

**Code**: [[# List secrets
curl -v -H "Authorization: Bearer <]]

> This command sends an HTTP GET request to the Kubernetes API server to list all the secrets in the default namespace. The -H option is used to set the Authorization header with the JWT token. The <jwt_token>, <master_ip>, and <port> placeholders should be replaced with the actual values for the target environment.

**Command** ([[List secrets using curl command]]):

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/default/secrets/
```

3. To list deployments in the default namespace, run the following command:

**Code**: [[# List deployments
curl -v -H "Authorization: Bear]]

> This command sends an HTTP GET request to the Kubernetes API server to list all the deployments in the default namespace. The -H option is used to set the Authorization header with the JWT token. The <jwt_token>, <master_ip>, and <port> placeholders should be replaced with the actual values for the target environment.

**Command** ([[List Deployments]]):

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/deployments

```

4. To list daemonsets in the default namespace, run the following command:

**Code**: [[# List daemonsets
curl -v -H "Authorization: Beare]]

> This command sends an HTTP GET request to the Kubernetes API server to list all the daemonsets in the default namespace. The -H option is used to set the Authorization header with the JWT token. The <jwt_token>, <master_ip>, and <port> placeholders should be replaced with the actual values for the target environment.

**Command** ([[List default namespace daemonsets]]):

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/apis/extensions/v1beta1/namespaces/default/daemonsets

```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[List default namespace daemonsets]]
- [[List Deployments]]
- [[List Pods]]
- [[List secrets using curl command]]

## Tags

- [[Interesting endpoints to reach]]
- [[Kubernetes]]
