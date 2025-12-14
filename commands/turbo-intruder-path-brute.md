---
data: '# Turbo Intruder for path traversal brute on internal /uploads'
tags:
  - brute-force
type: command
output: Discovered files like BountyPay.apk
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.895Z'
id: 67daca31-07c8-4bdf-b447-339b927844f1
verified: false
validated: true
submitted: true
---
# turbo-intruder-path-brute

## Command

```bash
# In Burp: Fuzz /uploads/§s
```

## Description

Brute internal directories post-redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wordlist | Directory names | Yes |

## Examples

### Basic Usage

```bash
# Payload positions for paths
```

## Expected Output

APK location.

## Related

- [[procedures/Exploit-Open-Redirect-and-Path-Traversal]]
