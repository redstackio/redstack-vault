---
id: dbc869b8-26b2-4e3d-9ca3-56887c6f3e7c
name: AWS ECS Cluster Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.665879+00:00'
updated_at: '2023-04-10T20:21:03.407922+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECS]]'
- '[[Enumeration]]'
- '[[Listing information about an specific cluster]]'
commands:
- '[[Describe ECS Cluster]]'
---

# AWS ECS Cluster Information Gathering

## Summary

The AWS ECS Cluster Information Gathering procedure aims to obtain information about a specific ECS cluster in order to identify potential attack vectors. This procedure can be used by an attacker to identify the number of instances running in a cluster, the CPU and memory usage, and the status of 

## Description

# Description

The AWS ECS Cluster Information Gathering procedure aims to obtain information about a specific ECS cluster in order to identify potential attack vectors. This procedure can be used by an attacker to identify the number of instances running in a cluster, the CPU and memory usage, and the status of each service running within the cluster. This information can be used to identify vulnerabilities in the cluster and plan further attacks. From a technical perspective, this procedure involves using the 'ECS Cluster Description' command to retrieve information about the cluster. From a business perspective, this procedure can help organizations identify potential security weaknesses in their AWS infrastructure and take appropriate measures to mitigate them.

## Requirements

1. Valid AWS credentials with permissions to access the target ECS cluster

1. Network access to the target ECS cluster

1. AWS CLI or SDK installed on the attacker's system

## Defense

1. Ensure that AWS credentials are properly secured and not shared with unauthorized individuals

1. Implement network segmentation to limit access to the ECS cluster

1. Regularly monitor the ECS cluster for suspicious activity

## Objectives

1. Retrieve information about a specific AWS ECS cluster

1. Identify potential attack vectors and vulnerabilities in the cluster

# Instructions

1. Use the 'aws ecs describe-clusters' command to get information about an ECS cluster.

This command requires the name of the cluster as an argument. It will return details about the cluster, including its ARN, status, and the number and status of its container instances. This command can be useful for troubleshooting and monitoring the health of your ECS clusters.

**Command** ([[Describe ECS Cluster]]):

```bash
aws ecs describe-clusters --cluster name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe ECS Cluster]]

## Tags

- [[Cloud - AWS]]
- [[ECS]]
- [[Enumeration]]
- [[Listing information about an specific cluster]]
