---
data: 'ffuf -u https://FUZZ.snapchat.com -w wordlist.txt -fc 200'
tags:
  - fuzzing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 3531c196-fc0f-43f9-ad20-76e244295d86
created_at: '2025-12-11T06:10:16.542Z'
updated_at: '2025-12-11T06:10:16.542Z'
verified: false
validated: true
submitted: true
---
# ffuf-fuzz-urls

## Command

```bash
ffuf -u https://FUZZ.snapchat.com -w wordlist.txt -fc 200
```

## Description

This command uses ffuf to fuzz URLs by replacing FUZZ with wordlist entries, filtering for HTTP 200 responses to discover valid endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with FUZZ placeholder | Yes |
| `-w` | Wordlist file | Yes |
| `-fc` | Filter by status code | No |

## Examples

### Basic Usage

```bash
ffuf -u https://FUZZ.target.com -w common.txt
```

### Advanced Usage

```bash
ffuf -u https://FUZZ.target.com -w common.txt -mc 200,301 -t 50
```

## Expected Output

List of discovered URLs with sizes and status codes.

## Related

- [[tools/ffuf]]
- [[procedures/Discover-Grafana-Instance-via-Fuzzing]]
