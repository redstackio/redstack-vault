---
id: aabb13f3-cf57-464d-83e1-5050ad9b59e2
name: AWS EKS Service Account Token Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.509841+00:00'
updated_at: '2023-04-10T20:20:21.815199+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
tags:
- '[[Cloud - AWS]]'
- '[[Getting the secret information from EKS]]'
- '[[Initial Access]]'
commands:
- '[[List Service Account Token]]'
---

# AWS EKS Service Account Token Theft

## Summary

This procedure involves stealing the Kubernetes Service Account Token from an Amazon Elastic Kubernetes Service (EKS) cluster. This token can be used to authenticate to the Kubernetes API server and gain access to the cluster. Attackers can use this technique to gain a foothold in the target enviro

## Description

# Description

This procedure involves stealing the Kubernetes Service Account Token from an Amazon Elastic Kubernetes Service (EKS) cluster. This token can be used to authenticate to the Kubernetes API server and gain access to the cluster. Attackers can use this technique to gain a foothold in the target environment and move laterally to other systems. To perform this attack, the attacker needs to have access to the AWS console or command line interface (CLI) and the appropriate permissions to list Kubernetes service account tokens.

 

## Requirements

1. Access to the AWS console or CLI.

1. Appropriate permissions to list Kubernetes service account tokens.

 

## Defense

1. Limit access to the AWS console and CLI to authorized personnel only.

1. Implement least privilege access controls to limit the permissions of users and roles in the environment.

1. Monitor the EKS cluster for unusual activity, such as the creation of new service accounts or tokens.

 

## Objectives

1. Steal the Kubernetes Service Account Token for an EKS cluster.

1. Gain access to the Kubernetes API server.

1. Move laterally to other systems in the target environment.

 

# Instructions

1. To list the Kubernetes service account token, run the following command:

kubectl exec <pod-name> -n <namespace> -- cat /var/run/secrets/kubernetes.io/serviceaccount/token

 

This command is used to retrieve the Kubernetes service account token which is required for authentication and authorization to access the Kubernetes API server. The token is stored in a file located at /var/run/secrets/kubernetes.io/serviceaccount/token inside the pod. The command can be run using kubectl exec with the pod name and namespace as arguments. The output of the command will be the contents of the token file.



**Command** ([[List Service Account Token]]):

```bash
https://website.com?rce.php?cmd=ls /var/run/secrets/kubernets.io/serviceaccount/token
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]

## Commands Used

- [[List Service Account Token]]

## Tags

- [[Cloud - AWS]]
- [[Getting the secret information from EKS]]
- [[Initial Access]]


