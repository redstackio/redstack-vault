---
data: 'ffuf -u https://TARGET/FUZZ -w wordlist.txt -fc 404'
tags:
  - fuzzing
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 78816d3c-85cd-483c-b0ac-06e3216c1266
created_at: '2025-12-11T03:47:39.544Z'
updated_at: '2025-12-11T03:47:39.544Z'
verified: false
validated: true
submitted: true
---
# ffuf-fuzz-subdomains

## Command

```bash
ffuf -u https://TARGET/FUZZ -w wordlist.txt -fc 404
```

## Description

Fuzzes URLs to discover subdomains or paths, filtering out 404 responses for valid endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | URL to fuzz | Yes |
| `-w` | Wordlist file | Yes |
| `-fc` | Filter by status code | No |

## Examples

### Basic Usage

```bash
ffuf -u https://snapchat.com/FUZZ -w wordlist.txt
```

### Advanced Usage

```bash
ffuf -u https://snapchat.com/FUZZ -w wordlist.txt -fc 404 -mc 200,301
```

## Expected Output

List of valid URLs with response codes and sizes.

## Related

- #ffuf
- [[procedures/Discover-Exposed-Grafana-via-Fuzzing]]
