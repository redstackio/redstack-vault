---
id: cmd-gitsploit-scan
data: gitsploit -u zomato -l 10
tags:
  - vuln-scan
type: command
output: 'Vulnerabilities: XSS (critical), IDOR (high)'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.227Z'
verified: false
validated: true
submitted: true
---
# gitsploit-scan

## Command

```bash
gitsploit -u zomato -l 10
```

## Description

Scans GitHub for vulns in repos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Username/org | Yes |
| -l | Limit results | No |

## Examples

### Basic Usage

```bash
gitsploit -u zomato -l 10
```

## Expected Output

List of 10 vulns.

## Related

- [[commands/git-clone-review]]
