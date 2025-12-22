---
data: './sslyze.py --regular apps.owncloud.com:587 --starttls=smtp'
tags:
  - cipher-analysis
  - ssl-scan
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.035Z'
id: 4cc8d58c-84eb-4fc0-844b-f5a0bb53e412
verified: false
validated: true
submitted: true
---
# sslyze-analyze-smtp

## Command

```bash
./sslyze.py --regular apps.owncloud.com:587 --starttls=smtp
```

## Description

Analyzes SSL/TLS on SMTP with STARTTLS, listing ciphers and certs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --regular | Standard scan | No |
| --starttls=smtp | Enable STARTTLS | Yes |
| target:port | Host:port | Yes |

## Examples

### Basic Usage

```bash
./sslyze.py --regular target:587 --starttls=smtp
```

### Advanced Usage

```bash
./sslyze.py --certinfo --reneg apps.owncloud.com:587 --starttls=smtp
```

## Expected Output

Ciphers (AECDH-AES256-SHA), cert (self-signed), vulns (renegotiation).

## Related

- [[procedures/Analyze-SMTP-Cipher-Suites-with-Sslyze]]
- [[commands/testssl-scan-target]]
