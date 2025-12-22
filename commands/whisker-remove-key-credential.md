---
id: 4ddc4a5c-799b-411d-9140-653807f2f186
name: whisker-remove-key-credential
type: command
executor: cmd
data: >-
  Whisker.exe remove /target:$_TARGET_NAME /domain:$_DOMAIN
  /dc:$_DOMAIN_CONTROLLER /remove:$_DEVICE_ID
output: null
created_at: '2023-04-06T03:56:06.261478+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-credentials
verified: true
validated: true
---

# whisker-remove-key-credential

## Command

```cmd
Whisker.exe remove /target:$_TARGET_NAME /domain:$_DOMAIN /dc:$_DOMAIN_CONTROLLER /remove:$_DEVICE_ID
```

## Description

Removes a specific key credential from the target by DeviceID GUID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /target:$_TARGET_NAME | Target SAM account | Yes |
| /domain:$_DOMAIN | Domain name | Yes |
| /dc:$_DOMAIN_CONTROLLER | DC FQDN | Yes |
| /remove:$_DEVICE_ID | GUID of the credential to remove | Yes |

## Examples

### Basic Usage

```cmd
Whisker.exe remove /target:computername$ /domain:contoso.local /dc:dc1.contoso.local /remove:2de4643a-2e0b-438f-a99d-5cb058b3254b
```

## Expected Output

"Credential removed successfully". No output on error.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/Whisker]]
