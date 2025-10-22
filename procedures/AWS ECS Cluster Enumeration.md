---
id: aaf266b1-dca2-4370-af54-0f56e5757cd1
name: AWS ECS Cluster Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.640775+00:00'
updated_at: '2023-04-10T20:20:53.746934+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing all ECS clusters]]'
commands:
- '[[List ECS Clusters]]'
---

# AWS ECS Cluster Enumeration

## Summary

The AWS ECS Cluster Enumeration procedure involves listing all ECS clusters in an AWS environment. This procedure can be used by an attacker to gain a better understanding of the target environment and identify potential targets for further attacks. To list all ECS clusters, the attacker can use th

## Description

# Description

The AWS ECS Cluster Enumeration procedure involves listing all ECS clusters in an AWS environment. This procedure can be used by an attacker to gain a better understanding of the target environment and identify potential targets for further attacks. To list all ECS clusters, the attacker can use the 'List ECS Clusters' command. This command will return a list of all ECS clusters in the target AWS environment.

From a technical standpoint, this procedure involves making API calls to the AWS ECS service using valid AWS credentials. The 'List ECS Clusters' command uses the AWS CLI to make these API calls. Business value of this procedure is that it helps security teams to identify and remediate any security weaknesses in their AWS environment before attackers can exploit them.

## Requirements

1. Valid AWS credentials

1. Access to the AWS CLI

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Monitor for any unusual API calls to the AWS ECS service

1. Implement least privilege access controls to limit the scope of any potential attacks

## Objectives

1. Identify all ECS clusters in the target AWS environment

1. Gain a better understanding of the target environment

# Instructions

1. This command lists all the ECS clusters in your AWS account.

The `aws ecs list-clusters` command takes no arguments. It simply returns a list of all the ECS clusters in your account. This command can be useful when you want to quickly see all the clusters that you have created. You can then use the names of the clusters returned by this command in other ECS commands to perform operations on those clusters.

**Command** ([[List ECS Clusters]]):

```bash
aws ecs list-clusters
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List ECS Clusters]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing all ECS clusters]]
