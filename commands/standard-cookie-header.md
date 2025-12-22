---
data: 'Cookie: a=1; b=2;'
tags:
  - cookie-parsing
type: command
executor: bash
platforms:
  - Web
id: a2f9f061-8fa6-44e8-b305-e9161bfbf01d
created_at: '2025-12-13T23:56:20.368Z'
updated_at: '2025-12-13T23:56:20.368Z'
verified: false
validated: true
submitted: true
---
# standard-cookie-header

## Command

```bash
Cookie: a=1; b=2;
```

## Description

Standard cookie header with semicolon separation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `a` | Value 1 | Yes |
| `b` | Value 2 | Yes |

## Examples

### Basic Usage

```bash
Cookie: a=1; b=2;
```

## Expected Output

Parsed as two cookies: a=1 and b=2

## Related

- [[procedures/Exploit-Broken-Cookie-Parsing-for-Smuggling]]
