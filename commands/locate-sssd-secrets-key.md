---
id: 3c3a5e54-2358-4b94-816e-846f047a9df9
name: locate-sssd-secrets-key
type: command
executor: bash
data: ls -la /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey
output: null
created_at: '2023-04-06T03:56:08.604056+00:00'
updated_at: '2023-10-10T20:26:03.243838+00:00'
platforms:
  - Linux
tags:
  - discovery
  - kerberos
verified: true
validated: true
---

# locate-sssd-secrets-key

## Command

```bash
ls -la /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey
```

## Description

This command locates and displays permissions for the SSSD secrets database and master key files on a Linux system using SSSD for Kerberos caching. It helps verify access before extraction in credential dumping scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/lib/sss/secrets/secrets.ldb` | Path to SSSD database | Built-in |
| `/var/lib/sss/secrets/.secrets.mkey` | Path to master key | Built-in |
| `-la` | Long listing with hidden files | Built-in |

## Examples

### Basic Usage

```bash
ls -la /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey
```

### With Error Suppression

```bash
ls -la /var/lib/sss/secrets/secrets.ldb /var/lib/sss/secrets/.secrets.mkey 2>/dev/null
```

## Expected Output

-rw------- 1 root root 12345 Oct 10 12:00 /var/lib/sss/secrets/secrets.ldb
-rw------- 1 root root  1024 Oct 10 12:00 /var/lib/sss/secrets/.secrets.mkey

## Related

- [[procedures/CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices]]
- [[commands/python-extract-secrets-sssdkcmextractor]]
