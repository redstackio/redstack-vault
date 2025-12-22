---
data: 'https://www.yelp.com/?canary=asdf'
tags:
  - cookie-setting
type: command
executor: bash
platforms:
  - Web
id: b19aa181-b01b-4876-ae11-c81561ac49cb
created_at: '2025-12-13T23:56:20.370Z'
updated_at: '2025-12-13T23:56:20.370Z'
verified: false
validated: true
submitted: true
---
# set-yelpmainpaastacanary-cookie

## Command

```bash
https://www.yelp.com/?canary=asdf
```

## Description

Sets the yelpmainpaastacanary cookie via query parameter on Yelp domains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `canary` | Value to set the cookie to | Yes |

## Examples

### Basic Usage

```bash
https://www.yelp.com/?canary=asdf
```

## Expected Output

Set-Cookie: yelpmainpaastacanary=asdf; Domain=.yelp.com; Path=/; Secure; SameSite=Lax

## Related

- [[procedures/Identify-Insecure-Cookie-Setting-via-Query-Parameter]]
