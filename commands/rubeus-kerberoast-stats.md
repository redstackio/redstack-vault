---
type: command
executor: cmd
data: Rubeus.exe kerberoast /stats
tags:
  - kerberoasting
  - enumeration
platforms:
  - Windows
verified: true
validated: true
---

# rubeus-kerberoast-stats

## Command

```cmd
Rubeus.exe kerberoast /stats
```

## Description

Gathers statistics on domain accounts' Kerberos encryption types and password ages using Rubeus. Helps prioritize targets with weak configs (e.g., RC4, old passwords) before roasting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /stats | Display encryption and password stats | Yes |

## Examples

### Basic Usage

```cmd
Rubeus.exe kerberoast /stats
```

## Expected Output

-------------------------------------   ----------------------------------
| Supported Encryption Type | Count |  | Password Last Set Year | Count |
-------------------------------------  ----------------------------------
| RC4_HMAC_DEFAULT          | 50    |  | 2018                   | 20    |
| AES128_CTS_HMAC_SHA1_96   | 30    |  | 2023                   | 10    |
-------------------------------------  ----------------------------------

## Related

- [[procedures/Kerberoasting-with-Rubeus]]
- [[tools/Rubeus]]
