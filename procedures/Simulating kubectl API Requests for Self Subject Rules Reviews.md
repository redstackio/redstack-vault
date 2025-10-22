---
id: 0f6bad0e-061f-4cdb-9264-89444890113f
name: Simulating kubectl API Requests for Self Subject Rules Reviews
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.123079+00:00'
updated_at: '2023-04-10T20:33:59.266404+00:00'
tags:
- '[[Container Environment]]'
- '[[Kubernetes]]'
- '[[Simulating `kubectl` API Requests]]'
commands:
- '[[Check Authorization]]'
---

# Simulating kubectl API Requests for Self Subject Rules Reviews

## Summary

This procedure involves simulating `kubectl` API requests to perform a Self Subject Rules Review. This is useful for an attacker to understand the permissions and access levels of a Kubernetes cluster. By simulating this request, an attacker can see what actions a user with a specific Service Accou

## Description

# Description

This procedure involves simulating `kubectl` API requests to perform a Self Subject Rules Review. This is useful for an attacker to understand the permissions and access levels of a Kubernetes cluster. By simulating this request, an attacker can see what actions a user with a specific Service Account can take within the Kubernetes environment. This procedure can be used to identify potential privilege escalation opportunities or to gain information for lateral movement within the environment.

To perform a Self Subject Rules Review, an attacker can send a POST request to the `/apis/authorization.k8s.io/v1/selfsubjectrulesreviews` endpoint with the Service Account token in the Authorization header. The response will contain a list of all the rules and permissions that the Service Account has within the Kubernetes environment.

## Requirements

1. Valid Service Account token

## Defense

1. Ensure that Service Accounts have the least privilege access required to perform their intended function within the Kubernetes environment

1. Regularly review and rotate Service Account tokens to limit the potential impact of compromised tokens

1. Monitor for anomalous activity within the Kubernetes environment, such as unusual API requests or unauthorized Service Account usage

## Objectives

1. Identify potential privilege escalation opportunities within the Kubernetes environment

1. Gain information for lateral movement within the environment

# Instructions

1. 

**Code**: [[# NOTE: only the Authorization and Content-Type he]]

> 

**Command** ([[Check Authorization]]):

```bash
$ kubectl -v9 auth can-i --list
```

## Commands Used

- [[Check Authorization]]

## Tags

- [[Container Environment]]
- [[Kubernetes]]
- [[Simulating `kubectl` API Requests]]
