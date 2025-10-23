---
id: 4f5ca41a-528b-4630-80f2-90ddac471cd7
name: Azure Storage Blob Download
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.496588+00:00'
updated_at: '2023-05-24T22:42:46.260531+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
platforms:
- Cloud
tags:
- '[[Azure Storage]]'
- '[[Azure Storage Blob]]'
- '[[Cloud - Azure]]'
- '[[List and download blobs]]'
commands:
- '[[Retrieve Azure Resource]]'
- '[[Retrieve Azure Storage Account]]'
- '[[Retrieve Blob Content]]'
- '[[Retrieve Storage Container]]'
---

# Azure Storage Blob Download

**Status**: ✓ Verified

## Summary

The Azure Storage Blob Download procedure allows an attacker to retrieve the contents of a blob stored in an Azure Storage account. This technique can be used to exfiltrate sensitive data from an organization's cloud storage. To use this procedure, the attacker must have valid credentials for the A

## Description

# Description

The Azure Storage Blob Download procedure allows an attacker to retrieve the contents of a blob stored in an Azure Storage account. This technique can be used to exfiltrate sensitive data from an organization's cloud storage. To use this procedure, the attacker must have valid credentials for the Azure Storage account.

Technical Explanation: The procedure uses the Retrieve Azure Storage Blob Content command to retrieve the contents of a blob. The command requires the name of the blob and the name of the container in which it is stored. Once the contents of the blob are retrieved, they can be exfiltrated using a C2 channel or alternative protocol.

Business Value: An attacker can use this technique to steal sensitive data from an organization's cloud storage. This can include intellectual property, financial information, and personally identifiable information (PII). The theft of this data can cause significant financial and reputational damage to the organization.

 

## Requirements

1. Valid credentials for the Azure Storage account

 

## Defense

1. Implement access controls to limit the permissions of users and applications that can access Azure Storage accounts

1. Monitor Azure Storage accounts for unusual activity, such as large amounts of data being downloaded

1. Encrypt sensitive data stored in Azure Storage accounts to protect it from unauthorized access

 

## Objectives

1. Retrieve the contents of a blob stored in an Azure Storage account

1. Exfiltrate sensitive data from an organization's cloud storage

 

# Instructions

<u>*Overvie</u>w*

 



**Code**: [[PS Az> Get-AzResource
PS Az> Get-AzStorageAccount ]]





## Steps

1. Use the 'Get-AzResource' command to retrieve information about the Azure resources.



**Command** ([[Retrieve Azure Resource]]):

```bash
Get-AzResource
```





**Command** ([[Retrieve Azure Storage Account]]):

```bash
Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>
```





**Command** ([[Retrieve Storage Container]]):

```bash
Get-AzStorageContainer -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context
```





**Command** ([[Retrieve Blob Content]]):

```bash
Get-AzStorageBlobContent -Container <NAME> -Context (Get-AzStorageAccount -name <NAME> -ResourceGroupName <NAME>).context -Blob
```



 



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Retrieve Azure Resource]]
- [[Retrieve Azure Storage Account]]
- [[Retrieve Blob Content]]
- [[Retrieve Storage Container]]

## Tags

- [[Azure Storage]]
- [[Azure Storage Blob]]
- [[Cloud - Azure]]
- [[List and download blobs]]


