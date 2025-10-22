---
id: 5f24cbcc-9f69-4ba5-ba42-d036c101c02a
name: Kubernetes RBAC Access Any Resource or Verb
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.229469+00:00'
updated_at: '2023-04-10T20:33:58.932756+00:00'
tags:
- '[[Access Any Resource or Verb]]'
- '[[Kubernetes]]'
- '[[RBAC Configuration]]'
commands:
- '[[Wildcard resource and verb access]]'
---

# Kubernetes RBAC Access Any Resource or Verb

## Summary

This procedure allows an attacker to gain access to any resource or verb in the Kubernetes cluster by modifying the Role-Based Access Control (RBAC) configuration. By doing so, the attacker can perform any action within the Kubernetes cluster, such as deploying new containers, modifying existing on

## Description

# Description

This procedure allows an attacker to gain access to any resource or verb in the Kubernetes cluster by modifying the Role-Based Access Control (RBAC) configuration. By doing so, the attacker can perform any action within the Kubernetes cluster, such as deploying new containers, modifying existing ones, or accessing sensitive data. This attack can be carried out by an attacker with valid credentials or by exploiting a vulnerability in the Kubernetes API server.

## Requirements

1. Valid credentials or a vulnerability in the Kubernetes API server

## Defense

1. Limit the privileges of service accounts and users to only what is necessary.

1. Monitor the Kubernetes API server logs for any suspicious activity.

1. Regularly review and update the RBAC configuration to ensure that only authorized users have access.

## Objectives

1. Gain access to any resource or verb in the Kubernetes cluster

# Instructions

1. To modify the RBAC configuration, run the following command:

**Code**: [[resources:
- '*'
verbs:
- '*']]

> This command modifies the RBAC configuration to allow access to any resource and verb in the Kubernetes cluster. The 'resources' field specifies the resources that the user or service account can access, while the 'verbs' field specifies the actions that the user or service account can perform on those resources. By setting the 'resources' field to '*', the user or service account can access any resource in the Kubernetes cluster. Similarly, by setting the 'verbs' field to '*', the user or service account can perform any action on those resources.

**Command** ([[Wildcard resource and verb access]]):

```bash
resources:
- '*'
verbs:
- '*'
```

## Commands Used

- [[Wildcard resource and verb access]]

## Tags

- [[Access Any Resource or Verb]]
- [[Kubernetes]]
- [[RBAC Configuration]]
