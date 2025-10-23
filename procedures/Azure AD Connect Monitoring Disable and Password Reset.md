---
id: 91608399-73df-454d-8b10-4e918441cbf9
name: Azure AD Connect Monitoring Disable and Password Reset
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.098274+00:00'
updated_at: '2023-04-10T20:19:32.884546+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Account Manipulation|T1098 - Account Manipulation]]'
tags:
- '[[Azure AD Connect]]'
- '[[Cloud - Azure]]'
---

# Azure AD Connect Monitoring Disable and Password Reset

## Summary

This procedure involves disabling real-time monitoring in Azure AD Connect and resetting the on-premises admin password. This can be used by an attacker to gain access to sensitive information in the cloud. Real-time monitoring allows for the detection of security events such as failed logins and p

## Description

# Description

This procedure involves disabling real-time monitoring in Azure AD Connect and resetting the on-premises admin password. This can be used by an attacker to gain access to sensitive information in the cloud. Real-time monitoring allows for the detection of security events such as failed logins and password changes. By disabling this feature, an attacker can perform actions without being detected. Resetting the on-premises admin password allows the attacker to gain access to the on-premises environment and potentially move laterally.

 

## Requirements

1. Access to Azure AD Connect

1. Access to on-premises environment

 

## Defense

1. Enable multi-factor authentication for all accounts

1. Monitor Azure AD Connect logs for suspicious activity

1. Regularly rotate on-premises admin passwords

 

## Objectives

1. Disable real-time monitoring in Azure AD Connect

1. Reset the on-premises admin password

 

# Instructions

1. undefined

 



**Code**: [[PS > Set-MpPreference -DisableRealtimeMonitoring $]]



> 

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Account Manipulation|T1098 - Account Manipulation]]

## Tags

- [[Azure AD Connect]]
- [[Cloud - Azure]]


