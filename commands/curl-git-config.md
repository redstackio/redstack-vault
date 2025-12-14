---
data: 'curl -sk https://app.bountypay.h1ctf.com/.git/config'
tags:
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.211Z'
id: d9f0e2b4-3c3e-4679-8099-3b08326c4fdc
verified: false
validated: true
submitted: true
---
# curl-git-config

## Command

```bash
curl -sk https://app.bountypay.h1ctf.com/.git/config
```

## Description

Retrieves the .git/config file from an exposed repository silently and with insecure SSL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | No |
| -k | Insecure SSL | No |

## Examples

### Basic Usage

```bash
curl -sk https://example.com/.git/config
```

## Expected Output

Git config content with remote URL https://github.com/bounty-pay-code/request-logger/.

## Related

- [[tools/Curl]]
- [[procedures/Reconnaissance-and-Exposed-Git-Discovery]]
