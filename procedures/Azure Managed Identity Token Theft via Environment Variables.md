---
id: 10347224-c030-4b73-8155-6f173e7d079e
name: Azure Managed Identity Token Theft via Environment Variables
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.166657+00:00'
updated_at: '2023-05-24T16:00:22.793564+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
platforms:
- Cloud
- Linux
- Web
- Windows
tags:
- '[[Cloud - Azure]]'
- '[[Environment Variables]]'
- '[[php]]'
- '[[Token from Managed Identity]]'
- '[[Web Applications]]'
commands:
- '[[Display environment variables Bash]]'
- '[[Display environment variables Powershell]]'
---

# Azure Managed Identity Token Theft via Environment Variables

**Status**: ✓ Verified

## Summary

Azure provides Managed Identities to simplify the management of credentials for applications and services. However, if the environment variables for the identity are not secured properly, an attacker can easily steal the token and use it to access resources within the Azure environment. This attack

## Description

# Description

Azure provides Managed Identities to simplify the management of credentials for applications and services. However, if the environment variables for the identity are not secured properly, an attacker can easily steal the token and use it to access resources within the Azure environment. This attack can be carried out by compromising the host that has access to the environment variables, or by exploiting a vulnerability in an application that uses the identity. Once the token is obtained, the attacker can use it to perform actions within the Azure environment, such as accessing storage accounts or virtual machines.

 

## Requirements

1. Access to a host or application that has access to the environment variables for the Managed Identity

 

## Defense

1. Ensure that environment variables for Managed Identities are properly secured

1. Implement access controls to limit the scope of the Managed Identity

1. Monitor for unusual activity within the Azure environment, such as access from unknown sources

 

## Objectives

1. Steal the token for a Managed Identity

1. Use the token to access resources within the Azure environment

 

# Instructions

1. Get an access token by leveraging environment variables using PHP code through a web-app vulnerability on an Azure Resource with a Managed Identity.





**Code**: [[system('curl "$IDENTITY_ENDPOINT?resource=https://]]







2. (Optional) Display the environment variables with Bash to find the values of the IDENTITY_HEADER and IDENTITY_ENDPOINT environmental variables.





**Command** ([[Display environment variables Bash]]):

```bash
env
```





3. (Optional) Display environment variables with Powershell to find the values of the IDENTITY_HEADER and IDENTITY_ENDPOINT environmental variables.





**Command** ([[Display environment variables Powershell]]):

```bash
dir env:
```





> This command is used to find the values of the IDENTITY_HEADER and IDENTITY_ENDPOINT environmental variables. These variables are used for authenticating API requests. The IDENTITY_HEADER variable contains the authentication token or API key, while the IDENTITY_ENDPOINT variable contains the URL for the authentication service. These values are necessary for making authenticated API requests.

## Platforms

- Cloud
- Linux
- Web
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Display environment variables Bash]]
- [[Display environment variables Powershell]]

## Tags

- [[Cloud - Azure]]
- [[Environment Variables]]
- [[php]]
- [[Token from Managed Identity]]
- [[Web Applications]]


