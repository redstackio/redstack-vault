---
id: 7a9cce62-c2d8-447b-8f5c-8ecc9778a0d5
name: get-aadint-access-token-for-intune-mdm-save-to-cache
type: command
executor: powershell
data: Get-AADIntAccessTokenForIntuneMDM -PfxFileName "$_PFX_FILE_PATH" -SaveToCache
output: null
created_at: '2023-04-06T03:56:15.982608+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - azure
  - intune
  - mdm
  - token
verified: true
validated: true
---

# get-aadint-access-token-for-intune-mdm-save-to-cache

## Command

```powershell
Get-AADIntAccessTokenForIntuneMDM -PfxFileName "$_PFX_FILE_PATH" -SaveToCache
```

## Description

This command obtains an access token for Intune MDM enrollment using a provided certificate file and caches it for use in device join operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -PfxFileName | Path to the .pfx certificate file for authentication | Yes |
| -SaveToCache | Persists the token in the module cache | Yes |

## Examples

### Basic Usage

```powershell
Get-AADIntAccessTokenForIntuneMDM -PfxFileName "C:\certs\mdm.pfx" -SaveToCache
```

## Expected Output

Token details displayed and cached:
```
AccessToken : eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik...
ExpiresOn : 2023-10-01T12:00:00Z
```

## Related

- [[procedures/Bypass-Azure-Conditional-Access-via-Fake-Device-Join]]
- [[tools/AADInternals]]
