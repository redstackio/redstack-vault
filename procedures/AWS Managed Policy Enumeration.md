---
id: 8b0900b9-2e3d-4fe5-a1bb-31eecc78a7b0
name: AWS Managed Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.292361+00:00'
updated_at: '2023-04-10T20:20:14.046645+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[4. Enumerating Policies]]'
- '[[Cloud - AWS]]'
- '[[Retrieving information about the specified managed policy]]'
commands:
- '[[Get IAM Policy]]'
---

# AWS Managed Policy Enumeration

## Summary

AWS Managed Policy Enumeration is a technique used by attackers to identify and retrieve information about the specified managed policy in an AWS environment. This information can be used to identify potential attack paths and vulnerabilities within the environment. Attackers can use the 'Get IAM P

## Description

# Description

AWS Managed Policy Enumeration is a technique used by attackers to identify and retrieve information about the specified managed policy in an AWS environment. This information can be used to identify potential attack paths and vulnerabilities within the environment. Attackers can use the 'Get IAM Policy' command to retrieve information about the specified managed policy, including the policy name, policy version, and policy document. By analyzing this information, attackers can gain insight into the permissions granted by the policy, and potentially identify weaknesses or misconfigurations that can be exploited to gain unauthorized access to AWS resources.

From a technical perspective, this technique involves using the 'Get IAM Policy' command to retrieve information about the specified managed policy. This command requires valid AWS credentials with the necessary permissions to access the policy.

From a business perspective, this technique can be used by attackers to gain unauthorized access to sensitive data or resources within an AWS environment. By identifying vulnerabilities and weaknesses in the environment, attackers can potentially steal data, disrupt business operations, or cause other types of harm.

 

## Requirements

1. Valid AWS credentials with the necessary permissions to access the policy.

 

## Defense

1. Ensure that AWS credentials are properly secured and not exposed to unauthorized users.

1. Implement least privilege access policies to limit the potential impact of an attack.

1. Regularly review and audit AWS policies to identify and remediate vulnerabilities and misconfigurations.

 

## Objectives

1. Identify and retrieve information about the specified managed policy in an AWS environment.

1. Identify potential attack paths and vulnerabilities within the environment.

1. Gain unauthorized access to AWS resources.

 

# Instructions

1. To retrieve an IAM policy, use the `aws iam get-policy` command followed by the ARN of the policy you want to fetch.

 

This command allows you to retrieve the details of a specific IAM policy. The `--policy-arn` option specifies the ARN of the policy you want to retrieve. The ARN uniquely identifies the policy and can be found in the AWS Management Console or by using the `aws iam list-policies` command. Once you have the ARN, simply replace `policy-arn` in the command with the actual ARN of the policy you want to retrieve. The output of this command will include the policy document, which contains the permissions defined in the policy.



**Command** ([[Get IAM Policy]]):

```bash
aws iam get-policy --policy-arn policy-arn
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get IAM Policy]]

## Tags

- [[4. Enumerating Policies]]
- [[Cloud - AWS]]
- [[Retrieving information about the specified managed policy]]


