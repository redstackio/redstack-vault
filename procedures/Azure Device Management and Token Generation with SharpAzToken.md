---
id: 395a5875-8ba6-4012-b030-8be483e95584
name: Azure Device Management and Token Generation with SharpAzToken
type: procedure
verified: true
submitted: true
created_at: '2023-05-24T07:30:25.190680+00:00'
updated_at: '2023-05-24T07:42:32.942941+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[Pass The PRT]]'
- '[[Primary Refresh Token]]'
- '[[Refresh Tokens]]'
commands:
- '[[SharpAzToken Device Keys]]'
- '[[SharpAzToken MDM]]'
---

# Azure Device Management and Token Generation with SharpAzToken

**Status**: ✓ Verified

## Summary

The SharpAzToken tool provides a set of commands that facilitate device  management and token generation for Azure resources. This procedure  focuses on two specific commands: 'mdm' and 'devicekeys'. The 'mdm'  command allows you to join a device to a Mobile Device Management (MDM)  server, while t

## Description

# Description

The SharpAzToken tool provides a set of commands that facilitate device  management and token generation for Azure resources. This procedure  focuses on two specific commands: 'mdm' and 'devicekeys'. The 'mdm'  command allows you to join a device to a Mobile Device Management (MDM)  server, while the 'devicekeys' command enables the generation of a  Primary Refresh Token (PRT) and session key from a Device Certificate.  These commands are essential for managing devices and accessing Azure  resources securely.



## Requirements

To execute these commands successfully, ensure the following:



`- You have the SharpAzToken tool installed and accessible.
- You possess the necessary access token or relevant components.
- The device is eligible and configured for MDM enrollment.
- You have the required permissions to interact with Azure resources.`



## Defense

To enhance security and protect your Azure resources, consider implementing the following defense measures:



- Limit the usage of the SharpAzToken tool to trusted individuals or applications.

- Regularly monitor logs and audit trails for any suspicious activities.

- Employ a robust credential rotation policy to mitigate the risk of unauthorized access.



## Instructions

Follow these steps to achieve the desired outcomes:



1. Join a device to MDM using the 'mdm' command:





**Command** ([[SharpAzToken MDM]]):

```bash
SharpAzToken.exe mdm --joindevice --accesstoken (or some combination from the token part) --devicename <Name> --outpfxfile <Some path>
```



- Replace `<Access Token>` with the appropriate access token required for authentication.

- Specify a unique `<Name>` for the device being joined.

- Provide the `<Some path>` where the resulting PFX file will be saved.



2. Generate a PRT and session key from a Device Certificate using the 'devicekeys' command:





**Command** ([[SharpAzToken Device Keys]]):

```bash
SharpAzToken.exe devicekeys --pfxpath XXXX.pfx --refreshtoken (--prtcookie / ---username + --password )
```



- Specify the path to the Device Certificate PFX file by replacing `<XXXX.pfx>`.

- Choose one of the available options for obtaining the refresh token:Use `--prtcookie` to acquire the PRT cookie from a Windows machine using Mimikatz.
Use `--username` and `--password` to provide the necessary credentials for obtaining the refresh token.


## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[SharpAzToken Device Keys]]
- [[SharpAzToken MDM]]

## Tags

- [[Cloud - Azure]]
- [[Pass The PRT]]
- [[Primary Refresh Token]]
- [[Refresh Tokens]]


