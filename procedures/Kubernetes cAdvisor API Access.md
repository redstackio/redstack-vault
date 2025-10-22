---
id: 39065df7-d668-4046-a4ad-02fb9ef0977b
name: Kubernetes cAdvisor API Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.432438+00:00'
updated_at: '2023-04-10T20:34:05.832062+00:00'
tags:
- '[[API addresses that you should know]]'
- '[[cAdvisor]]'
- '[[Kubernetes]]'
commands:
- '[[Curl Request to IP Address]]'
---

# Kubernetes cAdvisor API Access

## Summary

Kubernetes cAdvisor API provides an interface to access and view container resource usage data. This procedure aims to access the cAdvisor API address to gain visibility into the Kubernetes cluster's resource usage. By accessing this API, an attacker can identify valuable targets for further exploi

## Description

# Description

Kubernetes cAdvisor API provides an interface to access and view container resource usage data. This procedure aims to access the cAdvisor API address to gain visibility into the Kubernetes cluster's resource usage. By accessing this API, an attacker can identify valuable targets for further exploitation.

## Requirements

1. Access to the Kubernetes cluster

1. Access to the cAdvisor API address

## Defense

1. Restrict access to the Kubernetes cluster and cAdvisor API address.
Enable SSL certificate validation.
Monitor network traffic for any suspicious activity.

## Objectives

1. Gain visibility into the Kubernetes cluster's resource usage

# Instructions

1. Execute the following command in a terminal to access the cAdvisor API address. Replace <IP Address> with the IP address of the Kubernetes node where the target container is running.

**Code**: [[curl -k https://<IP Address>:4194]]

> -k: Allow connections to SSL sites without certificates.
https://<IP Address>:4194: The cAdvisor API endpoint URL.

**Command** ([[Curl Request to IP Address]]):

```bash
curl -k https://<IP Address>:4194
```

## Commands Used

- [[Curl Request to IP Address]]

## Tags

- [[API addresses that you should know]]
- [[cAdvisor]]
- [[Kubernetes]]
