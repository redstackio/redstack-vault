---
id: 0a77093c-5cb4-45c4-8f07-a94bd12865fa
name: Credentials In Files
type: sub-technique
mitre_id: T1552.001
mitre_url: null
created_at: '2023-04-06T00:31:26.497937+00:00'
updated_at: '2023-04-06T00:31:26.497937+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AWS API Gateway Stage Enumeration]]'
- '[[AWS CLI Configuration]]'
- '[[AWS IAM Access Key Enumeration]]'
- '[[AWS Secrets Manager - Describe Secret]]'
- '[[Credential Harvesting from DynamoDB]]'
- '[[Extracting Network Credentials using Powershell]]'
- '[[Gitrob Secret Harvesting]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Windows Privilege Escalation - Powershell History Looting]]'
---

# Credentials In Files

**MITRE ID**: T1552.001

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or servi

## Description

Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

It is possible to extract passwords from backups or saved virtual machines through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). (Citation: CG 2014) Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller. (Citation: SRD GPP)

In cloud and/or containerized environments, authenticated user and service account credentials are often stored in local configuration and credential files.(Citation: Unit 42 Hildegard Malware) They may also be found as parameters to deployment commands in container logs.(Citation: Unit 42 Unsecured Docker Daemons) In some cases, these files can be copied and reused on another machine or the contents can be read and then used to authenticate without needing to copy any files.(Citation: Specter Ops - Cloud Credential Storage)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 14 procedures using this sub-technique:

- [[AWS API Gateway Stage Enumeration]]
- [[AWS CLI Configuration]]
- [[AWS IAM Access Key Enumeration]]
- [[AWS Secrets Manager - Describe Secret]]
- [[Credential Harvesting from DynamoDB]]
- [[Extracting Network Credentials using Powershell]]
- [[Gitrob Secret Harvesting]]
- [[Twilio API Key Leakage]]
- [[Twilio API Key Leakage]]
- [[Twilio API Key Leakage]]
- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
- [[Windows Privilege Escalation - Powershell History Looting]]
