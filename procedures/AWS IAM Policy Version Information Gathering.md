---
id: de07cfab-8454-4c59-bc4b-2b14c3d11d5e
name: AWS IAM Policy Version Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.486198+00:00'
updated_at: '2023-04-10T20:20:07.669531+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Getting information about a specific policy version]]'
- '[[Privilege Escalation]]'
commands:
- '[[Get IAM policy version]]'
- '[[Retrieve EC2 Instance ID]]'
---

# AWS IAM Policy Version Information Gathering

## Summary

The AWS IAM Policy Version Information Gathering procedure is used to obtain information about a specific version of an IAM policy. This procedure can be used to identify the permissions and privileges associated with a particular IAM policy version. This information can be used to identify potenti

## Description

# Description

The AWS IAM Policy Version Information Gathering procedure is used to obtain information about a specific version of an IAM policy. This procedure can be used to identify the permissions and privileges associated with a particular IAM policy version. This information can be used to identify potential privilege escalation paths or other exploitation opportunities. Technical details of this procedure include the use of the 'Get IAM Policy Version' command to retrieve information about a specific IAM policy version and the 'Retrieve EC2 Instance ID' command to obtain the instance ID of an EC2 instance.

## Requirements

1. Valid AWS credentials with appropriate permissions

1. Access to the AWS console or AWS CLI

1. Knowledge of the IAM policy version to target

## Defense

1. Limit permissions for IAM users and roles to only what is necessary

1. Enable multi-factor authentication (MFA) for all IAM users

1. Regularly review and audit IAM policies for unnecessary permissions

## Objectives

1. Identify potential privilege escalation paths

1. Gather information about a specific IAM policy version

# Instructions

1. To get a specific version of an IAM policy, use the `aws iam get-policy-version` command.

**Code**: [[aws iam get-policy-version --policy-arn ARN --vers]]

> This command retrieves information about the specified version of the specified IAM policy. The `--policy-arn` option specifies the Amazon Resource Name (ARN) of the policy, and the `--version-id` option specifies the version number of the policy version to retrieve. If successful, the command returns a JSON object containing information about the policy version, including the policy document, policy version ID, and the date and time the version was created.

**Command** ([[Get IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn ARN --version-id ID
```

2. Use the above command to retrieve the ID of the EC2 instance you want to attach a role to.

This command uses the curl utility to retrieve the instance ID of the EC2 instance. The instance ID is required to attach a role to the instance. The curl utility is used to make a GET request to the metadata endpoint of the EC2 instance, which returns the instance ID. Once you have the instance ID, you can use it to attach a role to the instance using the AWS CLI or API.

**Command** ([[Retrieve EC2 Instance ID]]):

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get IAM policy version]]
- [[Retrieve EC2 Instance ID]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Getting information about a specific policy version]]
- [[Privilege Escalation]]
