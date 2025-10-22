---
id: 159e92f8-66a0-494b-b8ab-fa5b65344fa5
name: AWS CLI Profile Configuration for Persistence and Backdooring
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.654877+00:00'
updated_at: '2023-04-10T20:20:32.287060+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Configuring AWS cli for the new user]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[AWS Configure]]'
---

# AWS CLI Profile Configuration for Persistence and Backdooring

## Summary

AWS CLI Profile Configuration for Persistence and Backdooring is a technique used by attackers to gain persistent access to an AWS environment by configuring AWS CLI profiles for a new user. This technique is used to maintain access to the compromised AWS environment even if the initial access poin

## Description

# Description

AWS CLI Profile Configuration for Persistence and Backdooring is a technique used by attackers to gain persistent access to an AWS environment by configuring AWS CLI profiles for a new user. This technique is used to maintain access to the compromised AWS environment even if the initial access point is discovered and closed. The attacker can use this technique to create or modify system processes, modify file and directory permissions, or create new users with elevated privileges, depending on the permissions of the compromised user.

Technical Explanation: The attacker can use AWS CLI to create a new user and configure a new profile for that user. The attacker can then use this profile to perform various actions on the compromised AWS environment. The attacker can modify file and directory permissions, create or modify system processes, or create new users with elevated privileges. Once the attacker has access to the AWS environment, they can maintain access by creating a backdoor or using other persistence techniques.

Business Value: This technique can be used by attackers to maintain access to the compromised AWS environment even if the initial access point is discovered and closed. This can result in data theft, data destruction, or other malicious activities.

## Requirements

1. Access to the AWS environment

1. AWS CLI installed on the attacker's machine

1. Credentials for a new user with sufficient permissions

## Defense

1. Monitor AWS CLI configuration changes and user activity

1. Limit the permissions of the compromised user to prevent the attacker from performing malicious activities

1. Implement multi-factor authentication for AWS CLI access

## Objectives

1. Gain persistent access to the compromised AWS environment

1. Create or modify system processes

1. Modify file and directory permissions

1. Create new users with elevated privileges

# Instructions

1. Use this command to configure AWS CLI with a named profile. This is useful when you have multiple AWS accounts and want to switch between them easily.

The `aws configure` command is used to configure the AWS CLI on your local machine. The `--profile` option allows you to specify a named profile for the configuration. Once you run this command, you will be prompted to enter your AWS Access Key ID, AWS Secret Access Key, default region name, and output format. These values will be stored in a configuration file under your home directory. You can then use the `--profile` option with other AWS CLI commands to specify which profile to use for the command. For example, `aws s3 ls --profile example_profile` would list the contents of an S3 bucket using the `example_profile` profile.

**Command** ([[AWS Configure]]):

```bash
aws configure --profile example_profile
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]

## Commands Used

- [[AWS Configure]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Configuring AWS cli for the new user]]
- [[Persistence & Backdooring]]
