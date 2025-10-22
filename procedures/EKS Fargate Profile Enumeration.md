---
id: 21842600-6b46-456a-b011-b77cae601795
name: EKS Fargate Profile Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.955932+00:00'
updated_at: '2023-04-10T20:20:24.315852+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[EKS]]'
- '[[Enumeration]]'
- '[[Listing information about a fargate profile in a cluster]]'
commands:
- '[[Describe Fargate Profiles]]'
---

# EKS Fargate Profile Enumeration

## Summary

The EKS Fargate Profile Enumeration procedure involves listing information about a fargate profile in an EKS cluster. This procedure can be used by an attacker to gather information about the target environment, such as the number of pods running, the pod execution role ARN, and the subnets used by

## Description

# Description

The EKS Fargate Profile Enumeration procedure involves listing information about a fargate profile in an EKS cluster. This procedure can be used by an attacker to gather information about the target environment, such as the number of pods running, the pod execution role ARN, and the subnets used by the fargate profile. This information can be used to plan and execute further attacks against the target environment.

Technical Description: The EKS Fargate Profile Enumeration procedure involves using the "Describe Fargate Profile" AWS CLI command to gather information about a fargate profile in an EKS cluster. The command returns information such as the name of the fargate profile, the ARN of the pod execution role, the number of pods running, and the subnets used by the fargate profile.

Business Value: This procedure can be used by an attacker to gather information about the target environment, which can be used to plan and execute further attacks against the target environment. By understanding the target environment, an attacker can identify weaknesses and vulnerabilities that can be exploited to gain access to sensitive data or systems.

## Requirements

1. Valid AWS credentials with permissions to execute the "Describe Fargate Profile" command

1. Access to an EKS cluster

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement network segmentation and access controls to limit access to the EKS cluster

1. Monitor for suspicious activity and unauthorized access to the EKS cluster and AWS resources

## Objectives

1. Gather information about a fargate profile in an EKS cluster

1. Identify weaknesses and vulnerabilities in the target environment

1. Plan and execute further attacks against the target environment

# Instructions

1. Use this command to describe the Fargate profile of an Amazon EKS cluster.

**Code**: [[aws eks describe-fargate-profiles --cluster-name n]]

> The `describe-fargate-profiles` command is used to retrieve information about the Fargate profile of an Amazon EKS cluster. This includes details such as the ARN of the Fargate profile, the name of the profile, and the selectors used to determine which pods should be scheduled on Fargate. 

This command requires the `--cluster-name` flag to specify the name of the cluster, and the `--fargate-profile-name` flag to specify the name of the Fargate profile. If successful, the command will output a JSON object containing the details of the Fargate profile.

**Command** ([[Describe Fargate Profiles]]):

```bash
aws eks describe-fargate-profiles --cluster-name name --fargate-profile-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Describe Fargate Profiles]]

## Tags

- [[Cloud - AWS]]
- [[EKS]]
- [[Enumeration]]
- [[Listing information about a fargate profile in a cluster]]
