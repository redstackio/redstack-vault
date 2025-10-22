---
id: 3a54b0ce-0306-47c3-aa85-204e110ff425
name: Azure AD Connect Sync Connector Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.079057+00:00'
updated_at: '2023-04-10T20:19:23.011905+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Azure AD Connect]]'
- '[[Cloud - Azure]]'
---

# Azure AD Connect Sync Connector Check

## Summary

The Azure AD Connect Sync Connector Check procedure involves checking the status of the synchronization connector between on-premise Active Directory and Azure AD. This procedure is typically used by an attacker to determine if the synchronization is working properly, which can enable them to harve

## Description

# Description

The Azure AD Connect Sync Connector Check procedure involves checking the status of the synchronization connector between on-premise Active Directory and Azure AD. This procedure is typically used by an attacker to determine if the synchronization is working properly, which can enable them to harvest credentials and move laterally within the network. From a technical perspective, this procedure involves using the AD Sync Connector Check command to query the status of the synchronization connector. From a business value perspective, this procedure can enable an attacker to gain access to sensitive information and cause significant damage to an organization.

## Requirements

1. Access to the network

1. Credentials with sufficient privileges to query the status of the synchronization connector

1. AD Sync Connector Check tool

## Defense

1. Ensure that all systems are up-to-date with the latest security patches

1. Implement multi-factor authentication for all accounts

1. Monitor network traffic for any suspicious activity

## Objectives

1. Determine the status of the synchronization connector between on-premise Active Directory and Azure AD

1. Identify potential vulnerabilities in the synchronization process

1. Harvest credentials and move laterally within the network

# Instructions

1. This command is used to retrieve information about the Azure AD Connect synchronization connectors that are installed on the server.

**Code**: [[Get-ADSyncConnector]]

> The 'Get-ADSyncConnector' command is used to display the details of the synchronization connectors that are currently installed on the server. This command can be useful in determining if Azure AD Connect is properly installed and configured. The output of this command includes the name, type, and status of each connector, as well as other details such as the server name and the version of Azure AD Connect that is currently installed. The command can be further customized by using various parameters to filter the output or to retrieve additional information about the connectors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Azure AD Connect]]
- [[Cloud - Azure]]
