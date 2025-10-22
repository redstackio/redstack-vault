---
id: c7fe3bc4-5c6d-4128-ac01-9bf4e3113a3b
name: AWS EKS Node Group Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.887349+00:00'
updated_at: '2023-04-10T20:20:06.996359+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing all node groups in specified cluster]]'
commands:
- '[[List EKS Nodegroups]]'
---

# AWS EKS Node Group Enumeration

## Summary

The AWS Elastic Kubernetes Service (EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane. This procedure aims to list all node groups in a specified EKS cluster. Attackers can use this in

## Description

# Description

The AWS Elastic Kubernetes Service (EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane. This procedure aims to list all node groups in a specified EKS cluster. Attackers can use this information to understand the infrastructure and identify potential targets for further attacks. 

To list all node groups in an EKS cluster, the attacker can use the 'List EKS Nodegroups' command. This command sends a request to the AWS API to retrieve information about the node groups in the specified cluster.

This procedure can be useful for both red and blue teams. Red teams can use this information to identify potential targets for further attacks, while blue teams can use this information to monitor and secure their EKS clusters.

## Requirements

1. Valid AWS credentials with permissions to access the EKS cluster

1. Network access to the EKS cluster

## Defense

1. Ensure AWS credentials are properly secured and rotated regularly

1. Limit network access to the EKS cluster to only necessary IPs and ports

1. Monitor EKS clusters for suspicious activity, such as unexpected node group creation

## Objectives

1. List all node groups in a specified EKS cluster

1. Identify potential targets for further attacks

# Instructions

1. Use this command to list all the nodegroups in an Amazon EKS cluster.

The `aws eks list-nodegroups` command is used to retrieve a list of all the nodegroups in an Amazon EKS cluster. This command requires the `--cluster-name` argument to specify the name of the cluster. The output of this command is a JSON array of nodegroup names. This command can be useful for verifying that all the nodegroups in a cluster are running as expected.

**Command** ([[List EKS Nodegroups]]):

```bash
aws eks list-nodegroups --cluster-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List EKS Nodegroups]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing all node groups in specified cluster]]
