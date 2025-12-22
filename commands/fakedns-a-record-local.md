---
data: A *.local.yourdomain.com 0.0.0.0
tags:
  - dns
  - wildcard
  - localhost
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.239Z'
id: f7d97d98-70d5-4962-8e69-8e60b9a46e2d
verified: false
validated: true
submitted: true
---
# FakeDns Wildcard A Record for Local Subdomains

## Command

```bash
A *.local.yourdomain.com 0.0.0.0
```

## Description

Configures a wildcard A record in FakeDns to resolve any .local.yourdomain.com subdomain to 0.0.0.0 (resolves to 127.0.0.1), bypassing Bitwarden's private IP check for SSRF to localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| A | DNS record type | Yes |
| *.local.yourdomain.com | Wildcard subdomain pattern | Yes |
| 0.0.0.0 | IP resolving to localhost | Yes |

## Examples

### Basic Usage

```bash
A *.internal.example.com 0.0.0.0
```

### Advanced Usage

Combine with other records in FakeDns config file.

## Expected Output

Resolutions like test.local.yourdomain.com -> 0.0.0.0; test with `dig test.local.yourdomain.com`.

## Related

- [[commands/fakedns-a-record-www]]
- [[procedures/Setup-FakeDns-with-Malicious-Records]]
