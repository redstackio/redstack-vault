---
id: b4c91da1-66f3-4550-8f5e-346c16e76dbf
name: Azure Tenant Enumeration with az-cli
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.024604+00:00'
updated_at: '2023-05-25T04:48:48.379198+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
platforms:
- Cloud
tags:
- '[[az-cli]]'
- '[[Cloud - Azure]]'
- '[[Enumerate tenant with az cli]]'
- '[[Enumeration]]'
commands:
- '[[Azure Login]]'
- '[[List all function app names]]'
- '[[List all key vaults]]'
- '[[List all storage accounts]]'
- '[[List all virtual machine names]]'
- '[[List all virtual machines]]'
- '[[List all web apps]]'
---

# Azure Tenant Enumeration with az-cli

**Status**: ✓ Verified

## Summary

Azure Tenant Enumeration with az cli is a technique used to gather information about an Azure tenant using the Azure CLI. This technique can be used by an attacker to identify resources within the tenant, such as virtual machines, storage accounts, and network resources. The Azure CLI is a command-

## Description

# Description

Azure Tenant Enumeration with az cli is a technique used to gather information about an Azure tenant using the Azure CLI. This technique can be used by an attacker to identify resources within the tenant, such as virtual machines, storage accounts, and network resources. The Azure CLI is a command-line tool that provides a command-line interface to interact with Azure resources. The Azure CLI can be used to query Azure Resource Manager (ARM) for information about the resources in the tenant. This technique can be used by both red teamers and attackers to gain valuable intelligence about an Azure tenant.

 

## Requirements

1. Access to the Azure CLI

1. Valid Azure credentials

 

## Defense

1. Ensure that Azure credentials are not leaked or stolen

1. Use Azure Role-Based Access Control (RBAC) to limit access to resources

1. Monitor for suspicious activity in Azure logs

 

## Objectives

1. Gather information about the Azure tenant

1. Identify resources within the tenant

 

# Instructions

*<u>Overv*iew</u>

 



**Code**: [[# Login to Azure
PS> az login -u test@<TENANT NAME]]



## Steps

1. To get a list of Azure resources in your subscription, run the following commands in PowerShell:



**Command** ([[Azure Login]]):

```powershell
PS> az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
```





**Command** ([[List all virtual machines]]):

```bash
az vm list
```





**Command** ([[List all virtual machine names]]):

```bash
az vm list --query "[].[name]" -o table
```





**Command** ([[List all web apps]]):

```bash
az webapp list
```





**Command** ([[List all function app names]]):

```bash
az functionapp list --query "[].[name]" -o table
```





**Command** ([[List all storage accounts]]):

```bash
az storage account list
```





**Command** ([[List all key vaults]]):

```bash
az keyvault list
```



## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Azure Login]]
- [[List all function app names]]
- [[List all key vaults]]
- [[List all storage accounts]]
- [[List all virtual machine names]]
- [[List all virtual machines]]
- [[List all web apps]]

## Tags

- [[az-cli]]
- [[Cloud - Azure]]
- [[Enumerate tenant with az cli]]
- [[Enumeration]]


