---
id: cmd-uuid-003
data: subjack -w subdomains.txt -t 100 -o takeovers.json -ssl
tags:
  - takeover
  - validation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.557Z'
verified: false
validated: true
submitted: true
---
# subjack-validate

## Command

```bash
subjack -w subdomains.txt -t 100 -o takeovers.json -ssl
```

## Description

Validates subdomains for takeover vulnerabilities by checking service fingerprints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Wordlist file | Yes |
| `-t` | Threads | No |
| `-o` | Output file | Yes |
| `-ssl` | Include SSL checks | No |

## Examples

### Basic Usage

```bash
subjack -w subdomains.txt -o takeovers.json
```

### Advanced Usage

```bash
subjack -w subdomains.txt -t 100 -o takeovers.json -ssl -v
```

## Expected Output

JSON with vulnerable subdomains and services.

## Related

- [[commands/dig-ns-query]]
- [[procedures/Validate-Dangling-DNS-for-Takeover]]
