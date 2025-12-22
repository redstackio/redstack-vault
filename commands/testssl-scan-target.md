---
data: >-
  OPENSSL=/usr/local/Cellar/openssl/1.0.2d_1/bin/openssl bash testssl.sh
  apps.owncloud.com
tags:
  - ssl-scan
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.052Z'
id: 25cdb237-4e28-44df-95ac-befd96d4c02e
verified: false
validated: true
submitted: true
---
# testssl-scan-target

## Command

```bash
OPENSSL=/usr/local/Cellar/openssl/1.0.2d_1/bin/openssl bash testssl.sh apps.owncloud.com
```

## Description

Runs testssl.sh to scan the target for SSL/TLS protocols, ciphers, and vulnerabilities, using a specified OpenSSL binary for compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| OPENSSL | Path to OpenSSL binary | Yes |
| target | Domain to scan (default port 443) | Yes |

## Examples

### Basic Usage

```bash
OPENSSL=/usr/local/bin/openssl bash testssl.sh example.com
```

### Advanced Usage

```bash
OPENSSL=/usr/local/Cellar/openssl/1.0.2d_1/bin/openssl bash testssl.sh --ports=443,587 apps.owncloud.com
```

## Expected Output

Detailed report: protocols offered (TLS 1.2), ciphers (e.g., ADH-AES256-SHA), server prefs, PFS, and vulns like BREACH.

## Related

- [[commands/sslyze-analyze-smtp]]
- [[procedures/Scan-SSL-TLS-Cipher-Support-with-Testssl]]
