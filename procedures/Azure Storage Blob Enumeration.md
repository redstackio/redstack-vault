---
id: 24fde44b-95fa-41a7-b68d-e725b6facf97
name: Azure Storage Blob Enumeration
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.448051+00:00'
updated_at: '2023-05-24T22:11:13.092661+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
platforms:
- Cloud
tags:
- '[[Azure Storage]]'
- '[[Azure Storage Blob]]'
- '[[Cloud - Azure]]'
- '[[Enumerate blobs]]'
- '[[Enumeration]]'
commands:
- '[[Enumerate Azure Blobs with Microburst]]'
- '[[Invoke EnumerateAzureBlobs]]'
---

# Azure Storage Blob Enumeration

**Status**: ✓ Verified

## Summary

Azure Blob Storage Enumeration is a technique used to discover information about the available blobs in an Azure Storage Account. An attacker can use this information to identify sensitive data, such as credentials, or to identify potential targets for further attacks. This technique can be used in

## Description

# Description

Azure Blob Storage Enumeration is a technique used to discover information about the available blobs in an Azure Storage Account. An attacker can use this information to identify sensitive data, such as credentials, or to identify potential targets for further attacks. This technique can be used in combination with other techniques to gain access to an Azure environment.

To enumerate blobs, an attacker can use various tools or scripts that interact with the Azure Storage API. The attacker can identify the storage account name and key, and then use these credentials to authenticate and retrieve a list of available blobs. The attacker can then analyze the metadata of the blobs to identify potential targets for further attacks.

This technique can be valuable for both red teaming and penetration testing, as it allows security professionals to identify potential weaknesses in an Azure environment.

- Blobs - `*.blob.core.windows.net`

- File Services - `*.file.core.windows.net`

- Data Tables - `*.table.core.windows.net`

- Queues - `*.queue.core.windows.net`

## Requirements

1. Valid credentials for an Azure Storage Account

1. Access to the Azure Storage API

1. Tools or scripts to interact with the Azure Storage API

## Defense

1. Implement access controls to limit access to Azure Storage Accounts

1. Monitor for unusual activity, such as large numbers of requests to the Azure Storage API

1. Encrypt sensitive data within Azure Blob Storage

## Objectives

1. Enumerate available blobs in an Azure Storage Account

1. Identify sensitive data within the blobs

1. Identify potential targets for further attacks

# Instructions

1. Invoke the Microburst script

**Command** ([[Invoke EnumerateAzureBlobs]]):

```bash
. C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureBlobs.ps1
```

2.  Use the script to enumerate the azure blobs. 

**Command** ([[Enumerate Azure Blobs with Microburst]]):

```bash
Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt
```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Enumerate Azure Blobs with Microburst]]
- [[Invoke EnumerateAzureBlobs]]

## Tags

- [[Azure Storage]]
- [[Azure Storage Blob]]
- [[Cloud - Azure]]
- [[Enumerate blobs]]
- [[Enumeration]]
