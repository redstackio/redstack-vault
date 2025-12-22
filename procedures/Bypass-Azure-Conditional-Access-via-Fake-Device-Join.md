---
id: 617b2881-fb86-4360-a81d-ab22edb0e050
name: Bypass-Azure-Conditional-Access-via-Fake-Device-Join
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:15.991376+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Account Manipulation|T1098]]'
  - '[[techniques/Account Manipulation/Device Registration|T1098.005]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - Azure]]'
  - '[[tags/Conditional Access]]'
  - cloud
  - azure
  - aad
  - intune
  - bypass
commands:
  - '[[commands/get-aadint-access-token-for-aad-join-save-to-cache]]'
  - '[[commands/get-aadint-access-token-for-intune-mdm-save-to-cache]]'
  - '[[commands/join-aadint-device-to-azure-ad]]'
  - '[[commands/join-aadint-device-to-intune]]'
  - '[[commands/start-aadint-device-intune-callback]]'
platforms:
  - Azure
  - Windows
tools:
  - '[[tools/AADInternals]]'
validated: true
---

# Bypass-Azure-Conditional-Access-via-Fake-Device-Join

## Summary

This procedure uses the AADInternals PowerShell module to simulate device registration in Azure AD and Intune, marking a device as compliant to bypass conditional access policies that require device compliance for resource access.

## Description

In Azure environments, conditional access policies often enforce device compliance checks via Intune before granting access to sensitive resources. Attackers can bypass these by forging device join processes to Azure AD and Intune using AADInternals, creating a fake compliant device registration. This allows unauthorized access to protected applications and data without meeting actual compliance requirements like encryption or patching. The technique involves obtaining access tokens, joining the device with spoofed attributes, and triggering callbacks to simulate MDM enrollment. It targets hybrid or cloud-only Azure setups and requires initial authentication to Azure services.

## Requirements

1. PowerShell 5.1 or later with AADInternals module installed.
2. Valid Azure AD credentials with permissions to register devices (e.g., user or service principal).
3. A certificate file (.pfx) for Intune MDM authentication, generated via Azure portal or tools like New-SelfSignedCertificate.
4. Network access to Azure endpoints (login.microsoftonline.com, graph.microsoft.com).

## Defense

- Enable strict device compliance policies in Intune and monitor for anomalous registrations.
- Use Azure AD Identity Protection to detect unusual device join patterns.
- Implement certificate-based authentication and validate MDM enrollments via logs in Azure Monitor.
- Regularly audit device objects in Azure AD for spoofed attributes like unusual OS versions.

## Objectives

1. Simulate compliant device registration to evade conditional access controls.
2. Gain unauthorized access to Azure resources requiring device compliance.
3. Maintain persistence through fake device identity without triggering alerts.

## Instructions

### Step 1: Obtain Access Token for Azure AD Join

**Context**: Retrieve an access token for Azure AD device join operations and cache it for subsequent use. This step authenticates the session without prompting for credentials repeatedly.

**Command** ([[commands/get-aadint-access-token-for-aad-join-save-to-cache]]):
```powershell
Get-AADIntAccessTokenForAADJoin -SaveToCache
```

> This command fetches a token scoped for Azure AD join APIs and stores it in the module's cache. Expected output includes token details and confirmation of caching.

### Step 2: Join Device to Azure AD

**Context**: Register the device in Azure AD with spoofed details to establish initial trust. Specify a fake device name, type, and OS to avoid detection.

**Command** ([[commands/join-aadint-device-to-azure-ad]]):
```powershell
Join-AADIntDeviceToAzureAD -DeviceName "$_DEVICE_NAME" -DeviceType "$_DEVICE_TYPE" -OSVersion "$_OS_VERSION"
```

> Replace placeholders with values like DeviceName: "FakeDevice", DeviceType: "Windows", OSVersion: "10.0". Success is indicated by a new device object created in Azure AD.

### Step 3: Obtain Access Token for Intune MDM

**Context**: Get a token for Intune Mobile Device Management (MDM) enrollment using a certificate file. This enables compliance marking.

**Command** ([[commands/get-aadint-access-token-for-intune-mdm-save-to-cache]]):
```powershell
Get-AADIntAccessTokenForIntuneMDM -PfxFileName "$_PFX_FILE_PATH" -SaveToCache
```

> Provide the path to your .pfx certificate file. The command prompts for the certificate password if needed and caches the token. Expected output confirms token acquisition.

### Step 4: Join Device to Intune

**Context**: Enroll the device in Intune to simulate MDM compliance, allowing conditional access policies to treat it as trusted.

**Command** ([[commands/join-aadint-device-to-intune]]):
```powershell
Join-AADIntDeviceToIntune -DeviceName "$_DEVICE_NAME"
```

> Use the same device name from Step 2. This creates an Intune device record linked to the Azure AD join.

### Step 5: Start Intune Callback

**Context**: Trigger the MDM callback to finalize compliance status and complete the fake enrollment process.

**Command** ([[commands/start-aadint-device-intune-callback]]):
```powershell
Start-AADIntDeviceIntuneCallback -PfxFileName "$_PFX_FILE_PATH_MDM" -DeviceName "$_DEVICE_NAME"
```

> Use the MDM-specific .pfx file (often generated post-join). This simulates the device checking in with Intune, marking it compliant.

For a complete scripted execution, refer to the full code snippet in [[codes/aad-internals-fake-device-compliance-script]].
