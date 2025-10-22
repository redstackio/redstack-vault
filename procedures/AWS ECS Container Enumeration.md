---
id: 9eef2f06-db48-4b56-aa42-579816eca49f
name: AWS ECS Container Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.812949+00:00'
updated_at: '2023-04-10T20:20:10.090352+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing all containers in specified cluster]]'
commands:
- '[[List Container Instances in ECS Cluster]]'
---

# AWS ECS Container Enumeration

## Summary

The AWS ECS Container Enumeration procedure involves listing all containers in a specified cluster. This procedure can be used by an attacker to gain a better understanding of the target environment and identify potential targets for further exploitation. To perform this procedure, the attacker mus

## Description

# Description

The AWS ECS Container Enumeration procedure involves listing all containers in a specified cluster. This procedure can be used by an attacker to gain a better understanding of the target environment and identify potential targets for further exploitation. To perform this procedure, the attacker must have valid AWS credentials and access to the target cluster. The attacker can use the 'List ECS Container Instances' command to retrieve a list of all containers in the specified cluster.

## Requirements

1. Valid AWS credentials

1. Access to the target cluster

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement proper authentication and access controls to limit access to sensitive resources

1. Monitor for unusual or suspicious activity in the AWS environment

## Objectives

1. Identify potential targets for further exploitation

1. Gain a better understanding of the target environment

# Instructions

1. To list all the container instances in an ECS cluster, run the following command in the AWS CLI:

**Code**: [[aws ecs list-container-instances --cluster name]]

> This command lists all the container instances in the specified ECS cluster. The cluster name must be provided as an argument. This command can be useful to get an overview of the container instances in the cluster, and to check if any instances are not running or are experiencing issues.

**Command** ([[List Container Instances in ECS Cluster]]):

```bash
aws ecs list-container-instances --cluster name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[List Container Instances in ECS Cluster]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing all containers in specified cluster]]
