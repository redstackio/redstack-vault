---
id: 99e15c01-38a4-45d9-a3c0-38c99259b6dc
name: AWS ECS Task Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.749182+00:00'
updated_at: '2023-04-10T20:20:37.560442+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing tasks in specific cluster]]'
commands:
- '[[List Tasks in ECS Cluster]]'
---

# AWS ECS Task Enumeration

## Summary

AWS ECS Task Enumeration is used to identify running tasks in a specific cluster. An attacker can use this information to identify running services and to potentially identify vulnerabilities in those services. To perform this technique, the attacker must have access to the AWS CLI and valid AWS cr

## Description

# Description

AWS ECS Task Enumeration is used to identify running tasks in a specific cluster. An attacker can use this information to identify running services and to potentially identify vulnerabilities in those services. To perform this technique, the attacker must have access to the AWS CLI and valid AWS credentials. Once authenticated, the attacker can list tasks in a specific cluster using the 'aws ecs list-tasks' command. This technique can be used to identify potential targets for further exploitation.

## Requirements

1. Valid AWS credentials

1. Access to AWS CLI

## Defense

1. Ensure that AWS credentials are properly secured and rotated

1. Limit access to the AWS CLI to authorized personnel

1. Monitor AWS CloudTrail logs for suspicious activity

## Objectives

1. Identify running tasks in a specific cluster

1. Identify potential targets for further exploitation

# Instructions

1. Use this command to list all the tasks running in an Amazon ECS cluster.

The 'aws ecs list-tasks' command is used to list all the tasks running in an Amazon ECS cluster. In the command, replace 'name' with the name of the cluster you want to list the tasks for. This command returns a list of Amazon Resource Names (ARNs) for the tasks. You can use these ARNs to describe the tasks using the 'aws ecs describe-tasks' command.

**Command** ([[List Tasks in ECS Cluster]]):

```bash
aws ecs list-tasks --cluster name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[List Tasks in ECS Cluster]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing tasks in specific cluster]]
