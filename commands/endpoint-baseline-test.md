---
id: cmd-uuid-1
data: 'POST https://████████/elist/viewem6.php with rememail=test@att.net'
tags:
  - recon
type: command
output: Normal response without delay
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.960Z'
verified: false
validated: true
submitted: true
---
# Endpoint Baseline Test

## Command

```bash
# Burp Suite equivalent: POST /elist/viewem6.php
# Body: rememail=test@att.net
# Include cookies: v1st=A9532F64A9E711AF; PHPSESSID=1796d85a30d3addf5934c1f0fafec529
```

## Description

Sends a standard POST request to establish normal endpoint behavior and response time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rememail | Test email value | Yes |
| cookie | Session cookies | Yes |

## Examples

### Basic Usage

```bash
# As above
```

## Expected Output

Quick HTTP response with email listing or success message, no errors or delays.

## Related

- [[procedures/Identify-Vulnerable-Endpoint]]
