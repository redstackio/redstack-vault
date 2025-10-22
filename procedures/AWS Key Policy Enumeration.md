---
id: cbec736a-0a71-4e33-9b40-cb0aca2b4193
name: AWS Key Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.190393+00:00'
updated_at: '2023-04-10T20:20:15.443853+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing policies attached to a specific key]]'
commands:
- '[[List Key Policies for AWS KMS Key]]'
---

# AWS Key Policy Enumeration

## Summary

The AWS Key Policy Enumeration procedure involves listing policies attached to a specific key in order to discover the access control policies assigned to the key. This can be used to identify misconfigured policies or to identify keys that have overly permissive policies assigned to them. This pro

## Description

# Description

The AWS Key Policy Enumeration procedure involves listing policies attached to a specific key in order to discover the access control policies assigned to the key. This can be used to identify misconfigured policies or to identify keys that have overly permissive policies assigned to them. This procedure can be used by an attacker to gain information about the target's AWS environment and to identify potential attack vectors. On the defensive side, this procedure can be used by a security team to identify misconfigured policies and to remediate them before they can be exploited by an attacker.

To perform this procedure, the attacker will need to have valid AWS credentials and access to the AWS environment. The attacker will also need to have the appropriate permissions to list the policies attached to the key.

## Requirements

1. Valid AWS credentials

1. Access to the target's AWS environment

1. Appropriate permissions to list policies attached to the key

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement least privilege policies to limit the permissions of AWS users and roles

1. Regularly review and audit AWS policies to identify and remediate misconfigurations

## Objectives

1. Identify misconfigured policies

1. Identify keys with overly permissive policies

1. Gather information about the target's AWS environment

# Instructions

1. Use this command to list the key policies attached to a KMS key.

The 'aws kms list-key-policies' command is used to list the policies that are attached to a KMS key. This command requires the 'key-id' argument to specify the key for which you want to list the policies. The output of the command will be a JSON array containing the names of the policies attached to the key. You can use the policy names to view the details of the policy using the 'aws kms get-key-policy' command. This command can be useful when you need to review the policies attached to a key or when troubleshooting issues with access to a key.

**Command** ([[List Key Policies for AWS KMS Key]]):

```bash
aws kms list-key-policies --key-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Key Policies for AWS KMS Key]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing policies attached to a specific key]]
