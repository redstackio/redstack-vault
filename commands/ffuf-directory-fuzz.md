---
data: >-
  ffuf -w ./SecLists/Discovery/Web-Content/common.txt -u
  "https://app.bountypay.h1ctf.com/FUZZ" -ac
tags:
  - fuzzing
type: command
output: Discovery of .git/HEAD and other paths
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.013Z'
id: 574e636a-7d61-4319-a138-27b580b56ab5
verified: false
validated: true
submitted: true
---
# ffuf-directory-fuzz

## Command

```bash
ffuf -w ./SecLists/Discovery/Web-Content/common.txt -u "https://app.bountypay.h1ctf.com/FUZZ" -ac
```

## Description

Fuzzes directories and files on a web target using a wordlist to discover hidden paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w` | Wordlist path | Yes |
| `-u` | Target URL with FUZZ | Yes |
| `-ac` | Auto-calibrate | No |

## Examples

### Basic Usage

```bash
ffuf -w wordlist.txt -u "https://target/FUZZ"
```

## Expected Output

Hits on valid paths like .git/.

## Related

- [[tools/ffuf]]
