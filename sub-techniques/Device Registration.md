---
id: fb8e33dd-8b7b-460b-973e-fdc52eec6659
name: Device Registration
type: sub-technique
mitre_id: T1098.005
mitre_url: null
created_at: '2023-04-06T00:31:26.443856+00:00'
updated_at: '2023-04-06T00:31:26.443856+00:00'
parent_technique: '[[Account Manipulation|T1098 - Account Manipulation]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Device Registration

**MITRE ID**: T1098.005

**Parent Technique**: [[Account Manipulation|T1098 - Account Manipulation]]

This is a sub-technique of T1098 - Account Manipulation.

## Summary

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance.

MFA systems, such as Duo or Okta, 

## Description

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance.

MFA systems, such as Duo or Okta, allow users to associate devices with their accounts in order to complete MFA requirements. An adversary that compromises a user’s credentials may enroll a new device in order to bypass initial MFA requirements and gain persistent access to a network.(Citation: CISA MFA PrintNightmare)(Citation: DarkReading FireEye SolarWinds)

Similarly, an adversary with existing access to a network may register a device to Azure AD and/or its device management system, Microsoft Intune, in order to access sensitive data or resources while bypassing conditional access policies.(Citation: AADInternals - Device Registration)(Citation: AADInternals - Conditional Access Bypass)(Citation: Microsoft DEV-0537) 

Devices registered in Azure AD may be able to conduct [Internal Spearphishing](https://attack.mitre.org/techniques/T1534) campaigns via intra-organizational emails, which are less likely to be treated as suspicious by the email client.(Citation: Microsoft - Device Registration) Additionally, an adversary may be able to perform a [Service Exhaustion Flood](https://attack.mitre.org/techniques/T1499/002) on an Azure AD tenant by registering a large number of devices.(Citation: AADInternals - BPRT)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]
