---
id: 60bf04ee-9c5f-4823-a621-2e0e3a40fd01
name: AWS IAM Permissions Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.504988+00:00'
updated_at: '2023-04-10T20:19:51.396157+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[AWS - Enumerate IAM permissions]]'
- '[[Cloud - AWS]]'
commands:
- '[[Describe Locations]]'
- '[[Describe Matchmaking Rule Sets]]'
- '[[Enumerate IAM Permissions]]'
- '[[Git Clone and Install Requirements]]'
- '[[List Builds]]'
- '[[List Queues]]'
- '[[List Stack Sets]]'
---

# AWS IAM Permissions Enumeration

## Summary

The AWS IAM Permissions Enumeration procedure is used to identify which permissions an AWS credential has in order to determine the level of access an attacker has to AWS resources. This procedure involves using the 'AWS Credential Permission Enumeration' command to gather information about the IAM

## Description

# Description

The AWS IAM Permissions Enumeration procedure is used to identify which permissions an AWS credential has in order to determine the level of access an attacker has to AWS resources. This procedure involves using the 'AWS Credential Permission Enumeration' command to gather information about the IAM permissions associated with a given credential. This information can be used to identify potential targets for further exploitation or to better understand the scope of an existing attack.

From a technical perspective, this procedure involves making API calls to the AWS IAM service to retrieve information about the permissions associated with a given credential. This information includes the policies and roles associated with the credential, as well as any explicit permissions granted to the credential. This procedure can be performed using a variety of tools and scripts, including the AWS CLI and various third-party tools.

From a business perspective, this procedure can be used to identify potential security risks within an AWS environment and to help organizations better understand their exposure to attacks targeting AWS resources. By identifying potential vulnerabilities, organizations can take steps to remediate them and reduce the overall risk of a successful attack.

 

## Requirements

1. Valid AWS credentials with IAM permissions

1. Access to the AWS IAM service

1. AWS CLI or other tools for making API calls

 

## Defense

1. Ensure that AWS credentials are properly secured and rotated on a regular basis

1. Implement least privilege access controls to limit the scope of IAM permissions

1. Monitor AWS IAM activity for suspicious behavior and unauthorized access attempts

 

## Objectives

1. Identify the permissions associated with an AWS credential

1. Determine the level of access an attacker has to AWS resources

1. Identify potential targets for further exploitation

 

# Instructions

1. To enumerate the permissions associated with an AWS credential set using Enumerate-IAM, follow these steps:
1. Clone the Enumerate-IAM repository from GitHub using the command `git clone git@github.com:andresriancho/enumerate-iam.git`
2. Install the required dependencies using the command `pip install -r requirements.txt`
3. Run the Enumerate-IAM script using the command `./enumerate-iam.py --access-key <ACCESS-KEY> --secret-key <SECRET-KEY>`. Replace `<ACCESS-KEY>` and `<SECRET-KEY>` with the appropriate values for your AWS credential set.
4. The script will output a list of the permissions associated with the specified AWS credential set.

 



**Code**: [[git clone git@github.com:andresriancho/enumerate-i]]



> The `enumerate-iam` command is a tool used to enumerate the permissions associated with an AWS credential set. This command requires the `access-key` and `secret-key` parameters to be provided in order to authenticate with the AWS API. Once authenticated, the command will query the AWS API for information about the permissions associated with the specified credential set. The output of the command will be a list of the permissions associated with the specified credential set.



**Command** ([[Git Clone and Install Requirements]]):

```bash
git clone git@github.com:andresriancho/enumerate-iam.git
pip install -r requirements.txt

```





**Command** ([[Enumerate IAM Permissions]]):

```bash
./enumerate-iam.py --access-key AKIA... --secret-key StF0q...
```





**Command** ([[List Builds]]):

```bash
gamelift.list_builds()
```





**Command** ([[List Stack Sets]]):

```bash
cloudformation.list_stack_sets()
```





**Command** ([[Describe Locations]]):

```bash
directconnect.describe_locations()
```





**Command** ([[Describe Matchmaking Rule Sets]]):

```bash
gamelift.describe_matchmaking_rule_sets()
```





**Command** ([[List Queues]]):

```bash
sqs.list_queues()
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Describe Locations]]
- [[Describe Matchmaking Rule Sets]]
- [[Enumerate IAM Permissions]]
- [[Git Clone and Install Requirements]]
- [[List Builds]]
- [[List Queues]]
- [[List Stack Sets]]

## Tags

- [[AWS - Enumerate IAM permissions]]
- [[Cloud - AWS]]


