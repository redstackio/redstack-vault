---
id: cmd-uuid-16
data: ./salt.go
tags:
  - bruteforce
  - salt
type: command
output: mrgrinch463
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.600Z'
verified: false
validated: true
submitted: true
---
# Go Salt Bruteforce

## Command

```bash
./salt.go
```

## Description

Brute-forces MD5 salt using wordlist.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Script | salt.go | Yes |

## Examples

### Basic Usage

```bash
go run salt.go
```

## Expected Output

Found salt.

## Related

- [[procedures/Brute-Force-Salt-and-DNS-Rebinding-for-DDoS-Bypass]]
