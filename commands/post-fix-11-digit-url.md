---
data: 'http://google.com:12345678901'
tags:
  - dos
  - post-fix
type: command
output: Cannot be shared/posted
executor: text
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.123Z'
id: d30b0fe1-04ca-459f-b8e4-7c90d32cc68f
verified: false
validated: true
submitted: true
---
# post-fix-11-digit-url

## Command

```text
http://google.com:12345678901
```

## Description

11-digit port URL blocked by post-fix validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port | 11-digit port | Yes |
| domain | google.com | Yes |

## Examples

### Basic Usage

```text
http://google.com:12345678901
```

## Expected Output

Posting rejected due to length limit.

## Related

- [[Related Procedure]]
