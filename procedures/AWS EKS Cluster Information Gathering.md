---
id: 6db0fa7a-ac9b-454e-a2d8-697348551947
name: AWS EKS Cluster Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.863024+00:00'
updated_at: '2023-04-10T20:19:58.930036+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific cluster]]'
commands:
- '[[Describe EKS cluster]]'
---

# AWS EKS Cluster Information Gathering

## Summary

The AWS EKS Cluster Information Gathering procedure involves listing information about a specific EKS cluster. This can be useful for an attacker looking to gather information about the target's cloud infrastructure. The procedure involves using the 'EKS Cluster Description' command to retrieve inf

## Description

# Description

The AWS EKS Cluster Information Gathering procedure involves listing information about a specific EKS cluster. This can be useful for an attacker looking to gather information about the target's cloud infrastructure. The procedure involves using the 'EKS Cluster Description' command to retrieve information such as the cluster name, version, and endpoint. This information can provide insight into the target's cloud environment and help the attacker to plan their next steps. From a technical perspective, this procedure involves making an API call to the EKS service to retrieve the cluster description. The business value of this procedure is that it can help organizations to identify vulnerabilities in their cloud infrastructure and take steps to remediate them before they are exploited by attackers.

 

## Requirements

1. Valid AWS credentials with permissions to access the EKS service

1. Network connectivity to the EKS API endpoint

 

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement network segmentation to limit access to the EKS API endpoint

1. Regularly monitor EKS cluster activity for any suspicious behavior

 

## Objectives

1. Gather information about a specific EKS cluster

1. Identify vulnerabilities in the target's cloud infrastructure

 

# Instructions

1. To get a description of an Amazon EKS cluster, use the 'aws eks describe-cluster' command followed by the name of the cluster.
For example:

 

The 'aws eks describe-cluster' command is used to retrieve information about an Amazon EKS cluster. The 'name' argument specifies the name of the cluster for which you want to retrieve information. This command provides details such as the Kubernetes version, VPC configuration, and endpoint URL for the cluster. You can use this information to verify that the cluster is configured correctly and to troubleshoot any issues that you might encounter.



**Command** ([[Describe EKS cluster]]):

```bash
aws eks describe-cluster --name name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Describe EKS cluster]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing information about a specific cluster]]


