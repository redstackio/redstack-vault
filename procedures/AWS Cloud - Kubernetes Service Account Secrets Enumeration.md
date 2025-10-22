---
id: f171d1f9-9c37-4240-ae24-9b7201652c77
name: AWS Cloud - Kubernetes Service Account Secrets Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.484287+00:00'
updated_at: '2023-04-10T20:19:49.506455+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Initial Access]]'
commands:
- '[[List Files]]'
---

# AWS Cloud - Kubernetes Service Account Secrets Enumeration

## Summary

This procedure focuses on enumerating Kubernetes service account secrets in an AWS cloud environment. By listing these secrets, an attacker can obtain sensitive information such as tokens and certificates that can be used to authenticate to the Kubernetes API server and gain access to the cluster. 

## Description

# Description

This procedure focuses on enumerating Kubernetes service account secrets in an AWS cloud environment. By listing these secrets, an attacker can obtain sensitive information such as tokens and certificates that can be used to authenticate to the Kubernetes API server and gain access to the cluster. This can be achieved by using the 'List Kubernetes Service Account Secrets' command. This procedure can be used as an initial access method in a larger attack campaign.

## Requirements

1. Access to the AWS cloud environment

1. Authenticated access to the Kubernetes API server

## Defense

1. Ensure that access to the AWS cloud environment is properly secured with appropriate authentication and access controls

1. Implement network segmentation to limit access to the Kubernetes API server

1. Monitor for unusual activity such as unexpected Kubernetes API server authentication attempts

## Objectives

1. Enumerate Kubernetes service account secrets

1. Obtain sensitive information such as tokens and certificates

1. Use obtained credentials to authenticate to the Kubernetes API server and gain access to the cluster

# Instructions

1. To list the secrets of a Kubernetes service account, use the following command:

kubectl get secrets <service-account-name> -o json

This will return a JSON object containing all the secrets associated with the specified service account.

The 'kubectl get secrets' command is used to retrieve information about the secrets in a Kubernetes cluster. The '<service-account-name>' argument specifies the name of the service account whose secrets you want to list. The '-o json' flag is used to output the results in JSON format. This command can be useful for debugging and troubleshooting issues related to service account secrets.

**Command** ([[List Files]]):

```bash
https://website.com?rce.php?cmd=ls /var/run/secrets/kubernets.io/serviceaccount
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Files]]

## Tags

- [[Cloud - AWS]]
- [[Initial Access]]
