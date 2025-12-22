---
data: >-
  # Turbo Intruder fuzzing for directories on app.bountypay.h1ctf.com using
  SecLists
tags:
  - brute-force
type: command
output: Exposed paths like .git/HEAD
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.942Z'
id: 999945d4-db9d-418f-9430-7355a34cb711
verified: false
validated: true
submitted: true
---
# turbo-intruder-directory-brute

## Command

```bash
# In Burp: GET §s HTTP/1.1 Host: app.bountypay.h1ctf.com
```

## Description

Brute-force directories to find exposed resources like .git.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wordlist | SecLists common paths | Yes |
| base_url | Target like app.bountypay.h1ctf.com | Yes |

## Examples

### Basic Usage

```bash
# Fuzz paths
```

## Expected Output

200 responses for .git/config etc.

## Related

- [[procedures/Brute-Force-Directories-for-Exposed-Resources]]
