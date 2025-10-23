---
id: 29ef8da6-243d-4793-a178-b0430a719cda
name: AWS ECS Service Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.715435+00:00'
updated_at: '2023-04-10T20:20:18.385966+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific service]]'
commands:
- '[[Describe ECS Service]]'
---

# AWS ECS Service Enumeration

## Summary

AWS Elastic Container Service (ECS) is a highly scalable, high-performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of EC2 instances. The ECS Service Enumeration procedure involves listing information about a specifi

## Description

# Description

AWS Elastic Container Service (ECS) is a highly scalable, high-performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of EC2 instances. The ECS Service Enumeration procedure involves listing information about a specific service in order to gather intelligence about the service, such as its name, ARN, launch type, status, and task definition. This information can be used to identify potential vulnerabilities and misconfigurations in the service, as well as to gain a better understanding of the overall cloud environment.

From an offensive perspective, this technique can be used to identify potential targets for further exploitation or to gather information for a more targeted attack. From a defensive perspective, this procedure can be used to identify potential misconfigurations or vulnerabilities and to ensure that services are properly secured and monitored.

 

## Requirements

1. Valid AWS credentials with permissions to access ECS services

1. AWS CLI or SDK installed

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement least privilege access control to limit access to ECS services

1. Monitor for suspicious activity and unauthorized access to ECS services

 

## Objectives

1. Identify potential vulnerabilities and misconfigurations in the service

1. Gather intelligence about the service for further targeting

1. Ensure that services are properly secured and monitored

 

# Instructions

1. Use the aws ecs describe-services command to retrieve information about a specified ECS service.

 

This command requires the following arguments:
1. cluster: The name of the ECS cluster that the service is associated with.
2. services: The name of the service to describe.

This command returns a JSON object that contains information about the specified service, including its name, status, desired count, and running count. Additionally, it includes information about the tasks associated with the service, including their task definition, status, and health. This information can be useful for monitoring and troubleshooting purposes.



**Command** ([[Describe ECS Service]]):

```bash
aws ecs describe-services --cluster name --services name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe ECS Service]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing information about a specific service]]


