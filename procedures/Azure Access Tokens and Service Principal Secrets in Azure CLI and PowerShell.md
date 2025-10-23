---
id: f48058dc-ed22-45ba-9a02-f0d3e7605d79
name: Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell
type: procedure
verified: true
submitted: true
created_at: '2023-05-24T20:12:26.913841+00:00'
updated_at: '2023-05-24T20:14:07.909212+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
platforms:
- Cloud
tags:
- '[[Access Tokens]]'
- '[[Cloud - Azure]]'
- '[[Plain Text Credentials]]'
---

# Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell

**Status**: ✓ Verified

## Summary

Azure CLI and Azure PowerShell are prominent tools for managing Azure  resources. They conveniently store access tokens and service principal  secrets, facilitating interaction with Azure services without constant  authentication prompts. However, these credentials are stored in clear  text, posing

## Description

# Description

Azure CLI and Azure PowerShell are prominent tools for managing Azure  resources. They conveniently store access tokens and service principal  secrets, facilitating interaction with Azure services without constant  authentication prompts. However, these credentials are stored in clear  text, posing a potential security risk. This procedure focuses on the  safe handling and protection of these tokens to prevent unauthorized  access.



## Requirements

- A local or remote machine with Azure CLI or Azure PowerShell installed

- Active Azure subscriptions that are being accessed via the CLI or PowerShell

- Permissions to access the respective directories where tokens are stored

## Defense

- Ensure Azure CLI and PowerShell are only installed on secure, trusted systems

- Monitor for abnormal activity in system logs or unexpected access to the Azure resources

- Regularly rotate access tokens and secrets and avoid persistent login sessions wherever possible

## Objectives

- Safeguard access tokens and ServicePrincipalSecrets to avoid unauthorized access

- Maintain secure interaction with Azure resources for long running processes or frequent Azure management tasks



# Instructions



1. Azure CLI can store secrets in plain text in the following files:





**Code**: [[# Azure CLI stores access tokens in clear text in ]]





2. (Optional) Azure Powershell can store secrets in plain text:





**Code**: [[# Access tokens in clear text
c:\Users\<username>\]]



> Users can save tokens using the Save-AzContext command.



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Tags

- [[Access Tokens]]
- [[Cloud - Azure]]
- [[Plain Text Credentials]]


