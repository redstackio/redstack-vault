---
id: 054791c3-e96b-43b0-8741-dce63f2bd765
name: AWS EKS Fargate Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.934109+00:00'
updated_at: '2023-04-10T20:20:42.392187+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing Fargate in specified cluster]]'
commands:
- '[[List Fargate Profiles]]'
---

# AWS EKS Fargate Enumeration

## Summary

AWS Elastic Kubernetes Service (EKS) Fargate is a serverless compute engine for containers that works with Amazon EKS. This procedure allows an attacker to enumerate all Fargate profiles within a specified EKS cluster. From here, an attacker can identify potential targets for further exploitation, 

## Description

# Description

AWS Elastic Kubernetes Service (EKS) Fargate is a serverless compute engine for containers that works with Amazon EKS. This procedure allows an attacker to enumerate all Fargate profiles within a specified EKS cluster. From here, an attacker can identify potential targets for further exploitation, such as vulnerable container images or misconfigured permissions.

To list Fargate profiles in an EKS cluster, the attacker can use the 'List Fargate Profiles in EKS Cluster' command.

 

## Requirements

1. Valid AWS credentials with permissions to list Fargate profiles in the specified EKS cluster

 

## Defense

1. Restrict AWS credentials to only the necessary permissions for the user or role

1. Implement network segmentation to limit access to the EKS cluster

1. Monitor AWS CloudTrail logs for any unauthorized attempts to list Fargate profiles

 

## Objectives

1. Enumerate all Fargate profiles in a specified EKS cluster

1. Identify potential targets for further exploitation

 

# Instructions

1. To list all Fargate profiles in a specific EKS cluster, use the following AWS CLI command:

 

This command will list all the Fargate profiles associated with the specified EKS cluster. The `--cluster-name` option is used to specify the name of the EKS cluster. This command does not require any arguments.



**Command** ([[List Fargate Profiles]]):

```bash
aws eks list-fargate-profiles --cluster-name cluster-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Fargate Profiles]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing Fargate in specified cluster]]


