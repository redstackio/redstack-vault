---
id: c33c4f81-42e9-4fe3-a559-27a91d519bf0
name: start-aadint-device-intune-callback
type: command
executor: powershell
data: >-
  Start-AADIntDeviceIntuneCallback -PfxFileName "$_PFX_FILE_PATH_MDM"
  -DeviceName "$_DEVICE_NAME"
output: null
created_at: '2023-04-06T03:56:15.982723+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - intune
  - callback
  - mdm
verified: true
validated: true
---

# start-aadint-device-intune-callback

## Command

```powershell
Start-AADIntDeviceIntuneCallback -PfxFileName "$_PFX_FILE_PATH_MDM" -DeviceName "$_DEVICE_NAME"
```

## Description

This command initiates the Intune MDM callback to finalize device compliance status after enrollment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -PfxFileName | Path to the MDM certificate file | Yes |
| -DeviceName | Name of the device | Yes |

## Examples

### Basic Usage

```powershell
Start-AADIntDeviceIntuneCallback -PfxFileName "C:\certs\mdm-callback.pfx" -DeviceName "FakeDevice"
```

## Expected Output

Callback completion:
```
Callback initiated successfully.
Device marked as compliant.
```

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
