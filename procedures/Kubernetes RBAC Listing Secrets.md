---
id: 94a01250-9615-4407-b201-44cb2017500b
name: Kubernetes RBAC Listing Secrets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.204271+00:00'
updated_at: '2023-04-10T20:34:00.302330+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Kubernetes]]'
- '[[Listing Secrets]]'
- '[[RBAC Configuration]]'
commands:
- '[[Retrieve Secrets]]'
---

# Kubernetes RBAC Listing Secrets

## Summary

This procedure outlines how an attacker can list secrets in a Kubernetes cluster using the RBAC configuration. An attacker who has access to list secrets in the cluster can use the provided curl commands to get all secrets in the "kube-system" namespace. This procedure can be used to gather sensiti

## Description

# Description

This procedure outlines how an attacker can list secrets in a Kubernetes cluster using the RBAC configuration. An attacker who has access to list secrets in the cluster can use the provided curl commands to get all secrets in the "kube-system" namespace. This procedure can be used to gather sensitive information such as API keys, passwords, and other secrets.

## Requirements

1. Valid JWT token

1. Access to Kubernetes master IP and port

## Defense

1. Ensure RBAC is properly configured to limit access to secrets

1. Monitor Kubernetes API server logs for suspicious activities

1. Implement network segmentation to limit access to Kubernetes API server

## Objectives

1. List all secrets in the "kube-system" namespace

# Instructions

1. Replace <jwt_token>, <master_ip>, and <port> with the valid values.

**Code**: [[curl -v -H "Authorization: Bearer <jwt_token>" htt]]

> This command sends a GET request to the Kubernetes API server to list all secrets in the "kube-system" namespace. The "Authorization" header is used to pass the valid JWT token for authentication.

**Command** ([[Retrieve Secrets]]):

```bash
curl -v -H "Authorization: Bearer <jwt_token>" https://<master_ip>:<port>/api/v1/namespaces/kube-system/secrets/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Retrieve Secrets]]

## Tags

- [[Kubernetes]]
- [[Listing Secrets]]
- [[RBAC Configuration]]
