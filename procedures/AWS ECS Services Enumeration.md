---
id: 558befc5-1f78-479a-a4c2-fd8655b6e5ee
name: AWS ECS Services Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.689812+00:00'
updated_at: '2023-04-10T20:20:48.132689+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing all services in specified cluster]]'
commands:
- '[[List ECS Services]]'
---

# AWS ECS Services Enumeration

## Summary

AWS Elastic Container Service (ECS) is a highly scalable, high-performance container orchestration service. This procedure aims to enumerate all services in a specified cluster. This can be useful for an attacker to identify potential targets for further exploitation or to gain a better understandi

## Description

# Description

AWS Elastic Container Service (ECS) is a highly scalable, high-performance container orchestration service. This procedure aims to enumerate all services in a specified cluster. This can be useful for an attacker to identify potential targets for further exploitation or to gain a better understanding of the target environment. From a defensive perspective, this procedure can be used to monitor for unauthorized access or activity in the ECS environment. 

Technical: The procedure utilizes the AWS ECS ListServices API call to enumerate all services in a specified cluster. The output includes the ARN of each service, which can be used for further enumeration or exploitation. 

Business Value: By identifying all services in an ECS cluster, an attacker can gain a better understanding of the target environment and potentially identify critical services that could be targeted for disruption or exfiltration. From a defensive perspective, this procedure can be used to monitor for unauthorized access or activity in the ECS environment.

## Requirements

1. Valid AWS credentials with permissions to access the ECS ListServices API call

1. Access to the AWS ECS environment

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users or processes

1. Implement network segmentation to limit access to the ECS environment

1. Monitor for unauthorized access or activity in the ECS environment

## Objectives

1. Enumerate all services in a specified AWS ECS cluster

1. Identify potential targets for further exploitation

1. Monitor for unauthorized access or activity in the ECS environment

# Instructions

1. Use this command to list all the services in an ECS cluster.

The 'aws ecs list-services' command is used to list all the services in an ECS cluster. The '--cluster' option is used to specify the name of the cluster for which you want to list the services. The output of this command is a list of ARNs that represent the services in the specified cluster.

**Command** ([[List ECS Services]]):

```bash
aws ecs list-services --cluster name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List ECS Services]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing all services in specified cluster]]
