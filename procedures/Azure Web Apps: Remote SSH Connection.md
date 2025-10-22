---
id: 8d0da02b-a656-42cd-bd5a-5bd20843de9b
name: 'Azure Web Apps: Remote SSH Connection'
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.424582+00:00'
updated_at: '2023-05-24T21:55:54.554593+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
platforms:
- Web
tags:
- '[[Azure Web App]]'
- '[[Cloud - Azure]]'
- '[[Spawn SSH for Azure Web App]]'
- '[[SSH]]'
commands:
- '[[Create Remote Connection for Web App]]'
---

# Azure Web Apps: Remote SSH Connection

**Status**: ✓ Verified

## Summary

This procedure outlines the steps to spawn an SSH connection for an Azure Web App. This can be useful for persistent remote access to the web app, allowing an attacker to gain access to sensitive data or execute further attacks. To spawn an SSH connection, an attacker will first need to gain access

## Description

# Description

This procedure outlines the steps to spawn an SSH connection for an Azure Web App. This can be useful for persistent remote access to the web app, allowing an attacker to gain access to sensitive data or execute further attacks. To spawn an SSH connection, an attacker will first need to gain access to the Azure Web App. Once access is gained, the attacker can use this procedure to spawn an SSH connection and maintain access to the web app.

## Requirements

- The Azure CLI installed on a local or remote machine

- The subscription ID, resource group name, and app service name of the target Azure Web App

## Defense

1. Ensure that access to the Azure Web App is restricted to authorized users only

1. Monitor for any unauthorized SSH connections to the Azure Web App

1. Regularly review logs for any suspicious activity related to the Azure Web App

## Objectives

1. Leverage any obtained Azure credentials to target the Azure Web Apps

1. Establish a remote SSH connection to the Azure Web App to gain unauthorized control

1. Maintain persistent access to the Azure Web App

# Instructions

1.This command will create a remote connection to the Azure Web App, which can then be used to perform various operations on the app, such as deploying code or managing configurations.

**Command** ([[Create Remote Connection for Web App]]):

```bash
az webapp create-remote-connection --subscription <SUBSCRIPTION-ID> --resource-group <RG-NAME> -n <APP-SERVICE-NAME>
```

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Create Remote Connection for Web App]]

## Tags

- [[Azure Web App]]
- [[Cloud - Azure]]
- [[Spawn SSH for Azure Web App]]
- [[SSH]]
