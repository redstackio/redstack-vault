---
data: cat common.txt | xargs -P 30 -n 1 ./b64search.sh
tags:
  - brute-force
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.197Z'
id: 37223830-91f1-48a9-829a-e43f8151c9f0
verified: false
validated: true
submitted: true
---
# b64search-brute-ssrf

## Command

```bash
cat common.txt | xargs -P 30 -n 1 ./b64search.sh
```

## Description

Multithreaded brute forcing of directories via SSRF using a custom script and wordlist.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -P | Parallel processes | No |
| -n | Lines per command | No |

## Examples

### Basic Usage

```bash
cat wordlist.txt | xargs -P 10 ./script.sh
```

## Expected Output

Discovered paths like /uploads.

## Related

- [[tools/Custom-B64search-Script]]
- [[procedures/API-SSRF-Exploitation-for-Internal-Access]]
