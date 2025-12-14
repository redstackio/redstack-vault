---
data: set rhost facebooksearch.algolia.com
tags:
  - metasploit
  - target
type: command
output: RHOST set to facebooksearch.algolia.com
executor: msfconsole
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.940Z'
id: a30d0f2b-7d78-48a3-adc4-d6359f77fda9
verified: false
validated: true
submitted: true
---
# set-rhost-in-metasploit

## Command

```msfconsole
set rhost facebooksearch.algolia.com
```

## Description

Sets the target host IP or domain for the Rails exploit delivery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rhost | Target hostname or IP | Yes |

## Examples

### Basic Usage

```msfconsole
set rhost facebooksearch.algolia.com
```

## Expected Output

RHOST set to facebooksearch.algolia.com.

## Related

- [[Related Procedure: Configure-and-Execute-Rails-Deserialization-Exploit]]
