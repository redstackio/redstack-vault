---
id: a483c910-3db7-4b12-a979-6f4bd3da82af
name: Kubernetes API Request Simulation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.095742+00:00'
updated_at: '2023-04-10T20:34:03.455806+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Execution through API|T1106 - Execution through API]]'
tags:
- '[[Container Environment]]'
- '[[Kubernetes]]'
- '[[Simulating `kubectl` API Requests]]'
commands:
- '[[Fetch data using curl]]'
---

# Kubernetes API Request Simulation

## Summary

The Kubernetes API Request Simulation procedure is used to simulate `kubectl` API requests within a Kubernetes cluster. This procedure is useful when `kubectl` is not available within a container and manual API requests need to be crafted. The procedure involves crafting HTTP API requests manually 

## Description

# Description

The Kubernetes API Request Simulation procedure is used to simulate `kubectl` API requests within a Kubernetes cluster. This procedure is useful when `kubectl` is not available within a container and manual API requests need to be crafted. The procedure involves crafting HTTP API requests manually using a tool such as `curl` or a programming language such as Python. The Kubernetes API allows for various operations such as creating, updating, and deleting Kubernetes objects such as pods, services, and deployments. By simulating `kubectl` API requests, an attacker can gain access to sensitive information within the cluster, execute arbitrary code, and create persistence mechanisms.

## Requirements

1. Access to the Kubernetes API

1. Knowledge of the Kubernetes API

1. A tool such as `curl` or a programming language such as Python

## Defense

1. Ensure that only authorized users have access to the Kubernetes API server

1. Implement RBAC (Role-Based Access Control) to restrict access to sensitive resources within the cluster

1. Enable audit logging to detect unauthorized access to the Kubernetes API server

## Objectives

1. Simulate `kubectl` API requests within a Kubernetes cluster

1. Gain access to sensitive information within the cluster

1. Execute arbitrary code within the cluster

1. Create persistence mechanisms within the cluster

# Instructions

1. curl -k -H "Authorization: Bearer <TOKEN>" https://<API_SERVER>/api/v1/namespaces/<NAMESPACE>/pods

**Code**: [[curl]]

> This command will retrieve a list of pods within the specified namespace using the Kubernetes API. The `Authorization` header is used to authenticate the request using a bearer token. The `API_SERVER` is the URL of the Kubernetes API server and the `NAMESPACE` is the name of the Kubernetes namespace.

**Command** ([[Fetch data using curl]]):

```bash
curl http://example.com/data
```

2. import requests

url = "https://<API_SERVER>/api/v1/namespaces/<NAMESPACE>/pods"
headers = {
    "Authorization": "Bearer <TOKEN>",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers, verify=False)
print(response.json())

**Code**: [[Python]]

> This code will retrieve a list of pods within the specified namespace using the Kubernetes API. The `Authorization` header is used to authenticate the request using a bearer token. The `API_SERVER` is the URL of the Kubernetes API server and the `NAMESPACE` is the name of the Kubernetes namespace. The `Content-Type` header specifies that the request body is in JSON format. The `verify=False` parameter is used to disable SSL verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Execution through API|T1106 - Execution through API]]

## Commands Used

- [[Fetch data using curl]]

## Tags

- [[Container Environment]]
- [[Kubernetes]]
- [[Simulating `kubectl` API Requests]]
