---
id: 8bf2a2d9-f06a-4b72-9674-072dcfb0a20f
name: AWS CLI Configuration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.917204+00:00'
updated_at: '2023-04-10T20:19:56.506917+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Bash History|T1552.003 - Bash History]]'
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[Cloud - AWS]]'
- '[[Configure AWS cli]]'
commands:
- '[[AWS Configuration]]'
- '[[Check if AWS Credentials File Exists]]'
- '[[Configure AWS Profile]]'
---

# AWS CLI Configuration

## Summary

AWS CLI Configuration is a process to set up the AWS Command Line Interface (CLI) on your local machine. The AWS CLI is a powerful tool that allows you to interact with various AWS services from the command line. It provides a unified interface to manage your AWS resources, and can be used to autom

## Description

# Description

AWS CLI Configuration is a process to set up the AWS Command Line Interface (CLI) on your local machine. The AWS CLI is a powerful tool that allows you to interact with various AWS services from the command line. It provides a unified interface to manage your AWS resources, and can be used to automate tasks and scripts. By configuring the AWS CLI, you can access your AWS resources securely and efficiently, without having to use the AWS Management Console.

Technical Explanation: AWS CLI Configuration involves setting up access keys and secret access keys, which are used to authenticate your requests to AWS services. These keys can be obtained through the AWS Management Console or by using the AWS CLI. Once you have obtained the keys, you can configure the AWS CLI by running the 'aws configure' command and providing the necessary information.

Business Value: AWS CLI Configuration provides a secure and efficient way to manage your AWS resources. It allows you to automate tasks and scripts, which can save time and reduce the risk of errors. By using the AWS CLI, you can also avoid the need to use the AWS Management Console, which can be cumbersome and time-consuming.

## Requirements

1. AWS account with appropriate permissions

1. AWS CLI installed on local machine

1. Access keys and secret access keys for authentication

## Defense

1. Use multi-factor authentication (MFA) to secure access keys

1. Rotate access keys regularly to reduce the risk of compromise

1. Use AWS Identity and Access Management (IAM) to control access to AWS resources

## Objectives

1. To configure the AWS CLI on your local machine

1. To obtain access keys and secret access keys for authentication

1. To access AWS resources securely and efficiently

# Instructions

1. This command is used to configure the AWS CLI (Command Line Interface) with your access and secret access keys, region, and output format.

The 'aws configure' command requires you to input your access key ID, secret access key, default region name, and default output format. These values are used to authenticate and authorize your access to the AWS services. The access key ID and secret access key are provided by AWS when you create an IAM user. The default region name is the region where you want to run your AWS services. The default output format specifies the format in which the AWS CLI should display the output of the commands. You can choose from 'json', 'text', or 'table' formats.

**Command** ([[AWS Configuration]]):

```bash
aws configure
```

2. To configure AWS with a specific profile, use the `aws configure` command followed by the `--profile` flag and the name of the profile you want to create. This will prompt you to enter your AWS Access Key ID, Secret Access Key, Default region name, and Default output format. Once you have entered this information, your profile will be created and you can use it to run AWS CLI commands.

The `aws configure` command is used to set up your AWS CLI configuration. By using the `--profile` flag, you can create multiple profiles with different credentials and settings. This is useful when you are working with multiple AWS accounts or need to switch between different AWS environments. The `Access Key ID` and `Secret Access Key` are used to authenticate your AWS account, while the `Default region name` and `Default output format` are used to set the default region and output format for your profile.

**Command** ([[Configure AWS Profile]]):

```bash
aws configure --profile example_name
```

3. To access AWS resources using the AWS Command Line Interface (CLI) or AWS SDKs, you need credentials. The AWS credentials file stores your access key ID and secret access key, which are used to sign requests to AWS. By default, the AWS CLI looks for credentials in the ~/.aws/credentials file.

**Code**: [[~/.aws/credentials]]

> The AWS credentials file is a plain text file that consists of multiple sections, where each section represents a set of credentials for a specific AWS account. Each section has two keys: aws_access_key_id and aws_secret_access_key, which contain the access key ID and secret access key for the corresponding AWS account. Optionally, you can also include a third key called aws_session_token, which contains a temporary session token if you are using temporary security credentials. You can create and manage your AWS access keys and security credentials in the AWS Management Console.

**Command** ([[Check if AWS Credentials File Exists]]):

```bash
ls ~/.aws/credentials
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Bash History|T1552.003 - Bash History]]
- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[Credentials in Registry|T1552.002 - Credentials in Registry]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[AWS Configuration]]
- [[Check if AWS Credentials File Exists]]
- [[Configure AWS Profile]]

## Tags

- [[Cloud - AWS]]
- [[Configure AWS cli]]
