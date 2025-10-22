---
id: 344572c8-ee6e-4443-9bdc-526a0f3b6181
name: Kubernetes API Server Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.459294+00:00'
updated_at: '2023-04-10T20:34:06.178815+00:00'
tags:
- '[[API addresses that you should know]]'
- '[[Kubernetes]]'
- '[[Secure API Server]]'
commands:
- '[[Check Kubernetes API Health]]'
- '[[Get Kubernetes API Swagger]]'
- '[[Get Kubernetes API Version]]'
---

# Kubernetes API Server Enumeration

## Summary

The Kubernetes API server is a key component of Kubernetes and provides a RESTful API for interacting with the cluster. This procedure involves enumerating the API server's endpoints to gain a better understanding of the Kubernetes cluster. By discovering these endpoints, an attacker can identify p

## Description

# Description

The Kubernetes API server is a key component of Kubernetes and provides a RESTful API for interacting with the cluster. This procedure involves enumerating the API server's endpoints to gain a better understanding of the Kubernetes cluster. By discovering these endpoints, an attacker can identify potential attack vectors and misconfigurations in the cluster. This procedure can also be used by system administrators to audit their Kubernetes cluster and ensure that only authorized endpoints are exposed.

## Requirements

1. Access to the Kubernetes cluster API server.

1. Curl or similar tool to send HTTP requests.

## Defense

1. Ensure that the Kubernetes API server is properly secured and that only authorized endpoints are exposed.

1. Use RBAC to restrict access to the Kubernetes API server.

1. Monitor the Kubernetes API server logs for suspicious activity.

## Objectives

1. Identify potential attack vectors and misconfigurations in the Kubernetes cluster.

1. Audit the Kubernetes cluster to ensure that only authorized endpoints are exposed.

# Instructions

1. Replace <IP Address> with the IP address of the Kubernetes API server.

**Code**: [[curl -k https://<IP Address>:6443/swaggerapi
curl ]]

> The first command sends a GET request to the /swaggerapi endpoint to retrieve the OpenAPI specification for the Kubernetes API server. The second command sends a GET request to the /healthz endpoint to check the health of the Kubernetes API server. The third command sends a GET request to the /api/v1 endpoint to retrieve information about the Kubernetes API server's version, nodes, and namespaces.

**Command** ([[Get Kubernetes API Swagger]]):

```bash
curl -k https://<IP Address>:6443/swaggerapi
```

**Command** ([[Check Kubernetes API Health]]):

```bash
curl -k https://<IP Address>:6443/healthz
```

**Command** ([[Get Kubernetes API Version]]):

```bash
curl -k https://<IP Address>:6443/api/v1
```

## Commands Used

- [[Check Kubernetes API Health]]
- [[Get Kubernetes API Swagger]]
- [[Get Kubernetes API Version]]

## Tags

- [[API addresses that you should know]]
- [[Kubernetes]]
- [[Secure API Server]]
