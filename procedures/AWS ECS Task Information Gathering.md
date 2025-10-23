---
id: 33ec544c-b87c-48e2-b643-224f828687bf
name: AWS ECS Task Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.785680+00:00'
updated_at: '2023-04-10T20:20:46.758288+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing information about an specific task]]'
commands:
- '[[Describe ECS Tasks]]'
---

# AWS ECS Task Information Gathering

## Summary

The AWS ECS Task Information Gathering procedure allows an attacker to gather information about a specific task running on an ECS cluster. This information can be used to identify potential attack vectors and plan further actions. To execute this procedure, an attacker must have valid AWS API crede

## Description

# Description

The AWS ECS Task Information Gathering procedure allows an attacker to gather information about a specific task running on an ECS cluster. This information can be used to identify potential attack vectors and plan further actions. To execute this procedure, an attacker must have valid AWS API credentials and the necessary permissions to access the ECS service. Using the 'Describe ECS Tasks' command, the attacker can retrieve information such as the task's ARN, status, and other metadata.

 

## Requirements

1. Valid AWS API credentials

1. Permissions to access the ECS service

 

## Defense

1. Limit access to AWS API credentials

1. Implement least privilege access control for ECS permissions

1. Monitor for unusual activity related to ECS tasks

 

## Objectives

1. Identify potential attack vectors

1. Plan further actions

 

# Instructions

1. Use the 'aws ecs describe-tasks' command to get detailed information about one or more ECS tasks in a specified cluster.

 



**Code**: [[aws ecs describe-tasks --cluster name -tasks taskA]]



> This command requires the cluster name and task ARN(s) as arguments. The output will include information such as the task ARN, status, CPU and memory usage, and container details. Multiple task ARNs can be provided as arguments to get information about multiple tasks at once.



**Command** ([[Describe ECS Tasks]]):

```bash
aws ecs describe-tasks --cluster name -tasks taskArn
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe ECS Tasks]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing information about an specific task]]


