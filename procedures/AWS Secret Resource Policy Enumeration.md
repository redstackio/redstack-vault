---
id: 29165db5-f238-4366-9a52-38a3056b952f
name: AWS Secret Resource Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.128097+00:00'
updated_at: '2023-04-10T20:20:02.326393+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Getting policies attached to the specified secret]]'
commands:
- '[[Get Secrets Manager Resource Policy]]'
---

# AWS Secret Resource Policy Enumeration

## Summary

The AWS Secret Resource Policy Enumeration procedure involves retrieving policies attached to a specified secret in order to gain further insight into the access control mechanisms in place. This procedure can be used by an attacker to identify potential misconfigurations or weak access controls th

## Description

# Description

The AWS Secret Resource Policy Enumeration procedure involves retrieving policies attached to a specified secret in order to gain further insight into the access control mechanisms in place. This procedure can be used by an attacker to identify potential misconfigurations or weak access controls that can be exploited to gain access to sensitive data. To execute this procedure, the attacker uses the 'Get Secret Resource Policy' command to retrieve the policy attached to the secret.

The technical explanation of this procedure involves querying the AWS Secrets Manager API to retrieve the policy attached to a secret. The policy contains a set of permissions that define who can access the secret and what actions they can perform. By analyzing the policy, an attacker can identify potential vulnerabilities or misconfigurations that can be exploited to gain access to the secret.

The business value of this procedure is that it allows organizations to identify potential weaknesses in their access control mechanisms and take steps to address them before they can be exploited by attackers.

 

## Requirements

1. Valid AWS credentials with permissions to access the Secrets Manager API

 

## Defense

1. Ensure that secrets are properly secured and access is restricted to authorized personnel

1. Implement least privilege access controls to limit the scope of potential attacks

1. Regularly review and update access control policies to ensure they are effective and up-to-date

 

## Objectives

1. Retrieve policies attached to a specified secret

1. Identify potential misconfigurations or weak access controls

1. Gain insight into access control mechanisms in place

 

# Instructions

1. To get the resource policy for a secret, use the following command:

 

This command retrieves the resource-based policy attached to the specified secret. The resource-based policy is a JSON document that defines who can access the secret and what actions they can perform on it. The --secret-id parameter specifies the ID of the secret for which you want to retrieve the resource policy.



**Command** ([[Get Secrets Manager Resource Policy]]):

```bash
aws secretsmanager get-resource-policy --secret-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get Secrets Manager Resource Policy]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting policies attached to the specified secret]]


