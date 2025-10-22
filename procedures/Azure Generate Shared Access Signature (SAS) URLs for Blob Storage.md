---
id: de491b89-fac5-4399-8076-38b893fc6298
name: Azure Generate Shared Access Signature (SAS) URLs for Blob Storage
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.471883+00:00'
updated_at: '2023-05-24T22:34:09.711567+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
platforms:
- Cloud
tags:
- '[[Azure Storage]]'
- '[[Azure Storage Blob]]'
- '[[Cloud - Azure]]'
- '[[SAS URL]]'
---

# Azure Generate Shared Access Signature (SAS) URLs for Blob Storage

**Status**: ✓ Verified

## Summary

Azure Shared Access Signatures (SAS) are a secure way to provide  granular permissions to Azure Storage resources without exposing your  account keys. A SAS URL gives specific, time-limited permissions to  access objects in your storage account. This guide illustrates the  process of generating a S

## Description

# Description

Azure Shared Access Signatures (SAS) are a secure way to provide  granular permissions to Azure Storage resources without exposing your  account keys. A SAS URL gives specific, time-limited permissions to  access objects in your storage account. This guide illustrates the  process of generating a SAS URL for an Azure Blob Storage container  using Azure PowerShell or Azure CLI.

## Requirements

1. An active Azure subscription

1. Azure Storage Account and Blob container

1. Azure PowerShell or Azure CLI installed

## Defense

1. Limit the permissions provided by the SAS URL to only what's necessary

1. Limit the duration the SAS URL is valid to reduce potential misuse

1. Use HTTPS only option to ensure secure transmission of the SAS token

## Objectives

1. Generate a SAS URL for an Azure Blob Storage container

1. Securely manage access to Azure Blob Storage data

# Instructions

1.Install the `Az` module if you haven't already

**Code**: [[# Install the AZ Module
Install-Module -Name Az -A]]

2 (Optional) Using az-cli instead of the powershell module

**Code**: [[az login
token=$(az storage container generate-sas]]

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Tags

- [[Azure Storage]]
- [[Azure Storage Blob]]
- [[Cloud - Azure]]
- [[SAS URL]]
