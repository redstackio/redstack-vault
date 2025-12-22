---
id: cmd-gitsploit-927413
data: gitsploit search zomato --exploit
tags:
  - vuln-scan
type: command
output: 'Found 10 vulnerabilities: XSS (critical), DLL Hijacking (high)...'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.606Z'
verified: false
validated: true
submitted: true
---
# gitsploit-scan

## Command

```bash
gitsploit search zomato --exploit
```

## Description

Searches GitHub for Zomato vulns using gitSploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `search zomato` | Query term | Yes |
| `--exploit` | Include exploit info | No |

## Examples

### Basic Usage

```bash
gitsploit search keyword
```

### Advanced Usage

```bash
gitsploit search zomato --type xss
```

## Expected Output

Vulns listed with severity.

## Related

- [[Related Procedure: Vulnerability-Scanning-in-GitHub-with-gitSploit]]
