---
id: 252e554d-270a-4a3f-b678-0601ee26f288
name: Azure Resource Management and Privilege Checking with PowerShell
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.193985+00:00'
updated_at: '2023-05-24T08:08:13.420439+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Application Access Token|T1527 - Application Access Token]]'
tags:
- '[[Azure API via Powershell]]'
- '[[Cloud - Azure]]'
- '[[Token from Managed Identity]]'
---

# Azure Resource Management and Privilege Checking with PowerShell

**Status**: ✓ Verified

## Summary

This procedure focuses on utilizing PowerShell to interact with Azure  resources and check for specific privileges using the Invoke-RestMethod  cmdlet. It provides instructions on how to authenticate using a token,  retrieve a list of subscriptions, and access resource information.  Additionally, i

## Description

# Description

This procedure focuses on utilizing PowerShell to interact with Azure  resources and check for specific privileges using the Invoke-RestMethod  cmdlet. It provides instructions on how to authenticate using a token,  retrieve a list of subscriptions, and access resource information.  Additionally, it demonstrates how to check for runCommand privileges  within a resource group. By following these steps, you can effectively  manage Azure resources and verify necessary privileges.

## Requirements

To successfully execute these commands, ensure the following prerequisites:

- PowerShell is installed and accessible.

- Azure PowerShell modules are installed and up-to-date.

- Valid access token is available.

- Proper permissions are granted to access Azure resources.

## Defense

To enhance security and protect your Azure resources, consider implementing the following defense measures:

- Safeguard and limit the access to access tokens and account credentials.

- Regularly monitor logs and audit trails for any suspicious activities.

- Implement role-based access control (RBAC) to control access to Azure resources.

## Objectives

The primary objectives of these commands are as follows:

1. Authenticate using an access token.

1. Retrieve a list of subscriptions using the Azure Management API.

1. Access and retrieve information about Azure resources.

1. Check for runCommand privileges within a specific resource group.

# Instructions

1. To query the Azure REST API for the subscription ID, run the following PowerShell script. Replace <RG-NAME> with the name of your resource group and <RESOURCE> with the name of your virtual machine resource.

**Code**: [[# Retrieve a list of subscriptions
$Token = 'eyJ0e]]

> This command uses PowerShell to query the Azure REST API to get the subscription ID and other details. The script uses a token to authenticate the request and sends a GET request to the specified URI. The result is then returned as a value. The URI is then updated to query for runCommand privileges on resources. The user is instructed to replace certain values in the script with their own values before executing the command.

2. (Optional) Access and retrieve information about Azure Resources

**Code**: [[# Retrieve a list of subscriptions
$Token = 'eyJ0e]]

3. (Optional) Check for runCommand privileges within a specific Resource Group

**Code**: [[# Check for runCommand privileges
$Token = 'eyJ0eX]]

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Application Access Token|T1527 - Application Access Token]]

## Tags

- [[Azure API via Powershell]]
- [[Cloud - Azure]]
- [[Token from Managed Identity]]
