---
id: b26cb3ba-db40-40e7-98a8-46338e179cfa
name: AWS EKS Cluster Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.839142+00:00'
updated_at: '2023-04-10T20:19:58.273833+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing all EKS clusters]]'
commands:
- '[[List EKS clusters]]'
---

# AWS EKS Cluster Enumeration

## Summary

The AWS Elastic Kubernetes Service (EKS) is a fully managed Kubernetes service provided by AWS. EKS makes it easy to deploy, manage, and scale containerized applications using Kubernetes. This procedure focuses on listing all EKS clusters in the target AWS environment. This information can be usefu

## Description

# Description

The AWS Elastic Kubernetes Service (EKS) is a fully managed Kubernetes service provided by AWS. EKS makes it easy to deploy, manage, and scale containerized applications using Kubernetes. This procedure focuses on listing all EKS clusters in the target AWS environment. This information can be useful for an attacker to identify potential targets for further attacks. 

Technical Description: The procedure utilizes the AWS CLI command 'eks list-clusters' to list all EKS clusters in the target AWS environment. The command requires valid AWS credentials with permissions to list EKS clusters. 

Business Value: An attacker can use this procedure to identify potential targets for further attacks, such as attempting to gain access to the EKS cluster or the applications running on it.

 

## Requirements

1. Valid AWS credentials with permissions to list EKS clusters

1. Access to the AWS CLI

 

## Defense

1. Limit access to the AWS CLI and AWS credentials to authorized personnel only

1. Implement least privilege access to AWS resources, including EKS clusters

1. Monitor AWS API calls for suspicious activity

 

## Objectives

1. Identify all EKS clusters in the target AWS environment

1. Determine potential targets for further attacks

 

# Instructions

1. This command lists all the available Amazon Elastic Kubernetes Service (EKS) clusters in the specified AWS account.

 

Arguments:
None

This command requires no additional arguments. Simply running the command will return a list of all the available EKS clusters in the specified AWS account.

Example:

$ aws eks list-clusters
{
    "clusters": [
        "my-eks-cluster-1",
        "my-eks-cluster-2",
        "my-eks-cluster-3"
    ]
}

This command returns a JSON object containing an array of cluster names for all the available EKS clusters in the specified AWS account.



**Command** ([[List EKS clusters]]):

```bash
aws eks list-clusters
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List EKS clusters]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing all EKS clusters]]


