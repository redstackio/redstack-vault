---
id: cmd-uuid-1
data: 'curl https://hackyholidays.h1ctf.com/robots.txt'
tags:
  - recon
type: command
output: Plaintext flag content.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.497Z'
verified: false
validated: true
submitted: true
---
# Curl Access Robots Txt

## Command

```bash
curl https://hackyholidays.h1ctf.com/robots.txt
```

## Description

Fetches the robots.txt file from the target to check for exposed paths or flags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target robots.txt endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/robots.txt
```

## Expected Output

List of disallowed paths or embedded flag.

## Related

- [[procedures/Enumerate-Robots-Txt-for-Information-Disclosure]]
