---
id: e234dccc-617e-4a4a-be54-2cf1916c55bc
name: AWS EKS Node Group Information Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.911082+00:00'
updated_at: '2023-04-10T20:19:59.942257+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing specific information about a node group in a cluster]]'
commands:
- '[[Describe EKS Nodegroup]]'
---

# AWS EKS Node Group Information Enumeration

## Summary

The AWS Elastic Kubernetes Service (EKS) provides an easy way to deploy, manage, and scale containerized applications using Kubernetes on AWS. An attacker can use the 'Describe EKS Node Group' command to enumerate specific information about a node group in a cluster, such as the node group name, in

## Description

# Description

The AWS Elastic Kubernetes Service (EKS) provides an easy way to deploy, manage, and scale containerized applications using Kubernetes on AWS. An attacker can use the 'Describe EKS Node Group' command to enumerate specific information about a node group in a cluster, such as the node group name, instance types, and scaling configuration. This information can be used to identify potential targets for further attacks or to gain a better understanding of the target environment. 

Technical Explanation: The 'Describe EKS Node Group' command is part of the AWS CLI and can be used to retrieve information about a specific node group in an EKS cluster. The command requires valid AWS credentials with permissions to access the EKS service. 

Business Value: An attacker can use this procedure to gather information about the target's cloud infrastructure, which can be used to plan and execute further attacks. By understanding the target environment, the attacker can identify vulnerabilities and weaknesses that can be exploited to gain access to sensitive data or disrupt business operations.

 

## Requirements

1. Valid AWS credentials with permissions to access the EKS service

1. Access to the target's EKS cluster

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared between users

1. Use AWS IAM policies to restrict access to the EKS service and limit the permissions of users and roles

1. Monitor AWS CloudTrail logs for suspicious activity related to the EKS service

 

## Objectives

1. Identify specific information about a node group in an EKS cluster

1. Enumerate potential targets for further attacks

1. Gain a better understanding of the target environment

 

# Instructions

1. This command is used to describe an Amazon EKS node group in detail. It returns information about the node group, such as the node group name, cluster name, status, scaling configuration, and other details.

 

The 'cluster-name' argument specifies the name of the Amazon EKS cluster that the node group is associated with. The 'nodegroup-name' argument specifies the name of the node group to describe. This command can be useful for troubleshooting or getting more information about a particular node group in your cluster.



**Command** ([[Describe EKS Nodegroup]]):

```bash
aws eks describe-nodegroup --cluster-name name --nodegroup-name name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Describe EKS Nodegroup]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing specific information about a node group in a cluster]]


