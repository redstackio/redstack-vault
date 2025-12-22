---
type: command
executor: bash
data: >-
  gobuster dns -d $_TARGET_DOMAIN -w $_WORDLIST_PATH -t $_THREADS -q -o
  $_OUTPUT_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# gobuster-dns-subdomain-brute-force

## Command

```bash
gobuster dns -d $_TARGET_DOMAIN -w $_WORDLIST_PATH -t $_THREADS -q -o $_OUTPUT_FILE
```

## Description

This command uses Gobuster in DNS mode to brute-force subdomains by querying DNS records for entries from a wordlist. It is ideal for discovering hidden subdomains during network reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The target domain to enumerate (e.g., example.com) | Yes |
| $_WORDLIST_PATH | Path to the subdomain wordlist file (one entry per line) | Yes |
| -t $_THREADS | Number of concurrent threads (default: 10, recommended: 50 for speed) | No |
| -q | Quiet mode to suppress banner and extra output | No |
| -o $_OUTPUT_FILE | Output file to save results (default: stdout) | No |

## Examples

### Basic Usage

```bash
gobuster dns -d example.com -w /usr/share/wordlists/subdomains.txt
```

### Advanced Usage

```bash
gobuster dns -d example.com -w subdomains.txt -t 100 -q -o results.txt --wildcard
```

This adds wildcard handling for domains with wildcard DNS records.

## Expected Output

Real-time progress with discoveries:

```
[=] Target URI: https://example.com/

Found: admin.example.com [192.0.2.1]
Found: api.example.com [192.0.2.2]
...

Summary of sub-domains: 2
Queries: 10000
Speed: 500/s
```

Success is indicated by 'Found:' lines showing resolved subdomains.

## Related

- [[procedures/Brute-Force-Subdomains-with-Gobuster]]
- [[tools/Gobuster]]
