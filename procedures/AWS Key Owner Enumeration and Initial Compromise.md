---
id: c787ad8a-31a8-4cbc-9c44-48f9c1dc85e6
name: AWS Key Owner Enumeration and Initial Compromise
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.403953+00:00'
updated_at: '2023-04-10T20:20:31.956911+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Enumerating the owner of the key and initial compromise]]'
commands:
- '[[Get AWS caller identity]]'
---

# AWS Key Owner Enumeration and Initial Compromise

## Summary

This procedure involves enumerating the owner of an AWS key and then using this information to gain initial access to the AWS account. The attacker first uses the 'Get AWS Account ID and User Identity' command to identify the account owner. They then use the 'Get Caller Identity with AWS STS' comma

## Description

# Description

This procedure involves enumerating the owner of an AWS key and then using this information to gain initial access to the AWS account. The attacker first uses the 'Get AWS Account ID and User Identity' command to identify the account owner. They then use the 'Get Caller Identity with AWS STS' command to determine if the key has the necessary permissions to access the AWS console. If so, the attacker can then use the 'AWS Console Login' command to gain access to the console and further compromise the account.

This procedure can be used by attackers to gain access to sensitive data stored within the AWS account. By gaining access to the console, an attacker can create new resources, modify existing ones, and exfiltrate data.

## Requirements

1. Valid AWS key

1. Network access to AWS API endpoints

1. AWS CLI or other tool capable of interacting with AWS API

## Defense

1. Implement strong access controls for AWS keys and accounts

1. Monitor AWS API logs for unusual activity

1. Enable multi-factor authentication for AWS accounts

## Objectives

1. Identify the owner of an AWS key

1. Gain initial access to an AWS account

1. Compromise the AWS account

# Instructions

1. To get the AWS account ID and user identity, run the following command:

**Code**: [[aws sts get-caller-identity]]

> This command retrieves information about the AWS account and user identity associated with the credentials used to call the AWS STS GetCallerIdentity API. The command returns the AWS account ID, user ID, and ARN (Amazon Resource Name) of the caller's principal. The ARN includes the user, role, or federated user name, depending on the type of credentials used to call the API. This information can be useful for troubleshooting access issues and verifying that you are using the correct AWS account and user identity.

2. To get the AWS account ID and the Amazon Resource Name (ARN) of the IAM user or role associated with the current credentials, use the AWS CLI command 'aws sts get-caller-identity'. This command returns a JSON object containing the caller identity information. To specify a named profile, add the '--profile' option followed by the name of the profile to the command.

The 'aws sts get-caller-identity' command is used to retrieve the AWS account ID and the Amazon Resource Name (ARN) of the IAM user or role associated with the current credentials. This command is useful to check the permissions of the current user or to confirm that the correct credentials are being used. The '--profile' option is used to specify a named profile to use with the command. If the named profile is not specified, the default profile will be used.

**Command** ([[Get AWS caller identity]]):

```bash
aws sts get-caller-identity --profile example_name
```

3. To log in to the AWS Management Console with the root account, follow these steps:
1. Open the following link in your web browser: https://signin.aws.amazon.com/console
2. Enter the email address associated with your AWS account and click on the 'Next' button.
3. Enter the password associated with your AWS account and click on the 'Sign In' button.
4. You will be redirected to the AWS Management Console dashboard, where you can manage your AWS resources.

The root account is the highest level of access in AWS and has full control over all AWS services and resources. It is recommended to use IAM users instead of the root account for day-to-day operations to ensure better security and control over access to AWS resources.

4. To login to the AWS console, visit the URL provided and enter your account credentials.

This command provides a link to the AWS Console login page where you can enter your account credentials to access the AWS Management Console. If the account is not the root account, you can use the IAM user credentials to login instead.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Get AWS caller identity]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Enumerating the owner of the key and initial compromise]]
